---
title: >
    Two more Liquid Glass fixes in macOS 26.4
date: 2026-03-30 18:20:01 -0300
---

I wrote yesterday about some [visual changes I'd noticed in Apple's 26.4 series of OSs](https://anderegg.ca/2026/03/29/liquid-glass-updates-in-264). Today I noticed that I'd missed a couple of real doozies, both related to the new mega-corners in macOS Tahoe.

<img src="https://anderegg.s3.amazonaws.com/26.4-corner-big.png" width="340" height="325" style="margin: auto; border: 4px solid #556;" alt="A screenshot of a blank window corner in macOS Tahoe 26.4. A mouse pointer is showing the window resize icon, and the cursor is positioned well inside the window. You can also see that the scrollbar is all the way at the bottom, but the bottom is above the corner radius. This means that it's no longer showing under the window corner as in previous versions." title="A screenshot of a blank window corner in macOS Tahoe 26.4. A mouse pointer is showing the window resize icon, and the cursor is positioned well inside the window. You can also see that the scrollbar is all the way at the bottom, but the bottom is above the corner radius. This means that it's no longer showing under the window corner as in previous versions.">

First up, [Apple fixed the corner resizing area](https://developer.apple.com/documentation/macos-release-notes/macos-26_4-release-notes#:~:text=Fixed:%20Window%20resize%20pointer%20does%20not%20follow%20the%20window’s%20corner%20shape.)! This had driven me nuts. I looked up the release note linked above after noticing that the large-o-vision corners felt easier to resize. I was surprised that I hadn't seen this change being celebrated across my RSS feeds.

The second thing is that scroll bars now stop just above the corner radius for these gargantuan corners. This means they're no longer [awkwardly clipped off](https://daringfireball.net/linked/2026/01/12/macos-26-cut-corner). This bug was another paper cut making Liquid Glass on macOS feel rushed out the door, so I'm glad it's fixed.

<img src="https://anderegg.s3.amazonaws.com/26.4-corner-small.png" width="340" height="325" style="margin: auto; border: 4px solid #556;" alt="A screenshot of another corner of a blank window in macOS Tahoe 26.4. This one has a smaller radius than the one above. The scroll bar is this time at the very bottom, and clips under the corner even though the corner is smaller." title="A screenshot of another corner of a blank window in macOS Tahoe 26.4. This one has a smaller radius than the one above. The scroll bar is this time at the very bottom, and clips under the corner even though the corner is smaller.">

Sadly, this scrollbar fix isn't extended to windows with smaller radii. Above is a screenshot of Apple's Terminal app. The window corner looks much better here, but it's still larger than in previous versions of macOS. Because of this, the corner is still getting clipped a small amount.

I still loathe Tahoe's clown-shoe-sized window corners. I'm also really irritated that [there are so many corner sizes for windows to have these days](https://bsky.app/profile/gavin.anderegg.ca/post/3melniwfrlc2k). That said, I am happy that Apple is iterating quickly on these issues. We're almost certainly going to be stuck with this design for a long while, so we might as well make it as nice as it can be.