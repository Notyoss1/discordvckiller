# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'とーくん'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # Botの起動とDiscordサーバーへの接続
    #ぼいちゃready
    if message.content == "p!ready":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()

        await message.channel.send("ぼいちゃ砲　準備OKです！")
        print("vc ready")

    elif message.content == "p!end":
        if message.guild.voice_client is None:
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")
        print("vc ended")
        return
    
    #だんだす
    elif message.content == "p!dandas-fire":
        if message.guild.voice_client is None:
            return
        message.guild.voice_client.play(discord.FFmpegPCMAudio("dandas.mp3"))
        await message.channel.send("ダンダス砲　発射!")
        print("dandas started")

    #めぐみん
    elif message.content == "p!megmin-fire":
        if message.guild.voice_client is None:
            return
        message.guild.voice_client.play(discord.FFmpegPCMAudio("megmin.mp3"))
        await message.channel.send("めぐみん砲　発射!")
        print("megmin started")


client.run(TOKEN)