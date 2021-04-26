# Made By github.com/Lehoooo
from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands
import requests

TOKEN = open("token.txt", "r").read()
etherscanapikey = open("etherscantoken.txt", "r").read()

bot = commands.Bot(command_prefix='>')

cg = CoinGeckoAPI()

bot.remove_command('help')

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

    embed = discord.Embed(title=str(arg).capitalize() + " - " + str(arg2).upper())
    embed.add_field(name="Price:", value="```" + "$" + str(usdprice) + " " + str(arg2).upper() + "```", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
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
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def gas(ctx):
    await ctx.send("Getting Ethereum Gas Price. Please Wait.", delete_after=1)
    gasprice = requests.get(
        "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + etherscanapikey).json()
    highprice = gasprice["result"]["FastGasPrice"]
    mediumprice = gasprice["result"]["ProposeGasPrice"]
    lowprice = gasprice["result"]["SafeGasPrice"]

    print("Just searched for gas prices. Result was " + highprice + ", " + mediumprice + ", " + lowprice)

    embed = discord.Embed(title="Ethereum Gas Price")
    embed.add_field(name="High", value=str(highprice) + " GWEI", inline=False)
    embed.add_field(name="Medium", value=str(mediumprice) + " GWEI", inline=False)
    embed.add_field(name="Low", value=str(lowprice) + " GWEI", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


# @bot.command()
# async def trending(ctx):
#     trendingapi = requests.get("http://api.coingecko.com/api/v3/search/trending").json()
#
#     firstcoin = trendingapi["coins"]["item"]
#     print(firstcoin)

@bot.command()
async def btcwallet(ctx, arg):
    await ctx.send("Please Wait, Getting Wallet Info", delete_after=1)
    embed = discord.Embed(title="Info For Wallet " + str(arg))
    walletinfo = requests.get("https://blockchain.info/rawaddr/" + str(arg)).json()
    embed.add_field(name="Number Of Transactions", value=str(walletinfo["n_tx"]), inline=False)
    embed.add_field(name="Total Recieved", value=walletinfo["total_received"] / 100000000, inline=False)
    embed.add_field(name="Total Sent", value=str(walletinfo["total_sent"]), inline=False)
    embed.add_field(name="Current Balance", value=walletinfo["final_balance"] / 100000000, inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def btcfee(ctx):  # Check btc price
    embed = discord.Embed(title="Bitcoin Fee")
    btcfee_request = requests.get("https://bitcoinfees.earn.com/api/v1/fees/recommended").json()
    embed.add_field(name="Fastest", value=str(btcfee_request["fastestFee"]), inline=False)
    embed.add_field(name="Half Hour", value=str(btcfee_request["halfHourFee"]), inline=False)
    embed.add_field(name="Hour", value=str(btcfee_request["hourFee"]), inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="CryptoBot Help")
    embed.add_field(name="Price - Checks A Cryptocurrency Price", value="```>price <coin> <currency>```",
                    inline=False)  # price command
    embed.add_field(name="Ping - Checks if the coingecko API is responding", value="```>ping```",
                    inline=False)  # ping command
    embed.add_field(name="Gas - Checks the current Ethereum gas price", value="```>gas```", inline=False)  # gas command
    embed.add_field(name="Btcwallet - Shows you info about a Bitcoin wallet",
                    value="```>btcwallet <btc wallet address>```", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


@bot.command()
async def ltcfee(ctx):
    await ctx.send("Getting Litecoin Fee, Please Wait.", delete_after=1)
    embed = discord.Embed(title="Litecoin Sending Fee")
    ltcfeereq = requests.get("https://api.blockcypher.com/v1/ltc/main").json()

    highfee = ltcfeereq["high_fee_per_kb"]
    mediumfee = ltcfeereq["medium_fee_per_kb"]
    lowfee = ltcfeereq["low_fee_per_kb"]

    embed.add_field(name="High", value="```" + str(highfee / 100000000) + " LTC/KB" + "```", inline=False)
    embed.add_field(name="Medium", value="```" + str(mediumfee / 100000000) + " LTC/KB" + "```", inline=False)
    embed.add_field(name="Low", value="```" + str(lowfee / 100000000) + " LTC/KB" + "```", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho")
    await ctx.send(embed=embed)


async def info(ctx, arg, arg2):  # arg is the wallet type (btc or ltc) and arg2 is the wallet addy
    argcapatalise = str(arg.capitalize())

    if argcapatalise == "LTC":
        await ctx.send("Searching for ltc wallet", delete_after=1)

    elif argcapatalise == "BTC":
        await ctx.send("Searching for btc wallet", delete_after=1)

    elif argcapatalise == "ETH":
        await ctx.send("Searching for eth wallet", delete_after=1)


bot.run(TOKEN)
