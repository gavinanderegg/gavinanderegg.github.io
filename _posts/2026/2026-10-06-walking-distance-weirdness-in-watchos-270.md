---
title: >
    Walking distance weirdness in watchOS 27.0
date: 2026-10-06 21:02:16 -0300
---

It's been a couple of weeks since I got my Apple Watch Ultra 4. I've written about some [upcoming features that I'm not psyched about](https://anderegg.ca/2026/09/11/apple-watch-privacy-promises-wont-fix-how-it-feels), but I've otherwise been very happy with the upgrade. There's just one issue: the new walking distance estimation is completely busted for me.

I've previously used an Apple Watch Series 3, Series 5, Series 7, and Ultra 1. In each of those cases, the watch tracked my steps well and translated them into a reasonable approximation of my outdoor walking distance. When I got the Ultra 4, I noticed that this was no longer the case. Currently, I get around a third to half the distance for any given set of steps on an indoor walk exercise (or for the regular steps I put in throughout the day).

At first I figured that I might need [a few outdoor walks to calibrate it](https://support.apple.com/en-us/105048). But things are still way out of whack after a dozen 30+ minute outdoor walks. To be clear: when I do an outdoor walk/run exercise, I get the distance values I expect — likely because of GPS tracking. But every other sort of walk is undercounted distance-wise. [^1] As far as I can tell, step tracking is always correct. It's just that those steps are now worth less than half of my GPS-verified walking distance.

I worried that it might be a hardware issue with the watch. Looking into it, [I found others complaining about similar issues](https://www.reddit.com/r/AppleWatchFitness/comments/1whk8b8/anyone_else_having_issues_with_inaccurate_indoor/) — even on older watches. Distances were normal [until people installed watchOS 27](https://forums.macrumors.com/threads/watchos-27-messed-up-walking-pace.2489477/). The data is pretty noisy, though. Some people are only reporting minor differences, and others are seeing more distance rather than less.

The Ultra 4 came with watchOS 27.0, which my Ultra 1 couldn't update to. A feature of the new OS is a "[redesigned pedometer model](https://support.apple.com/en-euro/guide/watch/apdb93ea3872/watchos#:~:text=redesigned%20pedometer%20model)". I don't know if that's what's causing my issue, but that's my current guess.

I've [sent Apple some feedback](https://www.apple.com/feedback/), but it's unclear how widespread the issue is. It still could be a hardware issue, but I'm hoping that it's something that can be addressed with a software update. Again, this is my fifth Apple Watch, and I've not seen this sort of issue before.

If this is affecting you, at least you know you're not alone! [I recommend sending Apple some feedback](https://www.apple.com/feedback/) so they can hopefully get the issue fixed.

---

[^1]: I've even tried walking a known outdoor route, but not recording it as an outdoor walk. After, I had less than half the route's distance. GPS data might be the only thing giving correct walking distance, currently.