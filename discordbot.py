import discord
import praw

client = discord.Client()
reddit = praw.Reddit(
    client_id='client id here',
    client_secret='client secret here',
    user_agent='user agent here',
    username='username here'
    password='password here'
)

@client.event
async def on_ready():

    for post in reddit.subreddit('popular').top('week'):
        channel = discord.utils.get(client.get_all_channels(), name='general')
        await channel.send(post.title + ': ' + post.url)

client.run('bot token here')
