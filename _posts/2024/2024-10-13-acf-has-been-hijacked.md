---
title: >
    ACF has been hijacked
date: 2024-10-13 00:02:04 -0300
---

It's super late at night on Thanksgiving weekend in Canada. I shouldn't be thinking about weird internet drama, but here we are.

[Since I last wrote](https://anderegg.ca/2024/10/10/loyalty-test-checkbox) about the ongoing WordPress situation:

* Matt Mullenweg promoted a "fork" of WordPress that wasn't actually a fork.
* He then hijacked one of the most prominent plugins in the WordPress development world.

The first point is pretty minor, but highlights the depths of strangeness at play. [Vinny Green](https://x.com/vinnysgreen) created [a project called FreeWP](https://freewp.com/) that… actually, I don't actually know what it's about. You need to read the site for yourself. It seems to be an announcement of an organization that includes a news site, a class action lawsuit, and [some other things](https://freewp.com/faq/). It's not really clear to me, and it seems like it might be an elaborate troll.

This normally wouldn't be news, [except Matt Mullenweg made it so](https://wordpress.org/news/2024/10/spoon/). It's uncertain if Mullenweg even understood what Green was building, but Green was quick to point out that [it wasn't a fork of WordPress](https://x.com/vinnysgreen/status/1844488053060141233). Mullenweg then amended his post to include [AspirePress](https://aspirepress.org/about-us/), and noted a spelling error. The whole thing seems strange, but I'm assuming that Mullenweg wrote the blog post to make fun of potential WordPress forks.

The bigger issue happened on Saturday when [Automattic hijacked the Advanced Custom Fields (ACF) plugin](https://wordpress.org/news/2024/10/secure-custom-fields/). As I've written in the past, [ACF is a major plugin in the WordPress development world](https://anderegg.ca/2024/10/06/wordpress-vs-acf#:~:text=ACF%20is%20a%20WordPress%20plugin%20that%20is%20a%20requirement%20for%20many%20WordPress%20builds), and a requirement for many custom websites. It's also owned by WP Engine, the company Mullenweg is beefing with. In the previous link, I had guessed that Mullenweg intended to kick them out of the WordPress plugin directory. Turns out, they went one further.

In a post titled "[Secure Custom Fields](https://wordpress.org/news/2024/10/secure-custom-fields/)", and in the category "Security", Mullenweg posted that he was invoking "[point 18](https://github.com/wordpress/wporg-plugin-guidelines/blob/trunk/guideline-18.md)" of the plugin directory guidelines to hijack the ACF plugin. ACF is offered under the GPLv2 license. It's fair use within that license for Automattic to fork it and do whatever it wants with the source code.

But that's not the point. ACF is something that WordPress users trust and expect to come from a specific source. That Automattic would unilaterally decide to hijack such a popular plugin is completely insane. I'm not sure how this differs from a supply-chain attack. As I've written, the reason for this is invented and [brought on by Automattic's blocking of WP Engine employees from WordPress.org](https://anderegg.ca/2024/10/06/wordpress-vs-acf#:~:text=The%20issue%20here%20is%20that%20the%20ACF%20team%20has%20been%20blocked%20by%20Mullenweg%20from%20accessing%20WordPress.org%20and%20the%20infrastructure%20it%20provides.). Automattic just happened to find a mild vulnerability in ACF, and is now using **the block Automattic imposed** as a reason to take control of the plugin because the ACF team can't update the plugin while the block is in place.

This is some Grade-A 100% bullshit.

The ACF site has been [updated with a notice about the takeover](https://www.advancedcustomfields.com), but most users likely won't see this. The team behind the WordPress plugin directory could now update ACF to make any changes they'd like. If they're willing to do this, I wouldn't trust any plugins hosted on WordPress.org.

I really don't know what to say at this point. I assumed that ACF would be removed from the WordPress plugin directory, but I never would have guessed it would be hijacked. It seems like Mullenweg has lost the plot completely.

If you use WordPress for a living, I recommend strongly that you consider changing platforms.