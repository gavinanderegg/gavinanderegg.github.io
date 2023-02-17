---
title: Typeface Tournament
date: 2023-02-16 21:30:40 -0400
---

[Tim Bray recently wrote some thoughts on picking a new typeface for programming](https://www.tbray.org/ongoing/When/202x/2023/02/09/Monospace). [He then posted a followup with even more options](https://www.tbray.org/ongoing/When/202x/2023/02/14/More-Mono). These articles struck a chord with me, and I thought it would be fun to do another review of the available options.

I switched from using [Inconsolata-dz](https://nodnod.net/posts/inconsolata-dz/) to [Menlo](https://en.wikipedia.org/wiki/Menlo_(typeface)) in 2013, the last time I did a typeface survey. Menlo seems like a boring option (it’s been a default in macOS since 2009), but I find it extremely readable.

Since I last looked over the field, I found some new-to-me developer typography resources.

The first is [CodingFont.com](https://www.codingfont.com). This site has two modes: the first is a fun “tournament” where you match typefaces against each other. I tried this and ended up in a showdown between JetBrains Mono and Hack. Hack ended up being my winner, but I downloaded both to try with real code. The site also included a browsing mode which allows you to put two typefaces side-by-side. Sadly you can’t edit the text in the samples.

CodingFont.com is great, but there are a small number of typefaces compared. The selection seems similar to that of the [monospace collection in Google Fonts](https://fonts.google.com/?category=Monospace), though Google Fonts has a slightly different set at the time of writing. The additions in the Google Fonts collection include [Chivo Mono](https://fonts.google.com/specimen/Chivo+Mono), [Fragment Mono](https://fonts.google.com/specimen/Fragment+Mono), [Martian Mono](https://fonts.google.com/specimen/Martian+Mono), and [Spline Sans Mono](https://fonts.google.com/specimen/Spline+Sans+Mono).

(EDIT: [As noted by Tim Bray](https://mastodon.social/@timbray@hachyderm.io/109881181854977568), CodingFont.com also seems to alter the line-heights of the typefaces they show. This is unfortunate, but didn't seem to affect my "winning" choices. At least in Nova by Panic, [this is something that can be updated](https://help.panic.com/nova/preferences/#editor). It also seems to be editable under the `editor.lineheight` setting in Visual Studio Code.)

Another interesting site is [ProgrammingFonts.org](https://www.programmingfonts.org). It allows editing, and has some interesting filtering options, but has a lot of typefaces that I’d categorize as “zany”. Some of the options here are commercial, but I didn’t see that noted anywhere. The site was useful to me if only to quickly flit over larger set of varied typefaces. It didn't add anything new to the pile, though.

After spending some time waffling over minor details, I really ended up liking [Hack](https://sourcefoundry.org/hack/) for use on real code. I didn’t have Menlo available in CodingFont.com or ProgrammingFonts.org, so I was surprised how closely it resembled my current font when I installed it. It turns out that they’re both derived from [Bitstream Vera](https://en.wikipedia.org/wiki/Bitstream_Vera).

From Hack, I love the extra space around square brackets and parentheses. Also the additional separation between successive hyphens and underscores. I also like the “`i`” being curved on the bottom to match the “`t`”. One thing I don’t prefer is the large dot in “`0`”. I prefer Menlo’s slash, but it’s not a very strong preference.

My runners up from the CodingFont.com tournament were:

* [Inconsolata](https://fonts.google.com/specimen/Inconsolata) — I originally found this font in 2009 on a [recommendation from Dan Benjamin](https://web.archive.org/web/20090601171845/http://hivelogic.com/articles/view/top-10-programming-fonts). This was mere months before [Menlo was added to Mac OS X](https://en.wikipedia.org/wiki/Mac_OS_X_Snow_Leopard). I loved it then, and am still drawn to it now. The major issue at the time were the single- and double-quotes being slightly curved. Happily, [Inconsolata-dz](https://nodnod.net/posts/inconsolata-dz/) was around before Dan Benjamin’s post and I found that quickly. Even better, the version of Inconsolata on Google Fonts no longer seems to have this issue. I wondered about switching back for a change, but I really do prefer the Bitstream Vera style.
* [JetBrains Mono](https://www.jetbrains.com/lp/mono/) — I remember this being released a couple of years ago and finding it quite nice. I remember installing it, but wasn’t in the right headspace to switch typefaces at the time. I still think it looks quite good, and seeing it side-by-side with Hack on CodingFont.com gave me pause while voting. Hack won because it’s slightly more rounded and has slightly wider glyphs, but I think JetBrains have made a wonderful typeface.

### Examples

* [Hack](https://anderegg.s3.amazonaws.com/typefaces/hack.png)
* [Inconsolata](https://anderegg.s3.amazonaws.com/typefaces/inconsolata.png)
* [JetBrains Mono](https://anderegg.s3.amazonaws.com/typefaces/jetbrains-mono.png)
* [Menlo](https://anderegg.s3.amazonaws.com/typefaces/menlo.png)
