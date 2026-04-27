---
title: >
    Uptime golf
date: 2026-04-27 17:56:58 -0300
---

I've been noticing a lot of service outages lately. Some with [few enough nines](https://en.wikipedia.org/wiki/High_availability#%22Nines%22) that you'd think they were [going for a low score](https://en.wikipedia.org/wiki/Code_golf). My guess: this is probably going to get worse before it gets better, but maybe not for the reasons you'd think.

First off, let's look at GitHub. It launched in 2008 and was acquired by Microsoft in late 2018. For most of its life, it was boring infrastructure in the best possible way. More recently [it's been up and down like a yo-yo](https://damrnelson.github.io/github-historical-uptime/). The official status page currently lists most services at [two nines of uptime](https://www.githubstatus.com/) over the last 90 days… but counting slightly differently [makes it look even worse](https://mrshu.github.io/github-statuses/).

Some people have blamed AI for this. Not because everyone at GitHub is vibe coding now (though, that might not be helping things). Instead because [Microsoft is prioritizing AI projects over everything else](https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/), including at GitHub. GitHub also [has had a substantial influx of users](https://www.theinformation.com/newsletters/applied-ai/microsofts-github-sees-booming-traffic-outages-ai-agents-flood-platform) as more people are building software with AI and using AI agents. On top of all that, Microsoft recently started a [re-platforming effort to move GitHub services to Azure](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/). This is taking resources away from efforts that could help increase stability. [^1]

The companies providing AI services aren't doing much better. Anthropic's Claude has been [between one and two nines of uptime over the past three months](https://status.claude.com/uptime). OpenAI's ChatGPT has [done a bit better at around two nines](https://status.openai.com). There might be more of a reason to blame these outages on vibe coding, but I think the simpler answer is that it's tough to scale. These services are being used by more people every day, and the systems in play are novel.

The other service I've seen having issues a lot recently is Bluesky. Over the past month or so, the service has been pretty rough to use. A lot of folks in my feed are blaming these outages on vibe coding. But again, there have been better explanations. One outage was based on [a bit of an oopsie](https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2), but I've definitely seen worse before LLMs existed. The other was caused by [an extended attack on the platform](https://techcrunch.com/2026/04/17/its-not-just-you-bluesky-is-sorta-down/).

I'm writing about this because I keep seeing people blaming outages on "vibe coding". Here's the thing: I think people who uncritically use LLMs to generate code are racking up a lot of technical debt. But I also think that using "vibe coding" as a bogeyman isn't helping anyone. There are much simpler explanations for all of these things. Some of them can even already reasonably be blamed on AI!

More than that, I think there are likely more outages coming. Like it or not, LLMs are pretty great at generating code. They're also good at finding issues with systems. cURL author, Daniel Stenberg, [ended the project's bug bounty program](https://etn.se/index.php/nyheter/72808-curl-removes-bug-bounties.html) earlier this year after getting massive amounts of awful AI-generated vulnerability reports. He then [started getting a flood of legit issues](https://mastodon.social/@bagder/116336957584445742), [followed by more](https://mastodon.social/@bagder/116413131544356891), and [is anticipating even more](https://mastodon.social/@bagder/116475924516173079). Bad actors have the same access to these tools as well-meaning security folks.

Some people said [Claude's Mythos](https://red.anthropic.com/2026/mythos-preview/) was [simply hype](https://www.theregister.com/2026/04/22/anthropic_mythos_hype_nothingburger/), and I get it. Obviously major issues can be found with current models. But I don't think this bodes well for anyone. Even if LLM pricing starts [reflecting its actual cost](https://anderegg.ca/2026/04/22/llm-pricing-has-never-made-sense) soon, I worry that there might be more downtime to come.

---

[^1]: Also, as I'm writing this, [GitHub is currently experiencing another incident](https://news.ycombinator.com/item?id=47924775).