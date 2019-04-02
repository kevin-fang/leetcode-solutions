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
    if filename.endswith(".py") and filename != "make_links.py":
        filenames.append(filename)

filenames = sorted(filenames, key=lambda x: int(x.split(".")[0]))
for filename in filenames:
    link = create_leetcode(filename[:-3])
    readme += "* [{filename}]({leetcode}): [Solution]({filename_link})\n\n".format(leetcode=link, filename=filename[:-3], filename_link=create_github(filename))

with open("README.md", "w") as f:
    f.write(readme)
