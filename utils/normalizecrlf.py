#!python
# -*- coding: utf-8 -*-
# 
# Normalize line endings
#

import os
import os.path
import re

def normalize(path):
  f = open(path, 'rb')
  content = f.read()
  f.close()
  try:
    content = content.decode(encoding='UTF-8', errors='strict')
    contentold = content
    content = content.replace('\r\n', '\n').replace('\n', '\r\n')
    if content == contentold:
    	return False
    content = content.decode(encoding='UTF-8', errors='strict')
  except UnicodeError:
    return False
  f = open(path, 'wb')
  f.write(content)
  f.close()
  return True

def convertTree(start, pattern):
  regex = re.compile(pattern)
  for path in [
    os.path.join(root, n)
    for root, dirs, files in os.walk(start)
    for n in files if regex.search(n) is not None
  ]:
    converted = normalize(path)
    if converted:
      print('CONVERTED:', path)
    else:
      print('SKIPPED:', path)

if __name__ == '__main__':
  start = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  convertTree(start, r'\.(cs|sln|csproj|xml|resx)$');
