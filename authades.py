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
    # valida N
    try:
        n = int(nro) if nro else 1
        if not 1 <= n <= 9:
            raise ValueError
    except ValueError:
        return await ctx.send("Use `!teste N [D]` onde N é número de dados (1–9) e D é dificuldade (1–9).")
    
    # valida D
    diff = None
    if dificuldade:
        try:
            diff = int(dificuldade)
            if not 1 <= diff <= 9:
                raise ValueError
        except ValueError:
            return await ctx.send("Dificuldade deve ser um inteiro de 1 a 9.")
        
    # rola dados e calcula hits
    rolls = [random.randint(1, 10) for _ in range(n)]
    hits = [max(d - 7, 0) for d in rolls]
    total_hits = sum(hits)

    # ajusta diff para não passar do total de hits
    if diff is not None:
        diff = min(diff, total_hits)

    # monta a sequência única de ícones
    seq = ['🔹' if diff is None or i < diff else '🔸' for i in range(total_hits)]

    # distribui de volta por dado
    parts, idx = [], 0
    for d, h in zip(rolls, hits):
        icons = ''.join(seq[idx:idx + h])
        idx += h
        parts.append(f"{d} {icons}".strip())
    await ctx.send(", ".join(parts))

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
