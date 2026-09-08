---
title: >
    The Talk Show Timeline
date: 2026-09-08 13:23:04 -0300
---

I really enjoy [John Gruber's](https://daringfireball.net/) podcast *[The Talk Show](https://daringfireball.net/thetalkshow/)*. However, I've noticed that it's been a while since it was in my feed. I decided to chart previous episode dates to check some of my assumptions about release frequency.

Cutting to the chase, [here's a link to **The Talk Show Timeline**](https://anderegg.ca/tts-timeline/). You can click/tap on days to get a pinned tooltip, which lets you link out to a particular day's episode. I've tried to make this work well on mobile devices, but you'll likely find it works best on desktop.

A note about this: Gruber has mentioned in the past that there has been [a personal situation that he's been working through](https://daringfireball.net/2025/09/personal_note). He's also mentioned something to this effect on the podcast at points, but hasn't gone into detail. I don't need to know more than has been said, and I just hope things are alright.

[I've read Gruber's site since 2002](https://daringfireball.net/2002/08/baby_needs_a_new_pair_of_processors) [^1] and [listened to his podcasts since 2007](https://daringfireball.net/linked/2007/06/28/the-talk-show). In that time, I've learned that he operates on his own timeline… and has a penchant for procrastination. No shade here! He's set himself up with a work situation that I envy. I also don't want to seem grumpy about the lack of podcast episodes; I'm just trying to understand how this current break compares to those in the past.

Because it was easiest, and because it would answer my immediate questions, I only looked at the current iteration of The Talk Show. Happily, there's [a single page](https://daringfireball.net/thetalkshow/) which lists all the episodes. It had a tiny bit of data weirdness, [^2] but I was able to [turn this into a JSON file](https://github.com/gavinanderegg/tts-timeline/blob/main/episodes.json) with the details I cared about. With that, I used the [calendar heatmap chart](https://echarts.apache.org/examples/en/editor.html?c=calendar-heatmap) in [Apache ECharts](https://echarts.apache.org/en/index.html) to [display the episodes over time](https://anderegg.ca/tts-timeline/).

Some things I noticed:

* While it's been a while (29 days) since the last episode (on August 10), this isn't unheard of. The average is about 12 days between episodes, but there have been 6 other times when the episode gap has been at least this long.
* The longest gap was 62 days between December 24, 2024 and February 24, 2025.
* There's exactly one day with two episodes: July 19, 2014. It was "Cat Pictures" with Marco Arment, which got split into two "sides". [Here's a link to side 1](https://daringfireball.net/thetalkshow/2014/07/19/ep-088), and [here's side 2](https://daringfireball.net/thetalkshow/2014/07/19/ep-089).
* I mentioned procrastination: 73% of episodes take place on the 16th of a month or later. 28% of episodes take place on either the last or second-last day of the month. Again, no shade! It's something I chuckle about whenever I notice it.
* At the current rate, this year is about in line with output going back to 2023. While it has been a while since a new episode dropped, it's not out of whack statistically.

Anyway, this was a Labour Day project that was mostly for my own amusement. I expect there will likely be a new episode of The Talk Show some time fairly soon after tomorrow's Apple event.

I also don't know if I'll keep this chart up to date… though it's not terribly onerous to do now, so who knows.

---

[^1]: I found [Daring Fireball](https://daringfireball.net/) because I was researching the purchase of my first Mac around this time. It wasn't until October of 2002, but [I ended up buying](https://anderegg.ca/2026/04/01/apple-at-50-my-journey-to-the-mac) one of the machines he wrote about in [his first post that August](https://daringfireball.net/2002/08/baby_needs_a_new_pair_of_processors).

[^2]:
    The following dates don't match the main format:
    * Sunday 30 November, 2025
    * Mon, 24 Feb 2020 16:05:34 EDT
    * Tuesday 31 December 2019
    * Tuesday, June 25 2019
    * Sat, 16 Mar 2019 19:43:49 EDT
    * Wednesday 31 December 2014
    * Monday, 30 Jun 2014