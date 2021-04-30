# Made By github.com/Lehoooo
from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands
from discord.ext import tasks
import requests

TOKEN = open("token.txt", "r").read()

bot = commands.Bot(command_prefix='>')

cg = CoinGeckoAPI()

bot.remove_command('help')

print("\n\n\n\nStarting Crypto Bot - Made By Leho\n\n\n\n")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Looking At CryptoCurrency Prices! | cryptobot.party"))
    print("Ready")


@bot.command()
async def price(ctx, arg, arg2='USD'):  # arg is crypto, arg2 is the currency
    await ctx.send('Looking For Crypto ' + str(arg).capitalize() + '. Please Wait.', delete_after=1)

    coinsearch = cg.get_price(ids=arg, vs_currencies=arg2)
    usdprice = coinsearch[str(arg).lower()][str(arg2).lower()]

    print("Just Looked For " + str(arg) + ". Got response " + str(usdprice) + " " + str(arg2))

    embed = discord.Embed(title=str(arg).capitalize() + " - " + str(arg2).upper())
    embed.add_field(name="Price:", value="```" + "$" + str(usdprice) + " " + str(arg2).upper() + "```", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    coinping = requests.get("http://api.coingecko.com/api/v3/ping").json()
    pingresult = coinping["gecko_says"]
    answer = "DOWN"

    if pingresult == "(V3) To the Moon!":
        answer = "UP"

    print("Coingecko API Is " + answer + ". Response was: " + str(pingresult))

    embed = discord.Embed(title="Ping Test")
    embed.add_field(name="CoinGecko", value="API Is " + str(answer), inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def gas(ctx):
    await ctx.send("Getting Ethereum Gas Price. Please Wait.", delete_after=1)
    gasprice = requests.get("https://api.blockcypher.com/v1/eth/main").json()
    highprice = gasprice["high_gas_price"] / 1000000000
    mediumprice = gasprice["medium_gas_price"] / 1000000000
    lowprice = gasprice["low_gas_price"] / 1000000000

    print("Just searched for gas prices. Result was " + str(highprice) + ", " + str(mediumprice) + ", " + str(lowprice))

    embed = discord.Embed(title="Ethereum Gas Price")
    embed.add_field(name="High", value="```" + str(highprice) + " GWEI" + "```", inline=False)
    embed.add_field(name="Medium", value="```" + str(mediumprice) + " GWEI" + "```", inline=False)
    embed.add_field(name="Low", value="```" + str(lowprice) + " GWEI" + "```", inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def btcfee(ctx):  # Check btc price
    embed = discord.Embed(title="Bitcoin Fee")
    btcfee_request = requests.get("https://bitcoinfees.earn.com/api/v1/fees/recommended").json()
    embed.add_field(name="Fastest", value=str(btcfee_request["fastestFee"]), inline=False)
    embed.add_field(name="Half Hour", value=str(btcfee_request["halfHourFee"]), inline=False)
    embed.add_field(name="Hour", value=str(btcfee_request["hourFee"]), inline=False)
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="CryptoBot Help")
    embed.add_field(name="Price - Checks A Cryptocurrency Price", value="```>price <coin> <currency (default is "
                                                                        "USD)>```", inline=False)  # price command
    embed.add_field(name="Ping - Checks If The Coingecko API Is Responding", value="```>ping```",
                    inline=False)  # ping command
    embed.add_field(name="Gas - Checks The Current Ethereum Gas Price", value="```>gas```", inline=False)  # gas command
    embed.add_field(name="Btcfee - Checks The Current Bitcoin Transfer fee", value="```>btcfee```",
                    inline=False)  # btc fee command
    embed.add_field(name="Ltcfee - Checks The Current Litecoin Transfer fee", value="```>ltcfee```",
                    inline=False)  # ltc fee command
    embed.add_field(name="Info - Shows Info About A Crypto Wallet - Supported Wallet Types: btc, doge, eth, ltc",
                    value="```>info <wallet type> <wallet address>```", inline=False)  # wallet info command
    embed.add_field(name="Invite - Sends The Bot Invite Link", value="```>invite```", inline=False)
    embed.add_field(name="", value="", inline=False)

    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
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
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
    embed = discord.Embed()
    embed.add_field(name="Invite Link",
                    value="[Click Here!](https://discord.com/api/oauth2/authorize?client_id=828195695126380564&permissions=67611712&scope=bot)")
    embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx, arg, arg2):  # arg is the wallet type (btc, ltc or eth) and arg2 is the wallet addy
    argcapatalise = str(arg.upper())

    if argcapatalise == "LTC" or argcapatalise == "LITECOIN":
        await ctx.send("Please Wait, Getting LTC Wallet Info", delete_after=1)
        embed = discord.Embed(title="Litecoin Wallet Info")
        btcwalletinfo = requests.get("https://api.blockcypher.com/v1/ltc/main/addrs/" + str(arg2) + "/balance").json()

        totalrecieved = btcwalletinfo["total_received"] / 100000000
        totalsent = btcwalletinfo["total_sent"] / 100000000
        currentbalance = btcwalletinfo["final_balance"] / 100000000

        embed.add_field(name="Public Wallet Address", value="```" + str(arg2) + "```", inline=False)
        embed.add_field(name="Number Of Transactions", value=str(btcwalletinfo["final_n_tx"]), inline=False)
        embed.add_field(name="Total Recieved", value=str(totalrecieved) + " LTC", inline=False)
        embed.add_field(name="Total Sent", value=str(totalsent) + " LTC", inline=False)
        embed.add_field(name="Current Balance", value=str(currentbalance) + " LTC", inline=False)
        embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
        await ctx.send(embed=embed)


    elif argcapatalise == "BTC" or argcapatalise == "BITCOIN":
        await ctx.send("Please Wait, Getting BTC Wallet Info", delete_after=1)
        embed = discord.Embed(title="Bitcoin Wallet Info")
        btcwalletinfo = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + str(arg2) + "/balance").json()

        totalrecieved = btcwalletinfo["total_received"] / 100000000
        totalsent = btcwalletinfo["total_sent"] / 100000000
        currentbalance = btcwalletinfo["final_balance"] / 100000000

        embed.add_field(name="Public Wallet Address", value="```" + str(arg2) + "```", inline=False)
        embed.add_field(name="Number Of Transactions", value=str(btcwalletinfo["final_n_tx"]), inline=False)
        embed.add_field(name="Total Recieved", value=str(totalrecieved) + " BTC", inline=False)
        embed.add_field(name="Total Sent", value=str(totalsent) + " BTC", inline=False)
        embed.add_field(name="Current Balance", value=str(currentbalance) + " BTC", inline=False)
        embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
        await ctx.send(embed=embed)

    elif argcapatalise == "ETH" or argcapatalise == "ETHEREUM":
        await ctx.send("Please Wait, Getting ETH Wallet Info", delete_after=1)
        ethwalletinfo = requests.get("https://api.blockcypher.com/v1/eth/main/addrs/" + str(arg2) + "/balance").json()
        embed = discord.Embed(title="Ethereum Wallet Info")

        ethtotalrecieved = ethwalletinfo["total_received"] / 1000000000000000000
        ethtotalsent = ethwalletinfo["total_sent"] / 1000000000000000000
        ethcurrentbalance = ethwalletinfo["final_balance"] / 1000000000000000000

        embed.add_field(name="Public Wallet Address", value="```" + str(arg2) + "```", inline=False)
        embed.add_field(name="Number Of Transactions", value=str(ethwalletinfo["final_n_tx"]), inline=False)
        embed.add_field(name="Total Recieved", value=str(ethtotalrecieved) + " ETH", inline=False)
        embed.add_field(name="Total Sent", value=str(ethtotalsent) + " ETH", inline=False)
        embed.add_field(name="Current Balance", value=str(ethcurrentbalance) + " ETH", inline=False)
        embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
        await ctx.send(embed=embed)

    elif argcapatalise == "DOGECOIN" or argcapatalise == "DOGE":
        await ctx.send("Please Wait, Getting Dogecoin Wallet Info", delete_after=1)
        embed = discord.Embed(title="Dogecoin Wallet Info")
        btcwalletinfo = requests.get("https://api.blockcypher.com/v1/doge/main/addrs/" + str(arg2) + "/balance").json()

        totalrecieved = btcwalletinfo["total_received"] / 100000000
        totalsent = btcwalletinfo["total_sent"] / 100000000
        currentbalance = btcwalletinfo["final_balance"] / 100000000

        embed.add_field(name="Public Wallet Address", value="```" + str(arg2) + "```", inline=False)
        embed.add_field(name="Number Of Transactions", value=str(btcwalletinfo["final_n_tx"]), inline=False)
        embed.add_field(name="Total Recieved", value=str(totalrecieved) + " DOGE", inline=False)
        embed.add_field(name="Total Sent", value=str(totalsent) + " DOGE", inline=False)
        embed.add_field(name="Current Balance", value=str(currentbalance) + " DOGE", inline=False)
        embed.set_footer(text="CryptoBot | Made with ❤ by Leho | cryptobot.party")
        await ctx.send(embed=embed)

    else:
        await ctx.send("Sorry, " + str(argcapatalise) + " is not supported, Or you might have spelt it wrong :)",
                       delete_after=2)


@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(color=0xfb0021)
    embed.add_field(name="Error", value="There was an error excecuting the command.", inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)
