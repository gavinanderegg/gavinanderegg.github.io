---
title: Moving Away From S3 (for a Bit)
date: 2024-05-01 14:46:33 -0300
---

Yesterday, before getting [the TikTok article](https://anderegg.ca/2024/04/30/trying-to-understand-the-tiktok-ban) finished, I made a quick change to this site. I had seen a post from Maciej Pocwierz, "[How an empty S3 bucket can make your AWS bill explode](https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1)". It scared me because I had previously been serving images directly from S3. I don't think it's particularly likely that I would be affected by this, but it's a really worrying attack vector for anyone with a publicly viewable S3 bucket name.

I decided to move my assets directly into Git, so they're now hosted on GitHub. Having these sorts of assets directly in the repository doesn't feel great, but I think it's OK until I come up with a better solution. I don't use many images on this site, so it's only about 7 megabytes of content.

Happily, I saw [a post from Simon Wilson](https://simonwillison.net/2024/Apr/30/how-an-empty-s3-bucket-can-make-your-aws-bill-explode/) this morning which had an update linking to [a tweet from Jeff Barr](https://twitter.com/jeffbarr/status/1785386554372042890), the Chief Evangelist at AWS. It sounds like this is being looked into and there will hopefully be a solution soon.
