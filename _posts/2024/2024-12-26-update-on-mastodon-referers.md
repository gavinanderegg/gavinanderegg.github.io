---
title: >
    An update on Mastodon and referer headers
date: 2024-12-25 12:30:08 -0400
---

Earlier this year, [I looked into why Mastodon didn't include referer headers](https://anderegg.ca/2024/05/19/whats-up-with-mastodon-and-referer-headers). As someone who enjoys following web analytics, it seemed a shame that Mastodon appeared never to send any traffic. I knew this wasn't the case, but that lack of traffic data certainly wasn't doing Mastodon any favours in terms of marketing.

Yesterday I saw [this Mastodon post from Terence Eden](https://mastodon.social/@Edent/113714460267735559). I haven't been keeping tabs on social media and RSS sources as much over the last few weeks, so I missed [his original blog post](https://shkspr.mobi/blog/2024/12/mastodon-now-sends-referer-headers-hurrah/) about this. Turns out, Mastoson servers now have an [option to enable referer headers](https://github.com/mastodon/mastodon/commit/425311e1d95c8a64ddac6c724fca247b8b893a82)! This is enabled for everyone using Mastodon.social, as Terence and I both am. I think this is a great option, and I hope it's something that other large servers enable. I don't think it'll affect things dramatically, but I appreciate anything that helps spread the word about Mastodon.



