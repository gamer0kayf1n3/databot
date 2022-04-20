import lyricsgenius
import qrcode
from datetime import datetime
import keep_alive
import json as js
genius = lyricsgenius.Genius(
    'FGc7ioRYPnYTBca7hJiqWMiWAynW47skYdaHVC0vCIXwVDzpYaII5Up52VBR-ng7x')
now = datetime.now()
from PIL import Image{}
import os, re

print(os.getpid())
import random
import discord
import requests as rq
from discord.ext import commands
import requests as rq, json

import asyncio
import sys

print('Done with imports')

TOKEN = my_secret = os.environ['token']

bot = commands.Bot(command_prefix='!')
client = discord.Client()
guilds = str(len(bot.guilds))
print(guilds)
activity = discord.Game(
    name="Giving {guilds} Discord Servers Moderation and External Data")
#Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")
#Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
#Watching -> activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
bot = commands.Bot(command_prefix='!',
                   activity=activity,
                   status=discord.Status.invisible)
bot.remove_command('help')
evlist = []
f = open("js/questions.txt", "r")
for x in f:
    evlist.append(x)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='socialcreditadd')
async def addersub(ctx,user:discord.User,points):
    try:
      certifiedjudges = json.load(open("js/judges.json","r"))
      if ctx.message.author.id in certifiedjudges:
          socialcred = json.load(open("js/socialcred.json","r"))
          user = user.id
          socialcred['user'] += int(points)
          await ctx.send(f"Sent <@{user}> {int(points)}")
          json.dump(socialcred,open("socialcred.json", "w"))
      else:
          await ctx.send("I'm sorry, but you are not a certified judge. Ask my developer to add you in muser0943@gmail.com.")
    except Exception as e:
        await ctx.send(e)
isnsfw = False
@bot.command(pass_context=True)
async def toggle_nsfw(ctx):
  global isnsfw

  if isnsfw == False:
    await ctx.send("You asked for it...")
    isnsfw = True
  else:
    await ctx.send("You made the right choice, cultured soldier.")
    isnsfw = False
@bot.command(name='mysc')
async def addersub(ctx):
      try:
        socialcred = json.load(open("js/socialcred.json","r"))
        user = ctx.user.id
        val = socialcred[user]
        if val != None:
          await ctx.send(f"You have {val} social credit")
        else:
          socialcred[user] = 200
          await ctx.send(f"You have 200 social credit")
      except Exception as e:
          await ctx.send(e)

