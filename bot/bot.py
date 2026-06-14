"""
Pork Pay Telegram Bot — Phase A (quotes only, NO money moves)
=============================================================
This bot connects to Telegram and fetches live swap *quotes* from Jupiter.
It does NOT hold a wallet and CANNOT spend money yet. That's on purpose —
we prove the whole pipeline works safely before any funds are involved.

Run it:
    pip install -r requirements.txt
    # put your BotFather token in a .env file (see .env.example)
    python bot.py
"""

import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Load settings from .env (never hard-code secrets in the file) ---
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PLATFORM_FEE_BPS = int(os.getenv("PLATFORM_FEE_BPS", "50"))  # 50 = 0.5%

# Jupiter's free, no-API-key endpoint. (Paid tier is api.jup.ag with a key.)
JUPITER_QUOTE_URL = "https://lite-api.jup.ag/swap/v1/quote"

# Tokens the bot understands for now. mint = on-chain address, decimals = how
# many decimal places the token uses. We'll auto-load the full list later.
TOKENS = {
    "SOL":  {"mint": "So11111111111111111111111111111111111111112", "decimals": 9},
    "USDC": {"mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "decimals": 6},
    "BONK": {"mint": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263", "decimals": 5},
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Runs when a user sends /start."""
    await update.message.reply_text(
        "🐷 *Welcome to Pork Pay*\n\n"
        "I can quote token swaps on Solana.\n\n"
        "Try:\n"
        "`/quote 1 SOL USDC`\n\n"
        f"Known tokens: {', '.join(TOKENS)}\n\n"
        "_Phase A: I only quote — I can't move money yet._",
        parse_mode="Markdown",
    )


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Runs when a user sends /quote <amount> <from> <to>."""
    args = context.args
    if len(args) != 3:
        await update.message.reply_text(
            "Usage: /quote <amount> <from> <to>\nExample: /quote 1 SOL USDC"
        )
        return

    amount_str, from_sym, to_sym = args[0], args[1].upper(), args[2].upper()

    try:
        amount = float(amount_str)
    except ValueError:
        await update.message.reply_text("The amount must be a number, e.g. 1.5")
        return

    if from_sym not in TOKENS or to_sym not in TOKENS:
        await update.message.reply_text(
            f"I only know these tokens right now: {', '.join(TOKENS)}"
        )
        return

    in_tok, out_tok = TOKENS[from_sym], TOKENS[to_sym]
    raw_amount = int(amount * 10 ** in_tok["decimals"])  # to atomic units

    params = {
        "inputMint": in_tok["mint"],
        "outputMint": out_tok["mint"],
        "amount": raw_amount,
        "slippageBps": 50,
        "platformFeeBps": PLATFORM_FEE_BPS,  # your fee, baked into the quote
    }

    try:
        resp = requests.get(JUPITER_QUOTE_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        await update.message.reply_text(f"Couldn't fetch a quote: {e}")
        return

    out_amount = int(data["outAmount"]) / 10 ** out_tok["decimals"]

    await update.message.reply_text(
        f"🐷 *Pork Pay quote*\n\n"
        f"{amount:g} {from_sym} ≈ *{out_amount:,.4f} {to_sym}*\n"
        f"_(includes your {PLATFORM_FEE_BPS / 100:.2f}% fee)_\n\n"
        f"Phase A: quote only — no swap executed.",
        parse_mode="Markdown",
    )


def main():
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit(
            "No TELEGRAM_BOT_TOKEN found. Copy .env.example to .env and paste "
            "your token from BotFather."
        )
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    print("Pork Pay bot is running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
