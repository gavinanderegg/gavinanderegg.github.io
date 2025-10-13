---
title: >
    The Canon Cat
date: 2025-10-13 13:09:08 -0300
---

Here's another Wikipedia rabbit hole post. This time about the Canon Cat: a weird little computer from the late 1980s.

[As I've mentioned before](https://anderegg.ca/2025/07/04/insomnia-fractals-and-typography), I often read Wikipedia when trying to get back to sleep. This time I was looking into the [Data General Nova](https://en.wikipedia.org/wiki/Data_General_Nova) series of minicomputers. I had watched [a fun series on the Tech Tangents YouTube channel](https://www.youtube.com/watch?v=mBssIIRGkOw&list=PLJVwF78cppBgwAHYKMffuhs0jblPHCyvL) about the restoration of a microNOVA, and I was curious what Wikipedia would have to say about it. I was almost immediately sidetracked by [this image near the top of the article](https://commons.wikimedia.org/wiki/File:Data_General_NOVA_System.jpg).

To the right of the pictured Nova System were three microcomputers. I recognised the one at the bottom as an [Atari 400](https://en.wikipedia.org/wiki/Atari_8-bit_computers#400_and_800_release), and the one in the middle as a [Radio Shack TRS-80](https://en.wikipedia.org/wiki/TRS-80), but I wasn't familiar with the one at the top. Zooming in, I saw it listed as a "Canon Cat" on the placard. Though it wasn't familiar to me, it looked like the Platonic ideal of an 80's computer.

[The Wikipedia page for the Canon Cat is quite short](https://en.wikipedia.org/wiki/Canon_Cat), but it was dense with interesting bits. It was created by [Jef Raskin](https://en.wikipedia.org/wiki/Jef_Raskin)? The Macintosh guy? And it didn't have a mouse? It was based on [FORTH](https://en.wikipedia.org/wiki/Forth_%28programming_language%29)? What are those weird keys below the space bar?

This morning I did a bit more digging and I'm quite surprised that I hadn't come across this thing earlier. It's fascinating! [The Register posted an article about the Cat last year](https://www.theregister.com/2024/05/31/the_canon_cat/) that links to [a promo video on YouTube](https://www.youtube.com/watch?v=o_TlE_U_X3c) showing off the "Leap" buttons (those two red buttons below the space bar). It also demoed some interesting features of the OS, which was sort of an all-in-one office suite that the machine booted into. The article also includes a video showing how to [enter the FORTH console](https://youtu.be/jErqdRE5zpQ?si=peKyRAnWvpJk_NZj&t=119), along with links to documents on [canoncat.net](http://www.canoncat.net/). I also found [a Canon Cat page on Vintagecomputer.ca](https://vintagecomputer.ca/canon-cat/) with some excellent photos of the machine.

Most interesting to me was a link to [an emulated version of the Cat on Archive.org](https://archive.org/details/canoncat). This page also links to a [reference manual](https://archive.org/details/CatReferenceGuide/) and [workshop manual/repair guide](https://archive.org/details/CatWorkshopManual/).  Playing around in the emulator, I found the left and right Option keys on macOS could be used as Leap keys, and Control can be used as the "Use Front" key. There's a procedure on page 3 of this [tForth Manual](http://www.canoncat.net/cat/Cat%20tForth%20Documentation.pdf) for entering FORTH mode. However, I wasn't able to get this to work in the emulator. [^1] Please let me know if I'm doing something wrong here.

Anyway, this was a fun diversion on a lazy Thanksgiving long weekend. If you have any stories or other resources about the Canon Cat, please feel free to reach out on [Mastodon](https://mastodon.social/@gavinanderegg) or [Bluesky](https://bsky.app/profile/gavin.anderegg.ca).

---

[^1]: I did this by typing `Enable Forth Language` by itself on a line, hitting both Leap keys (left and right Option) to select that text, holding down "Use Front" (Control) and pressing Erase (Backspace or "Delete"), then holding "Use Front" + Shift + Space. This seems to freeze the emulator, though. I also found this emulator worked much better in Chrome than in Safari.