@bot.command(pass_context=True)
async def meme(ctx, *, topic=None):

    #random meme
    if topic == None:
        r = rq.get(('https://meme-api.herokuapp.com/gimme'),
                   allow_redirects=True)
        open(f'js/file.json', 'wb').write(r.content)
        with open('js/file.json') as f:
            meme_metadata = js.load(f)
        post = meme_metadata['postLink']  #
        subreddit = meme_metadata['subreddit']
        title = meme_metadata['title']  #
        photo_link = meme_metadata['url']  #
        nsfw = meme_metadata['nsfw']  #
        spoiler_ind = meme_metadata['spoiler']  #
        author = meme_metadata['author']  #
        ups = meme_metadata['ups']  #
        print(
            f'{"-"*20}\nDetails: \nPost Link: {post}\nSubreddit: {subreddit}\nTitle: {title}\nPhoto: {photo_link}\nNSFW? {nsfw}\nSpoiler? {spoiler_ind}\nAuthor: {author}\nUpvotes: {ups}'
        )
        if nsfw:
          if not isnsfw:

            await ctx.send('Post was marked NSFW, deleted')
          else:
                          embedVar = discord.Embed(
                  title=title,
                  description=
                  f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                  color=0x00ff00)
              embedVar.set_image(url=photo_link)
              embedVar.add_field(name='Post Link', value=post, inline=False)
              embedVar.add_field(name="Upvotes", value=ups, inline=False)
              await ctx.send(embed=embedVar)
  
      else:
          print(topic)
          r = rq.get((f'https://meme-api.herokuapp.com/gimme/{topic}'),
                     allow_redirects=True)
          open(f'js/file.json', 'wb').write(r.content)
          print(r.content)
          with open('js/file.json') as f:
              meme_metadata = js.load(f)
          post = meme_metadata['postLink']  #
          subreddit = meme_metadata['subreddit']
          title = meme_metadata['title']  #
          photo_link = meme_metadata['url']  #
          nsfw = meme_metadata['nsfw']  #
          spoiler_ind = meme_metadata['spoiler']  #
          author = meme_metadata['author']  #
          ups = meme_metadata['ups']  #
          if nsfw:
              if ctx.channel.is_nsfw():
                  print(
                      f'Details: \nPost Link: {post}\nSubreddit: {subreddit}\nTitle: {title}\nPhoto: {photo_link}\nNSFW? {nsfw}\nSpoiler? {spoiler_ind}\nAuthor: {author}\nUpvotes: {ups}'
                  )
                  embedVar = discord.Embed(
                      title=title,
                      description=
                      f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                      color=0x00ff00)
                  embedVar.set_image(url=photo_link)
                  embedVar.add_field(name='Post Link', value=post, inline=False)
                  embedVar.add_field(name="Upvotes", value=ups, inline=False)
                  await ctx.send(embed=embedVar)
              else:
                  await ctx.send('Post was marked NSFW, deleted')
          else:
              print(
                  f'Details: \nPost Link: {post}\nSubreddit: {subreddit}\nTitle: {title}\nPhoto: {photo_link}\nNSFW? {nsfw}\nSpoiler? {spoiler_ind}\nAuthor: {author}\nUpvotes: {ups}'
              )
              embedVar = discord.Embed(
                  title=title,
                  description=
                  f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                  color=0x00ff00)
              embedVar.set_image(url=photo_link)
              embedVar.add_field(name='Post Link', value=post, inline=False)
              embedVar.add_field(name="Upvotes", value=ups, inline=False)
              await ctx.send(embed=embedVar)
  


        else:
            embedVar = discord.Embed(
                title=title,
                description=
                f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                color=0x00ff00)
            embedVar.set_image(url=photo_link)
            embedVar.add_field(name='Post Link', value=post, inline=False)
            embedVar.add_field(name="Upvotes", value=ups, inline=False)
            await ctx.send(embed=embedVar)

    else:
        print(topic)
        r = rq.get((f'https://meme-api.herokuapp.com/gimme/{topic}'),
                   allow_redirects=True)
        open(f'js/file.json', 'wb').write(r.content)
        print(r.content)
        with open('js/file.json') as f:
            meme_metadata = js.load(f)
        post = meme_metadata['postLink']  #
        subreddit = meme_metadata['subreddit']
        title = meme_metadata['title']  #
        photo_link = meme_metadata['url']  #
        nsfw = meme_metadata['nsfw']  #
        spoiler_ind = meme_metadata['spoiler']  #
        author = meme_metadata['author']  #
        ups = meme_metadata['ups']  #
        if nsfw:
            if ctx.channel.is_nsfw():
                print(
                    f'Details: \nPost Link: {post}\nSubreddit: {subreddit}\nTitle: {title}\nPhoto: {photo_link}\nNSFW? {nsfw}\nSpoiler? {spoiler_ind}\nAuthor: {author}\nUpvotes: {ups}'
                )
                embedVar = discord.Embed(
                    title=title,
                    description=
                    f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                    color=0x00ff00)
                embedVar.set_image(url=photo_link)
                embedVar.add_field(name='Post Link', value=post, inline=False)
                embedVar.add_field(name="Upvotes", value=ups, inline=False)
                await ctx.send(embed=embedVar)
            else:
                await ctx.send('Post was marked NSFW, deleted')
        else:
            print(
                f'Details: \nPost Link: {post}\nSubreddit: {subreddit}\nTitle: {title}\nPhoto: {photo_link}\nNSFW? {nsfw}\nSpoiler? {spoiler_ind}\nAuthor: {author}\nUpvotes: {ups}'
            )
            embedVar = discord.Embed(
                title=title,
                description=
                f'from [{author}](https://www.reddit.com/user/{author})\nin [{subreddit}](https://reddit.com/r/{subreddit}) subreddit',
                color=0x00ff00)
            embedVar.set_image(url=photo_link)
            embedVar.add_field(name='Post Link', value=post, inline=False)
            embedVar.add_field(name="Upvotes", value=ups, inline=False)
            await ctx.send(embed=embedVar)


