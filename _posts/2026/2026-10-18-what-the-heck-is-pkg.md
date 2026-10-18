---
title: >
    What the heck is /pkg?
date: 2026-10-18 13:52:45 -0300
---

Recently, while troubleshooting a [PATH](https://en.wikipedia.org/wiki/PATH_%28variable%29) issue, I noticed an entry for `/pkg/env/global/bin`. At first, I worried that something had gone horribly wrong. Turns out, this is part of macOS 27.0… though no one is sure what it's for yet.

First, some background. Since Mac OS X 10.5 in 2007, the OS has included a [`path_helper`](https://hea-www.harvard.edu/~fine/OSX/path_helper.html) utility. This reads entries from `/etc/paths` as well as from any files in the `/etc/paths.d` directory. While one could potentially take advantage of this system, I (and I'd guess most others) handle adding new PATH entries using the [`.zshrc` file](https://zsh.sourceforge.io/Doc/Release/Files.html#Startup_002fShutdown-Files), or similar. The `path_helper` utility seems to be primarily used by Apple.

In macOS 10.15, an entry was added to `/etc/paths.d` to support the new location of the [`rvictl` utility](https://developer.apple.com/forums/thread/125402?answerId=392314022#392314022). In macOS 13.3, [Apple added some new entries](https://eclecticlight.co/2023/04/05/how-cryptexes-are-changing-macos-ventura/#comment-85119) to support [Cryptexes](https://eclecticlight.co/2023/04/05/how-cryptexes-are-changing-macos-ventura/). Now in macOS 27.0, there's a new `10-pmk-global` file [^1] which adds `/pkg/env/global/bin` to the PATH list.

I only started looking into this when I noticed an unfamiliar entry starting with `/pkg` in my PATH. I assumed something had gone awry. Then I saw that there was, indeed, a `/pkg` directory in the root of my filesystem. After freaking out slightly, I fell down this rabbit hole.

In a post about how [macOS's boot volume structure has been updated](https://eclecticlight.co/2026/09/19/macos-tahoe-26-4-changed-boot-volume-structure/), Howard Oakley explains that the `pkg` directory was added to the Data volume in macOS 26.4, but not added to the root of the Signed System Volume until 27.0. He also notes that [this is sort of a big deal](https://eclecticlight.co/2026/09/19/macos-tahoe-26-4-changed-boot-volume-structure/#comment-116877).

The weird thing is, as far as I can tell, no one seems to know what this new directory is for! It's odd that Apple would update their filesystem structure, add it to everyone's PATH, and there not be some explicable reason.

The `/pkg` directory contains four subdirectories: `env`, `etc`, `inv`, and `var`. Based on its name and those subdirectories, it's possible this could be used for an upcoming first-party package management system — but this is a wild guess. Apple recently [took over the Swift Package Index](https://www.theregister.com/software/2026/06/25/apple-takes-over-swift-package-index-vows-to-remove-github-dependency/5262048), but this seems unrelated. I don't know why you'd need a root-level directory to help with project-level dependencies. It's also not clear what the "pmk" in `/etc/paths.d/10-pmk-global` refers to.

Here's hoping we get more details on this at some point. In the meantime, maybe these details will help prevent someone else from freaking out when they see this entry in their PATH.

---

[^1]: Here the "10" part of the filename is to help with priority. Files starting with lower numbers are added to the path first, and therefore have priority.