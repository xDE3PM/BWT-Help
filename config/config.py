# config.example.py
# BWT-Uploader Configuration File v1.1.4
#
# HOW TO INSTALL:
#   bwt --config /path/to/config.example.py
#   or copy manually to: ~/.bwt-uploader/config.py
#
# Created by -= DE3PM =-

# ─────────────────────────────────────────────────────────────────────────────
# MAIN CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

config = {

    # ── TMDb ─────────────────────────────────────────────────────────────────
    # TMDb API key (used to fetch movie/TV metadata: title, poster, cast, etc.)
    # Get your key: https://www.themoviedb.org/settings/api
    "TMDb": {
        "API_KEY": ""           # YOUR_TMDB_API_KEY  (Required)
    },

    # ── Proxy ─────────────────────────────────────────────────────────────────
    # HTTP/HTTPS or SOCKS5 proxy for all outbound TMDb (and IMDb) requests.
    # Useful when the TMDb API is blocked in your region.
    # Leave empty ("") or omit to disable.
    #
    # Examples:
    #   "http://user:pass@proxy.example.com:8080"
    #   "socks5://127.0.0.1:1080"
    "proxy": "",

    # ── IMDb API version ──────────────────────────────────────────────────────
    # "v2"    → imdbapi   ( imdbapi tiffara.com)  [default]
    # "v1"    → imdbinfo  (IMDb GraphQL / HTML scraping only)
    # "v1+v2" → imdbinfo first, fall back to imdbapi on failure
    # "v2+v1" → imdbapi  first, fall back to imdbinfo on failure
    "imdb_api": "v2+v1",

    # ── Update notification ───────────────────────────────────────────────────
    # True  → print a notice at startup when a newer version is available
    # False → suppress the notice (forced updates still apply regardless)
    "update_notification": True,

    # ── Metadata options ──────────────────────────────────────────────────────
    # Include IMDb & TMDb info block in the torrent description (True/False)
    "imdb_and_tmdb_info": True,

    # Automatically build the BWT upload title from metadata (True/False)
    # True  → generate a clean title using DB metadata + media tags
    # False → use the raw file/folder name as-is (no processing)
    "auto_build_title": True,

    # Include AKA (alternative title) in the BWT upload title (True/False)
    # True  → append AKA when one is available  e.g. "Title AKA Alt Title"
    # False → never include AKA
    "aka_on_title": True,

    # ── Logo ──────────────────────────────────────────────────────────────────
    # Show the movie / TV series logo image in the description (True/False)
    # True  → fetch the logo from TMDb and embed it above the poster
    #         (only shown when a logo actually exists for the configured language)
    # False → no logo (poster only)
    "show_logo": True,

    # Language code for the logo to fetch from TMDb (ISO 639-1, e.g. "en", "hi")
    # Only a logo that exactly matches this language is used.
    # If no logo exists for this language, NO logo is shown — there is no
    # language-neutral fallback.  Default is "en".
    "logo_language": "en",

    # ── Paths ─────────────────────────────────────────────────────────────────
    # Directory where upload logs and output files are stored
    # Windows users: use a raw string  r"C:\Users\You\BWT-Uploader\Uploads"
    "uploads_logs_directory": "",   # leave blank to use default ~/Downloads/BWT-Uploader/Uploads

    # ── Screenshots ───────────────────────────────────────────────────────────
    # Number of screenshots to capture from the video
    "screenshots_number": 6,

    # Apply HDR → SDR tonemap for HDR sources before capturing (True/False)
    "tonemap_hdr": True,

    # FFmpeg tonemap method (used when tonemap_hdr is True)
    "hdr_method": "reinhard:desat=0",

    # Capture from keyframes only — faster but less accurate timestamps (True/False)
    "keyframes_only": True,

    # PNG compression level (0 = none / fastest, 9 = maximum / slowest)
    "compression_level": 6,

    # ── Image hosting ─────────────────────────────────────────────────────────
    # Number of parallel upload threads
    "upload_threads": 3,

    # Primary image host
    # Options: Freeimage, Imgbb, Imageride, Lookmyimg, Onlyimg, PTScreen
    "image_host": "",               # (Required)

    # Fallback hosts — used in order if the primary fails
    "fallback_image_host": "",      # (Required)
    "fallback_image_host_2": "",    # (Optional)

    # API keys for image hosts
    # Only fill in the keys for the hosts you actually use.
    "image_host_api_key": {
        "Freeimage":  "",           # YOUR_FREEIMAGE_API_KEY
        "Imgbb":      "",           # YOUR_IMGBB_API_KEY
        "Imageride":  "",           # YOUR_IMAGERIDE_API_KEY
        "Lookmyimg":  "",           # YOUR_LOOKMYIMG_API_KEY
        "Onlyimg":    "",           # YOUR_ONLYIMG_API_KEY
        "PTScreen":   "",           # YOUR_PTSCREEN_API_KEY
    },

    # ── BWTorrents tracker ────────────────────────────────────────────────────
    "BWTorrents": {
        # Main site URL
        "base_url": "https://bwtorrents.tv",

        # Tracker announce URL (used when creating .torrent files)
        "announce_url": "https://bwtorrents.tv/announce.php",

        # Login credentials
        "username": "",             # YOUR_USERNAME  (Required)
        "password": "",             # YOUR_PASSWORD  (optional if using a saved cookie)
    },

    # ── BBCode styling ────────────────────────────────────────────────────────
    "bbcode": {

        # Banner image displayed above the MediaInfo block
        "mediainfo_banner": "[img]https://i.ibb.co/DfF7Pbt/Media-Info.png[/img]",

        # Banner for BDInfo output (Blu-ray disc uploads)
        "bdinfo_banner": "[img]https://i.ibb.co/npQd6NX/BDInfo.png[/img]",

        # Banner for DVD info output
        "dvdinfo_banner": "[img]https://i.ibb.co/DD8cgDV0/DVDinfo.png[/img]",

        # Section header labels (BBCode — customise colours/fonts freely)
        "sections": {
            "general": "[size=4][color=#00FF7F]★ General ★[/color][/size]",
            "video": "[size=4][color=#00BFFF]★ Video Track ★[/color][/size]",
            "audio": "[size=4][color=#FF6D00]★ Audio Track ★[/color][/size]",
            "subtitle": "[size=4][color=#00E5C3]★ Subtitle ★[/color][/size]",
            "chapters": "[size=4][color=#FF0000]★ Chapters ★[/color][/size]"
        },
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# MAIN DESCRIPTION TEMPLATE
# ─────────────────────────────────────────────────────────────────────────────
#
# Default BBCode template for the torrent description.
# Customise the visual style freely, but do NOT remove any {placeholders} —
# they are substituted automatically by the description builder.
#
# Available placeholders:
#   {detailed_info}      — rich metadata block (poster, cast, ratings, overview)
#   {file_name}          — release name
#   {info_banner}        — MediaInfo / BDInfo / DVDInfo banner image
#   {media_info}         — full MediaInfo / BDInfo text output
#   {screenshot_bbcode}  — uploaded screenshot BBCode tags

BBCODE_TEMPLATE = """
{detailed_info}

[center]
[b][size=4][color=red]
[font=Arial]{file_name}[/font][/color]
[/size][/b]

{info_banner}

[quote]
{media_info}
[/quote]

[img]https://i.ibb.co/9vZTnQk/Screenshot.png[/img]

{screenshot_bbcode}

[i][b][size=5][color=#00BFFF][font=Georgia]Enjoy the download and please keep seeding![/font][/color][/size][/b][/i]
[/center]
"""


# ─────────────────────────────────────────────────────────────────────────────
# DETAILED MOVIE INFO TEMPLATE  (TMDb / IMDb metadata block)
# ─────────────────────────────────────────────────────────────────────────────
#
# Injected into BBCODE_TEMPLATE via {detailed_info}.
# Do NOT remove any {placeholders}.
#
# Available placeholders:
#   {title}        — movie / show title
#   {year}         — release year
#   {poster}       — poster image URL
#   {logo}         — logo image BBCode (empty string when show_logo=False or no logo found)
#   {dblinks}      — IMDb + TMDb links
#   {genres}       — genre list
#   {release_date} — release date
#   {runtime}      — runtime (e.g. 2h 15min)
#   {category}     — BWT category name
#   {director}     — director(s)
#   {writers}      — writer(s)
#   {cast}         — top cast members
#   {imdb_rating}  — IMDb rating
#   {imdb_votes}   — IMDb vote count
#   {tmdb_rating}  — TMDb rating
#   {tmdb_votes}   — TMDb vote count
#   {overview}     — plot overview

DETAILED_BBCODE_TEMPLATE = """
[center]
[font=Arial][size=6][color=#00BFFF][b][i]{title} ({year})[/i][/b][/color][/size][/font]

{logo}
[img]{poster}[/img]


{dblinks}
[/center]

[center]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/center]

[quote][pre][size=4]
[color=#FF9900][b]Genre........:[/b][/color] {genres}  
[color=#FF9900][b]Released.....:[/b][/color] {release_date}
[color=#FF9900][b]Runtime......:[/b][/color] {runtime}
[color=#FF9900][b]Category.....:[/b][/color] {category}

[color=#FF9900][b]Director.....:[/b][/color] {director}
[color=#FF9900][b]Writers......:[/b][/color] {writers}
[color=#FF9900][b]Cast.........:[/color][/pre] [font=Courier New]{cast}[/font][/b][pre]

[color=#FF9900][b]IMDb Rating..:[/color] {imdb_rating}/10[/b] {imdb_votes}
[color=#FF9900][b]TMDb Rating..:[/color] {tmdb_rating}/10[/b] {tmdb_votes}

[color=#00BFFF][b]Overview.....:[/color][/pre] [font=Courier New]{overview}[/font][/b]
[/size]
[/quote]

[center]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/center]
"""
