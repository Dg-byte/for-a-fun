try :
    import conf
except ImportError:
    pass


import discord
from discord.ext import commands
import img_handler as imhl
import os
import random
#
#
#
##Настраиваем расширенный доступ Intesnese
intense = discord.Intents.default()
intense.members = True
#
##Создаем подключение бота
#client = discord.Client(intents = intense)
#
#@client.event
#async def on_message(message):
#    # <Message 
#    # id=825338292228718603 
#    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#    # type=<MessageType.default: 0>
#    # author=<Member id=307383433036824579 name='dimaditriy' discriminator='1518' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>> 
#    # flags=<MessageFlags value=0>>
#
#    # Отправлятор является самим ботом 
#    if message.author == client.user:
#        return
#    # Отправлятор является другим ботом
#    if message.author.bot:
#        return
#
#
## Задаем канал для бота [Мой канал dmitri-bot]
#    if message.channel.id == 825309140045529108:
#        #Ответить пользователю в формате "Hello, {user.name} - your message {user.content}"
#        msg = None
#        # Отправляем сообщение в канал Channel используя метод send
#     
#        command = message.content.split(" ", maxsplit=1)
#        #1. /hello - просто сообщение
#        if message.content == "/hello":
#            msg = f'Hello, {message.author.name}. I am {client.user.name}'
#        
#        #2. /about_me - сообщение  пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")        
#        elif message.content == "/about_me":
#            msg = f'Your id is {message.author.id}'
#            if message.author.nick:
#                msg=f'and your nick is {message.author.nick}'
#
#                
#        #3. /repeat [] - повторить за пользователем 
#        elif command[0] == "/repeat":
#            msg = command[1]
#
#        #4. /get_member {id/name} - берём инфу по пользователю по типу about_me {если пусто != обрабатываем ошибку}
#        elif command[0] == "/get_member":
#            name = command[1]
#            for _, member in list(enumerate(message.author.guild.members)):
#                if name == member.name or name == member.id:
#                    msg = f'His username is {member.name} {f"and his nick is {member.nick}" if member.nick else ""} - {member.id}' 
#            if name == "":
#                msg = f'There is no one who has that id or name'
#
#        #5. /get_members  - список всех пользователй по "1. name {nick} id"       *(через webhook)
#        elif message.content == "/get_members":
#            msg = ""
#            if message.author.guild.name == "Bots":
#                for idx, member in list(enumerate(message.author.guild.members)):
#                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
#
#        #6. /get_сhannels  - список всех каналов категории Ботсы по "1. name id" *(через webhook)
#        elif message.content == "/get_channels":
#            msg = ""
#            if message.author.guild.name == "Bots":
#                for idx, channel in list(enumerate(message.author.guild.channels)):
#                    msg += f'{idx+1}. {channel.name} - {channel.id}\n'
#                    
       #7. /goto {id/name} - подключение бота в определенный канал (по умолчанию бот подключен в свой канал)          
#      elif command[0] == "/goto":
#          name_channel = command[1]
#          for _, channel in list(enumerate(message.author.guild.channels)):
#              if name_channel == channel.name or int(name_channel) == channel.id:
#                  message.channel.id = name_channel
#                  print("Ok")
#                  msg = f"Channel is changed"
#                  break
#              else: 
#                  msg = f"channel doesn't exist"
#                     
#
#        # Отправляем сообщение если оно есть
#        if msg != None:
#            await message.channel.send(msg)
#client.run(conf.bot_token)

#Объявляем бота с префиксом и расширенными правами
bot = commands.Bot(command_prefix = "!", intents = intense)

channel = 838001785620791328

whitelist = {
    #Сервер_id => {channel.id => "Server_name /     {channel_name}"}
    822806350886207538: {838001785620791328: "Bots / general"},
}

#@bot.command(name= "get_member")
#async def command_get_member(ctx, member: discord.Member=None):
#    msg = None
#    global channel
#    if ctx.channel.id == channel:
#
#        if member:
#            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'
#
#        if msg == None:
#            msg = "error"
#
#        await ctx.channel.send(msg)
#
#@bot.command(name = "hello")
#async def command_hello(ctx, *args): 
#    global channel
#    print(ctx)
#    if ctx.channel.id == channel:
#        msg= f'Hello to you! You said: "{" ".join(args)} "'
#        await ctx.channel.send(msg)
#
#@bot.command(name= "about_me")
#async def command_about_me(ctx, *args):
#    global channel
#    
#    if ctx.channel.id == channel:
#
#        msg = f'Your id is {ctx.author.id}'
#        if ctx.author.nick:
#            msg = f'and your nick is {ctx.author.nick}'
#    await ctx.channel.send(msg)
#
#@bot.command(name= "repeat")
#async def command_repeat(ctx, *args):
#    global channel
#    
#    if ctx.channel.id == channel:
#        if args != "":
#            msg = f'{" ".join(args)}'
#        else:
#            msg = f"You didn't write anything. Nothing to repeat"
#    await ctx.channel.send(msg)
#
#@bot.command(name = "get_members")
#async def command_get_members(ctx, *args):
#    global channel
#    if ctx.channel.id == channel:
#        msg = ""        
#        if ctx.author.guild.name == "Bots":
#            
#            for idx, member in list(enumerate(ctx.author.guild.members)):
#                print(idx)
#                msg += f'{idx+1}. {member.name} {f"[{member.nick}]" if member.nick else ""} - {member.id}\n'
#    await ctx.channel.send(msg)
#    msg = ""
#    if message.author.guild.name == "Bots":
#        for idx, member in list(enumerate(message.author.guild.members)):
#            msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'

