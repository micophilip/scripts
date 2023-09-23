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
category: leetcode
excerpt_separator: <!--more-->
author: mico
date: %s
---

A description of the other problem from leetcode
<!--more-->
more description goes here

```python
def greet():
  print('Hello world!')
```

## O-Notation:

$$\mathcal{O}(n\log{}n)$$

## Lessons Learnt:

## Notes:
* [Link to Problem](<<EDIT ME>>)
* [Link to Submission](<<EDIT ME>>)
* Runtime beats <<EDIT ME>> of `python3` submissions
* Memory usage beats <<EDIT ME>> of `python3` submissions
""" % (tag, timestamp)

with open(f'{jekyll_dir}/_posts/{date_only}-{post_title}.md', 'w+') as f:
  f.write(template)
