---
title: >
    Tabs and menus in Apple's 27.0 OSs
date: 2026-10-02 13:15:48 -0300
---

After living with Apple's 27.0 OSs since launch, I have some more annoyances to get off my chest. This time, it's all about how tabs and menus have gotten worse.

I've already [ranted about the Liquid Glass material in general](https://anderegg.ca/2026/09/20/liquid-glass-in-270), but these two design changes in particular have really been grinding my gears. I'll reiterate that Apple's latest OSs look substantially nicer to me than the previous set… but that only makes these setbacks more glaring. Also, many of these issues aren't nearly as bad in light mode — but I use dark mode exclusively on all platforms. Apple offers this appearance setting, so I think it's fair to criticize them when it's not holding up.

First up, let's talk tab bars. I think these looked awful in the original Liquid Glass redesign, and in 27.0 they look even worse. Below is an example of three tab bars from Safari in macOS. All of them are in dark mode.

<img src="https://anderegg.s3.amazonaws.com/27.0-design/tabs.webp" width="1001" height="145" alt="Examples of tab bars in Safari on macOS 26 and macOS 27.">

The top example is from macOS 26 with the "clear" Liquid Glass setting, the middle is macOS 27 with the default (mid-slider) version of Liquid Glass, and the bottom is macOS 27 with Liquid Glass at its most tinted. In each, the middle tab is selected (though I think the word "tab" is being quite generous to these globs).

In macOS 26, there was practically no difference between the clear and tinted versions of tabs. Similarly, the clearest and default/middle tabs in macOS 27 are effectively the same. Because of this, I'm leaving out the redundant examples.

Even though I still think it's ugly, I vastly prefer the macOS 26 version of these three options. It offers the most contrast, and it makes more sense in dark mode: the background is darker and the foreground of the active tab is lighter.

The middle example is what tabs look like in the default (mid-slider) version of Liquid Glass in macOS 27. There's now only a very faint outline around the active tab, and practically no difference in background colours. To me, this is unreasonably subtle. The effect is even worse when there are a lot of tabs open.

Lastly, there's macOS 27 with the fully tinted Liquid Glass setting. It's better, but it still looks less correct to me than the tab design from macOS 26.

It's difficult to put into words how much I loathe the look of this new tab bar design. I don't mind the more "bubbly" look of Liquid Glass throughout the 27 OSs for the most part. It gives UI elements more dimension than in the 26 OSs. But it doesn't work for tabs. Because the bubbly look is inside a trough, the active tab's glass effect ends up looking like a blur on the top and bottom. This reduces contrast further and makes the active tab harder for me to pick out. Even in dark mode with full tint, I find the active tab less visually clear than in 26's *clear* mode.

Now, I'm sure there are at least a few people reading who don't see what the fuss is about. If that's you, I assure you that the difference is more stark when you're not comparing things side by side. It's not impossible for me to pick out the active tab, but I think it's trickier than it needs to be! But, if you still don't believe me, here's a little experiment. Which of these do you think is most legible?

<img src="https://anderegg.s3.amazonaws.com/27.0-design/text-sample.webp" width="1001" height="372" alt="Sample latin text showing very low contrast background/foreground colour combinations.">

The text/background colours in the above image are based on the foreground/background colours used in the tab bar instances above. First is clear in macOS 26, then the default from macOS 27, then fully tinted in macOS 27. I think they're all pretty awful, but it's plainly clear that the middle one (the default tab bar contrast in macOS 27!) is unreadably bad.

My preference is the macOS 26 version because I'm using dark mode. In dark mode, light text appears on a darker background. Similarly, active UI elements have a lighter background than their surrounding elements. I'm sure there are counter-examples, but this is how just about everything else works in Apple's own apps!

It should be noted that Safari uses the system default tab bar design. I also see this design in Apple's Terminal app, in Pixelmator Pro, and elsewhere. I don't use Xcode daily anymore, but you'll also find them there — though in true Xcode fashion, they're ever so slightly nonstandard and also don't respect your tint setting. Below is a screenshot of Xcode using my current settings of dark mode with fully tinted Liquid Glass.

<img src="https://anderegg.s3.amazonaws.com/27.0-design/xcode.webp" width="882" height="88" alt="Part of an Xcode window showing its tab bar.">

Up next: menus. Below is an image showing four versions of the same menu in macOS. Top left is macOS 26 clear, top right is macOS 26 tinted, bottom left is macOS 27 default (mid-slider), and bottom right is macOS 27 fully tinted.

<img src="https://anderegg.s3.amazonaws.com/27.0-design/menus.webp" width="589" height="801" alt="Four examples of an open menu from macOS 26 and 27.">

It's a similar story here. In macOS 26's dark mode, I had no problem with system menus even when Liquid Glass was set to clear. In macOS 27, even in the fully tinted mode, the menus have much lower contrast. They also now lose all of Liquid Glass's refractive effects when at their most tinted. I think this is less of an issue than the tab design changes, but it's still a downgrade.

Again, I'm certain many people don't care about this. Some might wonder why I'm not turning on accessibility settings to help with these things, if they bother me so much. I've flirted with this (especially the "Increase Contrast" setting), but those settings have many knock-on effects. [^1] But honestly, I don't think accessibility settings should be required to have a reasonable amount of contrast in a design system. Maybe Apple disagrees, but I really hope more dark mode tweaks are coming.

---

[^1]: The "Increase Contrast" setting is under System Settings -> Accessibility -> Display -> Increase Contrast. Interestingly, you can use this setting along with the clearest version of Liquid Glass to almost get back to how things looked in macOS 26's version of tinted. However, it adds contrast-y lines around many UI elements that I find extremely distracting. It also alters colours on some elements to, strangely, make them less contrast-y. It feels unevenly applied and poorly implemented in several apps.