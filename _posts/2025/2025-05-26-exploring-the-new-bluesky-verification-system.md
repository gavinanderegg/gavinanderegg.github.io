---
title: >
    Exploring the new Bluesky verification system
date: 2025-05-26 16:15:10 -0300
---

On April 21st, the Bluesky team announced a [new account verification system](https://bsky.social/about/blog/04-21-2025-verification). In my opinion, one of the best bits about Bluesky was the ability to [verify yourself using a domain name](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial). This new system goes a step further, and I was curious about how it worked. This lead to me building a [quick-and-dirty verifier listing tool](https://anderegg.ca/bsky-verifier/).

First off, why bother with a new verification system? One big reason is that domain names are complex, and you have to be a pretty big nerd to [get everything set up correctly](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial). It also means that, if you're not a huge nerd, it's possible for someone to register a domain that looks legit and then start impersonating you. [Ernie Smith at Tedium wrote a great post that digs into this issue](https://tedium.co/2025/04/21/bluesky-blue-checkmark-revival-analysis/).

The new system allows the Bluesky team to verify people in two ways. The first is a "verified account", which similar to how things worked in the old days on Twitter. These are individual accounts that Bluesky sees as notable and supplies with a check mark. The second is the idea of "trusted verifiers". These are accounts that Bluesky blesses with the ability to verify other accounts. One example is WIRED, which has supplied verified status to its employees and others on the platform.

If you go to [WIRED's Bluesky profile](https://bsky.app/profile/wired.com), you'll see that they have a "scalloped" checkmark beside their name. Click that checkmark, and you'll see a short explanation of the system. To date, WIRED has verified 69 Bluesky accounts, including Zoë Schiffer's. If you head to [Schiffer's profile page](https://bsky.app/profile/zoeschiffer.bsky.social) and click the round checkmark there, you'll see that she was verified by WIRED on April 21st.

I was a bit torn about this system at first, but I've landed on thinking it's a good step beyond domain-based verification. Because the Bluesky team is distributing the ability for other people to verify accounts, this feels a bit better than how Twitter handled things. Even if a trusted verifier ever goes nuts and starts verifying nonsense accounts, you'll at least be able to see who the verifier is and judge things for yourself.

When this system was announced originally, the Bluesky team was only hand-picking accounts to verify. Starting on May 22nd, [there is now a form you can fill out to request verification](https://bsky.social/about/blog/04-21-2025-verification#:~:text=How%20to%20Get%20Verified%20on%20Bluesky). Many accounts have taken advantage of this, including [a](https://bsky.app/profile/en.ottawa.ca) [number](https://bsky.app/profile/cityofcalgary.bsky.social) [of](https://bsky.app/profile/govnl.bsky.social) [local](https://bsky.app/profile/peigov.bsky.social) [government](https://bsky.app/profile/cityofhamilton.bsky.social) [accounts](https://bsky.app/profile/toronto.ca), some ([like my city's](https://bsky.app/profile/hfxgov.bsky.social)) without any content yet.

---

Shortly after this system was announced, [I started digging into it](https://bsky.app/profile/gavin.anderegg.ca/post/3lnq36cpuj22z). The main question I wanted to answer was: how can I list the accounts that a trusted verifier has verified? It turned out to be fairly simple, and I started writing a quick tool to gather this data. After getting out from under some recent client work, I was able to get this into a sharable state.

> [You can try out my verifier info tool here.](http://anderegg.ca/bsky-verifier/)

> [The source is also available on GitHub.](https://github.com/gavinanderegg/bsky-verifier)

To use the tool, enter the account handle of a trusted verifier and click "go". The tool will grab the newest 100 verified accounts from that verifier. If there are more than that, you can click the "Load More" button at the bottom of the page to grab the next 100 until you have them all. If you query an account which isn't a trusted verifier, you'll see an error message.

Because of how open Bluesky and the [AT Protocol](https://atproto.com/) are, this all happens in the browser without the need for any servers or authentication. Here's how it works under the covers.

First, the tool reaches out to the API to turn the username you've entered into a [DID:PLC](https://atproto.com/specs/did). It does so by querying the [`app.bsky.actor.getProfile`](https://docs.bsky.app/docs/api/app-bsky-actor-get-profile) endpoint with the username as the `actor` parameter. From that response, it grabs the `did` value for the user. With that, it then queries the [DID PLC Directory](https://plc.directory/) to find out what [PDS](https://atproto.com/guides/glossary#pds-personal-data-server) the user is hosted on. It then reaches out to that PDS and requests the [`app.bsky.graph.verification`](https://atp.readthedocs.io/en/latest/atproto/atproto_client.models.app.bsky.graph.verification.html) collection. If that user is a trusted verifier, the request returns a set of accounts that the user has verified. It also returns a `cursor` string, which can be used to iterate over the collection.

It's still wild to me how straightforward it was to grab this data. It's another example of how [Bluesky is radically open](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won#:~:text=as%20of%20today.-,Radically%20open,-I%20think%20some).