# config.py v1.1.0

# MAIN CONFIGURATION

config = {
    
    # TMDb API key (used to fetch movie/TV metadata like title, poster, cast, etc.)
    # Get your API key here: https://www.themoviedb.org/settings/api
    "TMDb": {
        "API_KEY": ""  # YOUR_TMDB_API_KEY
    },
    
    # Include IMDb & TMDb information in the description (True/False)
    "imdb_and_tmdb_info": True,
    
    # Directory where upload logs will be stored
    "uploads_logs_directory": "", 
    
    # Number of screenshots to capture from the video file
    "screenshots_number": 6,

    # Screenshot capture options
    # Apply HDR -> SDR tonemap only for HDR sources
    "tonemap_hdr": True,
    # FFmpeg tonemap method/parameters (used when tonemap_hdr is enabled)
    "hdr_method": "reinhard:desat=0",
    # Extract frames from keyframes only
    "keyframes_only": True,
    # PNG compression level (0-9)
    "compression_level": 6,

    # Number of parallel threads for uploading screenshots
    "upload_threads": 3,

    # Primary image hosting service
    # Options: Freeimage, Imgbb, Imageride, Lookmyimg, Onlyimg, PTScreen
    "image_host": "Imageride",
    
    # Fallback image hosts (used if primary fails)
    "fallback_image_host": "Imgbb",
    "fallback_image_host_2": "Freeimage",

    # API keys for supported image hosts
    # Only required for the hosts you actually use
    "image_host_api_key": {
        "Freeimage": "",   # YOUR_FREEIMAGE_API_KEY
        "Imgbb": "",       # YOUR_IMGBB_API_KEY
        "Imageride": "",   # YOUR_IMAGERIDE_API_KEY
        "Lookmyimg": "",   # YOUR_LOOKMYIMG_API_KEY
        "Onlyimg": "",     # YOUR_ONLYIMG_API_KEY
        "PTScreen": ""     # YOUR_PTSCREEN_API_KEY
    },

    # BWTorrents Tracker Configuration
    
    "BWTorrents": {
        # Main site URL (alternatives available if down)
        "base_url": "https://bwtorrents.tv",

        # Tracker announce URL
        "announce_url": "https://bwtorrents.tv/announce.php",

        # Login credentials
        "username": "",  # YOUR_USERNAME
        "password": ""   # YOUR_PASSWORD
    },

    # BBCode Styling Configuration
    
    "bbcode": {

        # Banner displayed above MediaInfo
        "mediainfo_banner": "[img]https://i.ibb.co/DfF7Pbt/Media-Info.png[/img]",

        # Banner for BD/DVD info (if used)
        "bdinfo_banner": "[img]https://i.ibb.co/npQd6NX/BDInfo.png[/img]",
        "dvdinfo_banner": "[img]https://i.ibb.co/DD8cgDV0/DVDinfo.png[/img]",
        
        # Section headers styling
        "sections": {
            "general": "[b][color=green]★ General ★[/color][/b]",
            "video": "[b][color=blue]★ Video Track ★[/color][/b]",
            "audio": "[b][color=orange]★ Audio Track ★[/color][/b]",
            "subtitle": "[b][color=teal]★ Subtitle ★[/color][/b]",
            "chapters": "[b][color=red]★ Chapters ★[/color][/b]"
        },
    },
}


# MAIN DESCRIPTION TEMPLATE

# Default BBCode template for the torrent description.
# NOTE:
# You may customize the visual style and layout, but DO NOT remove the following placeholders:
# {file_name}, {media_info}, {screenshot_bbcode}, etc.

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

[b][size=5][color=green][font=Courier New]....Enjoying & Keep Seeding....[/font][/color][/size][/b]
[/center]
"""


# DETAILED MOVIE INFO TEMPLATE (TMDb / IMDb)

# This block generates rich metadata (poster, cast, ratings, overview)
# and is injected into the main BBCODE_TEMPLATE using {detailed_info}
# You may customize the visual style and layout, but DO NOT remove the following placeholders:
# {title}, ({year}, {poster}, etc.

DETAILED_BBCODE_TEMPLATE = """
[center]
[font=Arial][size=6][color=#00BFFF][b][i]{title} ({year})[/i][/b][/color][/size][/font]


[img]{poster}[/img]


{dblinks}
[/center]

[center]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/center]

[font=Courier New][size=4]
[color=#FF9900][b]Genre........:[/b][/color] {genres}  
[color=#FF9900][b]Released.....:[/b][/color] {release_date}  
[color=#FF9900][b]Runtime......:[/b][/color] {runtime}  
[color=#FF9900][b]Category.....:[/b][/color] {category}  

[color=#FF9900][b]Cast.........:[/b][/color] {cast}  
[color=#FF9900][b]Director.....:[/b][/color] {director}  
[color=#FF9900][b]Writers......:[/b][/color] {writers}  

[color=#FF9900][b]IMDb Rating..:[/b][/color] [b]{imdb_rating}/10[/b] {imdb_votes}  
[color=#FF9900][b]TMDb Rating..:[/b][/color] [b]{tmdb_rating}/10[/b] {tmdb_votes}  

[color=#00BFFF][b]Overview.....:[/b][/color] {overview}
[/size][/font]

[center]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/center]
"""
