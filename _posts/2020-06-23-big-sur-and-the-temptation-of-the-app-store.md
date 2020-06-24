---
title: Big Sur and the Temptation of the App Store
---

At WWDC this year, Apple announced their switch to “[Apple silicon](https://www.apple.com/newsroom/2020/06/apple-announces-mac-transition-to-apple-silicon/)” for Mac hardware. This had been heavily rumoured for years, and there was a lot of discussion about it. Some worried that Apple would use the transition as an excuse to lock down app delivery further — perhaps only allowing apps to be installed from the Mac App Store.

This didn’t happen. You can still choose to [install apps from identified developers](https://support.apple.com/en-ca/HT202491), or [install an unsigned app](https://support.apple.com/en-ca/guide/mac-help/mh40616/mac) if you trust it. But something else happened instead: Apple announced that iOS apps are coming directly to the Mac. Specifically, Macs that use their new chips and run the upcoming version of macOS, [Big Sur](https://www.apple.com/macos/big-sur-preview/).

I'm worried about this. Here's my thinking.

There are an order of magnitude more [iOS devices](https://www.theverge.com/2019/1/29/18202736/apple-devices-ios-earnings-q1-2019) than [macOS devices](https://techcrunch.com/2018/10/30/there-are-now-100-million-macs-in-use/) in use. I couldn’t find hard numbers, but I’d bet there are similarly way more iOS developers than macOS developers. This makes sense, as iOS is the newer and more exciting platform. Apple focused a lot of attention on iOS since introducing the iPhone, and the Mac became a bit more of a workhorse over time. People still develop apps for macOS, but there have been fewer over time. Also, many new Mac apps are developed with cross-platform tools like Electron.

That Electron piece is interesting. Slack is the poster-child for Electron on desktops, [but their iOS app is native](https://twitter.com/slackhq/status/931599784137363459). Personally, I think the Slack experience on iOS is nicer. With iOS apps coming to Big Sur, it’s not crazy to imagine Slack eventually shipping their iOS app on the Mac instead of the Electron version. Other developers with both macOS and iOS software would be in a similar position.

The thing about those iOS apps is that they have to come from the App Store, even on the Mac. Of course, developers can always choose to use the iOS version as a starting point and build a custom [SwiftUI](https://swiftwithmajid.com/2019/10/23/reusing-swiftui-views-across-apple-platforms/)/[Mac Catalyst](https://developer.apple.com/mac-catalyst/) version specifically for macOS – but going the easier route will be pretty tempting. Writing something once and publishing for multiple platforms saves on developer time, which is why Slack uses Electron for their desktop apps. It makes sense to put more resources into the version with the bigger audience as well, which probably why I prefer Slack on my iPad.

Before WWDC, I wasn’t worried about the ARM transition meaning the Mac would go App Store only. Sure, Apple would love for more apps to be in the App Store for security (and monetary) reasons, but the platform needs apps that the App Store can’t support. The whole “iOS apps on the Mac” wasn’t something I saw coming, though. Apple won’t enforce this change, but I worry that developing a “good enough” iOS app for the Mac might become the future of the platform.
