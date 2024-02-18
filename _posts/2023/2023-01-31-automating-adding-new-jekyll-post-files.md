---
title: Automating the Addition of New Jekyll Post Files
date: 2023-01-31 18:35:16 -0400
---

I've [been a fan](https://github.com/gavinanderegg/Osxome/tree/master) of static site generation for a while. When I switch over to GitHub Pages [in 2012](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/389ed7adb8207c2c5d7bf3847ea5de7f70665975), I used Jekyll because it was the [default option](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll). It's still great! But there are some rough edges that bug me.

This might seem like a small thing, but I've often been annoyed whenever I've needed to [create a markdown file for a new post](https://jekyllrb.com/docs/posts/). Typing out `YEAR-MONTH-DAY-my-title-here.md` is a bit of a pain. I've never done it enough that I wanted to do much about it, though.

That changed recently. [I decided to write a simple script](https://github.com/gavinanderegg/gavinanderegg.github.io/blob/master/post) to create empty post files with a proper name and front matter. I'm not sure if anyone else will find this useful, but I figured it would be good to share just in case.

You can grab the script here: [https://github.com/gavinanderegg/gavinanderegg.github.io/blob/master/post](https://github.com/gavinanderegg/gavinanderegg.github.io/blob/master/post)