#@bot.command(name= "mk")
#async def command_mk(ctx, fighter1: discord.Member=None, fighter2: discord.Member=None):
#    #msg = None
#    global channel
#    if ctx.channel.id == channel:
#        if fighter1 and fighter2:
#            msg = f'The first fighter is  {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""}, the second fighter is {fighter2.name} {f"({fighter2.nick})" if fighter2.nick else ""}\n Fight!'
#            #print(fighter1.avatar_url, fighter2.avatar_url)
#            #Передаем ответ разработчику
#            await imhl.vs_create(fighter1.avatar_url, fighter2.avatar_url)
#            await ctx.channel.send(msg)
#        elif fighter1:
#            msg = f'В бой вступают {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""} и {bot.user.name}'
#            await imhl.vs_create(fighter1.avatar_url, bot.user.avatar_url)
#            await ctx.channel.send(msg)
#            
#        #if msg == None:
#        #    msg = "error"
#        
#        await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))

# Декоратор - чекер @allowed_channel => True/False
def allowed_channel():
    async def predicate(ctx:commands.Context):
        # Если guild id и channel id валидны => True 
        if ctx.guild.id and whitelist:
            if ctx.channel.id in whitelist[ctx.guild.id].keys():
                return True

        #await ctx.channel.send("You're on wrong floor buddy")
        return False
    
    return commands.check(predicate)

"""
    Комманды бота
"""

@bot.command(name = "mka")
async def command_mka(ctx, fighter1:discord.Member=None, fighter2:discord.Member=None):
    if fighter1 and fighter2:
        await imhl.vs_create_animated(fighter1.avatar_url, fighter2.avatar_url)
        await ctx.channel.send(file =discrod.File(os.path.join("./img/result.gif")))
            
            
            
        #    msg = f'В бой вступают {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""} и {fighter2.name} {f"({fighter2.nick})" if fighter2.nick else ""}'
        #    await imhl.vs_create_animated(fighter1.avatar_url, fighter2.avatar_url)
        #elif fighter1:
        #    msg = f'В бой вступают {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""} и {bot.user.name}'
        #    await imhl.vs_create_animated(fighter1.avatar_url, bot.user.avatar_url)
        #else:
        #    msg = f'Введите имена противников используя @'
        #await ctx.channel.send(msg)
        #await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))


@bot.command(name = "join")
@allowed_channel()
async def vc_join(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel:                           
        await ctx.channel.send(msg = f"Подключаюсь к {voice_channel.name}")
        await voice_channel.connect()
#    if voice_channel and ctx.channel.id == channel:
#        if ctx.voice_client == None:
#            msg = f"Подключаюсь к {voice_channel.name}"
#            await ctx.channel.send(msg)
#            await voice_channel.connect()
#        else:
#            msg = f"Бот уже подключен к каналу"
#            await ctx.channel.send(msg)


@bot.command(name = "leave")
async def vc_leave(ctx):

    voice_channel = ctx.author.voice.channel

        if ctx.voice_client != None:
            await ctx.channel.send(f"Отключаюсь от {voice_channel.name}")
            await ctx.voice_client.disconnect()
        else:
            await ctx.channel.send(f"Бот уже отключен от канала")


@bot.command(name = "ost")
async def vc_ost(ctx):

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)  
    await ctx.channel.send(f"Fight!")
    await voice_client.play(discord.FFmpegPCMAudio(executable="./sounds/ffmpeg.exe", source="./sounds/mk.mp3"))



@bot.command(name = "fight")
@allowed_channel()
async def command_fight(ctx:commands.Context):
    fighter1 = None
    fighter2 = bot.user
    voice_channel = ctx.author.voice.channel
    
    if voice_channel:
        await vc_join(ctx)
        #Список активных пользователей 
        voice_members = voice_channel.members
        #Филььтруем пользователей, оставляя только людей 
        voice_members = [member for member in voice_members member.bot == False]        

        if len(voice_members) > 1:
            fighter1, fighter2 = [voice_members.pop(random.randint(0, len(voice_members)-1)), voice_members.pop(random.randint(0, len(voice_members)-1))]
        else:
            fighter1 = ctx.author
        
        
        await imhl.vs_create_animated(fighter1.avatar_url, fighter2.avatar_url)
        await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))

        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        await ctx.channel.send(f'Mortal Combat!')
        await voice_client.play (discord.FFmpegPCMAudio(source="./mp3/mk.mp3"))

    else:
        await ctx.channel.send("Зайдите в voice-канал")


    #if len(ctx.author.voice.channel.members) >= 2:
    #    fighter1 = ctx.author.voice.channel.members[0]
    #    fighter2 = ctx.author.voice.channel.members[1]
    #    msg = f'В бой вступают {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""} и {fighter2.name} {f"({fighter2.nick})" if fighter2.nick else ""}'
    #    
    #    await voice_channel.connect()
    #    await ctx.channel.send(msg)
    #    await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
    #    
    #    await voice_client.play(discord.FFmpegPCMAudio(executable="./sounds/ffmpeg.exe", source="./sounds/mk.mp3"))
    #if len(ctx.author.voice.channel.members) == 1:
    #    fighter1 = ctx.author.voice.channel.members[0]
    #    fighter2 = bot.user
    #    msg = f'В бой вступают {fighter1.name} {f"({fighter1.nick})" if fighter1.nick else ""} и {fighter2.name}'
    #    await imhl.vs_create_animated(fighter1.avatar_url, fighter2.avatar_url)
    #    await voice_channel.connect()
    #    
    #    
    #    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    #    await voice_client.play(discord.FFmpegPCMAudio(executable="./sounds/ffmpeg.exe", source="./sounds/mk.mp3"))








bot.run(os.environ["BOT_TOKEN"])