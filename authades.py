import os
import random
import discord
from discord.ext import commands

print("🔧 Iniciando bot no Azure...")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def teste(ctx, nro: str = None, dificuldade: str = None):
    try:
        n = int(nro) if nro else 1
        if not 1 <= n <= 9:
            raise ValueError
    except ValueError:
        return await ctx.send("Use `!teste N [D]` onde N e D são inteiros de 1 a 9.")
    
    diff = None
    if dificuldade:
        try:
            diff = int(dificuldade)
        except ValueError:
            return await ctx.send("Use `!teste N [D]` onde N e D são inteiros de 1 a 9.")
        
    rolls = [random.randint(1, 10) for _ in range(n)]
    hits = [max(d - 7, 0) for d in rolls]
    total = sum(hits)

    # cria a sequência global de ícones
    if diff is None:
        seq = ['🔹'] * total
    else:
        seq = ['🔹' if i < diff else '🔸' for i in range(total)]
        
    parts = []
    idx = 0
    for d, h in zip(rolls, hits):
        icons = seq[idx:idx+h]
        idx += h
        parts.append(f"{d} {''.join(icons)}".strip())
    await ctx.send(", ".join(parts))

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
