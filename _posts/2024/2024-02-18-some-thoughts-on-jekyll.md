---
title: Some Thoughts on Jekyll
date: 2024-02-18 14:01:00 -0400
---

[Jekyll](https://jekyllrb.com) is a static site generator built in [Ruby](https://www.ruby-lang.org/en/). It's been powering this site [since 2012](https://web.archive.org/web/20120927072029/http://anderegg.ca/) but I'm worried that might not be true for much longer. I'm a bit torn on how to feel about this.

First, a bit on static site generators (SSGs). Serving only static content is *fast*. With an SSG, you're effectively "pre-compiling" all server-side elements of a site at build time. Once you send the "compiled" version of the site to your server, the files just need to be served. This is the easiest possible thing for a web server to do, so it scales extremely well. A [recent post](https://anderegg.ca/2024/02/02/why-isnt-the-html-element-100-supported) was the number 1 post on [Hacker News](https://news.ycombinator.com) for over 6 hours. This generated a lot of traffic, but my site never slowed down.

There are many providers who specialize in hosting static content. A popular choice is [Netlify](https://www.netlify.com). I've really enjoyed working with their system in the past, and have recommended it to others. Heck, you can also just use [Amazon S3 to host static content](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html).

This site is hosted on [GitHub Pages](https://pages.github.com), which uses Jekyll by default. I enjoy using GitHub in general, and their Pages product is free. It's also powered by Microsoft's server infrastructure, which is no slouch. Getting set up to host using GitHub Pages is as easy as setting up a repo and pushing content built for Jekyll. Using a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) on your site is straightforward and also free. [Jekyll was also written with GitHub Pages in mind](https://github.blog/2008-12-18-github-pages/). It seems like a perfect match.

In August of 2019, [Jekyll 4.0](https://jekyllrb.com/news/2019/08/20/jekyll-4-0-0-released/) was released. The same day, a [GitHub issue was created](https://github.com/github/pages-gem/issues/651) requesting that GitHub Pages be updated to support the new version. That issue is still open, and as of [August 2022](https://github.com/github/pages-gem/issues/651#issuecomment-1208290235) an engineering manager at GitHub has indicated that this update isn't going to happen anytime soon. Also, previously the Jekyll to GitHub Pages flow was a special case that happened when committing to GitHub. Now it all uses [GitHub Actions](https://github.com/features/actions), putting Jekyll on about the same footing as any other SSG.

As of this writing, [Jekyll 3.9.5 is the version supported by GitHub Pages](https://pages.github.com/versions/). GitHub [continues to maintain](https://github.com/github/pages-gem/releases) the libraries used to support Pages, but I'm not convinced that there's much appetite for larger changes. If anything starts breaking because Jekyll 3.x is too old, my guess is that we're going to be told that GitHub Actions is a great alternative.

Because it's easier, I'm currently running the latest version of Jekyll 4.x locally and still using the default GitHub Pages updating flow. This hasn't bitten me yet, but it doesn't seem ideal. Also, Jekyll is also the only Ruby project I use frequently. I should probably set up the same level of library/environment control as I do with my Python projects, but I haven't so far. I've become quite proficient at fixing Jekyll when [Homebrew updates break it](https://docs.brew.sh/FAQ#why-does-brew-upgrade-formula-or-brew-install-formula-also-upgrade-a-bunch-of-other-stuff), but again: not great.

So, am I going to switch right away? No. But I've started looking at alternatives. The biggest two are [11ty](https://www.11ty.dev) and [Hugo](https://gohugo.io). 11ty has the advantage of being written in JavaScript, so the tooling is familiar to me and I feel I could manage it well. Hugo is written in [Go](https://go.dev), however it seems quite self-contained. If I'm not using the Jekyll-specific parts of GitHub Pages, I could effectively ignore how Hugo is built and just think of it as a black-box.

Whatever I do, I'm sure there will be tradeoffs. The publishing flow today with Jekyll and GitHub pages is going to be very hard to beat, but seeing [some of the cool things](https://rknight.me/blog/eleventy-post-graph-plugin/) people are doing with newer tools like 11ty has me feeling some serious FOMO.








