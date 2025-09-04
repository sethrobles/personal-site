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

In May 2024, I (with a team of three others) built a **Library Tracker** tool as part of MIT’s 2.00 course. Our client was an elementary school librarian who struggled to track when her younger, special-needs students completed tasks—like checking out books or returning overdue materials—in a chaotic classroom environment.

We were asked to design a **low-tech, privacy-conscious, and classroom-friendly** solution that would make task-tracking easier.

After numerous conversations with our client, we finally settled on our library tracker, with the main features listed below.

- **Board Body**
    - Built from layered 1/8" plywood sheets with slots for name-tag sliders.
    - RGB LEDs beneath each student’s photo and name, lighting up to indicate task completion.
    - One plywood sheet was lasercut for panel bending for singular component design
- **Librarian Control Box**
    - A teacher-activated **unlock switch** prevents students from changing lights when not allowed.
    - Buttons for marking tasks as complete, undoing the last action, or resetting all lights.
- **Electronics**
    - An **Arduino Mega** provided sufficient GPIO pins for the many LEDs and buttons.
    - Hand-soldered connections for power, ground, and signals across the tracker board.


<p align="center",padding=20px>
  <img src="tracker_on_display.jpeg" alt="tracker on display">
  <br>
  <span style="font-size:0.95em; color: #666; font-style:italic;">Tracker on display at final presentation</span>
</p>
