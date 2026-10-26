---
title: >
    Just put some HTML on the web
date: 2026-10-26 16:56:01 -0300
---

The internet is becoming a more dangerous place, and fast. [LLMs are only getting better at identifying security issues](https://anderegg.ca/2026/05/10/ai-and-software-security-the-slop-becomes-signal), and more people are taking advantage of this. Some people argue that [LLMs will eventually make large-scale vulnerabilities a thing of the past](https://blog.mozilla.org/en/firefox/ai-security-zero-day-vulnerabilities/). I'm not so sure. Either way, I think it's a good idea to have less stuff that can be hacked online. One way to do that is with statically generated sites.

This past week was a bad one for security issues. The most prominent one was [PHP2Shell](https://www.wiz.io/blog/php2shell-php-rce), which had PHP on the minds of non-technical folks — not a win for society. There was also [Node2Shell](https://cycode.com/blog/node2shell-cve-2026-111497/), which exploited Node's built-in [Brotli](https://en.wikipedia.org/wiki/Brotli) compression stack. [But there were a whole lot more](https://craci.com/resources/CVE-publication-trends?sev=critical).

<a href="https://craci.com/resources/CVE-publication-trends?sev=critical"><img src="https://anderegg.s3.amazonaws.com/cves.avif" width="2041" height="829" alt="A chart showing the number of reported critical security vulnerabilities jumping from around 300 a month to over 1,500 a month since November of 2025."></a>

Note that the above chart is only showing critical [CVEs](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures). Here's another [showing all CVEs](https://cve.0xosprey.com/). When [I last fretted about this in May](https://anderegg.ca/2026/05/10/ai-and-software-security-the-slop-becomes-signal), we were still doing rookie numbers. Things aren't likely to get better any time soon.

In my time, I've built a lot of stuff on the web. From the early 2000s to the mid-2010s, I specialized in building on top of [content management systems](https://en.wikipedia.org/wiki/Content_management_system) (CMSs). For most of that time, there was a [standard platform the team built with](https://craftcms.com/). This made sense for building larger sites, when people on our side would be doing much of the content work. In other cases, it was because "the client says they want to edit the site".

It's very possible your clients acted differently than mine, but the number of clients who actually edited their CMS-based site was a rounding error for me. Instead, our team usually got site change requests via email. Maybe there was a gung-ho junior person on the client's end who'd update things for a while, but it was almost always back to email once that person left. The only clients who routinely edited their sites were those with internal development teams. [^1]

More recently, I've seen a lot of folks building massively complex Node-based contraptions with server-side components to power what are effectively static websites. Lots of [SSR](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering), [hydration](https://react.dev/reference/react-dom/client/hydrateRoot), and the like. There's nothing inherently wrong with these strategies, but I'd argue that they're overkill for content-focused sites.

If you're building a complex web app, you're likely going to need a server in the mix. If so, you presumably have a plan to maintain it. Someone will have to apply security patches, but no one should find this surprising. On the other hand, if what you're building is mostly static and content-based, you should ask yourself if it's still worth it to use dynamic/server-side tooling.

How often will that site's content be updated, *really*? Do you have a plan to maintain the software it's built on? Will there be a maintenance contract in place with the client to cover the time to patch things? I'm betting that web software is going to need ever more attention in the future. Patching your CMS- or Node-based site every six months isn't going to cut it anymore, and clients may raise an eyebrow at the "security update" line items on their invoice. [^2]

What if, instead of all that, you just put some HTML on the web?

I got the idea of [static site generators](https://en.wikipedia.org/wiki/Static_site_generator) (SSGs) when I first heard of them, but it took a while for me to really get on board. When I switched this site over to [Jekyll](https://jekyllrb.com/) from [toto](https://github.com/cloudhead/toto) in [2012](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/91fd20e7bc0d3dc5ed32e56b5a274bbb09c2ea51), it started to click. What if all the interesting work happened at build time, and the output looked basically like a website from the 90s? That sure would be [lightning quick](https://pagespeed.web.dev/analysis/https-anderegg-ca/z5v71vvlnr?form_factor=mobile) and cheap to host! [^3] In fact, this site is hosted for free on [GitHub Pages](https://docs.github.com/en/pages), and has handled [many](https://news.ycombinator.com/item?id=42687121) [large](https://news.ycombinator.com/item?id=42150278) [traffic](https://news.ycombinator.com/item?id=39235001) [spikes](https://news.ycombinator.com/item?id=48891200) without breaking a sweat. The cherry on top is that I've never had to worry about applying security patches. [^4]

Though it's a good case study for a static site, a blog isn't all that interesting. [^5] Same goes for a standard brochure website. But since getting on the SSG bandwagon, I've found many other uses. Client dashboard? If the data's only changing every few hours, it's often cheaper to generate a set of JSON files than query the database. Custom data visualization? Again, I've had very good results building an SSG into the [ETL pipeline](https://en.wikipedia.org/wiki/Extract,_transform,_load). [Hugo](https://gohugo.io/) has been a huge boon here because of its [data source feature](https://gohugo.io/content-management/data-sources/).

There are other interesting examples in the wild. Cloudflare has had their documentation on [several flavours](https://blog.cloudflare.com/new-dev-docs/) of SSG [throughout the years](https://blog.cloudflare.com/open-source-all-the-way-down-upgrading-our-developer-documentation). [V&A wrote about](https://www.vam.ac.uk/blog/digital/how-we-brought-the-online-collections-into-the-modern-age-using-web-technology-of-the-past) their SSG transformation. Fastmail [documented their move from WordPress to Eleventy](https://www.fastmail.com/blog/building-a-blog/). For larger organizations, SSGs can save a lot in hosting costs. I think they'll also be saving ever more in security and maintenance.

But this stuff isn't just for nerds. [Publii is a great, free, and open-source tool](https://getpublii.com/) that can be used to graphically generate a static website. Also, I shouldn't discount hosted services like [Bear Blog](https://bearblog.dev/), [Pika](https://pika.page/), or [Micro.blog](https://micro.blog/). If you just want a place on the web without worrying about security issues, having someone else worry about that stuff isn't a bad idea, either.

I don't want to come off the wrong way here. There's nothing wrong with building dynamic software on the web. The point is: much of the web is mainly static anyway. Static sites are blazing fast, effectively free to host, and offer only the tiniest security footprint. If you're likely to get changes via email, you can save yourself (and your client!) some potential headaches by using a static site generator in the first place.

---

[^1]: In this case, we were usually doing the initial build, then training the client on how things worked. These builds were great because there was another team who would be responsible for keeping software up to date after the launch.

[^2]: Yes, some systems, like WordPress, will auto-update. However, if you're using version control, [you don't get updates by default](https://developer.wordpress.org/advanced-administration/upgrade/upgrading/#:~:text=Enable%20major%20updates-,For%20Developers:,-To%20enable%20automatic). Also, are you [auto-updating your plugins](https://developer.wordpress.org/advanced-administration/upgrade/upgrading/#plugin-theme-updates-via-filter)? That also requires special considerations.

[^3]: Sadly, I don't get four perfect 100%s on PageSpeed because my analytics provider blocks traffic coming from Google's bots. For normal visitors, it should be a 100% experience, though.

[^4]: Static sites aren't foolproof, of course. The server the site lives on could still be compromised, for example. But there's *so much less* that can go wrong, and the cost to rebuild a site is effectively zero if an incident does occur.

[^5]: Even though this site has significantly more content on it than many CMS- or Node-based sites I've helped build in the past.