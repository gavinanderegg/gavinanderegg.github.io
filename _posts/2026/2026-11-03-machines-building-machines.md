---
title: >
    Machines building machines
date: 2026-11-03 13:37:29 -0400
---

Yesterday, a group of MIT researchers released an article titled "[Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)". The piece describes a set of experiments which convincingly show OpenAI's latest Astra model is able to understand and successfully alter raw weight data. Wowzers!

It's a rough analogy, but an LLM's weights are sort of like its brain. A set of weights is a large pile of numbers generated during training, and an LLM's output is derived by running input through the weights using some [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) and a bit of randomization. While the steps to generate weights are well understood, the weights themselves are extremely opaque. There's ongoing work to try and [explain how weights work](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence), but researchers currently have a limited understanding of what these numbers do.

Based on this, I was quite surprised to learn that LLMs are able to act on raw weight data — even if it's still just in limited cases. It's unclear if OpenAI's model was trained on weight data. Even if it was, I still find these results surprising. The article shows the model accurately predicting what a never-before-seen set of weights was built to do, fixing another model by updating its weights, and creating new sets of weights that performed simple tasks. I would not have guessed any of that would be possible a couple of days ago.

While still just a proof of concept, I find it slightly unnerving. The whole "weights as a black box" thing has always felt a bit sketchy to me, even when I was working with much simpler machine learning models. Now these experiments hint at a future where LLMs could be self-improving in ways that aren't human-verifiable. Machines building machines, and we can only hope that they're not doing anything weird. I don't know if this strategy is scalable, but I'd guess that it's something more people will be exploring very soon.

More and more often these days, I wish we were living in less interesting times.