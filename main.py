# Made By github.com/Lehoooo
from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands
import requests


TOKEN = open("token.txt", "r").read()
etherscanapikey = open("etherscantoken.txt", "r").read()

bot = commands.Bot(command_prefix='>')

cg = CoinGeckoAPI()

print("\n\n\n\nStarting Crypto Bot - Made By Leho\n\n\n\n")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Looking At Crypto Prices!"))
    print("Ready")


@bot.command()
async def price(ctx, arg, arg2):

    await ctx.send('Looking For Crypto ' + str(arg).capitalize() + '. Please Wait.', delete_after=1)

    coinsearch = cg.get_price(ids=arg, vs_currencies=arg2)
    usdprice = coinsearch[str(arg).lower()][str(arg2).lower()]

    print("Just Looked For " + str(arg) + ". Got response " + str(usdprice) + " USD")

    embed = discord.Embed(title="CryptoBot")
    embed.add_field(name=str(arg).capitalize() + " - " + str(arg2).upper(), value="$" + str(usdprice), inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    coinping = requests.get("http://api.coingecko.com/api/v3/ping").json()
    ping = coinping["gecko_says"]
    answer = "DOWN"

    if ping == "(V3) To the Moon!":
        answer = "UP"

    print("Coingecko API Is " + answer + ". Response was: " + str(ping))

    embed = discord.Embed(title="Ping Test")
    embed.add_field(name="CoinGecko", value="API Is " + str(answer), inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)

@bot.command()
async def gas(ctx):
    await ctx.send("Getting Ethereum Gas Price. Please Wait.", delete_after=1)
    gasprice = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + etherscanapikey).json()
    highprice = gasprice["result"]["FastGasPrice"]
    mediumprice = gasprice["result"]["ProposeGasPrice"]
    lowprice = gasprice["result"]["SafeGasPrice"]

    print("Just searched for gas prices. Result was " + highprice + ", " + mediumprice + ", " + lowprice)

    embed = discord.Embed(title="Ethereum Gas Price")
    embed.add_field(name="High", value=str(highprice) + " GWEI", inline=False)
    embed.add_field(name="Medium", value=str(mediumprice) + " GWEI", inline=False)
    embed.add_field(name="Low", value=str(lowprice) + " GWEI", inline=False)
    embed.set_footer(text="Made with ❤ by Leho")
    await ctx.send(embed=embed)

# @bot.command()
# async def trending(ctx):
#     trendingapi = requests.get("http://api.coingecko.com/api/v3/search/trending").json()
#
#     firstcoin = trendingapi["coins"]["item"]
#     print(firstcoin)

@bot.command()
async def info(ctx, arg):
    embed = discord.Embed(title="Info For Wallet " + str(arg))
    walletinfo = requests.get("https://blockchain.info/rawaddr/" + str(arg)).json()
    embed.add_field(name="Number Of Transactions", value=str(walletinfo["n_tx"]), inline=False)
    embed.add_field(name="Total Recieved", value=str(walletinfo["total_received"]), inline=False)
    embed.add_field(name="Total Sent", value=str(walletinfo["total_sent"]), inline=False)
    embed.add_field(name="Current Balance", value=str(walletinfo["final_balance"]), inline=False)
    await ctx.send(embed=embed)



@bot.command()
async def btcfee(ctx):
    embed = discord.Embed(title="Bitcoin Fee")
    btcfee_request = requests.get("https://bitcoinfees.earn.com/api/v1/fees/recommended").json()
    embed.add_field(name="Fastest", value=str(btcfee_request["fastestFee"]), inline=False)
    embed.add_field(name="Half Hour", value=str(btcfee_request["halfHourFee"]), inline=False)
    embed.add_field(name="Hour", value=str(btcfee_request["hourFee"]), inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)
