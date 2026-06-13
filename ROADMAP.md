# Pork Pay — Roadmap to Real Payments 🐷💳

Goal: someone walks into a store and pays with "Pork Pay" through Apple Wallet,
your liquidity/flow makes it work, and you earn fees. Here's the honest path
from the swap widget you have today to that.

## The one hard truth up front

You **cannot** add "Pork Pay" to Apple Wallet as a payment method by yourself.
Apple Wallet payment cards must be real Visa/Mastercard cards issued through a
licensed bank/program. So "pay at a store via Apple Wallet" = **issue a real
card** through a partner who already holds the licenses. You build the brand and
app on top; they handle the regulated plumbing (KYC, money transmission, Apple
Pay provisioning). Trying to be the licensed entity yourself = lawyers, millions
in capital, and years. Don't. Ride a partner.

Also: settle in a **stablecoin (USDC)**, not a volatile memecoin. Nobody — not a
store, not a card network — wants the price to move 30% between tap and
settlement. PORK can be the brand; USDC is the money underneath.

---

## Phase 0 — Swap widget + fees ✅ (you're here)
Real revenue, zero licensing, no custody. Proves the "earn on flow" model.

## Phase 1 — Crypto → fiat off-ramp (next, still no license needed)
Add a "Cash Out" button that opens a licensed off-ramp so users sell crypto to
their bank/card. **You earn a referral cut; the partner is the licensed one.**
- Providers to research: **MoonPay**, **Transak**, **Stripe Crypto**,
  **Coinbase Onramp/Offramp**.
- Same business model as the swap fee — you're paid for sending them flow.
- Buildable by you, solo, soon.

## Phase 2 — Apple Wallet *pass* (brand presence, buildable solo)
Ship an actual **Apple Wallet pass** using Apple **PassKit** — a branded "Pork
Pay" card that shows balance/rewards/loyalty. It can't make Visa payments by
itself, but it plants your brand in Wallet and is a real, shippable thing one
developer can build. Great for marketing + getting an Apple Developer account
($99/yr) in place, which you'll need later anyway.

## Phase 3 — The real "Pork Pay Card" (the Apple Wallet payment dream)
Partner with a **Card-as-a-Service (CaaS)** provider that issues crypto-backed
Visa/Mastercards which auto-convert crypto→fiat at the point of sale and add to
Apple Wallet via Apple Pay. They own the licensing, KYC, and Apple provisioning.
You own the brand, the app, and a share of the interchange/fees.
- Providers to research: **Rain (rain.xyz)**, **Baanx**, **Immersve**,
  **Gnosis Pay**, **Lithic**, **Marqeta**, **Stripe Issuing**.
- This is the phase where "tap your phone at the register" becomes real.
- This is a real-company step: contracts, compliance review, probably an entity
  (LLC) and a lawyer. That's the cost of it being legitimate.

---

## What earns you money at each phase
| Phase | Revenue source | Who holds the license |
|-------|----------------|-----------------------|
| 0 | Swap referral fee | nobody needed |
| 1 | Off-ramp referral fee | the off-ramp partner |
| 2 | (brand/marketing, no $ yet) | n/a |
| 3 | Card interchange + fees | the CaaS/bank partner |

## First three things to actually do
1. Ship Phase 0 (set your fee account, get one real swap through it).
2. Spend an hour reading **Rain**, **Baanx**, and **Immersve** docs — see what a
   small partner actually has to bring to the table.
3. Get an **Apple Developer account** so Phase 2 is unblocked when you want it.

> Reality check, since you asked me to be honest: Phases 0–2 you can do yourself.
> Phase 3 is a business, not a script. That's not a reason to skip it — it's a
> reason to earn your way to it through 0–2 first.
