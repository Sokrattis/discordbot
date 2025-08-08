import os
import random
import discord
from discord.ext import commands

print("Iniciando bot no Azure...")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def teste(ctx, nro: str = None, dificuldade: str = None):
    try:
        n = int(nro) if nro else 1
    except ValueError:
        return await ctx.send("Use `!teste N [D]` onde N e D são inteiros.")
    if not 1 <= n <= 9:
        return await ctx.send("N deve ser um inteiro de 1 a 9.")
    diff = None
    if dificuldade:
        try:
            diff = int(dificuldade)
        except ValueError:
            return await ctx.send("Use `!teste N [D]` onde N e D são inteiros.")

    rolls = [random.randint(1, 10) for _ in range(n)]
    parts = []
    for d in rolls:
        hits = max(d - 7, 0)
        icons = ['🔅'] * hits
        if diff is not None and hits > diff:
            # troca os ícones que ultrapassam a dificuldade
            for i in range(diff, hits):
                icons[i] = '🔆'
        parts.append(f"{d} {''.join(icons)}".strip())

    await ctx.send(", ".join(parts))

token = os.getenv("DISCORD_TOKEN")
bot.run(token)