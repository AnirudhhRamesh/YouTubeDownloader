# YouTube Downloader

This Python script allows you to download YouTube videos in high quality, with options to specify time ranges.

## Features

- Downloads YouTube videos in high resolution (up to 1080p)
- Merges video and audio streams for best quality
- Supports downloading specific time ranges of videos
- Automatically installs ffmpeg if not present (on Debian-based systems)
- User-friendly Streamlit interface

## Requirements

- Python 3.6+
- pytubefix
- ffmpeg (will be automatically installed on Debian-based systems)
- Streamlit

## Installation and Running

To install and run the YouTube Downloader, follow these steps:

1. Clone the repository, create a virtual environment, install dependencies, and run the app:

```bash
git clone https://github.com/AnirudhhRamesh/YouTubeDownloader.git && \
python3 -m venv venv && \
source venv/bin/activate && \
pip3 install -r requirements.txt && \
streamlit run app.py
```

## Usage

```python
from youtube_downloader import YoutubeDownloader

yt_downloader = YoutubeDownloader()
output_file = yt_downloader.download("https://www.youtube.com/watch?v=VIDEO_ID", start_time="00:01:30", end_time="00:03:45")
```

- `start_time` and `end_time` are optional parameters to specify a time range to download.
- The downloaded video will be saved in the current directory with the video title as the filename.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Disclaimer

This tool is for personal use only. Respect copyright laws and YouTube's terms of service when using this downloader.
