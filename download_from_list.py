#!/usr/bin/env python

import os
import sys
from yt_dlp import YoutubeDL


def main(type):
    URLS = load_urls()
    opts = edit_opts(type)

    if 0 == len(URLS):
        return

    with YoutubeDL(opts) as ydl:
        error_code = ydl.download(URLS)
        print(error_code)

def load_urls():
    urls = []
    with open('urls.txt') as f:
        for line in f:
            urls.append(line.rstrip())

    return urls


def edit_opts(type):
    if 'audio' == type:
        opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
        opts['outtmpl'] = os.getcwd() +'\\audios\%(title)s.%(ext)s'
    elif 'video' == 'type':
        opts = {'format': 'best'}
        opts['outtmpl'] = os.getcwd() +'\\videos\%(title)s.%(ext)s'
    else:
        opts = {'format': 'best'}
        opts['outtmpl'] = os.getcwd() +'\\videos\%(title)s.%(ext)s'

    return opts


if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        type = args[1]
    else:
        type = "video"

    main(type)