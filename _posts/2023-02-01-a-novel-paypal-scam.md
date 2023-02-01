---
title: A Novel PayPal Scam
date: 2023-02-01 12:52:17 -0400
---

This morning I got an interesting scam email. It might not be a new scam, but it was the first time I'd seen it.

<img src="https://anderegg.s3.amazonaws.com/paypal-scam.png" width="454" height="502" style="margin: auto; border: 4px solid #556;" alt="An image of an invoice email with a payment button. Includes the following body text: Seller note to customer: Dear Customer, You sent a payment of $479.00 USD to Coinbase Corporation. If you did not make this payment or to cancel this transaction , please call our Help Desk number: PHONE NUMBER REDACTED. Cancellation after 24 hours from this email won't be valid for a refund. Have a great day! PayPal® Help Desk PHONE NUMBER REDACTED">

Inspecting the source, the email looked like it actually came from PayPal (SPF, DKIM, and DMARC all passed). The button also linked to what looked like a legitimate PayPal URL (starting with "*https://www.paypal.com/invoice*"). It took a second to dawn on me that it was a legit email, and I had just been sent a random "invoice" from a scammer.

[PayPal has documentation on how to send an such an invoice](https://www.paypal.com/us/cshelp/article/how-do-i-create-and-send-an-invoice-help319), which also currently includes a link at the top [mentioning this sort of scam](https://www.paypal.com/us/cshelp/article/Help201#Invoice).

There was also a note in the footer of the email:

> **Don't know this seller?**<br>
> You can safely ignore this invoice if you're not buying anything from this seller. PayPal won't ask you to call or send texts to phone numbers in an invoice. We don't ask for your credentials or auto-debit money from your account against any invoices. Contact us if you're still not sure.

I started out thinking this was a very sophisticated phishing attempt, but it turned out to be quite low-tech. Still, I think it's rather clever, poor punctuation on the "seller note" aside. The note about cancellations only being valid within 24 hours is an anxiety-heightening touch.

It also seems like a convenience feature that PayPal should consider locking down. I immediately assumed this was some form of scam, and was only interested in the technical details. It seems far too easy to pull off, and I worry that others might fall for it.
