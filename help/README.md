# 🚀 BWT-Uploader
**Torrent Upload Assistant for BWTorrents.Tv**

Upload torrents with ease using this assistant CLI.

**BWT-Uploader** is a powerful Python-based automation tool for uploading torrents to [BwTorrents](https://bwtorrents.tv). It automatically fetches metadata, handles MediaInfo, and generates BBCode descriptions — making the upload process fast and hassle-free.

> <strong>Created with ❤️ by [-=DE3PM=-](https://github.com/xDE3PM)</strong>

---

## ✨ Features

- **Automatic metadata detection** — retrieves IMDb ID, TMDb ID, trailer links, posters, and all essential metadata from the filename
- **Automated torrent creator** — generates optimized `.torrent` files with correct announce URL and automatic piece-size selection
- **Advanced media information extraction** — supports MediaInfo, DVDInfo, and BDInfo for standard video, DVD, and Blu-ray formats
- **Automated screenshot capture and upload** — ffmpeg-based with HDR → SDR tonemap support and parallel uploads to your preferred image host
- **BBCode description generator** — creates complete descriptions with poster, screenshots, MediaInfo, and IMDb / TMDb / YouTube links
- **Smart category detection** — automatically determines the correct upload category, with full manual override via `--category`
- **Freeleech eligibility checker** — evaluates freeleech qualification based on configurable size thresholds
- **Fully automated torrent upload** — seamless end-to-end workflow from metadata detection to final upload in a single command
- **CLI-friendly and highly customizable** — flexible arguments for every stage, with interactive name correction on-the-fly

---

## Requirements

### System Tools (Required)

You must have these tools installed and accessible from your system's PATH:

- [Python 3.9+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)
- [MediaInfo](https://mediaarea.net/en/MediaInfo)

---

## How to Use

### 1. Install latest version

```bash
pip install bwt-uploader
```

Or install a specific version:

```bash
pip install bwt-uploader==1.1.3
```

---

### 2. Config set up

Install the example config:

```bash
bwt --config /path/to/config.example.py
```

Or copy it manually:

```
~/.bwt-uploader/config.py
```

Open the file and fill in at minimum:

| Key | Description |
|-----|-------------|
| `TMDb.API_KEY` | Your [TMDb API key](https://www.themoviedb.org/settings/api) |
| `BWTorrents.username` | Your BWTorrents username |
| `BWTorrents.password` | Your BWTorrents password (or use saved cookie) |
| `image_host` | Primary image host (e.g. `Imageride`) |
| `image_host_api_key` | API key for your chosen image host |

Optional proxy (for regions where TMDb is blocked):

```python
"proxy": "http://user:pass@proxy.example.com:8080",
# or
"proxy": "socks5://127.0.0.1:1080",
```

---

### 3. Run uploader

```bash
bwt-uploader "path/to/your/file"
```
or
```bash
bwt "path/to/your/file"
```

---

### 4. Show help

```bash
bwt-uploader --help
```

---

## CLI Options

```
usage: bwt-uploader [-h] [--config CONFIG] [--force-config] [--version]
                    [--imdb IMDB] [--tmdb TMDB] [--category CATEGORY]
                    [--freeleech] [--request] [--recommended]
                    [--double-upload] [--no-tmdb] [--no-imdb-tmdb]
                    [--no-youtube] [--piece-length N]
                    [--dry-run] [--name NAME] [--output DIR]
                    [--skip-screenshots] [--num-screenshots N]
                    [--no-confirm] [--skip-screenshot-upload]
                    [--year YEAR] [--imdb-api VER] [--proxy URL]
                    [filepath]
```

| Option | Short | Description |
|--------|-------|-------------|
| `filepath` | — | Path to file or directory to upload |
| `--config` | `-C` | Install a config file to `~/.bwt-uploader/config.py` |
| `--force-config` | `-F` | Overwrite existing config without prompting |
| `--version` | `-v` | Show version and exit |
| `--imdb` | `-i` | IMDb ID or URL (e.g. `tt1375666` or full URL) |
| `--tmdb` | `-t` | TMDb ID or URL (e.g. `27205` or full URL) |
| `--category` | `-c` | Category ID (e.g. `119`, `145`) |
| `--freeleech` | `-f` | Force freeleech flag on this upload |
| `--request` | `-r` | Mark as request fulfillment |
| `--recommended` | `-R` | Mark as recommended upload |
| `--double-upload` | `-d` | Enable double upload mode |
| `--no-tmdb` | `-T` | Skip TMDb metadata fetch |
| `--no-imdb-tmdb` | `-IT` | Skip all DB fetching; derive category from file audio language |
| `--no-youtube` | `-Y` | Skip YouTube trailer lookup |
| `--piece-length` | `-p` | Piece length as `2^n` (16–27); auto-selected if omitted |
| `--dry-run` | `-D` | Run full pipeline but skip the actual upload |
| `--name` | `-n` | Set the BWT torrent name directly (skips interactive name prompt) |
| `--output` | `-o` | Override the upload output / log directory |
| `--skip-screenshots` | `-S` | Skip screenshot generation and upload entirely |
| `--num-screenshots` | `-N` | Number of screenshots to generate (overrides config value) |
| `--no-confirm` | — | Auto-confirm all yes/no prompts (for scripted / non-interactive use) |
| `--skip-screenshot-upload` | `-U` | Generate screenshots but skip uploading them to the image host |
| `--year` | `-y` | Override the year used in the BWT name (e.g. `1999`) |
| `--imdb-api` | — | IMDb API version: `v1`, `v2`, `v1+v2`, `v2+v1` |
| `--proxy` | — | Proxy URL for all outbound requests (e.g. `socks5://127.0.0.1:1080`) |

### Examples

```bash
# Upload a single file
bwt /path/to/Movie.2024.BluRay.mkv

# Upload a Blu-ray disc folder
bwt /path/to/Bluray Disk/

# Supply IMDb / TMDb IDs directly (skips auto-search)
bwt -i tt1375666 -t 27205 /path/to/Movie.mkv

# Use a proxy (useful when TMDb is blocked in your region)
bwt --proxy socks5://127.0.0.1:1080 /path/to/Movie.mkv

# Dry run — full pipeline, no upload
bwt --dry-run /path/to/Movie.mkv

# Skip screenshots entirely
bwt --skip-screenshots /path/to/Movie.mkv

# Non-interactive / scripted upload
bwt --no-confirm --dry-run /path/to/Movie.mkv
```

---

## Interactive Name Correction

When the auto-built upload name is displayed, you can answer **N** to enter correction args inline instead of restarting the process.

```
Correction args (combine freely, e.g. -t 12345 --year 1998):
  -i / --imdb   <id or url>   Re-fetch with a different IMDb ID / URL
  -t / --tmdb   <id or url>   Re-fetch with a different TMDb ID / URL
  --year        <year>        Override year  (e.g. 1999)
  --title       <title>       Override movie/show title
  --aka         <aka>         Set / replace AKA
  --no-aka                    Remove AKA entirely
  --res         <res>         Override resolution  (e.g. 1080p)
  --hdr         <hdr>         Override HDR tag  (e.g. DV HDR)
  --no-hdr                    Remove HDR tag
  --audio       <audio>       Override audio tag  (e.g. DD+ 5.1)
  --codec       <codec>       Override video codec tag
  --source      <source>      Override source  (e.g. BluRay)
  --edition     <edition>     Override edition
  --service     <service>     Override streaming service tag
  --tag         <group>       Override release group tag
  -n / --name   <full name>   Replace the entire BWT name manually
  -q / --quit                 Quit / exit uploader
```

When you supply `-i` or `-t`, the missing ID is **automatically resolved** (IMDb → TMDb or TMDb → IMDb) and a confirmation panel shows both IDs and links before the metadata is re-fetched.

---

## Category ID Reference

Use with `--category` / `-c`:

<details>
<summary><strong>Click to expand full category list</strong></summary>

| Value | Category |
|-------|----------|
| 178 | Anime |
| 179 | Appz |
| 145 | Bangla-Movies |
| 143 | Bhoipuri-Movies |
| 120 | Bollywood - 1080p WEB-Rips |
| 188 | Bollywood - 720p WEB-Rips |
| 123 | Bollywood - SDRips - WEB/DVD |
| 125 | Bollywood - Web Series |
| 116 | Bollywood - 1080p BluRay Rips |
| 124 | Bollywood - 3D Movies |
| 114 | Bollywood - 4K Ultra HD / Upscaled |
| 117 | Bollywood - 720p BluRay Rips |
| 122 | Bollywood - DVDRips 1080p/720p |
| 189 | Bollywood - Encoded DVDs |
| 190 | Bollywood - Movie Packs |
| 113 | Bollywood - Pre-Release |
| 118 | Bollywood - Remuxes BluRay |
| 115 | Bollywood - Untouched BluRay |
| 121 | Bollywood - Untouched DVDs |
| 119 | Bollywood - Untouched WEB-DLs |
| 186 | Dangal TV |
| 175 | EBooks |
| 183 | English Movies Hindi Dubbed |
| 177 | Games Console |
| 176 | Games PC |
| 185 | Gujarati-Movies |
| 194 | Hollywood - Movie Packs |
| 192 | Hollywood - 720p WEB-Rips |
| 193 | Hollywood - SDRips - WEB/DVD |
| 128 | Hollywood - 1080p BluRay Rips |
| 132 | Hollywood - 1080p WEB-Rips |
| 135 | Hollywood - 3D Movies |
| 126 | Hollywood - 4K Ultra HD / Upscaled |
| 129 | Hollywood - 720p BluRay Rips |
| 130 | Hollywood - BluRay Remuxes |
| 134 | Hollywood - DVDRips 1080p/720p |
| 191 | Hollywood - Encoded DVDs |
| 136 | Hollywood - Pre-Release |
| 127 | Hollywood - Untouched BluRay |
| 133 | Hollywood - Untouched DVDs |
| 131 | Hollywood - Untouched WEB-DLs |
| 141 | Kannada-Movies |
| 142 | Lollywood-Movies |
| 137 | Malayalam-Movies |
| 144 | Marathi-Movies |
| 180 | Mobile Stuff |
| 196 | Music Packs |
| 160 | Music - Classical |
| 161 | Music - Flacs |
| 162 | Music - Ghazals |
| 163 | Music - Hindi OSTs |
| 164 | Music - Instrumental |
| 165 | Music - Kannada Music |
| 166 | Music - Lollywood Music |
| 167 | Music - Malayalam Music |
| 168 | Music - Marathi Music |
| 170 | Music - Pop Music |
| 171 | Music - Punjabi Music |
| 172 | Music - Remix |
| 173 | Music - Tamil Music |
| 174 | Music - Telugu Music |
| 169 | Music - Videos |
| 182 | Other Movies |
| 181 | Pics / Wallpapers |
| 140 | Punjabi-Movies |
| 159 | Religion & Spirituality Audio |
| 184 | South Hindi Dubbed |
| 211 | Tamil - 1080p/720p WEBRips |
| 209 | Tamil - 4K Ultra HD / Upscaled |
| 216 | Tamil - BluRay Rips |
| 215 | Tamil - Movie Packs |
| 217 | Tamil - Remuxes BluRay |
| 214 | Tamil - SD WEBRips / DVDRips |
| 212 | Tamil - Untouched BluRay |
| 213 | Tamil - Untouched DVDs |
| 210 | Tamil - Untouched WEB-DLs |
| 201 | Telugu - 1080p/720p WEBRips |
| 199 | Telugu - 4K Ultra HD / Upscaled |
| 207 | Telugu - BluRay Rips |
| 205 | Telugu - Movie Packs |
| 208 | Telugu - Remuxes BluRay |
| 204 | Telugu - SD WEBRips / DVDRips |
| 202 | Telugu - Untouched BluRay |
| 203 | Telugu - Untouched DVDs |
| 200 | Telugu - Untouched WEB-DLs |
| 197 | Turkish Hindi Dubbed |
| 147 | TV - &TV |
| 219 | TV - Bengali |
| 146 | TV - Colors |
| 156 | TV - Documentary |
| 157 | TV - Hollywood |
| 218 | TV - Ishara TV |
| 221 | TV - JioTV |
| 148 | TV - Life OK |
| 198 | TV - MTV |
| 158 | TV - Others |
| 195 | TV - Packs |
| 149 | TV - Pakistani Dramas |
| 150 | TV - Sab TV |
| 220 | TV - Shemaroo Umang |
| 151 | TV - Sony |
| 155 | TV - Sports |
| 152 | TV - Star Bharat |
| 153 | TV - Star Plus |
| 154 | TV - Zee TV |

</details>

---

## Piece Size Reference

Used with `--piece-length` / `-p`. If omitted, the correct size is chosen automatically based on file size.

<details>
<summary><strong>Click to expand piece size table</strong></summary>

<br>

| Power (n) | Piece Size | Auto-selected for file sizes |
|-----------|------------|------------------------------|
| 16 | 64 KiB | < 100 MiB |
| 17 | 128 KiB | 100 – 200 MiB |
| 18 | 256 KiB | 200 – 400 MiB |
| 19 | 512 KiB | 400 – 800 MiB |
| 20 | 1 MiB | 800 MiB – 1.5 GiB |
| 21 | 2 MiB | 1.5 – 3 GiB |
| 22 | 4 MiB | 3 – 6 GiB |
| 23 | 8 MiB | 6 – 12 GiB |
| 24 | 16 MiB | 12 – 25 GiB |
| 25 | 32 MiB | 25 – 50 GiB |
| 26 | 64 MiB | 50 – 100 GiB |
| 27 | 128 MiB | 100+ GiB (maximum recommended) |

</details>

---

## Configuration Reference

The config file lives at `~/.bwt-uploader/config.py`. Key options:

| Key | Default | Description |
|-----|---------|-------------|
| `TMDb.API_KEY` | `""` | TMDb API key (required) |
| `proxy` | `""` | HTTP/HTTPS/SOCKS5 proxy URL (optional) |
| `imdb_api` | `"v2"` | IMDb library: `v1`, `v2`, `v1+v2`, `v2+v1` |
| `imdb_and_tmdb_info` | `true` | Include metadata block in description |
| `auto_build_title` | `true` | Auto-generate upload title from metadata |
| `aka_on_title` | `true` | Append AKA to title when available |
| `screenshots_number` | `6` | Number of screenshots to capture |
| `tonemap_hdr` | `true` | Apply HDR → SDR tonemap for HDR sources |
| `keyframes_only` | `true` | Capture from keyframes only (faster) |
| `compression_level` | `6` | PNG compression level (0–9) |
| `image_host` | `""` | Primary image host (required) |
| `fallback_image_host` | `""` | Fallback image host (required) |
| `upload_threads` | `3` | Parallel screenshot upload threads |
| `update_notification` | `true` | Show update notice at startup |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `httpx` | Async HTTP client for TMDb and tiffara REST API |
| `niquests` | HTTP client for IMDb scraping (WAF-aware) |
| `cloudscraper` | Tracker session with Cloudflare bypass |
| `lxml` | HTML parsing for IMDb `__NEXT_DATA__` extraction |
| `pydantic` | Data models and validation |
| `jmespath` | JSON path queries on IMDb response data |
| `pymediainfo` | MediaInfo Python bindings |
| `guessit` | Filename / title guessing |
| `rich` | Terminal output formatting |
| `bencode.py` | Torrent file encoding |
| `langcodes` | Language code → display name conversion |
| `imdbinfo-aws` | AWS WAF challenge solver for IMDb scraping |

---

## Contributing

Found a bug or have a feature suggestion?  
Feel free to open an [issue](https://github.com/xDE3PM/BWT-Uploader/issues) or [pull request](https://github.com/xDE3PM/BWT-Uploader/pulls).

---

## 🔗 Author

**[-= DE3PM =-](https://github.com/xDE3PM)**  
Proudly made for the BwT community ❤️

## 💬 Join Discord

https://discord.gg/5EHUfpNkDk

## 📢 Support

Need help, found a bug, or have suggestions?  
Feel free to reach out on Discord!

---

*MIT License — © 2026 -=DE3PM=-*