@bot.command(name='generateqr', aliases=['qr', 'qrcode', 'qrgen', 'genqr'])
async def qrgen(ctx, *, text):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('js/qrcode.png', format='png')
    file = discord.File("js/qrcode.png")
    await ctx.send(file=file)


@bot.command(name='generatecolor')
async def colorgen(ctx):

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    print(rgb)
    img = Image.new('RGB', (50, 50), color=rgb)
    img.save('js/pil_color.png')
    file = discord.File("js/pil_color.png")
    embedVar = discord.Embed(title=f"rgb({r}, {g}, {b})",
                             description="Color Generated",
                             color=0xffffff)
    embedVar.set_thumbnail(url="attachment://pil_color.png")
    embedVar.add_field(name="Hex",
                       value=f"{'%02x%02x%02x' % rgb}",
                       inline=True)
    embedVar.add_field(name="RGB", value=f"rgb({r}, {g}, {b})", inline=True)
    await ctx.send(file=file, embed=embedVar)


@bot.command(name='generatename')
async def namegen(ctx):
    r = rq.get(('https://randomuser.me/api/'), allow_redirects=True)
    open(f'js/name.json', 'wb').write(r.content)
    with open('js/name.json') as f:
        profile = js.load(f)
        gender = profile['results'][0]['gender']
        ########################
        name = profile['results'][0]['name']
        ########################
        title = name['title']
        first = name['first']
        last = name['last']
        if gender == 'male':
            color = 0x0000ff
        else:
            color = 0xff0000
        embedVar = discord.Embed(
            title=f"My name is...",
            description="credits to [randomuser.me!!!](https://randomuser.me/)",
            color=color,
            url="https://randomuser.me/")
        embedVar.add_field(name="Name",
                           value=f"**{title} {first} {last}**",
                           inline=True)
        embedVar.add_field(name="Gender", value=f"{gender}", inline=True)
        await ctx.send(embed=embedVar)


@bot.command(name='would_you_rather', aliases=['wyr', 'would', 'wyrather'])
async def wyr(ctx):
    randwyr = random.choice(evlist)
    await ctx.send(randwyr)


@bot.command(name='avatar')
async def get_user_icon(ctx, member: discord.Member):
    await ctx.send(member.avatar_url)


@bot.command(name='lyrics', aliases=['ly', 'lrc'])
async def get_lyrics(ctx, *, name):
    try:
        song_genius = genius.search_song(name)
        lyrics, genius_title, artist = song_genius.lyrics, song_genius.full_title, song_genius.artist
        if len(lyrics) > 4096:
            buffer = ""
            for x in lyrics:
                buffer = buffer + x
                if len(buffer) == 4096:
                    embed = discord.Embed(title=f"{genius_title}",
                                          description=buffer)
                    await ctx.send(embed=embed)
                    buffer = ""
        else:
            embed = discord.Embed(title=f"{genius_title}", description=lyrics)
            await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(e)


