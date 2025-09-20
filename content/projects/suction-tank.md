---
type: "project"
title: "Suction Tank Robot"
slug: "suction-tank"
date: "2025-08-21"
tags: ["Prototyping", "3D Printing", "Arduino", "Robotics"]
thumbnail: "suction-tank-thumb.jpg"
# hero: "suction-tank-hero.jpg"
summary: "A prototyped tank-style robot that uses suction to adhere to surfaces, designed with 3D printed parts and modular components."
github_url: "https://github.com/sethrobles/suction-tank"
# live_url: ""
show_toc: false
hidden: false
---

This project was my attempt to design a **tank-style robot that could climb and hold its position using suction**. The goal was to prototype a platform capable of moving across surfaces where wheels or tracks alone wouldn’t provide enough grip.

<h2 style="text-align:center;">Key Features</h2>

- **Tank Drive** – Independent tracks for maneuverability across flat and inclined surfaces.
- **Suction Chamber** – A sealed cavity beneath the chassis generated suction, helping the robot adhere to surfaces.
- **3D Printed Frame** – Fully FDM-printed components designed for modularity and quick iteration.
- **Compact Motor Integration** – Small DC motors embedded in custom housings to drive the tracks efficiently.

<h2 style="text-align:center;">Prototyping Process</h2>

I worked through several CAD design iterations before building functional prototypes:

1. **Frame & Tracks** – Modeled and printed tank treads with sprockets to improve traction and alignment.
2. **Suction System** – Tested different gasket materials and chamber sizes to maximize holding force.
3. **Assembly & Testing** – Printed parts on an FDM printer, experimenting with modular swaps for track tensioning and suction seals.

<h2 style="text-align:center;">Takeaways</h2>

Through this process, I learned the importance of **modularity for faster redesigns** and how small design changes, like gear shape and bracing, can have large impacts on performance. This project also raised new questions about the limits of suction-based adhesion, especially on steeper slopes and in potential underwater applications.

{{ carousel([
  {'src': '/static/uploads/projects/suction-tank/suction_track.png', 'alt': 'Suction Cup Track', 'caption': 'Suction Cup Track'},
  {'src': '/static/uploads/projects/suction-tank/bracing_progression.png', 'alt': 'Bracing Progression', 'caption': 'Bracing Progression'},
  {'src': '/static/uploads/projects/suction-tank/gear_progression.png', 'alt': 'Gear Progression', 'caption': 'Gear Progression'},
]) }}

---

This project combined **mechanical prototyping, CAD iteration, and hands-on testing**. While still in its early stages, the suction tank robot gave me valuable insight into designing for unconventional mobility systems.
