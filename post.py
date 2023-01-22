#!/usr/bin/env python

import os, re, datetime

title = input('Post title: ')

filename = title.strip().lower()
filename = re.sub(r'[^a-zA-Z0-9\s]', '', filename)
filename = re.sub('\s+', '-', filename)
filename = str(datetime.date.today()) + '-' + filename

header = '---\n'
header += 'title: ' + title + '\n'
header += 'date: ' + str(datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z')) + '\n'
header += '---\n'

filepath = os.path.join('./_posts', filename)

if not os.path.isfile(filepath):
    post = open(filepath, 'a')

    post.write(header)

    post.close()
else:
    print('Oops! That already exists!')


