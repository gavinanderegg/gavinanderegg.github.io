---
title: What Does It Mean to “Own Your Content”?
date: 2024-03-28 11:21:56 -0300
---

Late last year I was starting to hype myself up to write more. One thing I got hung up on was, "how do I post from my phone"? Honestly, I'm still slightly hung up on this. But thinking it through: I really don't post enough that it can't wait until I'm in front of a computer.

The fact that I was waffling about this got me thinking about two things. First: services like Facebook and Twitter made it simple to post from anywhere, which is how they got everyone to produce content for them. Second: I want to post more on my website instead of other people's services because I want to own my content — but what the heck does that even mean?

I started waffling about content ownership while playing with [Micro.blog](https://micro.blog). This is a service I [backed on Kickstarter](https://www.kickstarter.com/projects/manton/indie-microblogging-owning-your-short-form-writing/description) in 2017. I used the service a bit when it launched, but never stuck with it. I was very happy to support the project, but it was a strange middle-space between a social service like Twitter and posting to this website. I signed up again last year thinking that I could use it just for posting short-form content from my phone, but that also never really happened. The service is really great, I just couldn’t find a way to make a habit of using it.

One of the values of the Micro.blog team is [owning your data](https://micro.blog/about). Let's dig into that:

* You have to pay to host content on the service, [which is a good sign](https://www.metafilter.com/95152/Userdriven-discontent#3256046),
* you're encouraged to [use your own domain](https://help.micro.blog/t/custom-domain-names/53),
* there are multiple ways to [export your content from the service](https://help.micro.blog/t/exporting-from-micro-blog/557), including to WordPress or with periodic backups to a GitHub repository,
* ultimately, the service is a managed [Hugo](https://gohugo.io) host. It's reasonably easy to migrate your content because of this.

Does this count as "ownership"? I'm pretty sure the answer is yes, but I still had some questions in the back of my mind. Why do I think Micro.blog allows more ownership than Twitter did? Twitter allowed you to export your data after all. Twitter also allowed you to pay (although only for extra features). Do I own my Micro.blog content *more* because it has additional export options and can be tied to a domain I control? What if I’m using a default `micro.blog` URL instead?

I don’t mean to pick on Micro.blog here. Again, I think the service is great. I just thought there was an interesting juxtaposition between it and something like Twitter. I also spent some time wondering about my current setup. I'd like to think that I own the content hosted on this website!

The content you’re reading now is served via [GitHub Pages](https://pages.github.com). It’s hosted on servers ultimately owned by Microsoft. I use the built-in [Jekyll publishing flow](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll) provided by GitHub to push content to the web. I pay for none of this. Is the main difference between posting here versus, say, Facebook that I have my domain pointed at the content? Heck, do I even “own” my domain? This question might seem silly, but it’s quite scary if you think about it too long. I’m placing a huge amount of trust in my domain registrar, from whom I essentially rent the most important piece of my online presence. If things went wrong here, a lot of things that are very important to me could break.

Obviously, I'm overthinking this. That said, I did find it helpful to break down what I thought "ownership" meant in the context of content on the web.

I think that "ownership" implies some level of control. I want to put my work somewhere where I have the most say in how it's displayed and used. Do I give up some control by using GitHub? Yes, because I have to agree to their [terms of service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) — but every host has some version of this. With GitHub (as with Micro.blog) I can control what the content looks like and how it's put into the world.

Any host could potentially remove or disrupt my content, but I feel more in control when I have the ability to easily move a site elsewhere. In the case of this site, it would be very easy for me to move to a service like [Netlify](https://www.netlify.com/), [Vercel](https://vercel.com/), or any number of other hosts. This is especially true because this site is all just HTML, and it can be generated locally by Jekyll.

When I used Twitter, part of the deal was that they could show ads next to anything I posted there. When using the first-party app, they also showed trending topics which I often found irritating. I didn’t think about it very much at the time, but it was clear that I was using *Twitter’s service*, and they were in control over how my content appeared to people. There’s nothing inherently wrong with a trade-off like this, and I got a lot of utility from the service. It was something that bothered me more and more in the latter years, though.

I’m not going to pretend that I’m writing any deep thoughts here, but it is something that keeps popping into my head. I love that there’s a push for people to create more content on the web, and one of the reasons often cited for publishing on your own website is to “own your content”. I think that’s a good thing, but I don’t want to take it as read. Thinking this through also helped me feel better about services like Mastodon and Bluesky gaining more traction. Both have data ownership as an core value, even if most people likely won’t take advantage of that.
