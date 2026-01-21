---
title: >
    Reckoning with Liquid Glass
date: 2026-01-20 16:27:38 -0400
---

When Apple released its new operating systems last year, I wasn't in a hurry to upgrade. I had initially come away from WWDC 2025 excited about the new Liquid Glass design language, [but then became grumpy](https://anderegg.ca/2025/07/12/grumbling-about-liquid-glass). The visual effects looked nice to me, but they functioned more poorly than I'd hoped. Well, [I've finally updated all my devices](https://bsky.app/profile/gavin.anderegg.ca/post/3mca6hbjwuk2g) and I have some feelings.

My upgrade cycle kicked off with a new iPhone 17 Pro. I am exceedingly happy with the hardware. Less so the OS. Here's the thing: iOS 26 is mostly fine. My major issues are with the redesign, and I think they can all be fixed with refinement. This is definitely the platform I have the least problems with.

I waited a bit to get the phone, so it came with iOS 26.1. This introduced a new ["Tinted" version of Liquid Glass](https://www.macrumors.com/guide/ios-26-1-features/). I tried living with the defaults, but was much happier after applying the tinted look. The default "Clear" option makes things annoyingly illegible too often. The tinted version almost entirely solves this for me. Also, I think tinted looks significantly better than clear, especially in dark mode. The glassy effects are still there, but they're more subtle and less irksome.

That aside, here are some of the other issues I have with iOS 26:

1. Liquid Glass UI elements often disregard light/dark mode settings. I find this very distracting, and I don't understand why the UI needs to [flit between dark or light so often](https://mastodon.social/@chbeer/115146363054220735). I prefer dark mode, and the dark version of Liquid Glass always looks better to me than the light version. I think it's a failure of design if the clear mode requires this light-dark-light dance to be legible. Maybe Apple could keep things static while in tinted mode? Please?
2. In many first-party apps, content is only given the mildest of blurring/fading as it scrolls under the status bar at the top of the phone. In Photos, this is mostly fine. [When reading text in Safari](https://bsky.app/profile/gavin.anderegg.ca/post/3mcuobd4i422j), I find it very annoying.
3. I've mostly come to terms with it, but many UI elements [are now more squashed together](https://www.nngroup.com/articles/liquid-glass/#:~:text=nausea.-,Crowded%2C%20Smaller%20Tap%20Targets,-Apple). This is because Liquid Glass elements have to be further inset from the side of the screen. The point of the inset, so far as I can tell, is so that you can see more content. I guess that's kind of true? You can see glimpses of content, often blurred, if you try to peak around the UI elements. I don't find this helpful.
4. Even with the 26.2 updates, these OSs still have many visual glitches. At least once every couple of hours, [I'll spot a Liquid Glass control doing something weird](https://bsky.app/profile/gavin.anderegg.ca/post/3mcunjss47s2e). It's very rare that this is a usability issue, but it feels janky.

iPadOS 26 is mostly a win in my books. It also has the above issues, but [the new windowing interface](https://appleinsider.com/inside/ipados-26/tips/whats-new-with-ipad-app-windows-in-ipados-26-and-how-they-work) is a huge upgrade. I used my 13" iPad Pro with a Magic Keyboard while travelling over the holidays and was able to get more done with iPadOS than ever before. I was also very happy that Safari got an option to disable "Hide Tab Bar While Scrolling". [^1] I wish I could also select this in Safari on iOS.

One thing I *don't* like about iPadOS 26 are the massively rounded window corners. I can excuse a lot of what iPadOS does because it's really cute when it tries to act like a real computer. So when all iPadOS apps look like balloons in windowed mode, yeah it's stupid looking, but it's at least more useful than it's ever been. What really tickles me is that [the windows shrink to a more reasonable size when being moved to a corner](https://bsky.app/profile/gavin.anderegg.ca/post/3mcupohw3os2m). It's a weird solution to a problem that wouldn't exist if windows weren't bulbous.

Sadly, macOS Tahoe also gets the clown-shoe-assed window corners. Sometimes, anyway. [There are at least three sizes of border radius in play on macOS 26](https://bsky.app/profile/gavin.anderegg.ca/post/3mcurx3t6ck2h). [^2] Most of Apple's apps (Safari, Mail, Music, etc.) have the new huge corners. Apps that haven't been updated for Tahoe have the same radius as they did in macOS 15 (Photoshop and Panic's Nova are two I still see). There's also a middle-ground for apps like Apple's Terminal app and the current version of Visual Studio Code. In practice, the size of a window's corner feels almost random.

On top of that, Tahoe's massive corners are poorly implemented. [Scrollbars slide awkwardly under them](https://daringfireball.net/linked/2026/01/12/macos-26-cut-corner) and you're more likely to be able to resize an app [if you click outside its window](https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/). It's almost like they're a purely visual change that doesn't alter how windows function.

The other thing I find ugly is the new tab interface. Here's a screenshot of tabs in [Finder from macOS 15](https://512pixels.net/projects/aqua-screenshot-library/macos-15-sequoia/#jp-carousel-30384), and here's one [from macOS 26](https://512pixels.net/projects/aqua-screenshot-library/macos-26-tahoe/#jp-carousel-33764). In macOS 15, there's an actual tab metaphor happening, though it's a bit stretched. The active tab is attached to part of the UI, so it's clear what's being indicated. In macOS 26, the tab is a bright pill in a channel that's attached to nothing. I don't think anyone will be stumped by this, but it's not really a "tab" anymore.

An argument I've heard in praise of Liquid Glass: at least it's not flat. I get this, and I do appreciate buttons looking more button-ish in places, but I have to push back. Liquid Glass makes things more button-like only when there's, say, 1–2 items in a Liquid Glass container. The things you press are still flat. To demonstrate this, try opening up Safari on macOS 26. Right-click the top of the app and choose "Customize Toolbar…". [You can then drag over a dozen items into the same Liquid Glass blob](https://bsky.app/profile/gavin.anderegg.ca/post/3mcutfupksk2h). Now it's just a bunch of flat icons hanging out in a weird soup.

But no sane app developer is going to do that. It's weird that you can do it as a user, but it's not so bad. The real point of contention I have with the "less flat" argument is that most of the default OS widgets have been run over with a steamroller. Check out this [screenshot of the TV app in macOS 15](https://512pixels.net/projects/aqua-screenshot-library/macos-15-sequoia/#jp-carousel-30442). Compare it to the [same screen on macOS 26](https://512pixels.net/projects/aqua-screenshot-library/macos-26-tahoe/#jp-carousel-33849). Everything's flatter and lower contrast.

I also think Liquid Glass is overused on the Mac. In places, [UI elements are allowed to become smears of unreadable bullshit](https://eclecticlight.co/2025/12/28/last-year-on-my-mac-look-back-in-disbelief/#:~:text=Wet%2Don%2Dwet,-This%20technique%20is). I assumed this sort of thing was a bug at first, but it's been constant through many beta versions and three point-releases. I guess someone thinks it's fine? Similarly, [Nikita Prokopov recently wrote a great overview of the icons that now litter Tahoe's menus](https://tonsky.me/blog/tahoe-icons/). Prokopov's piece does an excellent job explaining how wrongheaded this idea is.

I'm sure there are people reading this and shaking their heads. Maybe I'm just an old grump who doesn't want to get with the times. Could be! But, these complaints aside, I don't hate the Liquid Glass effect. In fact, I really enjoy it on iPhone lock screen. Pulling the lock screen down from the top of the display looks great! In tinted mode, I appreciate the subtle effect content has on Liquid Glass blobs (as long as they're not randomly changing colour or size as I scroll). I think there's an interesting idea here, but I also think the details need a lot of addressing.

[I've written about it before](https://anderegg.ca/2025/09/10/quick-thoughts-on-apples-september-2025-event), but probably the angriest I've been while watching an Apple keynote was during last year's iPhone event. The event started with a quote from Steve Jobs: “*Design is not just what it looks and feels like. Design is how it works.*” I really like that quote and I feel it was being grossly misused by someone who didn't understand it.

For whatever reason, the rounded corners are the most galling example of this to me. Apple themselves have smaller corners on some of their apps, and they seem OK with non-updated apps having yet another corner size. As described above, the larger corners on Tahoe seem poorly implemented. Even iPadOS needs to special-case corners as they go full screen. These are all perfect examples of "how it looks" interacting poorly with "how it works". In other words: someone thought it looked pretty, so now we're shoehorning it in.

It's [heavily implied in that keynote video](https://www.youtube.com/watch?v=H3KnMyojEQU) that the corners in software match the corners in hardware, but this is bullshit. My iPhone Pro and iPad Pro do indeed have the same corner radius. But you know what radii don't match up?

* My iPhone and my Studio Display.
* My iPhone and my Mac Studio.
* **My iPhone and the stupid corners on Tahoe windows!**

That's right, the window corners on Tahoe and iPadOS have a much smaller radius than the iPhone's. [^3] I checked this on my Studio Display (running at native resolution) and on my iPad Pro.

Anyway, look: I get that the reason for a UI change can be "because it was time for a change". My hope is that the Liquid Glass UI will be refined over time and that these issues will addressed. I know a lot of well-meaning people worked hard on this stuff, but my guess is that there were [many bad calls made at the top](https://anderegg.ca/2025/12/05/bye-bye-alan-dye). [^4] macOS Tahoe is far and away the worst implementation of this design, but it's not unusably bad. [^5] It's definitely not unfixable… but I do think there's [a long way to go](https://bsky.app/search?q=%22liquid+glass%22).

---

[^1]: This is under Settings -> Apps -> Safari -> "Hide Tab Bar While Scrolling" (under the "Tabs" section). As I was reminded this holiday season, [Settings search is effectively useless](https://bsky.app/profile/gavin.anderegg.ca/post/3maqk2bpb6c2a).

[^2]: Rui Carmo says he can count [five different corner radii](https://taoofmac.com/space/notes/2025/09/15/2359#:~:text=five%20different%20sizes%20of%20window). I'm not sure what the other two are, though.

[^3]: Please, Apple, do not take this as an invitation to make the windows any more round.

[^4]: I was recently pointed to a Game Developers Conference video about Destiny 2. In it, the lead UI designer walked through the process of building out the game's interface. [Just before launch, the team became obsessed with an interesting idea](https://youtu.be/zp4NZ8i80QI?si=yRDclEA7nQmfQogU&t=2544). This idea had fundamental flaws, but the idea was interesting enough that they looked past them. Instead of taking a step back, the team ended up honing the flawed design almost to the point of shipping. Then, at the last minute, they realized their mistake and were able to ship something wonderful. Not sure why I thought of that just now.

[^5]: "macOS Tahoe: It's not unusably bad" is a pretty crap slogan, but I think it fits.
