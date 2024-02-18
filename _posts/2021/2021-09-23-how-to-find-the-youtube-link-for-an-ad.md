---
title: How to find the YouTube link for an ad
---

This morning I was catching up on Twitter when a friend's tweet caught my eye:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Just saw a lovely Kathleen Edwards ad for Ottawa in the middle of a totally unrelated YouTube video - I wish they let me share good ads, but it seems there&#39;s no easy way to do so. Feels like a missed opportunity</p>&mdash; Andrew Burke (@ajlburke) <a href="https://twitter.com/ajlburke/status/1440864506498879488?ref_src=twsrc%5Etfw">September 23, 2021</a></blockquote>

Ads on YouTube are just videos, but are usually unlisted. Either way, it can be a real pain to find them. I had previously figured this out by digging into the debugging info (which I've had to use in the past for other reasons), but this isn't straightforward. I figured I should write down the steps.

To find the video link for a YouTube ad:

* While the ad is playing, right click on the video and choose **"Copy debug info"** from the context menu.
Paste the content into a text editor and search for the string `addocid` (Ad Doc ID).
* This is the YouTube document string that you can use to watch the ad. For example, while writing this, I saw an ad for Export Development Canada, with an addocid of `WWsE1gnJWhw`.
* You can view the ad by appending that string to the end of a YouTube URL like this: `https://www.youtube.com/watch?v=`

So the link to the ad based on the above steps would be:

[`https://www.youtube.com/watch?v=WWsE1gnJWhw`](https://www.youtube.com/watch?v=WWsE1gnJWhw)

I've used this in the past to share ads I thought were funny or interesting. I've also used this to learn more about the organization/entity that paid for the ad. In some cases, I've up/downvoted the ad, which is only sometimes possible when the ad is displayed over another video.

---

[Discuss on Hacker News](https://news.ycombinator.com/item?id=28628932)