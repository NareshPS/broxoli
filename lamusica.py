"""It downloads youtube videos as mp3.
"""
#Youtube
import youtube_dl

#Commandline arguments
from argparse import ArgumentParser

#Path manipulations
from pathlib import Path

audio_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

video_opts = {
    'format': 'bestvideo/best',
    'outtmpl': '%(title)s.%(ext)s'
}

def parse_args():
    parser = ArgumentParser(description = 'It downloads the content from YouTube.')

    parser.add_argument(
        '-i', '--input_file',
        required = True, type = Path,
        help = 'It specifies the name of the file that contains Youtube video links [One per line].')
    parser.add_argument(
        '--video',
        action = 'store_true',
        help = 'It switches to the video download.')

    args = parser.parse_args()

    return args.input_file, args.video

if __name__ == '__main__':
    #Input parameters
    input_file, video = parse_args()

    #Derived parameters
    ydl_opts = video_opts if video else audio_opts

    #Placeholder for video links
    video_links = None

    with input_file.open() as handle:
        video_links = handle.readlines()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_links)
