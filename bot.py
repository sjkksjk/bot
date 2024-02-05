import discord
import random
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
def gen_pass(lans_pass):
        symbol= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        stroka = ""
        for i in range(lans_pass):
            stroka+=random.choice(symbol)
        return stroka
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$random'):
        stroka = gen_pass(10)
        await message.channel.send(stroka)
    else:
        await message.channel.send(message.content)

client.run("MTIwMTUxNjQ5NzgxNDY4MzY0OQ.G24_ZP.mFok2rS7vKa2zQPSh1bcvy2h7L9x3CqUHusdIk")