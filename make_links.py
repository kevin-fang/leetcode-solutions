#!/usr/bin/env python

import os

readme = """### LeetCode Solutions:

"""

def create_leetcode(filename):
    webpage_name = []
    for i in filename.split()[1:]:
        webpage_name.append(i.lower())

    return "https://leetcode.com/problems/" + "-".join(webpage_name)

def create_github(filename):
    prefix = "https://github.com/Kevin-Fang/leetcode-solutions/blob/master/"
    prefix += "%20".join(filename.split())
    return prefix

filenames = []
for filename in os.listdir("./"):
    if (filename.endswith(".py") or filename.endswith(".cpp")) and filename != "make_links.py":
        filenames.append(filename)

filenames = sorted(filenames, key=lambda x: int(x.split(".")[0]))
readme += "Total problems solved: {}\n\n".format(len(filenames))
for filename in filenames:
    no_ext_fn = "".join(filename.split(".")[0:2])
    link = create_leetcode(no_ext_fn)
    readme += "* [{filename}]({leetcode}): [Solution]({filename_link})\n\n".format(leetcode=link, filename=no_ext_fn, filename_link=create_github(filename))

with open("README.md", "w") as f:
    f.write(readme)