@bot.command(name='yt_video')
async def yt_search_vid(ctx, *, vidid):
    msg = await ctx.send('Please wait...')
    try:
        r = rq.get(
            f'https://www.googleapis.com/youtube/v3/videos?id={vidid}&part=snippet,statistics&key=AIzaSyAFaTn1mJcB910mDw98HacLEe6SNmA_ozQ',
            allow_redirects=True)
        data = js.loads(r.content.decode("utf-8"))
        jsondata = data['items'][0]
        snippet = jsondata['snippet']
        statistics = jsondata['statistics']

        thumb = snippet['thumbnails']['default']['url']

        published = snippet['publishedAt']
        channelId = snippet['channelId']
        title = snippet['title']
        description = snippet['description']
        channelTitle = snippet['channelTitle']
        if 'tags' not in snippet:
            tag_str = 'No tags set'
        else:
            tags = snippet['tags']
            tag_str = '\n'.join(tags)
        view = statistics['viewCount']
        like = statistics['likeCount']
        dis = statistics['dislikeCount']
        comment = statistics['commentCount']
        await msg.edit(content="compiling to embed")
        embed = discord.Embed(
            title=title, description=f"{channelTitle}'s video ({channelId})")
        embed.set_thumbnail(url=thumb)
        embed.add_field(name="Published", value=published, inline=False)
        embed.add_field(name="Views", value=view, inline=True)
        embed.add_field(name="Likes", value=like, inline=True)
        embed.add_field(name="Dislikes", value=dis, inline=True)
        embed.add_field(name="Comments", value=comment, inline=False)
        like = int(like)
        dis = int(dis)
        ratio = (like, dis)
        overall = like + dis
        percentage = like / overall
        int_percentage = round((percentage * 100), 2)
        one_digit = int(round((percentage * 100), -1) / 10)
        bar = str(one_digit * ':black_large_square:') + str(
            (10 - one_digit) * ':black_square_button:')
        output_field = f"({like}/{overall}) | {int_percentage}% | {bar}"
        embed.add_field(name="Likes vs Dislikes",
                        value=output_field,
                        inline=True)
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Description", description=description)
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Tags", description=tag_str)
        await ctx.send(embed=embed)
        await ctx.send(f'https://www.youtube.com/watch?v={vidid}')
    except Exception as e:
        await ctx.send(e)


@bot.command(name='yt_stats')
async def getid(ctx, *, userid):
    try:
        api_key = 'AIzaSyAFaTn1mJcB910mDw98HacLEe6SNmA_ozQ'
        r = rq.get(
            f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={userid}&key={api_key}',
            allow_redirects=True)
        data = js.loads(r.content.decode("utf-8"))
        userstats = data['items'][0]['statistics']
        viewers = userstats['viewCount']
        subcount = userstats["subscriberCount"]
        hidden = userstats["hiddenSubscriberCount"]
        vidcount = userstats["videoCount"]
        if hidden:
            embedVar = discord.Embed(title='YouTube Channel Statistics',
                                     description=f'',
                                     color=0x00ff00)
            embedVar.add_field(name='Channel Viewers',
                               value=f'{viewers}',
                               inline=True)
            embedVar.add_field(name='Channel Video Count',
                               value=f'{vidcount}',
                               inline=True)
            embedVar.add_field(name='Channel Subscribers',
                               value=f'Subscriber count is hidden.',
                               inline=True)
        else:
            embedVar = discord.Embed(title='YouTube Channel Statistics',
                                     description=f'',
                                     color=0x00ff00)
            embedVar.add_field(name='Channel Viewers',
                               value=f'{viewers}',
                               inline=True)
            embedVar.add_field(name='Channel Video Count',
                               value=f'{vidcount}',
                               inline=True)
            embedVar.add_field(name='Channel Subscribers',
                               value=f'{subcount}',
                               inline=True)
        await ctx.send(f'https://www.youtube.com/channel/{userid}')
        await ctx.send(embed=embedVar)
        r = rq.get((
            f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={userid}&part=snippet,id&order=date&maxResults=3'
        ),
                   allow_redirects=True)
        data = js.loads(r.content.decode("utf-8"))
        country = data['regionCode']
        latest = data['items'][0]
        twolatest = data['items'][1]
        threelatest = data['items'][2]
        ######
        onevidId = latest['id']['videoId']
        onevidDate = latest['snippet']['publishTime']
        onevidTitle = latest['snippet']['title']
        onevidDesc = latest['snippet']['description']
        twovidId = twolatest['id']['videoId']
        twovidDate = twolatest['snippet']['publishTime']
        twovidTitle = twolatest['snippet']['title']
        twovidDesc = twolatest['snippet']['description']
        threevidId = threelatest['id']['videoId']
        threevidDate = threelatest['snippet']['publishTime']
        threevidTitle = threelatest['snippet']['title']
        threevidDesc = threelatest['snippet']['description']
        embedVar = discord.Embed(title=f'{userid}\'s Latest Videos',
                                 description=f'Omitted to 3 results',
                                 color=0x00ff00)
        embedVar.add_field(
            name=f'{onevidTitle}',
            value=
            f'{onevidDate}\n{onevidDesc[:50]}\n{"https://www.youtube.com/watch?v="+onevidId}',
            inline=True)
        embedVar.add_field(
            name=f'{twovidTitle}',
            value=
            f'{twovidDate}\n{twovidDesc[:50]}\n{"https://www.youtube.com/watch?v="+twovidId}',
            inline=True)
        embedVar.add_field(
            name=f'{threevidTitle}',
            value=
            f'{threevidDate}\n{onevidDesc[:50]}\n{"https://www.youtube.com/watch?v="+threevidId}',
            inline=True)
        await ctx.send(embed=embedVar)

    except Exception as e:
        await ctx.send(e)


