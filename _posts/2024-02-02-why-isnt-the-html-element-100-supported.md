---
title: Why Isn't the &lt;html&gt; Element 100% Supported on CanIUse.com?
date: 2024-02-02 16:51:21 -0400
---

I saw a [Mastodon post](https://mastodon.gamedev.place/@Ronflaix/111862153259345050) that made me laugh this morning. It seemed sort of crazy that the `html` element [wouldn't have 100% support](https://caniuse.com/mdn-html_elements_html) on CanIUse.com. Heck, I've been using it since 1994 and it worked just fine back then! This led me down a bit of a rabbit hole.

A bit of background, first. [Can I Use…](https://caniuse.com) is a site that helps web developers track the adoption rate of web technologies. It estimates browser usage, measures feature compatibility, and spits out a number that tries to reflect how available a feature is. It's a site I've been using almost since [it launched in 2010](https://web.archive.org/web/20100430032738/http://caniuse.com/) and I've always found it really useful.

So why is it currently saying the `html` element only has 97.34% support? That's less than the current support percentage for the [`audio` element](https://caniuse.com/audio)!

One thing I learned when looking into this is that a lot of the data on the site actually comes from [MDN](https://developer.mozilla.org/en-US/) [^1]. MDN is another resource I use and trust, so this seems reasonable to me. It also often has stats about feature uptake, so it makes sense for CanIUse.com to piggyback on that.

Looking at the [MDN page for the `html` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html), it has a [browser compatibility section](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html#browser_compatibility). In that are two rows with a lot of red Xs. The first is for the optional `manifest` attribute on the `html` element. This is deprecated and was never standardized. The second is the related "[secure context required](https://w3c.github.io/webappsec-secure-contexts/)", which is an [Editor's Draft](https://www.w3.org/standards/types/#x2-3-editor-s-draft) — that is, not something currently on the standardization track. I don't know how this was previously related to the `html` element, but that use was also [never standardized and is deprecated](https://caniuse.com/mdn-html_elements_html_manifest_secure_context_required).

So, there are two features listed here that almost all browsers *correctly* do not support. But still, it doesn't look like this is the reason for the missing 2.66%. There are some browsers that are listed as "Support Unknown". Adding up all the current usage for these browsers comes to 2.53%. There's also an entry for Android Browser versions 2.1–4.3 which is listed as not supporting the `html` element — which I find highly dubious — but it's listed as having a usage share of 0%. I suppose there might be some rounding errors here that would bump the 2.53% to 2.66%? But I still find this very unclear.

So yeah, I don't have a great answer for this. If you do, please let me know! I've always taken the numbers from CanIUse.com with a few grains of salt, but I'll be adding a few more going forward. I still think it's a great resource.

--

[^1]: MDN used to stand for [Mozilla Developer Network](https://en.wikipedia.org/wiki/MDN_Web_Docs). Now it's just MDN. I spent a few minutes looking on the MDN site to see if I could find any mention of the full name, but I guess they're just all in on "MDN" now.
