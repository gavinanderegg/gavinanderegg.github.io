---
title: >
    WordPress vs. ACF
date: 2024-10-06 12:27:57 -0300
---

The WordPress drama has not dried up. [Since I wrote last](https://anderegg.ca/2024/09/28/the-hidden-wordpress-license),  Matt Mullenweg has done a number of interviews, WP Engine sued Automattic, the structure of the WordPress organization has become clearer, and over 150 employees left Automattic in a buy-out deal. Now it seems Mullenweg is going after a popular plugin to try and win his battle against WP Engine.

[Ernie Smith wrote an excellent overview of recent events](https://tedium.co/2024/10/03/wordpress-wp-engine-lawsuit-open-source-impact/) that gets us up to October 3rd. It linked to a video where [Theo Browne reviewed WP Engine's lawsuit against Automattic](https://www.youtube.com/watch?v=edCrrWj6WK4). The filing looks damning from the outside, and includes allegations of Mullenweg acting in a very sketchy way toward the CEO — giving out her personal phone number during an interview on X, and threatening to expose her "past interviews" if she didn't accept a job offer. It also confirms that Automattic's trademark terms required 8% of WP Engine's monthly revenue, which seems insane to me. A story about the lawsuit made it to Hacker News, where Mullenweg (photomatt) [posted comments late into the night](https://news.ycombinator.com/item?id=41726197).

Later, [Mullenweg posted about the status of an "alignment deal"](https://ma.tt/2024/10/alignment/) for employees who were unhappy with the current drama. The deal was quite generous, but required people to resign on short notice. Those who resigned also wouldn't be able to re-join. 159 employees, about 8.4% of the company, took him up on the offer.

The next day, [The Verge's Emma Roth had an interview with Mullenweg](https://www.theverge.com/2024/10/4/24262232/matt-mullenweg-wordpress-org-wp-engine). In it Mullenweg confirmed that WordPress.org was his personal website, and wasn't part of the WordPress Foundation. Mullenweg is quoted saying, "I happily provide WordPress.org services to literally every other host". He's also mentioned previously that he only has beef with WP Engine, and that no one else should worry. But he's previously gone after [GoDaddy](https://wptavern.com/godaddy-responds-to-mullenwegs-accusations-we-all-have-the-same-goal) and [Bluehost](https://wptavern.com/bluehost-misuses-wordpress-trademark-reigniting-controversy-over-recommended-hosts-page), so I'm not convinced others won't be targeted in the future.

That brings us roughly to the present as I write, and a new wrinkle in the story. It seem like Mullenweg is now targeting Advanced Custom Fields (ACF).

I wrote a bit about this [last time](https://anderegg.ca/2024/09/28/the-hidden-wordpress-license), but ACF is a WordPress plugin that is a requirement for many WordPress builds. It allows developers to easily create new data entry fields in the WordPress admin and then use the data in those fields in many different ways. If you've entered content in a custom WordPress site's admin, chances are very good that you've interacted with ACF.

At the end of September there was a Reddit post where [Mullenweg mused about bringing ACF into WordPress](https://www.reddit.com/r/Wordpress/comments/1frcor8/matt_brings_up_bringing_acf_pro_into_core/). It looks to be a screenshot of a Slack conversation, but it's hard to tell if this is legitimate.

Yesterday there was a post on X where the Automattic account "responsibly disclosed" a vulnerability in ACF. The X post has since been deleted, but [here's a Mastodon thread that brought it to my attention](https://sakurajima.moe/@chikorita157/113256114788720233). The thread also includes a screenshot of the [WordPress account posting](https://x.com/WordPress/status/1842523807451316604) "You wouldn't have to do all this if you dropped your lawsuits, apologized, and didn't abuse trademarks." It's an uncharacteristic post from that account, and some (including myself) guess it was posted by Mullenweg.

Mullenweg also [posted to X yesterday](https://x.com/photomatt/status/1842500184825090060) asking:

> What are the best alternatives to Advanced Custom Fields for people who want to switch away? Is there an easy way to migrate?
>
> I suspect there are going to be millions of sites moving away from it in the coming weeks.

The issue here is that [the ACF team has been blocked](https://x.com/wp_acf/status/1841843084700598355) by Mullenweg from accessing WordPress.org and the infrastructure it provides. This includes the SVN repositories (yes, in 2024 [WordPress still uses SVN](https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/)) that allow the ACF team to update their plugin. This puts the many WordPress sites using the plugin at risk if there is a serious vulnerability.

This is all a bit unclear at the moment, as some pieces of the story are second-hand. But it seems to me that Mullenweg wanted to find some issue with ACF, disclose the issue, and give a 30-day timeline for the issue to be fixed before the plugin is removed from WordPress.org plugin repository. All while the ACF team, which is part of WP Engine, has been banned from using WordPress.org services.

It should be noted here that the WordPress.org plugin repository is effectively the "app store" of the WordPress world. Most people install plugins via WordPress admin, and this functionality is powered by WordPress.org infrastructure. These same servers also power the WordPress plugin update mechanism. As Mullenweg said in the interview with The Verge, WordPress.org belongs to him, not the WordPress community.

The previous banning of WP Engine from accessing WordPress.org only affected WP Engine customers. This new twist, if true, will affect many WordPress users that aren't associated with WP Engine. From the outside, this seems like where Mullenweg is headed, and [those thinking along the same lines aren't happy about it](https://www.reddit.com/r/Wordpress/comments/1fwviwk/stage_appears_to_be_set_for_the_removal_of_acf/).

What a shitshow.