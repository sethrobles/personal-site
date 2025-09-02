---
type: "project"
title: "2.00 Library Tracker"
slug: "2-00-library-tracker"
date: "2024-05-10"
tags: ["Arduino", "Education", "Hardware", "Team Project"]
thumbnail: "library_tracker.jpg"
summary: "An Arduino-powered Library Tracker tool built for an elementary school librarian to help manage student tasks with LEDs, buttons, and a control board."
github_url: ""
live_url: ""
show_toc: false
hidden: false
---

# 2.00 Library Tracker

In May 2024, I (with a team of three others) built a **Library Tracker** tool as part of MIT’s 2.00 course. Our client was an elementary school librarian who struggled to track when her younger, special-needs students completed tasks—like checking out books or returning overdue materials—in a chaotic classroom environment.

We were asked to design a **low-tech, privacy-conscious, and classroom-friendly** solution that would make task-tracking easier.

![tracker on display](/static/uploads/projects/2-00-library-tracker/tracker_on_display.jpeg)

## Features

- **Tracker Board**
  - Built from layered 1/8" plywood sheets with slots for name-tag sliders.
  - RGB LEDs beneath each student’s photo and name, lighting up to indicate task completion.

- **Librarian Control Board**
  - A teacher-activated **unlock switch** to prevent students from changing lights when not allowed.
  - Buttons for marking tasks as complete, undoing the last action, or resetting all lights.

- **Electronics**
  - An **Arduino Mega** provided sufficient GPIO pins for the many LEDs and buttons.
  - Hand-soldered connections for power, ground, and signals across the tracker board.
