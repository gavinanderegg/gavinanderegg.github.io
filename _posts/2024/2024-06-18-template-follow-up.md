---
title: >
    Follow-up on templating structured data
date: 2024-06-18 10:41:44 -0300
---

When I [waffled about template-based XML](https://anderegg.ca/2024/05/24/on-templatebased-feed-generation), I mentioned that I discussed my issue with a friend. That friend, Mike Burke, wrote a follow-up post: [*On generating structured data from templates*](https://mrb0.com/2024/06/17/on-code-generation-from-templates/). It has several examples that demostrate the sorts of trouble you can get into when sticking data into a structured format. I agree with everything he's said, but still feel that RSS/Atom feeds are likely "safe enough" to template.

Unrelatedly, Meta launched their [Threads API](https://developers.facebook.com/docs/threads) today. I looked through the supplied [sample app](https://github.com/fbsamples/threads_api/tree/main) and found that they're using the [Pug templating system](https://pugjs.org/api/getting-started.html). I hadn't heard of this before, but it's similar to the [htmltag](https://github.com/LiftoffSoftware/htmltag) library that Mike used as an example in his post. Even more than with syndication feed templates, I feel that almost all HTML on the web isn't valid. Some might perfer to use templates like these, but I've been writing HTML for 30 years at this point… so I'll probably keep doing that.