#!/usr/bin/env python

# convert markdown (md) file to html

import json
import os
import markdown

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

def main():
    files = ["cs", "cs_sql"]
    for file in files:
        md = read_file(file + ".md")
        html = markdown.markdown(md)
        write_file(file + ".html", html)

if __name__ == '__main__':
    main()