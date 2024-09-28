---
title: >
    The hidden WordPress license
date: 2024-09-28 11:24:49 -0300
---

I wrote about the [WordPress vs. WP Engine drama](https://anderegg.ca/2024/09/26/wordpress-vs-wp-engine) a couple of days ago, but it's still taking up space in my head. For better or worse, WordPress powers about half of the web. I care deeply about the web, and I think it's being harmed by this nonsense.

Part of the reason is uncertainty. It seemingly started because [Matt Mullenweg's mother thought WP Engine was an official WordPress product](https://wordpress.org/news/2024/09/wp-engine/#:~:text=My%20own%20mother%20was%20confused%20and%20thought%20WP%20Engine%20was%20an%20official%20thing.). I don't buy this, though. There are a few problems I have with trademark issues or brand confusion being the primary cause.

* As I discovered as I was digging into the previous piece, [Automattic invested in WP Engine](https://automattic.com/ventures/). The name hasn't changed since that investment, so it seemingly wasn't a problem then.
* The WordPress Foundation [updated their clause about the letters "WP"](https://wordpressfoundation.org/trademark-policy/#:~:text=For%20example%2C%20many%20people%20think%20WP%20Engine%20is%20%E2%80%9CWordPress%20Engine%E2%80%9D%20and%20officially%20associated%20with%20WordPress%2C%20which%20it%E2%80%99s%20not.) after the fracas started. Up until the day before [Automattic's trademark blog post was published](https://automattic.com/2024/09/25/open-source-trademarks-wp-engine/), the entire paragraph was: "*The abbreviation “WP” is not covered by the WordPress trademarks and you are free to use it in any way you see fit*". [You can see the previous version on the Internet Archive](https://web.archive.org/web/20240924024555/https://wordpressfoundation.org/trademark-policy/).
* There are many other WordPress companies using the letters "WP" in their name or URLs. Some examples are [EasyWP](https://easywp.com/), [WPBeginner](https://www.wpbeginner.com/), [WPExplorer](https://www.wpexplorer.com/), and [WP Tavern](https://wptavern.com/). Will these companies also confuse Matt's mom? If not, how are they different? EasyWP is a hosting company, for example. Will they now also be required to license the trademark? I really doubt it, and for their sake, I hope not.

The other side of Mullenweg's argument is that WP Engine isn't "giving back enough". This reasoning feels squishy to me, and it makes me uncomfortable. WP Engine supplies and maintains some key WordPress plugins and services like [Advanced Custom Fields](https://www.advancedcustomfields.com/), [WP Migrate](https://deliciousbrains.com/wp-migrate-db-pro/), and [Local](https://localwp.com). Advanced Custom Fields is installed on every WordPress site I've ever worked on [^1]. WP Migrate and Local are solid tools that make local development much easier. These are just examples, but I think they're assets to the WordPress community.

Let's say that Mullenweg is right, though, and WP Engine must do more for the WordPress community. OK, great: how much more? Should every company give a certain amount of time/money to WordPress or face Mullenweg's displeasure? Is Mullenweg the sole arbiter of the amount that needs to be given?

WordPress.org has a program called [Five for the Future](https://wordpress.org/five-for-the-future/), which encourages companies to give back to WordPress through employee time. In return, these companies are recognised and get a bit more of a say in the future of WordPress. I think this is a great idea, but it's not a requirement for using WordPress for commercial purposes. If WP Engine pledged to join this program, would things be mended with Automattic? At this point I doubt it.

This is the thought that kept rolling around my head since the situation started. The scorched earth policy by Mullenweg makes it clear that there's a hidden license that you agree to when you use WordPress commercially. For most, it will never come into effect, but if you're big like WP Engine [or Godaddy before them](https://masterwp.com/mullenweg-godaddy-is-an-existential-threat-to-wordpress/), it may be enacted.

I'm a huge fan of open source software, but when you provide software this way, you give up some control. Mullenweg seems to want it both ways. People should be able to use his software however they see fit, but he seems to also want them to "give back *or else*". This is his right, of course, but I'm not convinced anyone has a clear picture of what this means.

There's another way to do things. [Craft CMS](https://craftcms.com/) is my favourite content management system. It's [source-available](https://github.com/craftcms) and free for some uses, but there's a [reasonable license fee](https://craftcms.com/pricing) for larger commercial projects. This agreement is much clearer to me. Maybe Mullenweg needs to come up with some different licensing terms that he's happy with? Otherwise, we're left guessing about how much "giving back" is required. Until that happens, I recommend against using WordPress commercially unless you're sure Matt Mullenweg will never be upset with you.

---

[^1]: In my opinion, Advanced Custom Fields (or something like it) is required to transform WordPress from a blogging platform with optional pages into a proper content management system. There's a very long rant contained in that previous sentence, but I'll leave it alone for today.