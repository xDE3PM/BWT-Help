# 🚀 BWT-Uploader v1.0.5
**Torrent Upload Assistant for BWTorrents.Tv**

Upload torrents with ease using this assistant CLI.

**BWT-Uploader** is a powerful Python-based automation tool for uploading torrents to [BwTorrents](https://bwtorrents.tv). It automatically fetches metadata, handles MediaInfo, and generates BBCode descriptions — making the upload process fast and hassle-free.

> <strong>Created with ❤️ by [-=DE3PM=-](https://github.com/xDE3PM)</strong>

---

## 🚀 Features

- 🔍 **Auto Metadata Detection**
  - Fetches IMDb ID, TMDb ID, trailer link, poster, and more
- ⚙️ **Automatically Torrent Createor**
  - Generates `.torrent` file with optimal settings
- 📄 **Media Info Generator**
  - Extracts and formats technical details using MediaInfo
- 🖼️ **Automatically Screenshot Generate & Upload**
  - Captures screenshots and uploads them to your preferred image host
- 🧾 **BBCode Description Generator**
  - Includes poster, screenshots, MediaInfo, IMDb/TMDb/YouTube links
- 📁 **Smart Category Selector**
  - Automatically detects or manually sets the correct category
- 📡 **Freeleech Checker**
  - Calculates and checks if upload qualifies for freeleech
- 📤 **Automatically Upload Torrent**
  - Full automation from detection to upload
- 💻 **Command-line Friendly**
  - Flexible CLI arguments with custom options

---

## 🧰 Requirements

### 🛠️ System Tools (Required)

You must have these tools installed and accessible from your system’s PATH:

- [Python 3.9+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)
- [MediaInfo](https://mediaarea.net/en/MediaInfo)

---

## 🚀 How to Use

### 1. Edit the config file

```bash
config/example_config.py
```

---

### 2. Run installer

```bash
python install.py
```

> Enter your config file path when prompted.

---

### 3. Run uploader

```bash
bwt-uploader "path/to/your/file"
```

---

### 4. Show help

```bash
bwt-uploader --help
```

---

## 💡 CLI Help

```
usage: bwt-uploader [-h] [--config CONFIG] [--force-config] [--version]
                    [--imdb IMDB] [--tmdb TMDB]
                    [--category CATEGORY] [--freeleech]
                    [--request] [--recommended]
                    [--double-upload] [--no-tmdb]
                    [--no-imdb-tmdb] [--no-youtube]
                    [--piece-length PIECE_LENGTH]
                    [filepath]
```

### Options

| Option          | Shortcut | Description                  |
| --------------- | -------- | ---------------------------- |
| filepath        | —        | Path to file or directory    |
| --config        | -C       | Install config file          |
| --force-config  | -F       | Overwrite existing config    |
| --version       | -v       | Show version                 |
| --imdb          | -i       | IMDb ID (e.g., 1234567)      |
| --tmdb          | -t       | TMDb ID (e.g., 123456)       |
| --category      | -c       | Category ID (e.g., 119, 145) |
| --freeleech     | -f       | Enable freeleech             |
| --request       | -r       | Mark as request              |
| --recommended   | -R       | Mark as recommended          |
| --double-upload | -d       | Enable double upload         |
| --no-tmdb       | -T       | Skip TMDb metadata           |
| --no-imdb-tmdb  | -IT      | Skip IMDb & TMDb             |
| --no-youtube    | -Y       | Skip YouTube trailer         |
| --piece-length  | -p       | Piece length (2^n, 16–27)    |

---

## 📁 Category ID Reference

Use the following Category ID when using the `--catagory` or `-c` option:

<details>
<summary><strong>Click to expand full category list</strong></summary>

| Value | Category                       |
| ----- | ------------------------------ |
| 178   | Anime                          |
| 179   | Appz                           |
| 145   | Bangla-Movies                  |
| 143   | Bhoipuri-Movies                |
| 120   | Bollywood - 1080p WEB-Rips     |
| 188   | Bollywood - 720p WEB-Rips      |
| 123   | Bollywood - SDRips - WEB/DVD   |
| 125   | Bollywood- Web Series          |
| 116   | Bollywood-1080p BluRay Rips    |
| 124   | Bollywood-3D-Movies            |
| 114   | Bollywood-4K Ultra HD / Upscal |
| 117   | Bollywood-720p BluRay Rips     |
| 122   | Bollywood-DVDRips 1080p/720p   |
| 189   | Bollywood-Encoded DVDs         |
| 190   | Bollywood-Movie Packs          |
| 113   | Bollywood-Pre-Release          |
| 118   | Bollywood-Remuxes BluRay       |
| 115   | Bollywood-Untouched BluRay     |
| 121   | Bollywood-Untouched DVDs       |
| 119   | Bollywood-Untouched WEB-DLs    |
| 186   | Dangal-Tv                      |
| 175   | EBooks                         |
| 183   | English Movies Hindi Dubbed    |
| 177   | Games Console                  |
| 176   | Games PC                       |
| 185   | Gujarati-Movies                |
| 194   | Hollywood - Movie Packs        |
| 192   | Hollywood- 720p WEB-Rips       |
| 193   | Hollywood- SDRips - WEB/DVD    |
| 128   | Hollywood-1080p BluRay Rips    |
| 132   | Hollywood-1080p WEB-Rips       |
| 135   | Hollywood-3D-Movies            |
| 126   | Hollywood-4K Ultra HD / Upscal |
| 129   | Hollywood-720p BluRay Rips     |
| 130   | Hollywood-BluRay Remuxes       |
| 134   | Hollywood-DVDRips 1080p/720p   |
| 191   | Hollywood-Encoded DVDs         |
| 136   | Hollywood-Pre-Release          |
| 127   | Hollywood-Untouched BluRay     |
| 133   | Hollywood-Untouched DVDs       |
| 131   | Hollywood-Untouched WEB-DLs    |
| 141   | Kannada-Movies                 |
| 142   | Lollywood-Movies               |
| 137   | Malayalam-Movies               |
| 144   | Marathi-Movies                 |
| 180   | Mobile Stuff                   |
| 196   | Music Packs                    |
| 160   | Music-Classical                |
| 161   | Music-Flacs                    |
| 162   | Music-Ghazals                  |
| 163   | Music-Hindi OSTs               |
| 164   | Music-Instrumental             |
| 165   | Music-Kannada Music            |
| 166   | Music-Lollywood Music          |
| 167   | Music-Malayalam Music          |
| 168   | Music-Marathi Music            |
| 170   | Music-Pop-Music                |
| 171   | Music-Punjabi-Music            |
| 172   | Music-Remix                    |
| 173   | Music-Tamil Music              |
| 174   | Music-Telugu Music             |
| 169   | Music-Videos                   |
| 182   | Other Movies                   |
| 181   | Pics/Wallpapers                |
| 140   | Punjabi-Movies                 |
| 159   | Religion & Spirituality Audio  |
| 184   | South Hindi Dubbed             |
| 211   | Tamil-1080p/720p WEBRips       |
| 209   | Tamil-4K Ultra HD - Upscaled   |
| 216   | Tamil-BluRay Rips              |
| 215   | Tamil-Movie Packs              |
| 217   | Tamil-Remuxes BluRay           |
| 214   | Tamil-SD-WEBRips / DVDRips     |
| 212   | Tamil-Untouched BluRay         |
| 213   | Tamil-Untouched DVDs           |
| 210   | Tamil-Untouched WEB-DLs        |
| 201   | Telugu-1080p/720p WEBRips      |
| 199   | Telugu-4K Ultra HD - Upscaled  |
| 207   | Telugu-BluRay Rips             |
| 205   | Telugu-Movie Packs             |
| 208   | Telugu-Remuxes BluRay          |
| 204   | Telugu-SD-WEBRips / DVDRips    |
| 202   | Telugu-Untouched BluRay        |
| 203   | Telugu-Untouched DVDs          |
| 200   | Telugu-Untouched WEB-DLs       |
| 197   | Turkish Hindi Dubbed           |
| 147   | TV - &Tv                       |
| 219   | TV-Bengali                     |
| 146   | TV-Colors                      |
| 156   | TV-Documentary                 |
| 157   | TV-Hollywood                   |
| 218   | TV-Ishara TV                   |
| 221   | TV-JioTv                       |
| 148   | TV-Life OK                     |
| 198   | TV-MTV                         |
| 158   | TV-Others                      |
| 195   | TV-Packs                       |
| 149   | TV-Pakistani Dramas            |
| 150   | TV-Sab TV                      |
| 220   | TV-Shemaroo Umang              |
| 151   | TV-Sony                        |
| 155   | TV-Sports                      |
| 152   | TV-Star Bharat                 |
| 153   | TV-Star Plus                   |
| 154   | TV-Zee TV                      |

</details>

## 📁 Piece Size Length Info

Use the following Piece Size Length when using the `--piece-length` or `-p` option:

<details>
<summary>📏 <strong>Click to view Piece Size Length Info</strong></summary>

<br>

| Power (n) | Piece Size | Automatically for File Sizes     |
|-----------|------------|----------------------------------|
| 16        | 64 KiB     | < 100 MiB                        |
| 17        | 128 KiB    | 100–200 MiB                      |
| 18        | 256 KiB    | 200–400 MiB                      |
| 19        | 512 KiB    | 400–800 MiB                      |
| 20        | 1 MiB      | 800 MiB – 1.5 GiB                |
| 21        | 2 MiB      | 1.5 – 3 GiB                      |
| 22        | 4 MiB      | 3 – 6 GiB                        |
| 23        | 8 MiB      | 6 – 12 GiB                       |
| 24        | 16 MiB     | 12 – 25 GiB                      |
| 25        | 32 MiB     | 25 – 50 GiB                      |
| 26        | 64 MiB     | 50 – 100 GiB                     |
| 27        | 128 MiB    | 100+ GiB (Maximum recommended)   |

</details>

---

## 🤝 Contributing

Found a bug or have a feature suggestion?  
Feel free to open an [issue](https://github.com/xDE3PM/BWT-Uploader/issues) or [pull request](https://github.com/xDE3PM/BWT-Uploader/pulls).

---

## 🔗 Author
**[-= DE3PM =-](https://github.com/xDE3PM)**  
Proudly made for the BwT community ❤️  

## 💬 Join Discord
https://discord.gg/C6h9uXACZ9  

## 📢 Support
Need help, found a bug, or have suggestions?  
Feel free to reach out on Discord!
