---
title: Blogging, Analytics, and GDPR
date: 2023-01-22 15:18:23 -0400
---

The [clown show at Twitter](https://anderegg.ca/2022/11/15/twitter-is-going-great) has reminded me how great it can be to own and control your content. I'd like to blog more, but getting motivated can be tough. As with [many other things](https://www.bungie.net/7/en/Destiny/NewLight), I find that making some numbers go up can help.

I removed Google Analytics (GA) from my site [almost two years ago](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/d334ad8fc494c44a90fc94f845b831f2b2474b52). I posted so infrequently that the traffic patterns weren't interesting. I also found the old version of GA to be relatively heavy in terms of page load.[^1] Mostly though, I've always been a bit put off by [how much data GA gathers](https://support.google.com/analytics/answer/9355658?hl=en).

Because it's free, GA is used on a lot of sites. Because it's on a lot of sites, Google can use it to aggregate a lot of data about visitors. This isn't bad *per se*, some site owners get tremendous value from GA! But it was overkill for my needs, and I didn't feel like the trade-off was worth it at the time.

So if I was going to use numbers as my blogging "carrot", what should I use? I briefly considered re-adding GA to my site, but decided against it. The product is in the middle of a [messy transition](https://support.google.com/analytics/answer/11583528?hl=en) from the old version (Universal Analytics) to a new, half-baked version (Google Analytics 4).[^2] I also wanted something lighter that tracked fewer things. I thought about building something myself, but I didn't want the maintenance headache. After looking at some other options, I settled on a trial of [Plausible Analytics](https://plausible.io/).

Plausible may not be a great fit for everyone. For example: if you'd like data about [new vs. returning users](https://plausible.io/data-policy#how-we-count-unique-users-without-cookies), it really doesn't help. It has some [basic conversion tracking](https://plausible.io/docs/pageview-goals), but nothing like the mildly creepy [custom conversion setups](https://support.google.com/analytics/answer/12846214) or [user flow reports](https://support.google.com/analytics/answer/9317498?hl=en) you can build with GA. Also, the hosted version of Plausible starts at [$9 USD/month for up to 10k pageviews](https://plausible.io/#pricing).

The minimal amount of tracking that Plausible provided was a plus to me, but the price was a sticking point at first. Happily, the [product is open source](https://github.com/plausible/analytics) and setting up a self-hosted version doesn't look too difficult. I figured I'd start with the trial and then see about self-hosting if I liked it… but I ended up subscribing after a week. The service was a great fit for my needs, and supporting a small team of developers felt like the right thing to do. If you're interested in seeing a live version of Plausible, [they offer a nice demo with stats from their own site](https://plausible.io/plausible.io).

During this whole period of waffling about stats products, one other point kept bubbling up: [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation).

I went down quite the rabbit-hole with this, but [the biggest takeaway was the Schrems II case](https://www.gdprsummary.com/schrems-ii/). In short: gathering personal data on users and sending that to third-parties can get one sued. In this case the personal data was an IP address and the third-party was Facebook. A [similar court case](https://www.theregister.com/2022/01/31/website_fine_google_fonts_gdpr/) focused on a GDPR violation around Google Fonts.[^3]

This seems insane to me, and makes me worry that GDPR (and laws like it) could harm small websites. I don't have a legal team, and in terms of GDPR protection, it's likely safer to post all my content on Facebook or the like. Sending users toward large corporations seems antithetical to at least part of this law.

So, does Plausible protect me from GDPR? I have no idea. It doesn't set any cookies, so I feel better about not showing an annoying cookie consent dialogue. But I'm still loading content from a third-party, which means people visiting my site are having their IP addresses forwarded somewhere else. [Plausible make a solid case for themselves](https://plausible.io/data-policy), but it's unclear to me how much that matters. As a tiny speck on the internet, I feel that it's probably fine either way. I'd just like to do as close to the correct thing as possible.

I just wish I didn't have to consider international law when setting up web stats!


---


[^1]: [My site is pretty svelte](https://1mb.club), and Google Analytics added something like 40% to the total page load time when I last checked.
[^2]: As a side note: I'm currently helping some clients with this, and it's a major pain.
[^3]: I'd removed Google Fonts from my site over [just over a year ago](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/2c7a0b48e09b46621751e166a5b90fce8cea8bb8), but it was mostly another way to reduce the page load.
