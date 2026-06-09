---
title: >
    WWDC 2026: weird but better than I feared
date: 2026-06-09 13:54:50 -0300
---

This year's WWDC keynote was an odd one. It was relatively short at around 76 minutes, for one thing. It also eschewed the usual OS-by-OS structure, but I think that's for the best. The biggest change was that there was really only one major thing Apple wanted to talk about: "Apple Intelligence".

Apple divided their keynote into three sections: platform improvements,
trust and safety, and Apple Intelligence. The Apple Intelligence part clocked in at over 40 minutes, or around 53% of the total video runtime. The trust and safety bit was around 14% of the video, and the platform improvements discussion was a hair over 15%. The rest was the intro, a small teaser for developers, and some closing pieces.

### Platform improvements

[This part](https://www.youtube.com/live/hF8swzNR1-o?si=zBQoniLbuNXU9EXr&t=305) was, by far, the most interesting piece for me. [As I wrote before the keynote](https://anderegg.ca/2026/06/07/thoughts-ahead-of-wwdc-2026), I've been feeling that Apple's software story has been backsliding for long time. This section is the closest thing we'll get to an admission of that. I worried that this would be hard to sell, but I shouldn't have doubted Apple's marketing department.

We were walked through a number of fixes to Liquid Glass, all of which looked like improvements to me. [Sidebars are no longer nonsensical panes of "floating" glass](https://www.apple.com/v/os/f/images/macos/improvements/search__hlzbyw6h3aye_large_2x.jpg)! [Window corners are smaller](https://www.apple.com/v/os/f/images/macos/apple_intelligence/safari__e2cxljed2p26_large_2x.jpg) and consistently sized! Controls look more like glossy buttons instead of flat circles! Apps have [visible toolbars](https://www.apple.com/v/os/f/images/macos/siri/write__e9mbn9lu18ia_large_2x.jpg) again! [Much better app icon rendering](https://mastodon.social/@marioguzman/116716594259379078)! [No more superfluous junk in menus](https://appleinsider.com/articles/26/06/09/macos-golden-gate-menus-revert-to-having-no-icons-by-each-item-as-it-should-be)! [A slider to control Liquid Glass transparency](https://www.youtube.com/live/hF8swzNR1-o?si=H8DqG8pO5hcJHW0l&t=460)! I still have quibbles about Liquid Glass, but these updates look to have fixed the biggest ones.

There were also a number of [examples of optimizations across platforms](https://www.youtube.com/live/hF8swzNR1-o?si=sEQNnzPJfb4_lwZJ&t=583). Things like AirDrop being faster, quicker switching between wifi and cellular connections, progress bars for slow-sending items in Messages, and improvements to search across all OSs. There were many more listed, and we'll have to see how they work in practice, but I'm happy to see it's not only visual improvements.

Everything in this section is fantastic, and I'm grateful for the work Apple has put in. That said, many of these changes fix things that Apple only recently broke. My hope is that we don't need to wait another 5–6 years for another "polish" release.

### Trust and safety

Apple spent a lot of time highlighting a few new features [that help parents control screen time and content access for their kids](https://www.youtube.com/live/hF8swzNR1-o?si=L4uYI4wDBdplaNP7&t=1016). These features all seem solid, but it was odd how much time they were given. My best guess is that Apple is, at least in part, sending a message to governments around the world. Bills like [KOSA in the US](https://en.wikipedia.org/wiki/Kids_Online_Safety_Act) and the disastrously stupid [C-22 in Canada](https://www.michaelgeist.ca/2026/05/tech-exodus-why-bill-c-22s-privacy-and-security-risks-will-drive-digital-services-out-of-the-country/) weaken privacy and security in the name of protecting kids. I think Apple is trying to show that there's another way forward.

### Apple Intelligence

[Now for the meat of the keynote](https://www.youtube.com/live/hF8swzNR1-o?si=k0vEosK2V-ahXa2e&t=1670). Here Apple showed off its new LLM-powered version of Siri, as well as system-wide machine learning features. As expected, this is mostly the same stuff they promised in 2024.

Siri now has its own app on all platforms, and you can chat with it like other LLM-based tools. This means that you can also refer back to previous requests and responses, which is helpful. Examples were shown off in what looked to be real-time, including several long pauses between questions and responses.

Alone, that's not much. You're still likely to get better results from Claude or ChatGPT. The interesting parts are the app integrations. These allow Siri to search things like email, chat messages, and calendar events when answering a question. That is, as long as those apps have been updated to allow Siri to access them. All of Apple's apps will be, of course. This is a neat trick, but it's also an artificial advantage. Other LLM providers would love to offer these types of integrations, but Apple won't give third-party developers that level of access.

While the new Siri looks somewhat interesting, I'm not sure how much I'll make use of it. Outside of developer betas, it's not available to try until "[later this year](https://www.youtube.com/live/hF8swzNR1-o?si=nfZw1Gx0CNiqVSzk&t=4095)", likely slightly after the new iPhone is released in September. I pay for Anthropic's Claude, which already handles much of what the new Siri provides. I also don't know when/if the apps I use will be updated to take advantage of Siri integrations. Plus, Claude and other LLMs will keep getting better between now and the new Siri's release.

Watching this section also left me with some uneasy feelings. [Apple is updating Image Playground](https://www.youtube.com/live/hF8swzNR1-o?si=TdESrjmt5Rpuzy3-&t=3616), an app for AI-based image generation. This kind of app really rubs me the wrong way, and I wish Apple wasn't shipping it in its operating systems. They also announced [Spatial Reframing](https://www.youtube.com/live/hF8swzNR1-o?si=d0rP1vfZ92-yGeBt&t=3844), a feature that lets you "retake" a photo at a different angle. It does this by combining some impressive image analysis with image generation for the bits outside the original photo's frame. I know Photoshop's been around a long while, but I don't love how difficult it's becoming to trust that an image is real. We were also shown an example of [updating your passwords automatically using AI](https://www.youtube.com/live/hF8swzNR1-o?si=VgAAButDwVgcFxxp&t=3270). No thank you!

As rumoured, [Shortcuts can also be generated automatically](https://www.youtube.com/live/hF8swzNR1-o?si=UK94oInWkDojzie2&t=3524). Same for [Safari extensions](https://www.youtube.com/live/hF8swzNR1-o?si=zTBIan647iCI_sLU&t=3243), which I didn't see coming. These both seem mostly reasonable to me, though I'm not sure use of either feature.

Apple was coy about any costs surrounding the use of Apple Intelligence features. [LLMs are far from free](https://anderegg.ca/2026/04/22/llm-pricing-has-never-made-sense) and it's not clear how usage will be metered. In the keynote, [Craig Federighi said](https://www.youtube.com/live/hF8swzNR1-o?si=hEjeYYYEP5ecVGoQ&t=4025), "Some features, including image generation, have daily usage limits because they rely on powerful server models. Increased access is available with most iCloud+ subscription plans […]". I'm hoping we get more details about this later in the week.

Lastly, there was some discussion about many of the features being handled on-device. This is excellent, but it's something I need to understand better. Apple didn't make it all that clear what features are handled where, but more details will be available in future sessions throughout the week.

### Everything else

I liked the [macOS Golden Gate name announcement](https://www.youtube.com/live/hF8swzNR1-o?si=AerjLM5BwLJMrOPK&t=212) bit at the top. Sometimes the wacky parts are a bit much for me, but this one was just right. I also got a kick out of [the raccoon cameo](https://www.youtube.com/live/hF8swzNR1-o?si=LzF_se3EIOapTnkG&t=3474). Tim Cook's farewell message at the end was nicely done, and I loved the [Callsheet callout](https://bsky.app/profile/danielpunkass.punkitup.com/post/3mnscf4o2av2a) in the "app rap" at the end.

Overall, I'm extremely happy about the fixes and polish coming to every platform (but especially the Mac). While Apple's AI features are mostly reheated announcements from 2024, they mostly look fine… with some caveats. In short, though keynote wasn't all that exciting, I feel like things may be on an upswing again. That feels so much better than the alternative.