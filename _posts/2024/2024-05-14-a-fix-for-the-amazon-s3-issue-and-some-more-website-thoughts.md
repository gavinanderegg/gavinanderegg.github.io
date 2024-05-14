---
title: A Fix for the Amazon S3 Issue and Some More Website Thoughts
date: 2024-05-14 10:13:08 -0300
---

Yesterday I saw that there was [an update about the Amazon S3 issue](https://aws.amazon.com/about-aws/whats-new/2024/05/amazon-s3-no-charge-http-error-codes/) that had [scared me away from the service](https://anderegg.ca/2024/05/01/moving-away-from-s3). Great news! I don't mind paying for storage and legitimate access — especially when it's so very cheap. I was just skittish about being charged for unauthorized people trying to target my public S3 bucket. I had my bucket URL as a public URL in my site's markup that felt like a plausible attack vector.

I like using S3, so I'll move my site asset files back to it soon. I use [Transmit by Panic](https://panic.com/transmit/) to access it, which makes everything simple. [I set up droplets](https://help.panic.com/transmit/transmit5/servers/#creating-droplets) for the buckets I use frequently, so uploading new files is as easy as dragging to an icon on my desktop.

This is an aside, but as I was writing the post about my Jekyll and  GitHub Pages workflow yesterday I was also thinking about how I wanted to use this site going forward. I've been [ultra concerned about the size of the site across the wire](https://512kb.club/#:~:text=anderegg.ca), as I want it to be one of the quickest loading things on the web. To that end, I've really not used many images in posts. I want to change that, but it's going to require some reworking.

I've also decided to stay on Jekyll for now. I had been planning not to do any redesign work or even layout tweaks until I landed on a potential replacement… but that's silly. I likely won't switch until I need to, as Jekyll continues to work fine. I'm only really bothered by it when setting up a computer from scratch, or when [Homebrew breaks things](https://docs.brew.sh/FAQ#why-does-brew-upgrade-formula-or-brew-install-formula-also-upgrade-a-bunch-of-other-stuff). I'd likely have similar issues with another static site generator.

All this to say: stay tuned for some minor UI tweaks to this site!
