BWT Uploader – Configuration Guide (v1.0.5)

This guide explains how to configure the config.py file for the BWT Uploader tool.


---

🔑 1. TMDb API Configuration

"TMDb": {
    "API_KEY": ""
}

Required to fetch movie/TV metadata

Get API key: https://www.themoviedb.org/settings/api



---

🎬 2. IMDb & TMDb Info Toggle

"imdb_and_tmdb_info": "True"

True → Enable metadata

False → Disable metadata



---

📂 3. Upload Logs Directory

"uploads_logs_directory": "Downloads/BWT-Uploader/Uploads"

Stores upload logs



---

📸 4. Screenshots Settings

"screenshots_number": 6

Number of screenshots per video



---

⚡ 5. Upload Threads

"upload_threads": 3

Parallel uploads

Recommended: 2–5



---

🖼️ 6. Image Hosting

Primary Host

"image_host": "Imageride"

Options:

Freeimage

Imgbb

Imageride

Lookmyimg

Onlyimg

PTScreen


Fallback Hosts

"fallback_image_host": "Imgbb"
"fallback_image_host_2": "Freeimage"


---

🔐 7. Image Host API Keys

"image_host_api_key": {
    "Freeimage": "",
    "Imgbb": "",
    "Imageride": "",
    "Lookmyimg": "",
    "Onlyimg": "",
    "PTScreen": ""
}

Add keys only for used services



---

🌐 8. BWTorrents Account

"BWTorrents": {
    "base_url": "https://bwtorrents.tv",
    "announce_url": "https://bwtorrents.tv/announce.php",
    "username": "",
    "password": ""
}

Alternative domains:

https://bwtorrents.cc

https://bwtorrents.xyz

https://bwtorrents.us



---

🎨 9. BBCode Styling

Media Info Banners

"mediainfo_banner": "[img]...[/img]",
"bdinfo_banner": "[img]...[/img]",
"dvdinfo_banner": "[img]...[/img]"

Sections

"sections": {
    "general": "...",
    "video": "...",
    "audio": "...",
    "subtitle": "...",
    "chapters": "..."
}

Screenshot Banner

"screenshot_banner": "[img]...[/img]"


---

🧩 10. BBCode Template

BBCODE_TEMPLATE = """
{header}

[center]
[b][size=4][color=red]
[font=Arial]{file_name}[/font][/color]
[/size][/b]

{media_info}

{screenshot_header}

{screenshot_bbcode}

[b][size=5][color=green][font=Courier New]
....Enjoying & Keep Seeding....
[/font][/color][/size][/b]
[/center]
"""

⚠️ Do NOT remove placeholders:

{header}

{file_name}

{media_info}

{screenshot_header}

{screenshot_bbcode}



---

🚀 Done!

You are ready to use the uploader.

Happy Uploading & Keep Seeding!
