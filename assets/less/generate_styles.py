#!/usr/bin/env python3

import subprocess

themeColors = [
    "#42A8C0", # Theme 1
    "#4CAC9D", # Theme 2
    "#5BB66F", # Theme 3
    "#A15277", # Theme 4
    "#FDA246", # Theme 5
    "#4B6A78", # Theme 6
]

counter = 0

for color in themeColors:
    counter += 1
    subprocess.run(["lessc", "--modify-var=theme-color=" + color, "./styles.less", "../../static/assets/css/styles-" + str(counter) + ".css" ])
