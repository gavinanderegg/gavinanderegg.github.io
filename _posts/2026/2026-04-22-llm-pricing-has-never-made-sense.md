---
title: >
    LLM pricing has never made sense
date: 2026-04-22 20:50:22 -0300
---

Yesterday, Claude Code disappeared from the $20/month subscription tier on Anthropic's website. Well, for some people. Then it came back. [As Simon Willison put it, it's all very confusing](https://simonwillison.net/2026/Apr/22/claude-code-confusion/).

Anthropic's Head of Growth, Amol Avasare, said [this was caused by a "test" gone slightly wrong](https://x.com/TheAmolAvasare/status/2046788872517066971). Apparently only 2% of users were supposed to see the new pricing page. But this suggests Anthropic is considering raising rates substantially for code generation product.

A day earlier, GitHub announced that its Copilot code generation product would be "[pausing new sign-ups, tightening usage limits, and adjusting model availability](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/)". Effectively, the product is going to get substantially worse for current users, and even worse for new users when they can sign up again.

Almost a year ago, [Sam Altman said there was an AI bubble](https://www.theverge.com/ai-artificial-intelligence/759965/sam-altman-openai-ai-bubble-interview). He also said that [OpenAI is losing money on its $200/month Pro subscriptions](https://fortune.com/2025/01/07/sam-altman-openai-chatgpt-pro-subscription-losing-money-tech/).

None of this should be surprising. OpenAI in particular [has raised over $290 billion dollars of investment](https://www.owler.com/company/openai/funding), and has not yet turned a profit. [It hopes to become profitable by 2030](https://www.wsj.com/tech/ai/big-techs-soaring-profits-have-an-ugly-underside-openais-losses-fe7e3184), but it's not clear how that will happen. Maybe ads? Anthropic made fun of this idea [during the last Super Bowl](https://www.adweek.com/brand-marketing/anthropic-makes-super-bowl-debut-promising-ad-free-ai/).

All of these companies have been raising vast sums from venture capitalists for years. Now it's starting to become clear that people would like to see some returns soon, please. Maybe it's just me, but I'm not sure how that'll happen. Perhaps they'll raise rates to sustainable levels, but I think that would price most users out of the market.

But there's another challenge: local LLMs. [It's already possible to run LLMs on local hardware](https://realpython.com/ollama/), and that's only going to get easier in the future. Apple's M-series chips are [extremely good at doing this today](https://openclawai.io/blog/openclaw-mac-mini-always-on-setup/). Open weight (read: free) models are [widely available](https://onyx.app/self-hosted-llm-leaderboard) and good enough that [most people probably couldn't tell the difference](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/). They also have the benefits of running on hardware that's sipping power most of the time, rather than slurping it down in massive data centres. [^1]

[As I've written before](https://anderegg.ca/2025/01/07/apple-and-the-ai-divide), I think LLMs can be very useful tools. I honestly think most "AI haters" [would agree with me on that front](https://bsky.app/profile/techconnectify.bsky.social/post/3mju324esy22f). The issue for many people isn't the technology itself (though there are many ethical issues in how it was trained). The issue is the stupid state of our capitalist system, and the weird way companies are trying to force it down everyone's throats.

I don't know what the future holds for the big AI companies, but I think there will be a profitability reckoning soon. The products will need to get worse, more expensive, or both if VCs are to get their money back. But even then, I'm not sure the math adds up. Will everyone keep paying more? Will people unsubscribe if chat sessions start including crappy ads? Will more people start running LLMs on commodity hardware? Whatever happens next, it doesn't seem ideal that so much investment money is tied to an [underpants gnome scheme](https://www.youtube.com/watch?v=WpnM37A4P_8).

---

[^1]: [To be clear](https://news.ycombinator.com/item?id=47876232), the reason I say here that local LLMs would be "sipping power most of the time" is that they'll only be in use some of the time. A data centre needs to run at full power all the time to be as cost-effective as possible. I can do inference work on my Mac Studio today, but I don't have a workload that requires me to do so most of the time. I don't think it's crazy to believe that people will also be running local inference on their *phones* in the next 5 years. If local LLM usage takes off, it will mean less need for large data centres. If that's true, overbuilding data centres is more revenue pressure for AI companies.