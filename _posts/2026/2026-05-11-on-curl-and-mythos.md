---
title: >
    On curl and Mythos
date: 2026-05-11 11:33:54 -0300
---

Yesterday, I wrote about [the massive increase in security issues being identified by AI](https://anderegg.ca/2026/05/10/ai-and-software-security-the-slop-becomes-signal). Daniel Stenberg, the author of curl, was a key part of that story. At first he was being overwhelmed by a torrent of "AI slop" reports. In the last few months, the reports have become almost all legitimate, but the pace hasn't changed. Today, [Stenberg posted about his recent experience with Claude Mythos](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/).

In my piece yesterday, I said Mythos' positioning was at least a bit of a marketing move. The model is being withheld by Anthropic due to its increased potential for finding security flaws. In Stenberg's post today, he wrote about the model being run against curl's codebase only to find a single low-impact issue (after weeding out some false positives and a small bug).

I found this piece interesting, but there are a few points I wanted to pick at. The first is that the curl team wasn't granted access to Mythos directly. Instead, a scan was run by an unnamed party with access to the model, and a report was produced. Apparently the curl team was initially promised access, but that access never materialized. This seems wild to me, as curl is an extremely important project. It highlights my concern that access to these tools might be uneven.

The piece also mentioned that around 20 bugs were found by the Mythos report, just not security issues. So, while helpful, the report didn't quite live up to the "dangerous" marketing from Anthropic in this case. That said, Stenberg also notes that they've fixed a lot of security flaws recently. Even though those flaws were found with pre-Mythos models, it's possible that the low-hanging fruit is already dealt with. On top of that, LLMs aren't deterministic. Another crack at running this might find more issues… but the more likely case is that Mythos is only incrementally better at finding issues than the current generation of models.

I still think we're in for a bit of a ride over the next couple of years, but it's interesting to see the mild reaction to Mythos from the curl team.
