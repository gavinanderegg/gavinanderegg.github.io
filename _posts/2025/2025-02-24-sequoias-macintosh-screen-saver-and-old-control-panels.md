---
title: >
    Sequoia's "Macintosh" screen saver and old Control Panels
date: 2025-02-24 13:29:30 -0400
---

I was recently on-site with a client and noticed that one person was using the new ["Macintosh" screen saver](https://www.macrumors.com/2024/06/11/macos-sequoia-wallpaper/) that was added in macOS Sequoia. If you haven't seen it, [here's a video of it in action](https://www.youtube.com/watch?v=pnjxehheT_I).

I knew that the screen saver had released, but I was very happy with [Relay's St. Jude screen saver](https://relay.experience.stjude.org/#:~:text=Donation%20Rewards) by [James Thomson](https://mastodon.social/@jamesthomson). Happily it turns out that you can run two different screen savers on macOS if you have more than one monitor.

To get this working under macOS Sequoia, first make sure your monitors set up as different "Spaces". You can do this by heading to `System Settings ➔ Desktop & Dock`, and under the "Mission Control" section, make sure "Displays have separate Spaces" is enabled. Then you can head to `System Settings ➔ Screen Saver`, and turn off "Show on all Spaces" to the left of the preview thumbnail. Now you can use the drop-down below the thumbnail to choose which monitor you want to configure.

I chose to set up the Macintosh screen saver on my secondary monitor, which is in portrait orientation. I set it to the "Spectrum" colour setting (same as in the example video linked above), and also enabled "Show as wallpaper". This has the nice effect of having the screen saver ease out of its animation and into the desktop wallpaper for that monitor when you wake your machine.

I switched to the Mac in 2002 with the release of [Mac OS X Jaguar](https://en.wikipedia.org/wiki/Mac_OS_X_Jaguar). Previously, I lived in the PC world and didn't have much love for anything Apple-related. After I switched, I found myself curious about the earlier days of the Mac. This screen saver made me want to dig further into some of the details.

A nice effect of the screen saver and its wallpaper mode is the subtle shadowing on the chunky pixels. I'm assuming this is a nod to the [Macintosh Portable](https://en.wikipedia.org/wiki/Macintosh_Portable) and its early active-matrix LCD. The screen on the Portable had a distinctive "floating pixel" look. I love how this looks, though I think it would have been a pain to use day-to-day. Colin Wirth [produced an excellent video about the machine](https://www.youtube.com/watch?v=Okz14yztJ3I) on his channel "This Does Not Compute". You can see the some close-ups of the effect [starting around the 2:30 mark](https://youtu.be/Okz14yztJ3I?si=k9DZP6ErqyKOIOZo&t=150).

Watching the screen saver also had me curious about what version of system software was being shown off. Turns out it's more than one. Two tools I used to start looking into this were [GUIdebook's screenshots section](https://guidebookgallery.org/screenshots) and [Infinite Mac](https://infinitemac.org/) — a site that lets you run fully-loaded versions of classic Macs in your browser.

I was most fascinated when the screen saver scrolled over versions of the Control Panel. Especially the version from System 1. You can see this [starting at 0:12](https://youtu.be/pnjxehheT_I?si=viQZrEAxXigvDE0z&t=14) in the example video. This thing is a marvel of user interface design. Pretty much everything that can be configured about the original Macintosh is shown, without words, in this gem of a screen.

![An enlarged image of the original Macintosh Control Panel](https://anderegg.s3.amazonaws.com/Macintosh/Control%20Panel%20-%20System%201.png)

[Low End Mac has a good overview](https://lowendmac.com/2005/innovative-macintosh-system-1-0/#:~:text=Next%20is%20the%20Control%20Panel) of what's going on here, but I feel like it's the sort of thing you could intuit if you played with it for a minute or two. One thing I learned while writing this is that you can click the menu bar in the desktop background preview to cycle through some presets!

My only nitpicks about this screen are that it uses a strange [XOR'd](https://en.wikipedia.org/wiki/Exclusive_or) cross instead of the default mouse pointer. I'm assuming this was to make it easier to edit the desktop background, but it still feels like an odd choice. Also, the box with controls how many time the menu blinks is one pixel narrower than the two boxes below it. This would have driven me insane, and I'm amazed it [still looked this way in System 2.1](https://infinitemac.org/1985/System%202.1).

![A weird 1 pixel offset on the top right control panel box.](https://anderegg.s3.amazonaws.com/Macintosh/Offset.png)

The Macintosh screen saver shows its time based on your system clock. I use 24-hour time, and that's respected in the screen saver even when it's showing the original Control Panel. This, ironically, is an anachronism. [24-hour time wasn't an option until System 4](https://www.versionmuseum.com/history-of/classic-mac-os#:~:text=Mac%20OS%20System%204%20Control%20Panel%20%281987%29).

The screen saver also includes a version of Control Panel from System 6. You can see this [at around 9:08](https://youtu.be/pnjxehheT_I?si=NmyAXOyW_9vvIkG_&t=548) in the example video. This Control Panel shows its version as 3.3.3 in the bottom left. I believe this makes it System 6.0.7 or 6.0.8. [You can run System 6.0.8 using an emulator on Archive.org](https://archive.org/details/mac_MacOS_6.0.8).

![An enlarged image of the Macintosh Control Panel from System 6.0.8](https://anderegg.s3.amazonaws.com/Macintosh/Control%20Panel%20-%20System%206.0.8.png)

While this version allows for many more options, it's far less playful. This general style — with the scrollable list of setting sections on the left — started with System 4. [System 3 had the last all-in-one Control Panel layout](https://guidebookgallery.org/screenshots/macos30#:~:text=General%20in%20System%203.0). System 7 migrated to the [Control Panels folder](https://guidebookgallery.org/screenshots/macos70#:~:text=Settings%20menu%20in%20System%207.0%20%28Control%20Panels%29), where each panel is its own file, and you could easily add third-party panels to the system.

Anyway, this has been far too many words about a screen saver released eight months ago. If you find this interesting, I encourage you to give the Macintosh screen saver a go. I also recommend poking around at old versions of classic Mac OS. I had a lot of fun digging into this!