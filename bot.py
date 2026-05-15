from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import random

TOKEN = os.getenv("TOKEN")

player = {
    "season": 1,
    "goals": 0,
    "assists": 0,
    "coins": 100,
    "rating": 60,
    "club": "Arsenal"
}

clubs = ["Real Madrid", "Man City", "Barcelona", "PSG", "Bayern"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Career Bot Ready!\nUse /spin")

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player["season"] += 1
    player["goals"] = random.randint(0, 40)
    player["assists"] = random.randint(0, 20)

    performance = player["goals"] * 2 + player["assists"]
    player["coins"] += performance

    if performance > 50:
        player["rating"] += 3

    offer = ""
    if player["rating"] >= 65:
        offer = f"\n🔁 Transfer offer: {random.choice(clubs)}"

    await update.message.reply_text(
        f"🎰 Season {player['season']}\n"
        f"Goals: {player['goals']}\n"
        f"Assists: {player['assists']}\n"
        f"Coins: {player['coins']}\n"
        f"Rating: {player['rating']}"
        + offer
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spin", spin))

    app.run_polling()

main()
