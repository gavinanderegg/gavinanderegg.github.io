---
title: >
    Using GitHub as a CMS
date: 2024-10-16 13:22:00 -0300
---

A couple of days ago, [I saw this Mastodon post from Casey Liss](https://mastodon.social/@caseyliss/113308279629674546). I had previously used [GitHub Codespaces](https://github.com/features/codespaces) when working with a client, but it was a bit much. It relies on VMs that run on GitHub servers to give you a [VS Code](https://code.visualstudio.com) instance. Those VMs take a while to spin up and you have a limited number of hours per month depending on your plan. It's a neat service, but I wasn't interested in using it for personal projects.

What Casey mentions in his toot is different. This is the strangely named "[github.dev editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)". You can get to it by pressing the `.` key on any GitHub repo you have access to while logged in. It runs locally in your browser, so there are no usage limits. Files are saved locally (using [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)), so you can save things on a local machine before committing. Like with other versions of VS Code, [you can sync your settings](https://code.visualstudio.com/docs/editor/settings-sync).

I'm currently writing this post using the github.dev editor now! Because of my [GitHub Pages blogging setup](https://anderegg.ca/2024/05/13/how-i-write-for-the-web-jekyll-and-github-pages), I just need to commit my changes to have a new post appear on my site. The editor is set up with mostly the same configuration I use in the desktop verison of the editor, so it's a reasonably nice editing experience as well. As Casey points out, this is a great way to quickly edit files hosted in GitHub from an iPad, so that's how I'm giving that a shot.

There are some caveats, though. Although I did sync my settings, [it doesn't properly use the typeface I'd prefer](https://anderegg.ca/2023/02/16/typeface-tournament). The editor is set to use the ["Hack" font](https://sourcefoundry.org/hack/), but it's rendering with the system font instead. I also tried on macOS and also didn't load Hack, so this doesn't seem to be an iPad-specific issue. There's also no spell checking, which is a pain for writing. I looked to see if there was a way to enable this with a plugin, but it turns out that most plugins don't work with the web editor. That's quite understandable, but may be limiting for some. Also, I can't easily preview things locally before they go live.

None of these are showstoppers, though. I'm definitely not going to replace my current workflow with the github.dev editor, but I'm really happy it exists! I'm certain it's something I'll use for posting or editing again in the future.
