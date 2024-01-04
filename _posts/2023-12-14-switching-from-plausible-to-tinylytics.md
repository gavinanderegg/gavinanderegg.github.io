---
title: Switching from Plausible to Tinylytics
date: 2023-12-14 10:16:46 -0400
---

A while back I wrote some [thoughts about web analytics packages](https://anderegg.ca/2023/01/22/blogging-analytics-and-gdpr). I knew I wanted to write more and thought that having some numbers-go-up would help to sustain that [^1]. After some waffling, I decided to use Plausible [a bit more than a year ago](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/af20825af2ddcb624d3291c2f324e04b93368c45).

Plausible is a really great service — but when the annual renewal was coming up, I decided to switch. One complaint I have with Plausible is that the number of pageviews per month is soft-capped at [10,000 on the $90/year plan](https://plausible.io/#pricing). They allow for occasional overages without issue, but I brushed against it twice and felt a bit nervous about that. It also had a lot of features I wasn't going to use. I really just want to know what pages are getting what views and how things are trending.

I could have upgraded to the $190/year plan for more pageviews, but this felt a bit steep for my needs. I had also considered building some simple custom analytics, but the renewal deadline snuck up on me. Instead, I decided to try another indie analytics service I'd seen around: [Tinylytics](https://tinylytics.app).

Tinylytics is built by [Vincent Ritter](https://vincentritter.com), who I remember hearing about when he started working on [Micro.blog](https://micro.blog) [^2]. The project launched in [June of 2023](https://vincentritter.com/2023/06/12/16-19-05), so it wasn't around when I was originally surveying the analytics field.

I've been using the service since November 29, and it's been great so far! The biggest draw is that it offers straightforward pageview stats with [10 times the headroom as Plausible at about half the cost](https://tinylytics.app/home#pricing). It also provides uptime monitoring and a ["kudos" system](https://tinylytics.app/docs/showing_kudos), which seems interesting. There's a free 1,000 pageview a month plan, and also a [live demo of the stats of the Tinylytics site](https://tinylytics.app/public/JbG7t9oxahYPH58qxqa4) if you'd like to see what the stats dashboard looks like.

Landing on Tinylytics has cured the itch to try and build something myself, I think. It's a great, well-priced service that fits my needs really well. I hope to keep using it for a good long while.

---

[^1]: [*Insert usual lack-of-blog-update excuses here.*] I started off pretty strong this year, but got bogged down after February when things got busier. Now that I'm in holiday-mode, I'm thinking bloggy thoughts again.

[^2]: Micro.blog is a great service. If you want a quick way to host short- or long-form content that syndicates to many other services and is also ActivityPub enabled, it's really worth checking out. [Manton Reese](https://www.manton.org), the guy behind the project, [discussed all the great features of Micro.blog on the ShopTalk podcast](https://shoptalkshow.com/586/).
