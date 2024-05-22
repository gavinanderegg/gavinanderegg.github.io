---
title: Jekyll Might Have Failed Me?
date: 2024-05-22 18:35:03 -0300
---

I use tags in [Bear](https://bear.app/) to save links and quick notes for reference. A few of them are ideas for work-related things or future project ideas, but most are just cool things I want to keep track of. I've been thinking for a while: why keep those locked in Bear? I really like how many other sites, [Kottke.org](https://kottke.org/) being a great example, share short content.

I'm still waffling about how/if I want to set this up, but I decided to at least test how this could work. I was able to easily set up the [collection in Jekyll](https://jekyllrb.com/docs/collections/), and played with a quick layout for it. I then looked at how RSS/Atom feeds work. I was thinking that I might want to have multiple feeds. Maybe not everyone wants quick posts, for example. If I did set this up, I'd also want an "everything" feed and long-posts-only feed. I like how this is done on [Daring Fireball](https://daringfireball.net/feeds/).

Turns out, [that doesn't](https://github.com/jekyll/jekyll-feed/issues/289) [seem possible](https://github.com/jekyll/jekyll-feed/issues/390). The [jekyll-feed plugin](https://github.com/jekyll/jekyll-feed/) that's provided by [GitHub Pages](https://pages.github.com/versions/) creates a single feed file for each content type. There's no way to combine them via the plugin, and I'd prefer not to do this myself. I'm a big fan of using libraries to generate XML in general. There's a lot that that go wrong when creating XML with templates. [^1] Sadly, [that seems to be what the current plugin is doing](https://github.com/jekyll/jekyll-feed/blob/master/lib/jekyll-feed/feed.xml). I'd also prefer to use an RSS/Atom library, as I'm certain there's a lot that can go wrong there as well.

I'm not even sure this is something I want to do. I'm also not sure I should care that much about how my feed is generated. But hitting this one roadblock is also making me rethink sticking with Jekyll. Even if the issue with jekyll-feed is fixed, it's unclear if it would work with the [older version of Jekyll used by GitHub Pages](https://anderegg.ca/2024/02/18/some-thoughts-on-jekyll). I plan on looking into how this might work with [Hugo](https://gohugo.io/) and [11ty](https://www.11ty.dev/) next.

---

[^1]: The 3rd edition of *[XML in a Nutshell](https://www.google.ca/books/edition/_/_QAhsNWUSFoC)* has 689 pages! I sadly owned the 2nd edition of this, and it was well used. Good book, bad topic.
