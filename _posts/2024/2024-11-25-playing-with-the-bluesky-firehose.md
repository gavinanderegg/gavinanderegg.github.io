---
title: >
    Playing with the Bluesky firehose
date: 2024-11-25 17:59:56 -0400
---

Over the weekend I started playing around with [Jetstream](https://docs.bsky.app/blog/jetstream), a project from the Bluesky team to deliver a JSON based firehose of [atproto data](https://atproto.com/guides/overview). Here's an overview of the simple project I built with that data.

I was inspired by [a post from Simon Willison](https://simonwillison.net/2024/Nov/20/bluesky-websocket-firehose/) where he showed off a tool for viewing raw Jetstream content. I was surprised to learn that Jetstream is offered as a [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) that doesn't require any authentication.

It looked simple, so I decided to build quick demo. There are already [tools like Firesky](https://firesky.tv/) for streaming the full firehose. Firesky has ways to filter the incoming data, but they're a bit hidden. I thought it might be nice to have something where filtering is core to the UI.

[You can play with my Bluesky Filter app here](https://anderegg.ca/bsky-filter/).

To use it, first enter some text in the input field at the top and hit the "go" button. This will start a connection to Jetstream, and new firehose content will start streaming in. Any content where the text in the input field matches a part of the post content will be displayed. The "posts encountered" number shows the total number of posts coming in from Jetstream. Newer posts will show up on top, and older posts will be pushed down. You can use the "stop" button to close the connection, and the "clear" button to remove all the entries added so far. One potential use for this would be to follow a hashtag or a topic like "Apple". You can also click the post text to go to that post on Bluesky, or click the username to see that user's profile.

I will note that this was very easy to build, and much of the effort was building out the UI. Because Jetstream pushes JSON content over an open connection, the app doesn't require a server component — everything is client-side. All of this is much easier than parsing binary CBOR data and CAR files, which are the native formats for transmitting Bluesky data in the atproto stack. [Here are more details around how and why Jetstream was created](https://jazco.dev/2024/09/24/jetstream/).

What's most interesting to me is how easy it is to slurp down all data from Bluesky. While digging into this project, I also came across a project where the creator shows off [posts that have been deleted in realtime](https://bsky.app/profile/bad-example.com/post/3l53o5atwio2t).

As I've written before, [I think Bluesky is radically open](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won#:~:text=as%20of%20today.-,Radically%20open,-I%20think%20some) and I worry that people might not clock what this means. For my purposes, I would never do anything on Bluesky that I wouldn't also advertise on the open web — including liking posts. I also fully expect that all Bluesky content is getting scraped for things like training LLMs.

Anyway, this was a fun little thing to build. If you're interested, you can [check out the GitHub repo here](https://github.com/gavinanderegg/bsky-filter).