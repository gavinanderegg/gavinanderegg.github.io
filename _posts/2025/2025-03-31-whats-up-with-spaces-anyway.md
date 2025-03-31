---
title: >
    What's up with spaces anyway?
date: 2025-03-31 15:57:18 -0300
---

Recently a friend of mine told a tale of debugging woe. After configuring a third-party SaaS product, he provided a coworker with the secrets needed for integration. These needed to be included in some JSON files, and were helpfully provided as a JSON string for easy copying. Long story short: somewhere along the way, some regular spaces were replaced with [non-breaking spaces](https://en.wikipedia.org/wiki/Non-breaking_space). It took a while for them to track down why things weren't working.

JSON is pretty simple. [The format's homepage](https://www.json.org/) contains a series of [syntax diagrams](https://en.wikipedia.org/wiki/Syntax_diagram) which describe it succinctly. The diagrams have only gotten slightly more descriptive [since that site was launched in 2008](https://web.archive.org/web/20081006033103/https://www.json.org/json-en.html). JSON accepts the following as whitespace: space, linefeed, carriage return, and horizontal tab. All characters you can easily type with a North American keyboard layout in ASCII or Unicode.

{% highlight json %}
"layout": "post.html",
"tags": [ "posts" ]
{% endhighlight %}

Non-breaking spaces are also quite straightforward.