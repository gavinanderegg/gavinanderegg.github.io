---
title: >
    Recall: What the Heck, Microsoft?
date: 2024-06-04 08:49:03 -0300
---

When Microsoft [first announced their new Recall feature](https://www.theverge.com/2024/5/20/24159258/microsoft-recall-ai-explorer-windows-11-surface-event), I was intrigued. I had heard about a similar project, [Rewind](https://www.rewind.ai), discussed on [ATP back in 2022](https://atp.fm/507) and it sounded like it would be genuinely useful.

Microsoft including Rewind as an OS-level feature means that it has full access to everything. Recall can have deeper functionality than a 3rd-party app like Rewind, which could provide a richer experience. But it also has access *everything*, which is troubling for privacy-minded individuals and [CIOs](https://en.wikipedia.org/wiki/Chief_information_officer). I'm not someone who would install Rewind, but I would give a system-level feature like Recall a shot. Providing it was private and secure, of course.

Recall is touted as being private, and I believe this. The feature is currently only available on new [Copilot+ PCs](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/), and analysis is done on-device, without help from a cloud provider. Great! But it turns out that it stores all the data from this analysis in an [SQLite database in the user's home folder](https://doublepulsar.com/recall-stealing-everything-youve-ever-typed-or-viewed-on-your-own-windows-pc-is-now-possible-da3e12e9465e). The folder is protected by [UAC](https://en.wikipedia.org/wiki/User_Account_Control), but this can be [bypassed by unprivileged malware](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/disable-user-account-control#:~:text=More%20important%2C%20Same%2Ddesktop%20Elevation%20in%20UAC%20isn%27t%20a%20security%20boundary.%20It%20can%20be%20hijacked%20by%20unprivileged%20software%20that%20runs%20on%20the%20same%20desktop.). Better yet, [the feature is on by default](https://www.theverge.com/2024/6/3/24170305/microsoft-windows-recall-ai-screenshots-security-privacy-issues#:~:text=Microsoft%20is%20currently%20planning%20to%20enable%20Recall%20by%20default%20on%20Copilot%20Plus%20PCs.).

Microsoft's history with security has been a series of peaks and valleys. In 2002, they launched their ["Trustworthy Computing" campaign](https://en.wikipedia.org/wiki/Trustworthy_computing#Microsoft_and_Trustworthy_Computing) after a series of high profile issues with their products. Since then, Microsoft periodically sends a top-down message that security should be job #1. [This most recently happened via memo a month ago](https://www.theverge.com/24148033/satya-nadella-microsoft-security-memo). I feel like this feature missed that memo.

The good news is that Copilot+ PCs aren't out until later this month. It's likely that Microsoft can do something to mitigate this, even if it's just making the feature opt-in. The feature seems legitimately useful to me, but I definitely wouldn't want to use it in this state.

