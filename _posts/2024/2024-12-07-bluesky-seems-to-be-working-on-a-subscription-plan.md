---
title: >
    Bluesky seems to be working on a subscription plan
date: 2024-12-07 17:33:02 -0400
---

Yesterday, user [@saeri.xyz](https://bsky.app/profile/saeri.xyz) on Bluesky [posted some screenshots](https://bsky.app/profile/saeri.xyz/post/3lcnlqu5lu22v) of a potential upcoming Bluesky subscription plan.

The thread also included a link to a pull request titled "[[Subs] Draft](https://github.com/bluesky-social/social-app/pull/6977)". Digging into the repository for the [social-app project](https://github.com/bluesky-social/social-app) on GitHub, I also found a branch named "[subs/base](https://github.com/bluesky-social/social-app/tree/subs/base)". In it, I found a [SubscriptionsDialog.tsx](https://github.com/bluesky-social/social-app/blob/subs/base/src/components/dialogs/SubscriptionsDialog.tsx) file that contained the following text:

> Here's the thing: we don't have any premium features yet because all our servers are on fire. Support us now so we can put the fires out and get working on those features!
>
> What you'll get now:
>
> * A supporter badge on your profile
> * A warm fuzzy feeling knowing you helped us out
>
>  What you'll get soon:
>
> * Custom profile colors
> * Longer and higher quality videos
> * Custom app icons

The file also [lists some pricing details](https://github.com/bluesky-social/social-app/blob/subs/base/src/components/dialogs/SubscriptionsDialog.tsx#L97C1-L154C73). It seems to start at $6/month for the monthly plan, going up to $8/month after 12 months. There is also an annual plan starting at $60/year, renewing at $80/year.

This is a work in progress, so it's safest to assume these details may change. That said, something like this subscription is likely the best way for Bluesky to generate revenue. The Verge [recently launched their subscription plan](https://www.theverge.com/2024/12/3/24306571/verge-subscription-launch-fewer-ads-unlimited-access-full-text-rss), and on the [latest episode of The Vergecast](https://www.theverge.com/2024/12/6/24314746/agi-openai-sam-altman-cable-subscription-vergecast) the hosts say that they were very happy with the uptake. [^1] I suspect many Bluesky users would be happy to help ensure the service sticks around.

I find it interesting that this is coming to light because the official Bluesky client is open source. The closest analogue to this sort of thing is Mastodon, which also has [open source apps](https://github.com/mastodon). However, Mastodon is [primarily funded through donations](https://joinmastodon.org/sponsors).

---

[^1]: I signed up and was [happy to do so](https://bsky.app/profile/gavin.anderegg.ca/post/3lcgvwcwwj22j). I've been reading The Verge since the beginning, and I think they do the best tech reporting in the business.