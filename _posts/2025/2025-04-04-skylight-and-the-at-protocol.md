---
title: >
    Skylight and the AT Protocol
date: 2025-04-04 14:57:25 -0300
---

Since [my last piece about Bluesky](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won), I've been using the service a lot more. Just about everyone I followed on other services is there now, and it's way more fun than late-stage Twitter ever was. Halifax is particularly into Bluesky, which reminds me of our local scene during the late-2000s/early-2010s Twitter era.

That said, I still have reservations about the service. Primarily around the whole [decentralized/federated piece](https://anderegg.ca/2024/11/23/how-decentralized-is-bluesky-really). The Bluesky team continues to work toward the goal of creating a decentralized and open protocol, but they've got quite a way to go.

Part of my fascination with Bluesky is due to its radical openness. There is no similar service that allows users [unauthenticated access to the firehose](https://anderegg.ca/2024/11/25/playing-with-the-bluesky-firehose), or that [publishes in-depth stats](https://bsky.jazco.dev/stats) around user behaviour and retention. I like watching numbers go up, so I enjoy following those stats and collecting some of my own.

A few days ago I noticed that the rate of user growth was accelerating. Growth had dropped off steadily since late January. As of this writing, there are currently around [5 users a *second*](https://bsky-users.theo.io) signing up for the service. It was happening around the same time as tariff news was dropping, but that didn't seem like a major driver. Turned out that the bigger cause was [a new Tiktok-like video sharing app called Skylight Social](https://skylight.social/). I was a bit behind on tech news, so I missed when [TechCrunch covered the app](https://techcrunch.com/2025/04/01/mark-cuban-backs-skylight-a-tiktok-alternative-built-on-blueskys-underlying-technology/). It's gathered more steam since then, and today is one of the highest days for new Bluesky signups since the US election.

As per the TechCrunch story, Skylight has been given some initial funding by Mark Cuban. It's also selling itself as ["decentralized" and "unbannable"](https://web.archive.org/web/20250403203203/https://skylight.social/). I'm happy for their success, especially given how [unclear the Tiktok situation is](https://www.theverge.com/news/642158/tiktok-america-ban-amazon-applovin-rumor-deadline), but I continue to feel like everyone's getting credit for work they haven't done yet.

Skylight Social goes out of its way to say that it's powered by the [AT Protocol](https://atproto.com/). They're not lying, but I think it's truer at the moment to say that the app is powered by Bluesky. In fact, [the first thing you see](https://anderegg.s3.amazonaws.com/skylight-signup.png) when launching the app is a prompt to sign up for a "BlueSky" account [^1] if you don't already have one. The Bluesky team are [working on better ways to handle this](https://docs.bsky.app/blog/2025-protocol-roadmap-spring#pds-account-management), but it's work that isn't completed. At the moment, Skylight is not decentralized.

I decided to sign up and test the service out, but this wasn't a smooth experience. I started by creating an [App Password](https://bsky.social/about/blog/5-19-2023-user-faq#:~:text=Please%20generate%20an%20App%20Password), and tried logging using the "Continue with Bluesky" button. I used both my username and email address along with the app password, but both failed with a "wrong identifier or password" error. I saw a few other people [having the same issue](https://bsky.app/search?q=skylight.social%E2%80%AC+identifier). It wasn't until later that I tried using the "Sign in to your PDS" route, which ended up working fine. The only issue: I don't run my own PDS! I just use custom domain name on top of Bluesky's first-party PDS. In fact, it looks like [third-party PDSs might not even be supported at the moment](https://bsky.app/profile/basking.monster/post/3llva5zlsfs2s).

Even if/when you can sign up with a third-party PDS, this is just a data storage and authentication platform. You're still relying on Skylight and Bluesky's services to [shuttle the data around](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay) and [show it to you](https://docs.bsky.app/docs/advanced-guides/federation-architecture#app-views).

I'm not trying to beat up on Skylight specifically. I want more apps to be built with open standards, and I think TikTok could use a replacement — especially given that [*something* is about to happen tomorrow](https://techcrunch.com/2025/03/31/trump-says-tiktok-deal-will-come-before-april-5-deadline/). I honestly with them luck! I just think the "decentralized" and "unbannable" copy on their website should currently be taken with a shaker or two of salt.

---

[^1]: I don't know why, but seeing "BlueSky" [camel-cased](https://en.wikipedia.org/wiki/Camel_case) drives me nuts. Most of the Skylight Social marketing material doesn't make this mistake, but I find it irritating to see during the first launch experience.