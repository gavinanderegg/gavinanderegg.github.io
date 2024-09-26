---
title: >
    WordPress vs. WP Engine
date: 2024-09-26 17:42:20 -0300
---

The WordPress world received a massive dose of drama over the last week. Before I get to my thoughts, here's a rough timeline of recent events.

---

**September 20:** On the last day of [WordCamp US](https://us.wordcamp.org/2024/), Matt Mullenweg was scheduled for [an in-person Q&A session](https://us.wordcamp.org/2024/session/an-in-person-qa-with-matt-mullenweg/). You can [check it out on YouTube](https://www.youtube.com/live/fnI-QcVSwMU). He starts by reading [a blog post from September 17](https://ma.tt/2024/09/ecosystem-thinking/) to the crowd. He then gives his perspective on a private equity firm called [Silver Lake](https://www.silverlake.com) and a specific managing director named [Lee Wittlinger](https://www.silverlake.com/people/lee-wittlinger/).

**September 21:** Mullenweg [posted this article](https://wordpress.org/news/2024/09/wp-engine/) which reiterates a few points from the Q&A session, but also specifically calls WP Engine "a cancer to WordPress". It calls WP Engine out for not having post revisions on by default.

**September 23:** [WP Engine announces on X](https://x.com/wpengine/status/1838350670564377051) that it has sent a [cease and desist letter](https://wpengine.com/wp-content/uploads/2024/09/Cease-and-Desist-Letter-to-Automattic-and-Request-to-Preserve-Documents-Sent.pdf) to Automattic (Mullenweg's company). The letter includes screenshots of text messages allegedly sent by Mullenweg. The texts include demands for payment, and were being sent up until the moment before Mullenweg started his Q&A session.

**Between September 24 – 25:** The [WordPress Foundation's trademark policy page](https://wordpressfoundation.org/trademark-policy/) was updated to include language that make the use of the letters "WP" less clear. [Previously the page said](https://web.archive.org/web/20240924024555/https://wordpressfoundation.org/trademark-policy/): "*The abbreviation “WP” is not covered by the WordPress trademarks and you are free to use it in any way you see fit.*"

**September 25:** Automattic responded with [a blog post](https://automattic.com/2024/09/25/open-source-trademarks-wp-engine/), a [cease and desist letter](https://automattic.com/2024/wp-engine-cease-and-desist.pdf), and [supporting exhibits](https://automattic.com/2024/wp-engine-cease-and-desist-exhibits.pdf). The blog post and letter accuse WP Engine of infringing on WordPress and WooCommerce trademarks, and the exhibit document provides example screenshots.

Later the same day, WP Engine customers reported issues accessing the WordPress.org infrastructure. This means that WP Engine users currently can't get security updates for WordPress or plugins. Mullenweg then [posted an article](https://wordpress.org/news/2024/09/wp-engine-banned/) confirming that WP Engine was banned from accessing WordPress provided services.

---

What a mess. Maybe there's something we're not seeing from the outside, but to me this looks like Mullenweg has gone off the deep end. Is this a personal beef with Silver Lake? With Lee Wittlinger? If not, every commercial enterprise has the word "WordPress" in their marketing copy needs to watch out.

I've used WP Engine happily for several projects and found it to be a fine host. Yes, [they disable the revisions system by default](https://wpengine.com/support/platform-settings/#Post_Revisions). But this isn't some "hack" — [WordPress provides a built-in way to configure or disable this system](https://wordpress.org/documentation/article/revisions/#revision-options).

Also, as I was digging into this, I learned that Automattic invested in WP Engine. In fact, it was [the first investment made by Automattic's A8c Ventures](https://automattic.com/ventures/) in 2011. They didn't seem concerned trademark issues at that point. I'm curious what changed?

One thing is the trademark policy page I mentioned above. They previously noted that "WP" was fine, and anyone could use it. [As Kev Quirk points out](https://kevquirk.com/blog/my-thoughts-on-the-wordpress-drama), there are a number of companies with "WP" as part of their name. Are they now in danger? I really doubt they've all made licensing agreements with Automattic. Some of the screenshots used in [Automattic's cease and desist letter](https://automattic.com/2024/wp-engine-cease-and-desist-exhibits.pdf) look pretty similar to many other WordPress hosts I've seen across the web.

Also, why is Automattic, a for-profit company, requiring money from WP Engine for the use of the WordPress trademark? WordPress.com is Automattic's moneymaker. It's set apart from the open source WordPress project, and a direct competitor to WP Engine. The WordPress trademark is controlled by the WordPress Foundation. I'm not a lawyer, but this seems rather problematic to me. As far as I can tell, these concerns should be separated.

There are a lot of details missing, but this looks like a grudge gone public. At the moment, this seems to be mostly harming WP Engine customers who are now less safe. If WP Engine's side of the story is true, then Mullenweg is acting like a mafia boss. One thing's for sure: I definitely wouldn't want to be in the WordPress hosting game at the moment.