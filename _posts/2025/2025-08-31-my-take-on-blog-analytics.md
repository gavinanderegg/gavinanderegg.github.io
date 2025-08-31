---
title: >
    My take on blog analytics
date: 2025-08-31 17:23:03 -0300
---

I recently read [*You do not need “analytics” for your blog because you are neither a military surveillance unit nor a commodity trading company*](https://www.thisdaysportion.com/posts/contra-analytics/) by Leon Paternoster. It's a well-argued piece, and I agree with the general thrust… but I also won't be removing analytics from my site anytime soon.

I deal with a lot of data for clients. One of my first pieces of advice in these projects is: don't collect more than you need. Often, this advice needs reiterating during a project. It's hard advice to follow! Having a wide swath of data can be potentially helpful in the future. If you haven't properly developed a plan for what you want to measure, there's a chance you can fix this in the future by having over-collected in the past.

The problem is, the entity collecting the data is responsible when that data leaks. If the data being collected wasn't core to a business objective, then [you're going to look like a buffoon](https://www.halifaxexaminer.ca/economy/utilities/nova-scotia-power-still-silent-on-why-it-stored-customers-social-insurance-numbers/). Also, even if each data point isn't sensitive by itself, [it's possible for those points to become sensitive in the aggregate](https://www.pnas.org/doi/full/10.1073/pnas.2300976120).

All of this to say: I agree in principle with Paternoster here. If you're writing a blog, there's a good chance that it's something you're doing for yourself as a hobby. You probably *don't* need analytics, especially if you're just adding them because "*it's the done thing*".

So why do *I* include analytics on this site? For two main reasons. I'm very motivated by having numbers go up. I'm also curious, and want to know when/why one of my posts gets traction.

Paternoster argues that, ultimately, it doesn't matter how much traffic a post gets. If you were going to benefit from a post's popularity, this would manifest itself in some other way than some chart in a dashboard. I think this is an enlightened view, but it's one I might be slightly too shallow to live by. Seeing those numbers go up gives me a positive jolt, and it makes me want to write more. For me, that's reason enough to track stats.

Another point from Paternoster is that you're surveilling people if you capture their information without their consent. I have some sympathy for this view, but it feels slightly naïve. I've been building on the web since the mid-90s. In all of that time, there have been server logs. I remember using [Analog](https://en.wikipedia.org/wiki/Analog_%28program%29) on early websites to view web log data. Just because it's always been done doesn't mean there's a good reason to keep doing it, but web logs have their place. They help identify malicious behaviour and are useful for identifying server issues. This is how the web works, and the information collected in these logs doesn't seem excessive to me.

That said, when people think "web stats" these days, the default is Google Analytics (GA). GA can (and usually is!) set up to collect far more data than a web log does. I reflexively had Google Analytics on this site for a long time, but [removed it in 2021](https://github.com/gavinanderegg/gavinanderegg.github.io/commit/d334ad8fc494c44a90fc94f845b831f2b2474b52). At the time, I wasn't writing much, but noticed that GA was more than doubling the size of every page load. [^1]

The other part of this is the whole "[if you're not paying for it, you're the product](https://www.metafilter.com/95152/Userdriven-discontent#3256046)" bit. GA is a top-tier analytics system offered for free by one of the world's largest companies. You'd have to be an idiot to think they're not getting something out of this deal. I don't think it's some super-shady conspiracy or anything, but I do think there's a huge amount of data over-collection happening. I agree with Paternoster that not every site needs to be a part of this network.

Anyway, after GA, I operated without a stats package for a while — but also wasn't really writing much. Later, I decided to focus on writing on this site more. As mentioned, having stats helped me stick to it. [I started with Plausible Analytics](https://anderegg.ca/2023/01/22/blogging-analytics-and-gdpr) because it was less intrusive and the total payload was [much smaller than GA](https://plausible.io/lightweight-web-analytics). It was also overkill for my needs, and I bumped up against the limits of the entry-level tier pretty quickly.

Before it came time to renew, I learned about [Tinylytics](https://tinylytics.app/). This seemed much more my speed. It cost less, tracked less, and was even smaller in terms of transfer size. [I'm still using it today](https://anderegg.ca/2023/12/14/switching-from-plausible-to-tinylytics). This is my middle ground between an enlightened, stats-free life and data over-collection. I recommend the service if these trade-offs sound about right for you as well.

---

[^1]:  At the time, the GA script added more than 130kB to every page load. The average size of any page load on this site was around 70kB. Those sizes are about the same today.