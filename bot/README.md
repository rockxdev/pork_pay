# Pork Pay — Telegram Bot 🐷🤖

A Telegram front-end for Pork Pay. People swap through chat; you earn a fee.
Same model as BONKbot / Trojan / Maestro.

## Where we are: Phase A (safe)

This version **only fetches quotes**. It has no wallet and cannot move money.
We get the whole pipeline working with zero funds at risk, *then* add real
swaps (Phase B) with your wallet.

## Setup (5 steps)

1. **Create the bot on Telegram.**
   - Open Telegram, search for **@BotFather**.
   - Send `/newbot`, follow the prompts, pick a name + username.
   - BotFather gives you a **token** (looks like `123456:ABC-DEF...`). Copy it.

2. **Make your .env file.** In this `bot/` folder, copy `.env.example` to `.env`
   and paste your token:
   ```powershell
   Copy-Item .env.example .env
   ```
   Then open `.env` and replace the placeholder with your real token.

3. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run it:**
   ```powershell
   python bot.py
   ```

5. **Test it.** In Telegram, open your bot and send:
   ```
   /start
   /quote 1 SOL USDC
   ```
   It should reply with a live quote. 🎉

## Phase plan

- **A (now):** bot talks + quotes. No money. ✅ buildable today.
- **B (next):** real swaps using *your* wallet + your fee account.
- **C (later, careful):** multi-user. This means custodying other people's
  keys — a serious security undertaking. Not until B is rock-solid.

## Safety

- Your `.env` (with the bot token) is gitignored — never commit it.
- Never put a wallet seed phrase or private key in any file in this repo.
