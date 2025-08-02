---
title: >
    Why is the Online Safety Act causing Bluesky user growth?
date: 2025-08-02 14:19:58 -0300
---

Over the past few days, Bluesky has had accelerated user growth. This happened at the same time as UK's Online Safety Act came into effect. I don't know exactly why this is the case, but I have some ideas.

First, I want to start with a quick aside. I think that efforts like the [Online Safety Act](https://www.gov.uk/government/collections/online-safety-act), [KOSA](https://en.wikipedia.org/wiki/Kids_Online_Safety_Act), and Canada'a [Bill S-209](https://www.parl.ca/legisinfo/en/bill/45-1/s-209) are some security reducing, privacy invading, speech restricting, "[won't somebody please think of the children](https://en.wikipedia.org/wiki/Think_of_the_children)" level bullshit. Here's [an excellent video overview of the issues of S-209](https://www.youtube.com/watch?v=cBJe3gB2Po4) from David Fraser. [Here's more from Michael Geist](https://www.michaelgeist.ca/2025/07/risky-business-the-legal-and-privacy-concerns-of-mandatory-age-verification-technologies/). S-209 is what might affect me most directly, but its issues are shared among other efforts.

With that out of the way, on to Bluesky. As a social network on the internet, the Bluesky team have to abide by the Online Safety Act or face hefty fines. [^1] To do so, they're [requiring age verification](https://bsky.social/about/blog/07-10-2025-age-assurance) to [access DMs and some moderation settings](https://bsky.app/profile/bsky.app/post/3lunvnx3rmc2y). These changes to the app were rolled out on July 23. The next day, and for the days following, [the service got a surprising bump in sign-ups from new users](https://bskycheck.com/stats.php). What's the deal?

I don't have a full explanation, but I have some thoughts. One guess is that other services could have taken a more heavy-handed approach to moderation. This wouldn't surprise me, but I don't have any evidence. Another possibility is that, if you have to hand over private information to keep using a service, maybe you give it to a service you trust more (or distrust less). It could also be a "grass is greener" kind of thing, and age verification was a good enough excuse to try another service.

There's one thing Bluesky has going for it that's different about all of its competitors, though. [It's based on a completely open protocol](https://atproto.com/). This isn't some Linux neckbeard selling point, either. For the protocol to function, all posts have to be publicly accessible. [^2] This goes for adult content along with everything else. If you're scrolling your timeline and see a piece of content that's blocked for you on the Bluesky app, you can [use another service to get to that content](https://skyview.social/). These can also easily be run locally, so governments would have a hard time playing whack-a-mole to take them down.

[I've gone into a bit more detail on how this works previously](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won), but the short version is that Bluesky is an "AppView" on top of the AT Protocol. Data is housed on a series of Personal Data Servers (PDSs), and a Relay service is used to index that data so it can be accessed by AppViews. This design is fairly convoluted, but the aim is for the whole thing to be decentralized. [^3] The main upshot is: everything must be open and public for it to work.

Is this why people are flocking to Bluesky recently? No idea. I'm pretty certain most people don't know this is the case. But if there's a group of people who'd be motivated to figure it out, one might do well to bet on those with surging hormones and a lot of time on their hands.

I have absolutely no idea how this openness interacts with the law. There are some people running their own PDS instances, but the vast majority of content on the service is hosted by servers managed by the Bluesky team. Is it enough that the main Bluesky AppView blocks this content without age verification? Who knows! I'm not trying to narc on Bluesky here. It's just an interesting wrinkle caused by the open protocol. Ultimately, I think this is [yet another issue with a very stupid law](https://www.theverge.com/analysis/714587/uk-online-safety-act-age-verification-reactions).

---

[^1]: Those fines can reach "[up to 10% of qualifying worldwide revenue](https://www.gov.uk/government/collections/online-safety-act#:~:text=impose%20fines%20of%20up%20to%2010%25%20of%20qualifying%20worldwide%20revenue)". Bluesky does not currently generate any meaningful revenue, so I'm not exactly sure how that would work. I'm sure OFCOM would figure something out.

[^2]: Note that this isn't the case for DMs. [Those are handled outside of the AT Protocol](https://docs.bsky.app/blog/2024-protocol-roadmap#:~:text=Basic%20%22Off%2DProtocol%22%20Direct%20Messages%20%28DMs%29%3A). I think that's why they're explicitly mentioned as requiring age verification.

[^3]: I'll skip [the usual grumbling](https://anderegg.ca/2024/11/23/how-decentralized-is-bluesky-really) about the decentralization issue here. That said, I mean to write an update about this in the near future. The Bluesky team has continued to advance the decentralization story, and there have been [interesting developments on this front](https://bsky.app/profile/bnewbold.net/post/3lscf7nho322t).