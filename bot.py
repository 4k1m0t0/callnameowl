#coding: utf-8
# call OpenJTalk for windows
import discord
import subprocess
import winsound
from datetime import datetime


def jtalk(t):
    # depend on your install folder 
    OPENJTALK_BINPATH = 'c:/open_jtalk/bin'
    OPENJTALK_DICPATH = 'c:/open_jtalk/dic'
    OPENJTALK_VOICEPATH = 'c:/open_jtalk/bin/mei_normal.htsvoice'
    #OPENJTALK_VOICEPATH = 'c:/open_jtalk/bin/cmu_us_arctic_slt.htsvoice'
    open_jtalk=[OPENJTALK_BINPATH + '/open_jtalk.exe']
    mech=['-x',OPENJTALK_DICPATH]
    htsvoice=['-m',OPENJTALK_VOICEPATH]
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)

    # convert text encoding from utf-8 to shitf-jis
    c.stdin.write(t.encode('shift-jis'))
    c.stdin.close()
    c.wait()

    # play wav audio file with winsound module
    winsound.PlaySound('open_jtalk.wav', winsound.SND_FILENAME)


def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    print(text)
    jtalk(text)

#if __name__ == '__main__':
#    say_datetime()

client = discord.Client()
#state = discord.VoiceState()
#voicechannel = discord.VoiceChannel(state, guild, data)

@client.event
async def on_ready():
    #if sakiniitara:
    #    client.get_channel(after.channel.id).connect()
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$come"):
        #channel = discord.utils.get(client.guild.voice_channels, name=message.author.name)
        print(message.author.id, client.user.id)
        #await client.join_voice_channel(message.author.voice_channel)
        #await client.get_channel(after.channel.id).connect()
        VID = 704352114389942377
        await client.get_channel(VID).connect()
        
    #if message.content.startswith("$bye")
        #await client.

CHANNEL_ID = 704352114389942376
GUILD_ID = 704352114389942373
guild = client.get_guild(GUILD_ID)
@client.event
async def on_voice_state_update(member, before, after):
    #print(member.id, client.user)
    if member.id==client.user:
        print(member.id, client.user)
        return
    channel = client.get_channel(CHANNEL_ID)
    #await channel.send(guild.voice_channels)
    print(after.channel!=None)
    if after.channel!=None:
        jtalk("{}が来たよ!".format(member.name))
        print(member.voice.channel)
        #await client.get_channel(after.channel.id).connect()

client.run("Nzc1NjgzMTE4NzQ0ODYyNzgw.X6p5Mw.IVn7d2k_c00zTYKr8IB0fBbxYto")

