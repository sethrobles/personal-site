---
type: "blog"
title: "LED Array"
slug: "led-array"
date: "2025-09-06"
tags: ["KiCAD", "PCB Design"]
thumbnail: "../../projects/led-array/led-array-thumb.png"
# hero: "flask-week-hero.jpg"
summary: "Reflections on my first week diving deep into Flask, building small apps, and realizing the joys (and quirks) of web development with Python."
github_url: "https://github.com/sethrobles/led-array"
# live_url: "https://flask-week.demo.com"
show_toc: false
hidden: false
---

This is a blog describing the process of setting up my [LED Array project](https://sethrobles.github.io/projects/led-array.html). It was my first time laying out a multi-layer PCB, so much of the process was about learning to work with KiCAD.

A lot of the inspiration for this project came from [Phil's Lab STM32 help](https://www.youtube.com/watch?v=aVUqaB0IMh4). I learned a lot of the basics of laying out components in a schematic and routing the schematic. I also am very thankful to my friend Miguel, who provided an extraordinary amount of guidance and advice.

I'm working on setting up the PCB-layout in KiCAD, which I have nver done. There are 32x32 LEDs, so there's a lot of components to lay out and I don't want to do it on my own. Thankfully i have hiearchical sheets set up and am not trying to use replicate layout.

The schematic process was closely following what followed in the video. However, I decided to use a buck converter instead of the linear regulator for better efficiency and to try doing something new.

I decided to use hiearchical schematics for the LEDs to simplify the schematic and PCB process. I intended to use **Replicate Layout**, which can be downloaded in KiCAD's 'additional plug-ins manager.'
