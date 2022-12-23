---
title: Setting up WebFinger
---

I set up a [Mastodon account](https://mastodon.social/@gavinanderegg) over a month ago and have been enjoying my time there. It's niche, it's small, and it feels more like the olden days of Twitter — back when social media was less about "engagement". It's possible that Mastodon will eventually suffer from [the same issues](https://www.pnas.org/doi/10.1073/pnas.2024292118) that sucked the joy from Twitter, but its been fun to explore so far.

One piece I find fascinating is the underlying [ActivityPub protocol](https://activitypub.rocks) that powers the "[Fediverse](https://en.wikipedia.org/wiki/Fediverse)". [John Voorhees](https://mastodon.macstories.net/@johnvoorhees) recently wrote [an excellent article about the promise of ActivityPub](https://www.macstories.net/stories/making-activitypub-your-social-media-hub-for-mastodon-and-other-decentralized-services/) which inspired me to play around more with the protocol.

As a first step, I decided to set up [WebFinger](https://webfinger.net) on my domain. This is a Fediverse take on the old Unix [`finger` protocol](https://en.wikipedia.org/wiki/Finger_(protocol)) that allowed people to share information about themselves on computer networks. With WebFinger, users on a [domain](https://en.wikipedia.org/wiki/Domain_name) can publish information about where they exist in the Fediverse. This can help others to find people using their domain/email address, and also to verify that someone is who they claim to be.

I host this site using [GitHub Pages](https://pages.github.com). It's a great service, but can be limiting at times. Happily, it was quite easy to get working! It's set up [statically](https://guide.toot.as/guide/use-your-own-domain/#5-static-files) for now, but there are some Jekyll-specific hooks I may use later. Now that it's working, people can [search for me via my domain or email address](https://webfinger.net/lookup/?resource=https%3A%2F%2Fanderegg.ca) and find me on Mastodon.
