---
title: >
    Maybe Bluesky has "won"
date: 2024-11-15 15:36:51 -0400
---

November has sucked so far. One upside of the terrible nonsense is that more people are fleeing X. Many are choosing Bluesky. I've seen a bunch of takes about this recently, but I keep seeing things I disagree with. I figure that's a good enough excuse to write more about this weird-assed social network.

### Decentralized? Federated? Neither.

When writing about Bluesky, I've seen folks mention that it's  either federated or decentralized. I'm here to tell you that it's currently neither. This one really irks me because the service is getting the credit for work it hasn't done.

One problem here is that the whole "decentralized" thing is complicated. I believe the Bluesky team is putting in a lot of good-faith effort to becoming a decentralized platform. But, this work is tricky because their architectural choices are quite novel.

[As I've written previosuly](https://anderegg.ca/2024/10/21/thoughts-on-the-recent-migration-from-x-to-bluesky), the AT Protocol (atproto) that powers Bluesky is [really complex](https://docs.bsky.app/docs/advanced-guides/federation-architecture). It's made up of three main parts: Personal Data Servers (PDSs), Relays, and App Views.

Currently people can set up their own [PDSs](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay), which will host both their identity's signing keys and their content on Bluesky. Setting this up requires a fair amount of server-level knowledge, but it's relatively cheap (maybe $15/month USD) and lets people control their own data. This is kind of like hosting your own website. The content will be available if someone knows how to get to it. By default, it's just some stuff sitting on a server somewhere.

The PDS part of the stack is interesting to me. In Bluesky's view, it's great if people start hosting their own PDSs — it means they don't have to pay for people's content storage!  It also means that users can relocate their data at any time. This is something that ActivityPub should do better. That said: yes, it's a bit of a pain to move my data from one Mastodon server to another, but it's something that's currently possible. The only server that's actively reading PDSs and doing anything productive with them is the one Bluesky controls. More on this in a second.

Next up the chain are [Relays](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay). These are what gather data from PDSs and make it available to the atproto ecosystem. If a PDS is like a website, a Relay is like Google. Relays constantly look at PDSs to see if there's any new content, and then index that content so it's actually useful. The trouble with this is that it's expensive and there's **a lot** of data. I recently [read an interesting post](https://alice.bsky.sh/post/3laega7icmi2q) outlining the steps required to self-host Bluesky content. The author mentions that setting up a Relay requires [around 4.5 TB of disk space](https://alice.bsky.sh/post/3laega7icmi2q#:~:text=make%20sure%20you%20have%20at%20least%20~4.5%20TB%20of%20disk%20space), and that it's [growing by around 18 GB a day](https://bsky.app/profile/alice.mosphere.at/post/3laewhb55zp2v) [^1]. However, that was said before the most recent bump in growth. The data and processing requirements will only accelerate as more people use the service.

While the Relay aggregates the data, it doesn't do anything to display it to users. That's up to the [App View](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay), which is what most people think of as "Bluesky". This is the piece that pulls out data that has been scraped by a Relay and turns it into something useful. In the case of Bluesky — the social network — it's about showing you posts from people you follow, not showing you stuff from people you've blocked, and notifying you of people who've mentioned you. The idea here is that this part could be replaced with something that isn't a social network, and could be used for just about anything. The problem is that it's currently extremely loosely defined, and also [hasn't been implemented by anyone else](https://alice.bsky.sh/post/3laega7icmi2q#:~:text=documented%20here.-,AppView,-The%20elephant%20in).

There are two other things that are directly under Bluesky's control: the [DID:PLC](https://github.com/did-method-plc/did-method-plc) and [DMs](https://anderegg.ca/2024/05/23/digging-into-bluesky-dms). [DIDs](https://www.w3.org/TR/did-core/) are an open standard to allow people to identify things in a distributed way. However, the PLC method that Bluesky uses is currently under their control. It was [previously known as the "placeholder" method](https://github.com/did-method-plc/did-method-plc/blob/0e8370fc1e616e6f1f76f8b8c445d6dfe8e95f04/README.md), because they intended to get away from it as soon as they could build something decentralized. Instead, they (I think wisely) decided to stick with it for the meantime. However, if you want to look up a DID:PLC, you need to query the Bluesky servers. This is important because every user is identified by a DID:PLC, and all interactions need to reference them.

Similarly, [DMs are currently handled outside of atproto](https://docs.bsky.app/blog/2024-protocol-roadmap#:~:text=Basic%20%22Off%2DProtocol%22%20Direct%20Messages%20%28DMs%29). They're not part of the atproto spec, and need to go through Bluesky's servers. I'm not sure how or when these will be updated.

All this to say: the Bluesky team seems like they're earnestly working toward a decentralized platform, but they have a lot of work ahead of them. Years of effort, in my estimation. In the meantime, Bluesky is slightly more decentralized than, say, Facebook — but not by much. Yes, you can host your own data. Yes, you can scrape all of the content on the network. But you can't do anything with it unless you're attached to the Bluesky service. I believe this will change with time, but it will be prohibitively expensive and we're not there yet.

I'll also add that the reason I'm a big fan of a ActivityPub solution like Mastodon is that it's [quite inexpensive](https://masto.host/pricing/) to run your own complete stack unless you're extremely famous. Hosting a Mastodon instance is a one-step process, and you then control everything. To get the same experience with atproto, you'll need to spend hundreds or thousands of dollars a month, and even then you still don't control everything as of today.

### Radically open

I think some might be surprised to learn how open Bluesky is. It's trivially easy to [grab an export of any user's data](https://docs.bsky.app/blog/repo-export). It's also a core assumption of the service that all the data (aside from out-of-protocol stuff like DMs) is completely open. You can watch the [firehose of data](https://firesky.tv/) go by if you'd like. If you want to run a Relay, you have to download all the data. This is because the data in the network is all [cryptographically signed based on what came before it](https://atproto.com/specs/repository). The protocol does this using the [Merkle tree structure](https://en.wikipedia.org/wiki/Merkle_tree), which is also how Git stores data. The issue with this is: if you want to look at one piece of content in the system, you also need to know about everything that happened before. For people using the Bluesky service, this isn't something you need to think about. But behind the scenes, it's helpful to know that everything being added to the service could potentially be available for anyone else to use for any purpose.

### Financial concerns

Bluesky is currently free to use, and I think they intend it to stay that way. This is easier when there are fewer users, and I'd bet that the technical choices discussed above make things more expensive to run. The CEO, [Jay Graber](https://en.wikipedia.org/wiki/Jay_Graber), seems like a smart person who's trying to do the right thing. However, she's also someone with a background in the crypto industry who [recently accepted funding lead by a crypto investor](https://bsky.social/about/blog/10-24-2024-series-a). What does that mean for the service? Who knows! But it doesn't sound great to me. Investors like to make returns. Bluesky is currently only making money by [reselling domains for usernames](https://bsky.social/about/blog/7-05-2023-namecheap). I don't think that's going to foot the bill for all this.

### Small things

The above pieces are things I worry about, but I'm pretty sure I'm in the minority. Most people don't care about decentralization or even if their content is being scraped. I can't imagine they care how the service is being paid for. But here are two nitpicks I'll add here that I think are more product-level: repost control and post editing.

On Mastodon and Twitter-of-old, I was able to follow a user, but only see posts from them. Many people hit the repost button a lot, and overwhelm my feed. I'd love the ability to selectively disable reposts from a user without having to build a custom feed to do so.

Also, it would be great to edit posts! I believe this is tricky because of the Merkle tree structure mentioned above, but it's a pain these days when every other platform has the feature.

### Good things

Now that I've gotten some grumpiness out of my system, I would like to recognise some legitimately great things that Bluesky is doing. First up, domain-based usernames.

You can follow me on Bluesky as [@gavin.anderegg.ca](https://bsky.app/profile/gavin.anderegg.ca). I was able to set this up easily by [adding a TXT record to my domain that links to my DID:PLC](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial). This is great! It allows me to effectively "blue check" myself, in a [similar way to Mastodon](https://joinmastodon.org/verification). The domain-based approach is quite flexible, and I think it's a great solution.

Bluesky also offers both [composable moderation](https://bsky.social/about/blog/4-13-2023-moderation) and the ability to [choose your own algorithm](https://bsky.social/about/blog/7-27-2023-custom-feeds). I'm someone who just wants to see a chronological feed of posts from the folks I follow, but I absolutely understand the appeal of these features. It's made especially clear when compared to Threads, which only wants to show me [inane engagement bait](https://www.theverge.com/2024/10/7/24264382/threads-engagement-bait-problem-mosseri-meta) by default. There are even some [third-party services](https://www.southernfriedscience.com/a-quick-and-dirty-guide-to-making-custom-feeds-on-bluesky/) which make setting up your own custom feed easier.

I also really love the idea of [starter packs](https://bsky.social/about/blog/06-26-2024-starter-packs). If you're someone who's joining the service, picking who you want to follow is rough. A starter pack lets you to follow a set of users recommended by someone you trust. Anyone can create a starter pack, so it's easy to grab a few and have a lively feed a few moments after joining.

### Everyone's experience is different

As people are fleeing X, I've seen a lot of thoughts from people about engagement. I'm on Mastodon, Bluesky, and Threads. On each network, I've seen a post like, "I joined and I've got more engagement here than anywhere else". I'm certain that's true for that person, but I think this is so variable as to be useless.

I joined Mastodon in late 2022, along with the [Relay](https://www.relay.fm/), [ATP](https://atp.fm/), and [Daring Fireball](http://daringfireball.net) crowd. I get a lot of engagement on Mastodon! I'm also a white guy who cares too much about expensive technology. Bluesky seems to be winning with artists and random local groups. I [mentioned this before](https://anderegg.ca/2024/10/21/thoughts-on-the-recent-migration-from-x-to-bluesky), but my new city councillor [campaigned on Bluesky](https://bsky.app/profile/lecwhite.bsky.social) and it was to her credit!

I bring this up because I think different social networks might "fit" better for some than others. I've seen Bluesky described as having "[theater kid energy](https://www.garbageday.email/p/bluesky-s-the-new-twitter-probably#:~:text=that%20Bluesky%20had%20%E2%80%9C-,theater%20kid%20energy,-.%E2%80%9D%20%28He%E2%80%99s%20not%20exactly)", which, heck, I'm here for! Others have said Mastodon has a "[homeowner's association](https://www.zdnet.com/article/i-tried-replacing-twitter-with-bluesky-threads-and-mastodon-heres-what-i-found/#:~:text=joining%20a%20Mastodon%20server%20feels%20a%20lot%20like%20joining%20a%20homeowner%27s%20association)" vibe. I haven't personally felt that, but I recognise that the content warnings and block lists can give that impression.

### Maybe Bluesky has "won"

I don't know what the social media landscape will look like in 6 months, but I'd bet things will change. If Bluesky comes out as a "winner" and more posting happens there, I think I'm generally fine with that. At least for now.

The whole Twitter mess has taught me not to attach myself too closely with these things anymore. I hung on far too long to Twitter while it made me feel terrible. My goal going forward is to post more to my own site and aggregate to any social channel I currently care about. I'm happy to interact on any that I'm a part of, but I'm also going to be much quicker to pull the ripcord if things start going down hill.


---


[^1]: Alice, the author of the story and the Bluesky post I linked to, reached out to me. It turns out that the 18 GB/day figure was only taking into account content from [Jetstream](https://docs.bsky.app/blog/jetstream), which provides JSON data rather than the raw [DAG-CBOR](https://atproto.com/specs/data-model) data used by atproto. This means the actual growth rate is about 10x as much.
