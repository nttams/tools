# This program converts subtitle file type SRT to VTT
# Both are simple, but VTT is native supported by html5

import json
import os

def read_file(file_path):
    try:
        f = open(file_path, 'r')
        data = f.read()
        f.close()
    except Exception as err:
        raise Exception('error: ', err)

    return data

def write_file(file_path, content):
    f = open(file_path, 'w')
    f.write(content)
    f.close()

def convert_srt_to_vtt(lines):
    result = "WEBVTT\n\n"
    for line in lines.splitlines():
        if line.find("-->") != -1:
            line = line.replace(",", ".")
        result += line + "\n"

    return result

def convert_file_srt_to_vtt(file_path):
    lines = read_file(file_path)
    result = convert_srt_to_vtt(lines)

    name_without_ext = os.path.splitext(file_path)[0]

    write_file(name_without_ext + ".vtt", result)

def main():
    files = os.listdir('./')

    for f in files:
        if f.endswith(".srt"):
            convert_file_srt_to_vtt(f)

if __name__ == '__main__':
    main()