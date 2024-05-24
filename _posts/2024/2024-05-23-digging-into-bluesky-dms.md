---
title: Digging into Bluesky DMs
date: 2024-05-23 19:18:54 -0300
---

Yesterday, [the Bluesky team announced](https://bsky.social/about/blog/05-22-2024-direct-messages) that direct messages (DMs) were now available in first-party clients. I thought I'd dig into this to see if I could figure out how this worked.

I first found a mention of this feature coming on the roadmap. It's under the headline "[Basic "Off-Protocol" Direct Messages](https://docs.bsky.app/blog/2024-protocol-roadmap#product-features)". Based on the description here, it looks like this is a centralized side-channel outside of the protocol. I assume this is separate from "[Non-Public Content](https://atproto.com/specs/atp#future-work)" mentioned in the atproto docs, and is more of a stopgap.

I then looked to see if I could find any technical details about the implementation. I assumed DMs are handled outside of the [PDSs](https://github.com/bluesky-social/pds), but I decided to look just in case. [The most recent commits to the repo](https://github.com/bluesky-social/pds/commits/main/?since=2024-05-20&until=2024-05-23) just bumped API and PDS version numbers. I then found mention of a ["convo" message type in the client source](https://github.com/bluesky-social/social-app/tree/efdcfd09e6040fd6fd9a6bfe090733ff7ebe00b3/src/state/messages/convo), and then a line that referenced [`api.chat.bsky.convo`](https://github.com/bluesky-social/social-app/blob/efdcfd09e6040fd6fd9a6bfe090733ff7ebe00b3/src/state/messages/convo/agent.ts#L528). This helped me find some [entries in the API docs](https://docs.bsky.app/docs/api/chat-bsky-convo-list-convos).

Now it's clear how one could access DM content… but I was hoping there'd be more detail on how the system works from a backend perspective. I'm assuming there are servers separate from the ones handling the atproto work that are just for DMs? Maybe the team doesn't want to talk about/document these because it's a stopgap? Perhaps they just haven't gotten around to it? Maybe I've just completely missed it somewhere?

I also decided to look and see if anyone else was using this. There are a handful of third-party clients, and [Klearsky](https://github.com/mimonelu/klearsky) is [in the process of integrating DMs](https://github.com/mimonelu/klearsky/commit/bf0db9b42975c0620f0061402570b23544c7a3ef). I didn't learn much more from this, but it was interesting to see [the work started on May 19th](https://github.com/mimonelu/klearsky/commit/2c6d2d503377b1d59842c8d75a9ed79d9918cbb1) — three days before the feature was officially released. It turns out that the API endpoints were [added to the docs on May 13th](https://github.com/bluesky-social/bsky-docs/commit/4d81515c0ec72cbb05cc8eaf9cfdb8a9c5725662). It also turns out that the feature was [found by users on a staging server](https://bsky.app/profile/pfrazee.com/post/3kszzni4kgh2h) ahead of the release date as well.

So, not much detail on how this works behind the scenes. At least it's nice to know that the API endpoints exist and are documented.
