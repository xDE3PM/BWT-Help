"""
==================== CONFIG HELP ====================

Fill the values below with your own details.

[TMDb]
- API_KEY:
  Your TMDb (The Movie Database) API key.
  Get it from: https://www.themoviedb.org/settings/api

[General Settings]
- imdb_and_tmdb_info:
  "True" or "False" → Add IMDb & TMDb info to description.

- uploads_logs_directory:
  Folder name where upload logs will be saved.

- screenshots_number:
  Number of screenshots to generate from the video.

- upload_threads:
  Number of parallel uploads (higher = faster but heavier).

[Image Hosting]
- image_host:
  Main image hosting service.
  Options: Freeimage, Imgbb, Imageride, Lookmyimg, Onlyimg, PTScreen

- fallback_image_host / fallback_image_host_2:
  Backup hosts if main one fails.

- image_host_api_key:
  Add API keys only for the hosts you use.

[BWTorrents]
- base_url:
  Tracker website URL.

- announce_url:
  Tracker announce URL (usually /announce.php).

- username:
  Your tracker username.

- password:
  Your tracker password.

[BBCode Settings]
- mediainfo_banner / bdinfo_banner / dvdinfo_banner:
  Image URLs for section banners.

- sections:
  Customize titles for MediaInfo sections.

- screenshot_banner:
  Banner shown above screenshots.

[BBCODE_TEMPLATE]
- Do NOT remove placeholders:
    {file_name}
    {media_info}
    {screenshot_bbcode}
- You can customize style, colors, fonts.

=====================================================
"""
