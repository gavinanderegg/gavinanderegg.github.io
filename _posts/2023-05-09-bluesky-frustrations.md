---
title: Bluesky Frustrations
date: 2023-05-09 10:38:21 -0300
---

Over the past couple of weeks, my news and Mastodon feeds have been overloaded with discussion of Bluesky. This has made me rather grumpy, but I’ve had a hard time articulating why.

About a week ago, I read [an excellent piece by Erin Kissane](https://erinkissane.com/blue-skies-over-mastodon) where she did a good job debunking some of the anti-Bluesky sentiment I’d seen on Mastodon. She points out one of the big complaints I have with Bluesky: it’s associated with Jack Dorsey, someone I [absolutely do not trust](https://twitter.com/jack/status/1518772756069773313). [He announced the Bluesky project at the end of 2019](https://twitter.com/bluesky/status/1204766347512537088), and is [currently on the board](https://blueskyweb.xyz/faq#:~:text=What%20is%20the%20corporate%20structure%20of%20Bluesky%3F).


#### Squishy feelings
I agreed with almost every point in Erin’s piece. Yes, Mastodon is clunky and needs to be more welcoming. There is a lot of NIMBY-ism from people who have been on the service for years. Some people want everything behind a content warning, others find any warning annoying. Having to choose a server is a bigger stumbling block than nerds like to believe it is. But I still love the place, and I want it to get better.

This is definitely part of my frustration. I have a team that I’m cheering for, and it’s made some huge gains in a short time. There are now some incredibly good apps for the platform, like [Mona](https://www.macstories.net/reviews/mona-a-unique-mix-of-customization-options-and-features-you-wont-find-in-any-other-mastodon-app/) and [Ivory](https://tapbots.com/ivory/). [Momentum has started to build around the underlying protocol](https://www.theverge.com/2023/4/20/23689570/activitypub-protocol-standard-social-network).  It seems like a [shame to start another protocol](https://xkcd.com/927/), and it’s painful to see people [spending hundreds of dollars to score invites to Bluesky](https://techcrunch.com/2023/05/02/bluesky-invites-become-a-hot-commodity-as-demand-for-the-twitter-alternative-outstrips-access/).

I also love that there’s no algorithmically suggested content on Mastodon. When I used Twitter, I did so in apps that only showed a chronological timeline. Whenever I used the first-party Twitter app or website, it would always try to surface “top content”. These were hashtags, posts, or users the service thought I should see – and there was usually something in there that left me feeling worse. One of the bigger complaints with Mastodon is that it’s hard to find users to follow or content you might like. I get that, but my life improved when I stepped away from Twitter’s “engagement based” content.


#### Technical frustrations
A lot of people are testing out Bluesky because it’s the new hot thing. Fair enough! If I got an invite, I would likely set up an account just to stake my claim.

Erin mentions that it’s refreshing to see a new take on a distributed social platform. That’s a valid take, and I get it. My more curmudgeonly view is: [the AT Protocol has been in development for more than 2 years](https://github.com/bluesky-social/atproto/commit/b3110f0eb58c05c34ccec29447bb9b8b2f082373), and it’s still extremely unclear how chunks of it will work.

[Eric Rescorla has a great piece about his initial explorations of the AT Protocol](https://educatedguesswork.org/posts/atproto-firstlook/). In it, he gives a good overview of the pieces that seem underspecified in the documentation. The piece is from November of last year, but [the documentation hasn’t changed much since then](https://github.com/bluesky-social/atproto-website/commits/main/content/specs). It’s mostly been fixing typos, schema changes, and some password details. Still a lot of unanswered questions.

It also feels over-engineered and possibly suffering from some [Not Invented Here](https://en.wikipedia.org/wiki/Not_invented_here) syndrome. This is a long video, but [Joe Beda’s exploration of current state of the AT Protocol](https://www.youtube.com/watch?v=9tZrxSyRPH0) was an interesting watch. There are some novel ideas in the AT Protocol! On the other hand, there are some concrete worries. Why use [Merkle Search Trees](https://atproto.com/guides/data-repos#data-layout) if people can delete things? Doesn’t that mean data repositories will need to be rewritten every time a delete happens? [^1] [DIDs seem interesting](https://atproto.com/guides/identity#identifiers), but the plan to have a centralized “Placeholder” method that will be replaced “[within the next few years](https://atproto.com/specs/did-plc#:~:text=We%20expect%20a%20method%20to%20emerge%20that%20fits%20the%20bill%20within%20the%20next%20few%20years)” doesn’t seem great. The [“big graph services” part of the decentralized equation](https://atproto.com/guides/overview#achieving-scale) seems like it will require substantial compute/network resources, and may end up being *de facto* centralized. Plus, [a rather complex data storage mechanism](https://atproto.com/guides/data-repos#:~:text=Every%20node%20is%20an%20IPLD%20object%20%28dag%2Dcbor%29%20which%20is%20referenced%20by%20a%20CID%20hash)? [A new in-house schema system](https://atproto.com/specs/lexicon)? It feels like a lot.

None of this is show-stopping, but it does feel half-baked and over-complex. I’m not saying that developing a new decentralized social media protocol is easy, but I feel like simpler might be better here. The AT Protocol does have some novel features over ActivityPub, but ActivityPub exists in a decentralized form today. I think it’s going to be a while before the Bluesky developers can fully deliver on their promises.


#### But it’s fun!
All of the above is just technical junk. I’m in the vast minority for caring about any of this. Obviously the system works as a centralized Twitter replacement today, and I doubt most people care whether it becomes decentralized in the future. It’s broken in some sketchy ways ([like people being able to claim domains they don’t own](https://news.ycombinator.com/item?id=35820815)), but it’s a closed beta and getting patched quickly. Also, Bluesky might be succeeding because it’s a [quirky place to shitpost](https://www.theverge.com/2023/5/2/23708385/bluesky-weather-report-moderation-app-store). [A lot of folks](https://mastodon.social/@gruber/110314382066961654) [seem to be](https://www.theverge.com/2023/4/15/23683846/bluesky-twitter-clone-at-protocol-favorite) [having a great time](https://www.wired.com/story/bluesky-is-fun/)!

I wonder, though: how much of the fun will be left once it’s decentralized, open to the public, and (presumably) monetized? Yes, it’s slicker than Mastodon at present, but things like decentralization and [algorithmic choice](https://atproto.com/guides/overview#algorithmic-choice) are deeply nerdy topics. Maybe the Bluesky team have great ideas for adding these features and maintaining a fun user experience? Maybe the service will have inertia by the point these features exist and it won’t matter? I’m somewhat skeptical.

Assuming the future techie stuff isn’t a stumbling point, there are also some real privacy concerns. [Block lists are currently public data](https://twitter.com/MattBinder/status/1652142389165797377), and it’s unclear how this can be avoided. The AT Protocol seems to require all records be “[crawlable](https://atproto.com/guides/overview#achieving-scale)”, so it's not clear how private content could work. [At least right now, you can download everything](https://worthdoingbadly.com/bsky/). [^2] This data will be a boon to academics and hostile state actors alike. Because ActivityPub is a simpler publish/subscribe system, it's much more difficult to get large data sets like this. On Mastodon in particular, it's protected by the federated server structure. This is what makes Mastodon difficult to search, which is an annoyance to some and a privacy/security feature to others.

Speaking of annoyances, I'm curious what Bluesky's monetization strategy will be. Many seem to think Bluesky is VC funded. [Instead, it’s a public benefit corporation](https://blueskyweb.xyz/faq#:~:text=Bluesky%2C%20the%20company%2C%20is%20a%20Public%20Benefit%20LLC.). Still, it needs to pay for server costs and employee salaries somehow. [Mastodon does this almost entirely through Patreon](https://www.theverge.com/23658648/mastodon-ceo-twitter-interview-elon-musk-twitter#:~:text=No%2C%20that%E2%80%99s%20pretty%20much%20it.). Will Bluesky do something similar? I sort of doubt it. My guess is that they’ll want to chase growth somehow, and my worry is that it’ll be with something cryptocurrency-based. Even if that’s not the case, this seems like another way the service could become less fun pretty quickly.


#### Who cares?
I’m writing this mostly to get it off my chest. Mastodon works for me, and I’m excited about ActivityPub. I’m not really trying to convince anyone that Bluesky is somehow terrible. That said, I’m skeptical about several pieces:

* Bluesky’s association with Jack Dorsey makes me uneasy.
* The AT Protocol documentation contains several technical claims that seem tricky to pull off. Maybe it’ll be a decentralized paradise in a year? It just seems like there’s a good deal of handwaving at the moment.
* People are having a great time! But I suspect this is because the service is currently small, simple, and centralized. Once the decentralized systems are in place, there’s a good chance it’ll be more confusing. Once more people are there, it might be more like bad-Twitter.
* Some of the Bluesky’s technical approaches are novel, I worry that some people may be blinded by the lack of privacy they provide.
* It’s also unclear what the monetization strategy is. A bad funding model could make the service less fun in a hurry.

All of these are challenges for the future. I selfishly wish that more people would focus on improving ActivityPub and Mastodon. I also think that Bluesky might be more popular as a small, quirky, centralized platform than it will be once its promises are fulfilled.


<hr>


[^1]: I can’t find this in the documentation anywhere, but it's [mentioned in a Hacker News comment](https://news.ycombinator.com/item?id=35845887). It seems like there will be “deletions” which sound like the content will stick around, and “purges” (like Git rebase) which are likely to be inefficient.

[^2]: This is both hilarious and pretty irritating. You can get every post via the API now, but you can’t link to a post on the web if you’re not logged in? Huh?

