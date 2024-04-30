---
title: What file types does Apple’s Archive Utility open?
---

#### Short version:
As of macOS Catalina (10.15.6), Apple's Archive Utility will try to open files with the following extensions:

* [.7z](https://en.wikipedia.org/wiki/7-Zip)
* [.aar](https://en.wikipedia.org/wiki/Apache_Axis2)
* [.as](https://en.wikipedia.org/wiki/AppleSingle_and_AppleDouble_formats)
* [.bin](https://en.wikipedia.org/wiki/Disk_image)
* [.bz](https://en.wikipedia.org/wiki/Bzip2)
* [.bz2](https://en.wikipedia.org/wiki/Bzip2)
* [.bzip2](https://en.wikipedia.org/wiki/Bzip2)
* [.cpgz](https://en.wikipedia.org/wiki/Cpio)
* [.cpio](https://en.wikipedia.org/wiki/Cpio)
* [.gz](https://en.wikipedia.org/wiki/Gzip)
* [.hqx](https://en.wikipedia.org/wiki/BinHex)
* [.pax](https://en.wikipedia.org/wiki/Pax_(command))
* [.tar](https://en.wikipedia.org/wiki/Tar_(computing))
* [.tbz](https://en.wikipedia.org/wiki/Tar_(computing))
* [.tbz2](https://en.wikipedia.org/wiki/Tar_(computing))
* [.tgz](https://en.wikipedia.org/wiki/Tar_(computing))
* [.txz](https://en.wikipedia.org/wiki/Tar_(computing))
* [.uu](https://en.wikipedia.org/wiki/Uuencoding)
* [.xip](https://en.wikipedia.org/wiki/.XIP)
* [.xz](https://en.wikipedia.org/wiki/XZ_Utils)
* .yaa
* [.z](https://en.wikipedia.org/wiki/Compress)
* [.zip](https://en.wikipedia.org/wiki/Zip_(file_format))

#### Long version:
This morning I was reading [an article about improvements to the Brotli compression algorithm](https://dev.to/riknelix/fast-and-efficient-recompression-using-previous-compression-artifacts-47g5), and found myself wondering: "_What compression formats does Apple’s Archive Utility support by default?_". Searching Google didn’t immediately turn up anything (something I’ve been finding more and more recently), so I wondered if there’s a way to inspect the application to find out what it supported.

There was a [Super User answer that pointed me in the right direction](https://superuser.com/questions/440657/search-for-files-which-will-open-a-certain-application-in-mac-os-x/440670#440670), but Archive Utility didn’t have an `Info.plist` with the file information. What it had instead was a bunch of icons that listed the extension names for supported files. It’s not 100% clear if this list is exhaustive, but it’s good enough for me.

![Archive Utility's Resources folder](/assets/archive-utility.png)

You can find this folder here:

`/System/Library/CoreServices/Applications/Archive\ Utility.app/Contents/Resources`

After finding the list, I fell down a rabbit hole of investigating seldom-used compression formats. I’ve added links above to Wikipedia pages for all the formats I could find. The `.bin` link is a general one, as I’m not sure exactly which format is supported here. The `.aar`, `.as`, and `.uu` formats were unknown to me, but I’m pretty sure the links are correct for these. The one standout was `.yaa`, which I’d also never heard of. It appears to be Mac-specific. There’s a man page for it (`man yaa` in a Terminal window) which provides a bit more detail. [It seems it was added in High Sierra](https://www.mackungfu.org/NewcommandlinetoolsinHighSierra).

I probably shouldn't find this surprising, but [StuffIt](https://en.wikipedia.org/wiki/StuffIt) files (`.sit`, `.sitx`) aren't supported by this utility. StuffIt, though now discontinued, is still a commercial project. But those archives are still so strongly linked with classic Mac OS that it's hard to see `.hqx` in the list without immediately thinking of `.sit`.

While I'm on the topic, there's a great [list of archive formats](https://en.wikipedia.org/wiki/List_of_archive_formats) on Wikipedia as well. I got immediate waves of nostalgia from seeing `.arj` and `.lha` in that list.