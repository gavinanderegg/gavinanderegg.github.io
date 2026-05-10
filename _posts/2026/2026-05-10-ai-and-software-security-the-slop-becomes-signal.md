---
title: >
    AI and software security: the slop is now signal
date: 2026-05-10 15:13:41 -0300
---

No matter how you feel about AI, it's changing the world of software. The "T" in ChatGPT was [invented to improve language translation](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need), and large language models (LLMs) are very good at this. Interestingly, translating between French and Japanese is effectively the same as translating between English and Python for these systems. As LLMs improve, we're also finding that there's little difference between "help me fix mistakes in this document", and "find the flaws in this codebase". LLMs are now great at both tasks, but the latter has much larger implications.

Last month, [Anthropic announced Claude Mythos](https://red.anthropic.com/2026/mythos-preview/), a next generation model which shows a significant leap in performance over currently available models. During testing, Anthropic noticed that the model was also much better at finding software flaws. The biggest improvements here come from identifying chains of issues which can be combined to produce a larger effect. Because of this, they decided not to release the model to the general public. Instead, they started [Project Glasswing](https://www.anthropic.com/glasswing), which invited key software vendors to find issues in their code first.

Some are calling this a marketing stunt. It's at least a bit of that. Anthropic's brand focuses on trust and safety, so holding back a model due to cybersecurity worries helps promote that ideal. However, [the model's system card](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf) shows real improvements across the board. More than that, we're already dealing with AI systems affecting security *today*.

[Daniel Stenberg](https://daniel.haxx.se/) is the original author and lead developer of [cURL (and the `libcurl` library)](https://en.wikipedia.org/wiki/CURL). cURL is a command-line tool for transferring things over the internet. It's [nearly 30 years old](https://curl.se/docs/history.html), and it's boring infrastructure in the best possible way. The `libcurl` library (which allows people to embed cURL's functionality into their apps) is used in [just about everything](https://curl.se/docs/companies.html).

Last year, Stenberg wrote about how AI submissions were making reviewing bug reports [much more difficult](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/). In that post, he links to [previous thoughts about AI](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/). He's not been a fan, and his reasoning was understandable — other people's use of AI was making his job worse. In January of this year, he [shut down cURL's bug bounty program](https://www.theregister.com/security/2026/01/21/curl-shutters-bug-bounty-program-to-stop-ai-slop/5063039) to try and stem the deluge of AI bug reports.

But then something changed. As the bug bounty was being wound down, people were realizing that Anthropic's [Opus 4.5 model](https://www.anthropic.com/news/claude-opus-4-5), released in November of 2025, was [a massive leap forward in terms of code generation](https://burkeholland.github.io/posts/opus-4-5-change-everything/). As more people started using this model, and similarly powerful ones from other AI vendors, the quality of the automated bug reports improved dramatically.

At the beginning of April, Stenberg noted that he was seeing less "AI slop", and was now dealing with a [tsunami of reasonable bug reports](https://mastodon.social/@bagder/116336957584445742). Just two weeks later, he shared [a thread of charts](https://mastodon.social/@bagder/116413131544356891) he was preparing for a presentation. More reports than ever, less slop, and a higher quality of reports overall.

It's not just cURL seeing this, either. Mozilla, makers of Firefox, have [written about the same change in bug reports](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) from slop to helpful over the last several months. So have [the Linux kernel team](https://lwn.net/Articles/1065620/). Some of those issues [have been around for nearly a decade](https://copy.fail/), and could potentially have already been exploited. In a startlingly short amount of time, AI generated bug reports have gone from being a nuisance to being legitimately helpful.

The issue is, even if these reports are helpful, they're coming in faster than ever. There will always be more people looking for flaws than people willing or able to fix them. Finding flaws can be profitable, either through bug bounty reports or [by sale to state-level actors](https://www.halcyon.ai/blog/russian-operation-zero-opzero-specializes-in-acquiring-zero-day-exploits). A troubling new pattern comes from the nature of open source: it happens in public. Security researchers can now have AI agents review all patches committed to a project. Those agents might find new issues, or even patches for high-impact vulnerabilities. In the former case, maybe they've found [a new bug to report](https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not). [^1] In the latter, maybe they have [a new attack vector](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures) to leverage before anyone patches it.

As frightening as this all sounds, some people are more optimistic. Mozilla recently [published some initial thoughts](https://blog.mozilla.org/en/firefox/ai-security-zero-day-vulnerabilities/) about their work using the Claude Mythos preview. The main upshot is: yes, there are more attackers than defenders, but software defects aren't infinite. If defenders can use systems like Mythos on their own codebases, they can potentially fix vulnerabilities before anyone has a chance to abuse them. Maybe future software could be defect-free.

Personally, I think this might be a bit too hopeful. A larger organization like Mozilla will have the resources to be ever-vigilant, but not everyone will. If you run a large open source project, [you can get Claude access for free](https://claude.com/contact-sales/claude-for-oss)… but the world is built on [a pile of tiny projects](https://xkcd.com/2347/). When those fall over, [very bad things can happen](https://en.wikipedia.org/wiki/Npm_left-pad_incident). Even if the Mozilla take is correct, I worry that things will get worse before they get better.

Whatever the future holds, I suspect that most people reading this won't be security researchers or maintainers of software packages. Here are some concrete steps the rest of us can take:

### Software is forever
An early lesson every developer learns is: software is never done. Even if you're not adding new features, there's always another security patch to apply or an API that's being changed out from under you. This was true in the days before LLMs, and it's even more true now.

I've been working with more clients who have been vibe-coding apps. When used as internal tools, these apps can be genuinely helpful. However, I worry when I see they have access to important data or are hosted next to critical systems. If you have a system connected to the internet (or some other untrusted environment), you *must* have a plan to maintain it for as long as it will exist. Someone has to ensure the system is secure and apply patches when they become available. This has always been a good idea, but now it's imperative.

### Update as soon as possible
If there's an update for your operating system or your phone, you should install it as soon as you can. Again, this has always been good advice, but it matters a lot more now.

### Really think before clicking things
Phishing attempts powered by AI are more able to appear legitimate. They're also easier to personalize. Recently Adobe's customer support platform was targeted in a [fairly novel phishing scheme](https://www.bleepingcomputer.com/news/security/google-new-unc6783-hackers-steal-corporate-zendesk-support-tickets/). I suspect we'll see more like this going forward.

<p style="color: #FFF6; text-align: center">...</p>

We're in an odd moment. It's possible we're at the start of something genuinely good, a time when security defenders can start outpacing attackers. It's also possible that things are just about to hit the fan in ways we'll all notice. Whatever the case, the software you depend on today will need someone watching it tomorrow. That part hasn't changed, and probably never will.

---

[^1]: [Here's the prompt](https://github.com/califio/publications/blob/main/MADBugs/iTerm2/prompts.md) used to identify this issue.