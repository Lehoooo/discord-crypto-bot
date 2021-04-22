# Made By github.com/Lehoooo
from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands
import requests


TOKEN = open("token.txt", "r").read()

bot = commands.Bot(command_prefix='>')

cg = CoinGeckoAPI()

print("Starting Crypto Bot - Made By Leho")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Looking At Crypto Prices!"))
    print("Ready")


@bot.command()
async def price(ctx, arg):
    await ctx.send('looking for crypto ' + str(arg) + '. Please wait.')

    coinsearch = cg.get_price(ids=arg, vs_currencies='usd')
    usdprice = coinsearch[arg]["usd"]

    print("just looked for " + str(arg) + ". Got response " + str(usdprice) + " USD")
    # await ctx.send("crypto " + str(arg) + " is currently at price " + str(usdprice) + " USD")

    embed = discord.Embed(title="CryptoBot")
    embed.add_field(name=str(arg).capitalize(), value="$" + str(usdprice), inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    coinping = requests.get("http://api.coingecko.com/api/v3/ping").json()
    ping = coinping["gecko_says"]
    answer = "DOWN"

    if ping == "(V3) To the Moon!":
        answer = "UP"

    # await ctx.send("Coingecko API Is " + answer) // send answer without embed
    print("Coingecko API Is " + answer + ". Response was: " + str(ping))

    embed = discord.Embed(title="Ping Test")
    embed.add_field(name="CoinGecko", value="API Is " + str(answer), inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)

@bot.command()
async def gas(ctx):
    gasprice = requests.get(" https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=ZEJC89JQVC5EXBSTDEFF4QTYJI3BTRR4Z8").json()
    highprice = gasprice["result"]["FastGasPrice"]
    mediumprice = gasprice["result"]["ProposeGasPrice"]
    lowprice = gasprice["result"]["SafeGasPrice"]

    print("Just searched for gas prices. Result was " + highprice + ", " + mediumprice + ", " + lowprice)

    embed = discord.Embed(title="Etherium Gas Fee")
    embed.add_field(name="High", value=str(highprice) + " GWEI", inline=False)
    embed.add_field(name="Medium", value=str(mediumprice) + " GWEI", inline=False)
    embed.add_field(name="Low", value=str(lowprice) + " GWEI", inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)

@bot.command()
async def trending(ctx):
    trendingapi = requests.get("http://api.coingecko.com/api/v3/search/trending").json()

    firstcoin = trendingapi["coins"]["item"]
    print(firstcoin)

bot.run(TOKEN)
