





from riotwatcher import LolWatcher
import discord
key = "apikey"
watcher = LolWatcher(key)

def printStats(summonerName):
    summoner = watcher.summoner.by_name("na1", summonerName)
    summonerID = summoner['id']
    stats = watcher.league.by_summoner("na1", summonerID)
    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']
    wins = int(stats[0]['wins'])
    losses = int(stats[0]['losses'])
    winrate = int(wins / (wins + losses) * 100)
    userData = (
        summonerName
        + " is currently ranked in "
        + str(tier)
        + ", "
        + str(rank)
        + " with "
        + str(lp)
        + " LP and a "
        + str(winrate)
        + "% winrate."
    )
    return userData
  
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$stats'):
        summonerName = message.content.split("$stats ", 1)[1]
        userData = printStats(summonerName)
        await message.channel.send(userData)
client.run("discordtoken")







