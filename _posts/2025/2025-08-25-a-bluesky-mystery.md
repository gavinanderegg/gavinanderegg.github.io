---
title: >
    Mystery of the missing Bluesky posts
date: 2025-08-25 21:06:00 -0300
---

**UPDATE:** I heard back from Bryan Newbold, protocol engineer at Bluesky, about this. [It seems this is an issue with the AppView layer of the protocol when it comes to large threads](https://bsky.app/profile/bnewbold.net/post/3lxbcnv2hjc2b). There's a new API in the works that's set to help out with this problem. I'm glad to hear it wasn't just me missing something obvious!

---

I feel slightly embarrassed posting about this, but it's really bothering me. I'm writing now about some posts that seem to have been ignored by Bluesky.

This weekend, Chris Plante asked a question: "[What was the first video game that scared you?](https://bsky.app/profile/plante.bsky.social/post/3lx37gbfbgs23)"

I happened to be looking at Bluesky's web client at just about the moment he asked this. [I replied 9 minutes later](https://bsky.app/profile/gavin.anderegg.ca/post/3lx37xhvozk2o) with a note about [*Last Half of Darkness*](https://www.mobygames.com/game/34940/last-half-of-darkness/), a DOS game released over 35 years ago. [^1] I then checked the thread to find that my post didn't appear there. I thought that was weird, but assumed it was a caching issue.

Later, I checked back and saw that the thread had gotten a lot of replies. I still didn't see my post in the thread using the web UI, so I decided to see if I could dig it view it in the Bluesky API.

I wasn't sure exactly what endpoint to check, but I came across [Simon Willison's Bluesky Thread Viewer](https://tools.simonwillison.net/bluesky-thread). I checked out [the source code for this](https://github.com/simonw/tools/blob/9ff34cda38da953e59e412597b7cab3000dab97b/bluesky-thread.html#L4), and using that was able to generate a URL to grab [the API data for this thread](https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=at%3A%2F%2Fdid%3Aplc%3Aghn6sa6xjvsyqlcvrisc4rec%2Fapp.bsky.feed.post%2F3lx37gbfbgs23&depth=1000). My post wasn't in here.

At this point, I felt weird. [I tried posting again](https://bsky.app/profile/gavin.anderegg.ca/post/3lx5otehwx22j). After I posted a second time I could immediately see other people in the API data who had posted after me, but neither of my posts appeared in the data.

At the time of writing, I see that there are 895 replies to the parent post ([based on the reply counter in the web UI](https://bsky.app/profile/plante.bsky.social/post/3lx37gbfbgs23)), but only 396 posts in the API data. It's definitely not just a me thing. That said, I don't understand what's happening here.

Both [my first post](https://bsky.app/profile/gavin.anderegg.ca/post/3lx37xhvozk2o), and [my later post](https://bsky.app/profile/gavin.anderegg.ca/post/3lx5otehwx22j) show that they're attached to the parent. The API data doesn't show any moderation or label data that should limit [post 1](https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=at%3A%2F%2Fdid%3Aplc%3Akmeoup7vs37oby2a77nu6yk4%2Fapp.bsky.feed.post%2F3lx37xhvozk2o) or [post 2](https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=at%3A%2F%2Fdid%3Aplc%3Akmeoup7vs37oby2a77nu6yk4%2Fapp.bsky.feed.post%2F3lx5otehwx22j).

Do Bluesky's system's choke when too many posts happen too quickly? Under 900 replies doesn't seem like all that many, if so. Also, why did my later post also not get indexed after things slowed down? Maybe the thread API is artificially limited to make things easier for clients? If so, how are the included responses chosen? Is stuff just straight-up broken?

I'm very willing to believe I'm missing something obvious, but this seems contrary to my understanding of Bluesky's systems. Based on my reading of [the documentation](https://docs.bsky.app/docs/api/app-bsky-feed-get-post-thread), it seems like I should be able to get up to 1,000 posts at a time using the API. I'm seeing less than half of the purported 895! I collected these thoughts into [a thread on Bluesky](https://bsky.app/profile/gavin.anderegg.ca/post/3lx5unyuu5s25), so feel free to double check that as well. I'd be very happy to be corrected on anything I'm doing wrong or misunderstanding here!

---

[^1]: Both [MobyGames](https://www.mobygames.com/game/34940/last-half-of-darkness/) and [Wikipedia](https://en.wikipedia.org/wiki/Last_Half_of_Darkness) say the game was released in 1989, but the [copyright date on the screenshots say 1990](https://www.mobygames.com/game/34940/last-half-of-darkness/screenshots/dos/309609/). Either way, not a new game.
