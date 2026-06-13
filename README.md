# Pork Pay 🐷

A branded swap widget. People swap tokens through it on Solana; you earn a fee
on every swap. Built on the Jupiter plugin (it does the routing + liquidity
sourcing; you collect a referral fee).

## What this is (and isn't, yet)

- ✅ **Right now:** a working swap tool that earns you fees. This is real.
- 🔜 **Later (the real "Pork Pay"):** crypto → fiat → Apple Wallet. That's a
  much bigger, regulated build. See `ROADMAP.md`.

## Run it (3 steps)

1. **Get your fee account.** Go to https://referral.jup.ag/dashboard, connect a
   Solana wallet (e.g. Phantom), and create a referral account. Copy its
   address. While there, "initialize" fee accounts for the tokens you want to
   be paid in (start with USDC and SOL).
2. **Edit `config.js`.** Paste your referral account address; set your fee.
3. **Open the site.** Easiest way that actually works with wallets:
   ```powershell
   # from this folder, in PowerShell:
   python -m http.server 5173
   ```
   Then open http://localhost:5173 in your browser.

   > Don't just double-click `index.html` — wallet connections often need a real
   > `http://` server, which is what the command above gives you.

## Files

| File         | What it's for                                  |
|--------------|------------------------------------------------|
| `index.html` | The page + branding + where the widget mounts  |
| `config.js`  | Your wallet & fee — the only thing you edit     |
| `ROADMAP.md` | The path toward real fiat/Apple Wallet payments |

## How the fee works

Jupiter finds the best swap route across Solana liquidity. When the swap
executes, your `referralFee` (in basis points) is skimmed to your
`referralAccount`. You don't custody anyone's funds — you're paid for routing.
