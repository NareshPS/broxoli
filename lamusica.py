"""It downloads youtube videos as mp3.
"""
#Youtube
import youtube_dl

#Commandline arguments
from argparse import ArgumentParser

#Path manipulations
from pathlib import Path

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def parse_args():
    parser = ArgumentParser(description = 'It downloads the Youtube videos as mp3.')
    parser.add_argument(
        '-i', '--input_file',
        required = True, type = Path,
        help = 'It specifies the name of the file that contains Youtube video links [One per line].')

    args = parser.parse_args()

    return args.input_file

if __name__ == '__main__':
    #Input parameters
    input_file = parse_args()

    #Placeholder for video links
    video_links = None

    with input_file.open() as handle:
        video_links = handle.readlines()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_links)