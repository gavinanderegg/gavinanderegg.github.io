---
title: >
    Walking distance weirdness in watchOS 27.0
date: 2026-10-06 21:02:16 -0300
---

It's been a couple of weeks since I got my Apple Watch Ultra 4. I've written about some [upcoming features that I'm not psyched about](https://anderegg.ca/2026/09/11/apple-watch-privacy-promises-wont-fix-how-it-feels), but I've otherwise been very happy with the upgrade. There's just one issue: the new walking distance estimation is completely busted for me.

I've previously used an Apple Watch Series 3, Series 5, Series 7, and Ultra 1. In each of those cases, the watch did a great job translating my steps into a reasonable approximation of my walking distance. After using the Ultra 4 for a day, I noticed that my step counts were steady, but my walking distance was way down. I was getting slightly less than half the normal distance.

At first I figured that I might need [a few outdoor walks to calibrate it](https://support.apple.com/en-us/105048). But things are still way out of whack after a dozen 30+ minute outdoor walk exercises. To be clear: when I do an outdoor walk/run exercise, I get the distance values I expect — likely because of GPS tracking. But every other sort of walk is undercounted distance-wise. [^1] Step tracking seems correct, but those steps are now worth far less than my GPS-verified walking distance.

I worried that it might be a hardware issue with the watch. Looking into it, [I found others complaining about similar issues](https://www.reddit.com/r/AppleWatchFitness/comments/1whk8b8/anyone_else_having_issues_with_inaccurate_indoor/) — [even after updating existing watches](https://discussions.apple.com/thread/256360699). Distances were normal [until people installed watchOS 27](https://forums.macrumors.com/threads/watchos-27-messed-up-walking-pace.2489477/). The data is pretty noisy, though. Some people are only reporting minor differences, and others are seeing more distance rather than less.

The Ultra 4 came with watchOS 27.0, which my Ultra 1 couldn't update to. A feature of the new OS is a "[redesigned pedometer model](https://support.apple.com/en-euro/guide/watch/apdb93ea3872/watchos#:~:text=redesigned%20pedometer%20model)". I don't know if that's what's causing my issue, but it's my current guess.

I've [sent Apple some feedback](https://www.apple.com/feedback/), but it's unclear how widespread the issue is. It still could be a hardware issue, but I'm hoping that it's something that can be addressed with a software update. Again, this is my fifth Apple Watch, and I've not seen this sort of issue before.

If this is affecting you, at least you know you're not alone! [I recommend sending Apple some feedback](https://www.apple.com/feedback/) so they can hopefully get the issue fixed.

**Update:** Today I tried [resetting my calibration data](https://support.apple.com/en-us/105048#:~:text=Reset%20your%20calibration%20data) before going out for a walk. I got the expected distance from the outdoor walk exercise. I then did a 15-minute indoor walk exercise and still only got around half the expected distance. I'm still really hoping that Apple can address this in a software update!

---

[^1]: I've even tried walking a known outdoor route, but not recording it as an outdoor walk. After, I had less than half the route's distance. GPS data might be the only thing giving correct walking distance, currently.