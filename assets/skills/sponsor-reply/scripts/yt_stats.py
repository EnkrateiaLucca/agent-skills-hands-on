#!/usr/bin/env python3
"""Pull live channel + per-video stats from the YouTube Data API v3.

The number that matters for sponsorship pricing is not subscriber count -- it is
what a new video can be expected to do. So this reports the MEDIAN views of recent
long-form uploads that have had time to mature (default: published 30+ days ago),
which is a far better predictor than an average dragged around by one viral hit.

Reads YOUTUBE_API_KEY and YOUTUBE_CHANNEL_HANDLE (or _ID) from a .env sitting next
to SKILL.md. No third-party dependencies -- stdlib only.

  python3 scripts/yt_stats.py --out stats.json
  python3 scripts/yt_stats.py --videos 40 --mature-days 45
"""
import argparse, json, os, re, statistics, sys, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://www.googleapis.com/youtube/v3/"
SHORT_MAX_SECONDS = 180  # YouTube Shorts cap; anything longer counts as long-form


# Checked in order; the first hit for a given key wins. Lucas keeps shared keys in
# ~/.secrets/globals.env, so the skill reads that directly rather than making him
# copy the key into a second place where it can drift or leak into a repo.
ENV_PATHS = [
    Path(__file__).resolve().parent.parent / ".env",
    Path.cwd() / ".env",
    Path.home() / ".secrets" / "globals.env",
]
# The YouTube Data API is just a Google API key, so accept either name.
KEY_NAMES = ["YOUTUBE_API_KEY", "GOOGLE_API_KEY"]


def load_env():
    """Load .env-style files into os.environ without clobbering the real env."""
    loaded, seen = [], set()
    for candidate in ENV_PATHS:
        resolved = candidate.resolve()
        if resolved in seen or not candidate.is_file():
            continue
        seen.add(resolved)
        for line in candidate.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("export "):
                line = line[7:]
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        loaded.append(str(candidate))
    return loaded


def api_key():
    for name in KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name], name
    return None, None


def get(endpoint, **params):
    params["key"] = api_key()[0]
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        sys.exit(f"YouTube API error {e.code} on {endpoint}: {body}")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach the YouTube API ({e.reason}). Network blocked?")


def parse_duration(iso):
    m = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


def resolve_channel():
    cid = os.environ.get("YOUTUBE_CHANNEL_ID")
    handle = os.environ.get("YOUTUBE_CHANNEL_HANDLE")
    if cid:
        data = get("channels", part="snippet,statistics,contentDetails", id=cid)
    elif handle:
        data = get("channels", part="snippet,statistics,contentDetails",
                   forHandle=handle if handle.startswith("@") else "@" + handle)
    else:
        sys.exit("Set YOUTUBE_CHANNEL_HANDLE or YOUTUBE_CHANNEL_ID in .env")
    items = data.get("items") or []
    if not items:
        sys.exit("Channel not found. Check YOUTUBE_CHANNEL_HANDLE / _ID in .env")
    return items[0]


def recent_video_ids(uploads_playlist, want):
    ids, token = [], None
    while len(ids) < want:
        page = get("playlistItems", part="contentDetails",
                   playlistId=uploads_playlist, maxResults=min(50, want - len(ids)),
                   **({"pageToken": token} if token else {}))
        ids += [i["contentDetails"]["videoId"] for i in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            break
    return ids[:want]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--videos", type=int, default=30,
                    help="how many recent uploads to inspect (default 30)")
    ap.add_argument("--mature-days", type=int, default=30,
                    help="a video counts as mature this many days after publish")
    ap.add_argument("--sample", type=int, default=12,
                    help="how many mature long-form videos to take the median over")
    ap.add_argument("--out", help="write JSON here as well as stdout")
    a = ap.parse_args()

    env_files = load_env()
    key, key_name = api_key()
    if not key:
        sys.exit("No YOUTUBE_API_KEY or GOOGLE_API_KEY found. Looked in:\n  "
                 + "\n  ".join(dict.fromkeys(str(p) for p in ENV_PATHS))
                 + "\nAdd one of those keys -- I won't guess view numbers.")

    ch = resolve_channel()
    stats, uploads = ch["statistics"], ch["contentDetails"]["relatedPlaylists"]["uploads"]

    vids = []
    ids = recent_video_ids(uploads, a.videos)
    for i in range(0, len(ids), 50):
        for v in get("videos", part="snippet,statistics,contentDetails",
                     id=",".join(ids[i:i + 50])).get("items", []):
            secs = parse_duration(v["contentDetails"].get("duration"))
            vids.append({
                "id": v["id"],
                "title": v["snippet"]["title"],
                "published": v["snippet"]["publishedAt"],
                "views": int(v["statistics"].get("viewCount", 0)),
                "duration_s": secs,
                "long_form": secs > SHORT_MAX_SECONDS,
            })

    cutoff = datetime.now(timezone.utc) - timedelta(days=a.mature_days)
    def mature(v):
        return datetime.fromisoformat(v["published"].replace("Z", "+00:00")) < cutoff

    long_mature = [v for v in vids if v["long_form"] and mature(v)]
    long_mature.sort(key=lambda v: v["published"], reverse=True)
    sample = long_mature[:a.sample]
    shorts = [v for v in vids if not v["long_form"] and mature(v)][:a.sample]

    if not sample:
        sys.exit(f"No long-form uploads older than {a.mature_days} days in the last "
                 f"{a.videos} videos. Raise --videos or lower --mature-days.")

    views = sorted(v["views"] for v in sample)
    recent6 = [v["views"] for v in long_mature[:6]]
    prior6 = [v["views"] for v in long_mature[6:12]]

    out = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "env_files": env_files,
        "key_source": key_name,
        "channel": {
            "title": ch["snippet"]["title"],
            "id": ch["id"],
            "subscribers": int(stats.get("subscriberCount", 0)),
            "total_views": int(stats.get("viewCount", 0)),
            "video_count": int(stats.get("videoCount", 0)),
        },
        "long_form": {
            "sample_size": len(sample),
            "mature_days": a.mature_days,
            "median_views": int(statistics.median(views)),
            "mean_views": int(statistics.mean(views)),
            "min_views": views[0],
            "max_views": views[-1],
            "trend_recent6_median": int(statistics.median(recent6)) if recent6 else None,
            "trend_prior6_median": int(statistics.median(prior6)) if prior6 else None,
        },
        "shorts": {
            "sample_size": len(shorts),
            "median_views": int(statistics.median([v["views"] for v in shorts])) if shorts else None,
        },
        "sampled_videos": sample,
    }

    lf = out["long_form"]
    print(f"{out['channel']['title']} — {out['channel']['subscribers']:,} subs, "
          f"{out['channel']['total_views']:,} total views")
    print(f"Long-form median (n={lf['sample_size']}, mature {a.mature_days}d): "
          f"{lf['median_views']:,} views   [range {lf['min_views']:,}–{lf['max_views']:,}]")
    if lf["trend_recent6_median"] and lf["trend_prior6_median"]:
        d = lf["trend_recent6_median"] / lf["trend_prior6_median"] - 1
        print(f"Trend: last 6 vs previous 6 → {d:+.0%}")
    if out["shorts"]["median_views"]:
        print(f"Shorts median (n={out['shorts']['sample_size']}): "
              f"{out['shorts']['median_views']:,} views")

    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\nWrote {a.out}")


if __name__ == "__main__":
    main()
