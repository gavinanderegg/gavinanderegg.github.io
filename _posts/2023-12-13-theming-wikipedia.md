---
title: Theming Wikipedia
date: 2023-12-13 19:49:17 -0400
---

Earlier this year, [Wikipedia got a nice redesign](https://wikimediafoundation.org/news/2023/01/18/wikipedia-gets-a-fresh-new-look-first-desktop-update-in-a-decade-puts-usability-at-the-forefront/). When it happened, I didn't notice. I've been using a non-default theme for nearly 20 years.

A while back I mentioned this to some friends who were surprised to learn this was a thing. It makes sense that it isn't well known: changing or customizing themes (called "skins" by MediaWiki) requires creating a Wikipedia user account. Since the site is perfectly usable without logging in, I'd bet only a tiny percentage of users have accounts. [Theming looks to have been introduced with the "Cologne Blue" skin in 2002](https://en.wikipedia.org/wiki/Wikipedia:Skin#:~:text=Cologne%20Blue%20was%20created%20in%202002), so it's been around for a while! [^1].

The [Wikipedia:Skin page](https://en.wikipedia.org/wiki/Wikipedia:Skin#) contains the following screenshots of each currently supported skin:

* [Vector 2022](https://upload.wikimedia.org/wikipedia/commons/7/71/English_Wikipedia_Vector_2022_full_screenshot.png) (the current default skin)
* [Vector 2010](https://upload.wikimedia.org/wikipedia/commons/e/e9/Vector.css.png)
* [MonoBook](https://upload.wikimedia.org/wikipedia/commons/e/ed/Monobook.css.png)
* [Timeless](https://upload.wikimedia.org/wikipedia/commons/b/b7/English_Wikipedia_Timeless_full_screenshot.png)
* [Minerva Neue](https://upload.wikimedia.org/wikipedia/commons/1/1d/English_Wikipedia_Minerva_Neue_screenshot.png)

The same page also has screenshots of two deprecated skins:

* [Modern](https://upload.wikimedia.org/wikipedia/commons/5/50/Modern.css.png)
* [Cologne Blue](https://upload.wikimedia.org/wikipedia/commons/1/11/Cologneblue.css.png)

I'm currently using a theme based on Timeless. I had been using the base Timeless skin for effectively since signing up, but decided to [tweak it a bit in 2021](https://meta.wikimedia.org/w/index.php?title=User:GavinAnderegg/global.css&action=history). I increased the size of the type, increased the spacing between lines, and set the default typeface to [Palatino](https://en.wikipedia.org/wiki/Palatino). Here's a link to [the 2021 version of my `global.css` file](https://meta.wikimedia.org/w/index.php?title=User:GavinAnderegg/global.css&oldid=22369729).

Earlier this year, after I learned of the Wikipedia redesign, I checked back in on my overrides. I realized that it would likely be better to have the CSS associated directly with the theme, so [I moved things from `global.css` to `timeless.css`](https://en.wikipedia.org/w/index.php?title=User:GavinAnderegg/timeless.css&action=history). Here's a link to [the current version of my `timeless.css` override](https://en.wikipedia.org/w/index.php?title=User:GavinAnderegg/timeless.css).

[The Wikipedia:Skin page has instructions for how to customize a skin](https://en.wikipedia.org/wiki/Wikipedia:Skin#Customisation), if you want to try this for yourself. You can also add or override JavaScript behaviour globally or for a specific skin, though I haven't done this.

For the curious, [this is what my theme looks like in Safari](https://anderegg.s3.amazonaws.com/wikipedia-theme.png). As well as the changes above, I also shrunk the size of the main content column, and removed the band of colour just below the sticky header.

---

[^1]: It was definitely around in 2005 when I created my account to [remove an errant smiley from the World of Warcraft page](https://en.wikipedia.org/w/index.php?title=World_of_Warcraft&diff=prev&oldid=18905041).




