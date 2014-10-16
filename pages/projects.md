Projects
========
This is a collection of interesting things I may have worked on, but right now it's pretty incomplete.

Feel free to contact me if you have any questions: andrew@mauragis.com

---
Bofhwits: An IRC Bot
--------------------
[github](https://github.com/amauragis/bofhwits)

This is a silly project in Go to handle quoting of an IRC channel.  It's a project I started to learn Go, and mess with some
basic web integration.

Basically someone says something funny, and you indicate to the bot that you thought this particular thing was funny. 
The bot will then parse what you quoted it, and post it to twitter or another custom microblogging site. A particular 
challenge of note is parsing a variety of potential input formats (because it must handle a copy and paste, and IRC
clients are not particularly consistent in this regard).

---

Oculus-ASR
----------
At [Michigan Technological University](www.mtu.edu), as an alternative to a Senior Capstone project, there are a number
of groups called "Enterprises" that allow undergraduates to work on a longer-term team project with real-world goals
and interactions.  One of those enterprises, the [Aerospace Enterprise](www.aerospace.mtu.edu) is responsible for the
Oculus-ASR microsatellite, part of the Air Force Research Lab's University Nanosat Program (AFRL UNP). Oculus-ASR was
the winner of the sixth iteration of the UNP program, and is scheduled to launch on a Falcon Heavy on STP-2.  Since
the official end of the sixth competition in January 2011, the team has been finalizing and integrating
the flight hardware.

I was responsible for the design and implementation of the satellites communication system, redesign of the battery
charge controller, and systems engineering.

![Oculus-ASR Exploded View](projects/oculus-exploded-web.jpg "Oculus-ASR Exploded View")

---

Equiangular Spiral Antenna
--------------------------
[[paper]](projects/antenna.pdf)

One of my later courses at [MTU](www.mtu.edu) was in antenna design.  At the end of the course, students designed and modelled
custom built antennas.  We chose to design an equiangular spiral antenna, [originally proposed by John Dyson in 1959](http://www.google.com/patents/US2958081).
Our target bandwidth was 10:1, but due to construction problems, we were limited to a narrower band.

The antenna was constructed using a 1/32" copper sheet fastened to an acrylic sheet for stability, and fed with a copper
hardline.  We used FEKO to simulate the antenna results and verified them in an anechoic chamber on campus.

![Antenna Construction](projects/antenna0.png "Antenna Construction") ![Antenna 1GHz Far Field](projects/antenna1.png "Antenna 1GHz Far Field")


