---
title: >
    I guess I'm using WebP now?
date: 2026-10-08 15:23:05 -0300
---

After using the same few image formats for 20+ years, I'm now on the WebP bandwagon. That isn't something I thought I'd ever say. Now I'm wondering how soon it'll be before I can use a couple more.

When Google [announced the WebP format in 2010](https://blog.chromium.org/2010/09/webp-new-image-format-for-web.html) it was interesting, but only academically. WebP support was [added to Chrome in 2011](https://blog.chromium.org/2011/05/webp-in-chrome-picasa-gmail-with-slew.html), [^1] but other browsers took their time supporting it: [Edge in 2018](https://web.archive.org/web/20181223160828/https://blogs.windows.com/msedgedev/2018/10/04/edgehtml-18-october-2018-update/), [Firefox in 2019](https://www.firefox.com/en-US/firefox/65.0/releasenotes/), and [Safari in 2020](https://developer.apple.com/documentation/safari-release-notes/safari-14-release-notes). Until there was [baseline support](https://caniuse.com/webp), the format was [only being used selectively by content delivery networks](https://blog.cloudflare.com/a-very-webp-new-year-from-cloudflare/). Even then, WebP was a pain to work with. Photoshop didn't get native support [until 2022](https://www.cgchannel.com/2022/02/adobe-ships-photoshop-23-2/), and its "[Save for Web](https://helpx.adobe.com/photoshop/desktop/save-and-export/save-files/save-for-web.html)" and "[Export As](https://helpx.adobe.com/photoshop/desktop/save-and-export/export-files-to-different-formats/export-settings-and-export-location-preferences.html)" features *still* don't support the format.

Because of all this, I found WebP annoying. [I wasn't alone, either](https://wptavern.com/webp-by-default-on-hold-for-6-1-after-new-objections-from-wordpress-lead-developers). Things weren't helped by Google's eagerness to push the format. Their Lighthouse tool would often [complain that images weren't in WebP](https://developer.chrome.com/docs/lighthouse/performance/uses-webp-images), even when file size savings were relatively minor and format support was immature. For the past 20+ years, I've only really used [JPEGs](https://en.wikipedia.org/wiki/JPEG), [PNGs](https://en.wikipedia.org/wiki/PNG), and (later) [SVGs](https://en.wikipedia.org/wiki/SVG) to serve images on the web. [^2]

Since [ditching Photoshop](https://anderegg.ca/2026/07/12/an-infuriating-goodbye-to-photoshop) for Pixelmator Pro, I now have [much nicer tooling](https://support.apple.com/en-ca/guide/pixelmator-pro/pixdae75632d/mac) for dealing with WebP images. It turns out they're pretty good? In the past two [Liquid Glass](https://anderegg.ca/2026/10/02/two-more-270-design-grumbles) [grumble-pieces](https://anderegg.ca/2026/09/20/liquid-glass-in-270), I used WebPs because they were smaller than JPEGs or PNGs at the same visual quality. This won't always be the case, but I've not yet encountered a situation where WebP doesn't come out on top. Google has some findings on this for [lossy](https://developers.google.com/speed/webp/docs/webp_study) and [lossless](https://developers.google.com/speed/webp/docs/webp_lossless_alpha_study) versions of WebP.

It's not very surprising that WebP has advantages over JPEG or PNG. Even when I found the format annoying, I knew there were benefits. The difference is that I no longer have to go out of my way to use the format. Now I'm wondering if/when newer standards like [JPEG XL](https://en.wikipedia.org/wiki/JPEG_XL) or [AVIF](https://en.wikipedia.org/wiki/AVIF) will be supported by Pixelmator Pro. AVIF in particular looks very promising to me, and it also has [baseline support across browsers](https://caniuse.com/avif). Just a few days ago, [Google announced it was shipping JPEG XL support](https://developer.chrome.com/blog/jpeg-xl-in-chrome), [^3] so that might [hit baseline](https://caniuse.com/jpegxl) in the near future as well.

I'm certainly not as annoyed by AVIF or JPEG XL. Hopefully I won't have to wait as long to easily take advantage of them.

---

[^1]: And, of course, Opera.

[^2]: [GIFs](https://en.wikipedia.org/wiki/GIF) were also around, but only really for memes. Now they're usually [transformed into much smaller videos](https://techcrunch.com/2014/06/19/gasp-twitter-gifs-arent-actually-gifs/). I last used GIFs on the regular when I was [laying things out with tables](https://en.wikipedia.org/wiki/Spacer_GIF).

[^3]: [After having dropped it not too long ago](https://www.phoronix.com/news/Chrome-Dropping-JPEG-XL-Reasons). Google's gonna Google.