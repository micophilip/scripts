from datetime import datetime
import sys
import os

now = datetime.now()
tag = sys.argv[1]
post_title = sys.argv[2]
jekyll_dir = os.getenv('JEKYLL_DIR')
date_only = now.strftime('%Y-%m-%d')
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

template = """---
layout: post
tag: %s
title: <<EDIT ME>>
category: blog
excerpt_separator: <!--more-->
author: mico
date: %s
---

An introduction to the post topic
<!--more-->
Actual post goes here

Code if needed

```python
def greet():
  print('Hello world!')
```
""" % (tag, timestamp)

with open(f'{jekyll_dir}/_posts/{date_only}-{post_title}.md', 'w+') as f:
  f.write(template)