@bot.command(name='rb_user')
async def rbuser(ctx, *, username):
    try:
        message = await ctx.send(
            "Your command was received. Gathering API data...")
        r = rq.get(
            f'https://users.roblox.com/v1/users/search?keyword={username}&limit=10',
            allow_redirects=True)
        search = js.loads(r.content.decode("utf-8"))
        userid = search['data'][0]['id']  #
        displayName = search['data'][0]['displayName']  #
        r = rq.get(f'https://users.roblox.com/v1/users/{userid}',
                   allow_redirects=True)
        basic = js.loads(r.content.decode("utf-8"))
        desc = basic['description']  #
        date = basic['created'][:10]  #
        banned = basic['isBanned']  #
        r = rq.get(f'https://users.roblox.com/v1/users/{userid}/status',
                   allow_redirects=True)
        status = js.loads(r.content.decode("utf-8"))
        status = status['status']  #
        r = rq.get(
            f'https://accountinformation.roblox.com/v1/users/{userid}/roblox-badges',
            allow_redirects=True)
        badge = js.loads(r.content.decode("utf-8"))
        badges = []
        for x in badge:
            badges.append(x["name"])
        badges_str = ', '.join(badges)
        r = rq.get(
            f'https://badges.roblox.com/v1/users/{userid}/badges?limit=10&sortOrder=Asc',
            allow_redirects=True)
        gameb = js.loads(r.content.decode("utf-8"))['data']
        awards = []
        for x in gameb:
            name = x['name']
            desc2 = x['description']
            out = f'***{name}***\n{desc2}'
            awards.append(out)
        combined = '\n'.join(awards)
        r = rq.get(
            f'https://friends.roblox.com/v1/users/{userid}/friends/count',
            allow_redirects=True)
        jsfile = js.loads(r.content.decode("utf-8"))
        friends = jsfile['count']
        r = rq.get(
            f'https://friends.roblox.com/v1/users/{userid}/followers/count',
            allow_redirects=True)
        jsfile = js.loads(r.content.decode("utf-8"))
        followers = jsfile['count']
        r = rq.get(
            f'https://friends.roblox.com/v1/users/{userid}/followings/count',
            allow_redirects=True)
        jsfile = js.loads(r.content.decode("utf-8"))
        following = jsfile['count']
        print(desc)
        r = rq.get(
            f'https://games.roblox.com/v2/users/{userid}/favorite/games',
            allow_redirects=True)
        jsfile = js.loads(r.content.decode("utf-8"))
        fgames = jsfile['data']
        outarray = []
        for x in fgames:
            name = x['name']
            descfgame = x['description'][:100]
            ou = [f'***{name}***', descfgame]
            out = '\n'.join(ou)
            outarray.append(out)
            #print(x)
        favegame = '\n'.join(outarray).replace('[ Content Deleted ]',
                                               ':no_entry_sign: ')
        print(favegame)
        r = rq.get(f'https://groups.roblox.com/v1/users/{userid}/groups/roles',
                   allow_redirects=True)
        jsfile = js.loads(r.content.decode("utf-8"))['data'][:10]
        outputstring = ''
        outputarray = []
        for x in jsfile:
            outputstring = f'***{x["group"]["name"][:100]}***\n{x["group"]["description"][:50]}\nRole: {x["role"]["name"][:50]}'
            outputarray.append(outputstring)
        GroupsandRoles = '\n'.join(outputarray).replace(
            '[ Content Deleted ]', ':no_entry_sign: ')
        print(GroupsandRoles)
        aaaaembed = discord.Embed(title="First 10 Groups",
                                  description=GroupsandRoles[:2048])
        await message.edit(
            content=
            "API data from ROBLOX was gathered. Compiling to embed data...")
        embed = discord.Embed(title=f'{username}\'s profile')
        embed.set_thumbnail(
            url=
            f"https://www.roblox.com/bust-thumbnail/image?userId={userid}&width=420&height=420&format=png"
        )
        embed.add_field(name="Username", value=username, inline=True)
        embed.add_field(name="Display Name", value=displayName, inline=True)
        embed.add_field(name="Date Account Made", value=date, inline=True)
        embed.add_field(name="UserID", value=userid, inline=True)
        if desc == '':
            desc = 'None'
        print(f'Value is {desc}')
        embed.add_field(name="Description", value=desc, inline=False)
        embed.add_field(name="Banned", value=str(banned), inline=True)
        if status == '':
            embed.add_field(name="Status", value=status, inline=False)
        if badges_str == '':
            badges_str = 'None'
        embed.add_field(name="Roblox Badges", value=badges_str, inline=False)
        embed.add_field(name="Experience Badges", value=combined, inline=False)
        embed.add_field(name="Friends", value=friends, inline=True)
        embed.add_field(name="Followers", value=followers, inline=True)
        embed.add_field(name="Following", value=following, inline=True)
        print(f'Value is {desc}')
        await message.edit(content="Done.")
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Favorite Games", description=favegame)
        await ctx.send(embed=embed)
        await ctx.send(embed=aaaaembed)
        embed = discord.Embed(title="Avatar - Full Body")
        embed.set_image(
            url=
            f"http://www.roblox.com/Thumbs/Avatar.ashx?x=420&y=420&Format=Png&userId={userid}"
        )
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Avatar - Bust")
        embed.set_image(
            url=
            f"https://www.roblox.com/bust-thumbnail/image?userId={userid}&width=420&height=420&format=png"
        )
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Avatar - Full Face")
        embed.set_image(
            url=
            f"https://www.roblox.com/headshot-thumbnail/image?userId={userid}&width=420&height=420&format=png"
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(e)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        pass


@bot.command(name='help', aliases=['how', 'howto'])
async def help(ctx):
    embedVar = discord.Embed(title='Help',
                             description=f'List of commands',
                             color=0x00ff00)

    await ctx.send(embed=embedVar)


@bot.event
async def on_message(ctx):
    author = ctx.author.id
    user_msg = ctx.content
    user = ctx.author
    usern = ctx.author.name
    try:
        if ctx.author == bot.user:
            return
        """
        def detect_sauce(inw: str):
          unverified_sussy_codes = re.findall("\\d{5,6}",inw)
          to_be_returned = []
          for code in unverified_sussy_codes:
            if rq.get(f"https://nhentai.net/g/{code}").status_code == 200:
              to_be_returned.append(code)
          else:
            pass
          print(to_be_returned)
          return to_be_returned
        verified_sauce_list = detect_sauce(user_msg)
        if verified_sauce_list:
          await ctx.channel.send(f"Sauce was detected. <@{author}>'s message has been deleted.\n||The following sauce codes has been detected. `{verified_sauce_list}`||\nNote: to the following user: Oi, a bit sussy right there.",delete_after=10)"""
        if ctx.attachments is not None:
            for x in ctx.attachments:
                r = rq.post("https://api.deepai.org/api/nsfw-detector",
                            data={'image': x.url},
                            headers={
                                'api-key':
                                '045c9070-5d57-4c2c-b03e-2af33dfb3548'
                            })
                if r.json()['output']['nsfw_score'] >= 0.40:
                    await ctx.delete()
                else:
                    return
        print(x.url)
        print("is")
        print(r.json()['output']['nsfw_score'])
        msg_snipedel = await ctx.channel.send(
            "**(I am missing permission/my developer deliberately didn't add code/the developer was forced not)** to delete my own message, so please do not try to snipe the last image sent. Do not attempt to snipe it, or you are getting banned. NSFW Level of Last Image: "
            + str(r.json()['output']['nsfw_score']))
        await bot.process_commands(ctx)
    except Exception as e:
        print(e)
        await bot.process_commands(ctx)


keep_alive.keep_alive()
bot.run(TOKEN)
