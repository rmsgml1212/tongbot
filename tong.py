#import from
import discord
import asyncio
import pytz
import datetime
import time
import random

from discord.ext import commands
from datetime import date, datetime
from discord import colour
from discord import channel
from discord import emoji
from discord import message
from discord import user
from discord import embeds


#변수
client = discord.Client()
msg = message
token = "ODY2MTk2NjA4NzUyNDE4ODM2.YPPCdA.bgu8V8fnPf5ogmCcDD2rWhHpaa8"
inging = "온라인..." #봇의 상태(3컷)
inginging = "통큰봇은 지금 온라인입니다." #봇의 상태(상황)


#레디
@client.event
async def on_ready(): 
  async def message(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)

  print("[ Bot Start ] \n-- 봇이 시작되었습니다 -- \n봇 제작자 : 근짱#1339\n")
  print(("""[ Bot Info ]\n[1] Bot Name : {} \n[2] Bot Discord ID : {}""").format(client.user.name, client.user.id))
  await message(['!도움말로 도움말 열기','버전 7.0'])


#도움말 안내
@client.event
async def on_message(msg):
    if msg.content == "!도움말":
        embed = discord.Embed(title=":question: 도움말", description="통큰봇 도움말", color=0x62c1cc)
        embed.add_field(name="!대화", value="통큰봇과 대화하기 입니다.", inline=False)
        embed.add_field(name="!놀이 도움말", value="통큰봇과 노는 방법을 알려드립니다.", inline=False)
        embed.add_field(name="!출첵 도움말", value="출석체크를 방법을 알려줍니다.", inline=False)
        embed.add_field(name="!뽑기 시리즈", value="뽑기 시리즈를 알려드립니다.", inline=False)
        embed.add_field(name="!봇 상태", value="현재 봇 상태를 확인할수있습니다.", inline=False)
        embed.add_field(name="!ID", value="자신의 ID를 쉽게 알수있습니다.", inline=False)
        embed.add_field(name="!봇 초대", value="통큰봇을 서버에 초대를 할수있습니다.", inline=False)
        embed.add_field(name="!봇 사용시 주의사항", value="봇 사용시 주의사항을 알려드립니다.", inline=False)
        embed.add_field(name="!자주 묻는 질문", value="봇에 관해 자주 묻는 질문들을 모았습니다.", inline=False)
        embed.add_field(name="!신기능", value="새로운 명령어를 알려드립니다.", inline=False)
        embed.add_field(name="!검색도움말", value="유튜브,페이스북,네이버카페,네이버블로그,네이버통합검색을 해줍니다.", inline=False)
        embed.add_field(name="!청소", value="정한 숫자만큼 청소를 합니다.", inline=False)
        embed.add_field(name="!따라해", value="통큰봇이 따라합니다.", inline=False)
        embed.add_field(name="접두사", value="`!`", inline=False)
        embed.add_field(name="제작자", value="근짱#1339", inline=False)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == "!봇 사용시 주의사항":
        embed = discord.Embed(title=":no_entry: 봇 사용시 주의사항", description="봇 사용시 주의사항입니다. 꼭 지켜주세요", color=0x62c1cc)
        embed.add_field(name="1.", value="봇을 사용할때는 도배를 하지 않습니다.", inline=False)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == "!자주 묻는 질문":
        embed = discord.Embed(title=":question: 자주 묻는 질문", description="사람들이 자주 묻는 질문을 모아 봤습니다!..", color=0x62c1cc)
        embed.add_field(name="Q. 통큰봇은 무슨시간 무슨 날짜에 켜지나요?", value="통큰봇은 월화수목금토일 모두 열리고 사정이 있으면 안내를 드립니다 \n 그리고 시간은 빠르면 10~12시 늦어도 5시~6시입니다.", inline=True)
        embed.add_field(name="Q. 봇 업데이트안내는 어디서 확인하나요?", value="곧 한국 디스코드 서버에 생길 예정일것이니 그곳에서 서버링크 타서 \n 들어오시면 됩니다.", inline=True)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send("할 말", embed=embed) 

    if msg.content == "!신기능":
        embed = discord.Embed(title=":exclamation:신기능", description="따끈따끈한 통큰봇의 신기능", color=0x62c1cc)
        embed.add_field(name="!검색도움말", value="`8월20일`", inline=False)
        embed.add_field(name="!청소", value="`8월21일`", inline=False)
        embed.add_field(name="!따라해", value="`8월21일`", inline=False)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == "!검색도움말":
        embed = discord.Embed(title=":question: 검색 도움말", description="통큰봇 검색도움말", color=0x62c1cc)
        embed.add_field(name="!유튜브검색", value="YOUTUBE검색", inline=False)
        embed.add_field(name="!페이스북검색", value="페이스북검색\n(페이스북은 작동이 되지않을수있습니다.)", inline=False)
        embed.add_field(name="!네이버카페검색", value="네이버카페검색", inline=False)
        embed.add_field(name="!네이버블로그검색", value="블로그검색", inline=False)
        embed.add_field(name="!네이버검색", value="네이버통합검색", inline=False)
        embed.add_field(name="도움", value="_저브#4398")
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == "!출첵 도움말":
        embed = discord.Embed(title=":question: 출석체크 도움말" , description="출석체크하는 방법을 알려드립니다.", color=0x62c1cc)
        embed.add_field(name="!출석체크", value="출석체크를 도와줍니다.", inline=True)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)
    

    if msg.content == "!대화":
        embed = discord.Embed(title=":question: 대화 도움말", description="통큰봇 대화하기 도움말", color=0x62c1cc)
        embed.add_field(name="ㅋㅋ", value="`웃어줌`", inline=True)
        embed.add_field(name="너 못생김", value="대답해줌.", inline=True)
        embed.add_field(name="너 잘생김", value="대답해줌.", inline=True)
        embed.add_field(name="나 잘생김", value="대답해줌.", inline=True)
        embed.add_field(name="너 사랑해", value="대답해줌.", inline=True)
        embed.add_field(name="아니", value="대답해줌.", inline=True)
        embed.add_field(name="뭐해", value="대답해줌.", inline=True)
        embed.add_field(name="뭐함", value="대답해줌.", inline=True)
        embed.add_field(name="뭐해", value="대답해줌.", inline=True)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "!뽑기 시리즈":
        embed = discord.Embed(title=":tv: 뽑기 시리즈", description="통큰봇 뽑기 시리즈", color=0x62c1cc)
        embed.add_field(name="!여친 생길 가능성", value="여자친구 생길 가능성을 알려줍니다. (10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%)", inline=True)
        embed.add_field(name="!뽑기", value="(꽝, 당첨)", inline=True)
        embed.add_field(name="!오늘의 운세", value="오늘의 운세를 알려드립니다 (10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%)", inline=True)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)





    if msg.content == "!놀이 도움말":
        embed = discord.Embed(title="놀이 도움말", description="봇과 노는 방법을 알려드립니다.", color=0x62c1cc)
        embed.add_field(name="안녕하세요", value="이건 노는건 아니지만...", inline=False)
        embed.add_field(name="!뽑기", value="꽝이나 당첨으로 답해줍니다.(랜덤으로)", inline=False)
        embed.add_field(name="!싫어하는 모든 것", value="봇이 싫어하는것을 알려드립니다.", inline=False)
        embed.add_field(name="!(가위, 바위, 보)", value="가위 바위 보중 1개를 쓰면 가위바위보를 해줌.", inline=False)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)
        

#주고 답하고:
    if msg.content == "안녕하세요":
        embed = discord.Embed(colour=discord.Colour.red(), title="안녕하세요~^^", description='안녕하세요~^^')
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)
    

    if msg.content == "!반응 코로나":
        embed = discord.Embed(colur=discord.Color.blue(), title="코로나 바이러스 시러시러")
        await msg.channel.send(""f"{msg.author.mention}")
        message = await msg.channel.send(embed=embed)
        await message.add_reaction('🦠')


    if msg.content == "ㅋ":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('ㅋㅋㅋㅋㅋ(근데 왜 웃고 있지)')


    if msg.content == "!너 못생김":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('너도')


    if msg.content == "!너 잘생김":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('내가 좀 잘생기긴 했지~')
        await asyncio.sleep(2)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('훗~')


    if msg.content == "!나 잘생김":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('왜 그래')
        await asyncio.sleep(2)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('무서워')


    if msg.content == "!너 사랑해":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('감사')


    if msg.content == "!아니":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('뭐가 아닐까~')


    if msg.content == "!뭐해":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('코딩 당하는 중')


    if msg.content == "!뭐함":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('코딩 당하는 중')


    if msg.content == "죽어":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('그냥 제발 나를 죽여줘..')


    if msg.content == "!출석체크":
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('출석체크가 완료되었습니다.')

       
    if msg.content == "!멍청이":
        embed = discord.Embed(colour=discord.Colour.red(), title="멍청이라는 말은 나빠요!", description='나쁜사람')
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "!봇 상태":
        embed = discord.Embed(colour=discord.Colour.red(), title=inging, description=inginging)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "통큰":
        ran = random.choice([1, 2, 3, 4])
        if ran == 1:
            d = "뭐"
        if ran == 2:
            d = "왜"
        if ran == 3:
            d = "왜 불러"
        if ran == 4:
            d = "부르지 마"
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(d)


    if msg.content == "!로블록스하자":
        ran = random.choice([1, 2, 3, 4])
        if ran == 1:
            d = "싫어"
        if ran == 2:
            d = "왜"
        if ran == 3:
            d = "그래 근데 너 내 계정 없잖아 ㅋㅋㄹㅃㅃ"
        if ran == 4:
            d = "로블 안함"
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(d)


    if msg.content == "!배그하자":
        ran = random.choice([1, 2, 3, 4])
        if ran == 1:
            d = "싫어"
        if ran == 2:
            d = "그래 대신 내 계정 너가 찾아서 친추 보내"
        if ran == 3:
            d = "싫은데 내가 왜 얼마줄건데 100만원 주면 하지~~"
        if ran == 4:
            d = "..."
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(d)


#게임
    if msg.content == "!뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        embed = discord.Embed(colour=discord.Colour.red(), title=d)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == '!타이머 5':
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send('타이머를 시작합니다(5초)')
        await asyncio.sleep(1)
        await msg.channel.send(""f"{msg.author.mention}이(가)보낸 메세지 1초지남 ")
        await asyncio.sleep(1)
        await msg.channel.send(""f"{msg.author.mention}이(가)보낸 메세지 2초지남 ")
        await asyncio.sleep(1)
        await msg.channel.send(""f"{msg.author.mention}이(가)보낸 메세지 3초지남 ")
        await asyncio.sleep(1)
        await msg.channel.send(""f"{msg.author.mention}이(가)보낸 메세지 4초지남 ")
        await asyncio.sleep(1)
        await msg.channel.send(""f"{msg.author.mention}이(가)보낸 메세지 5초지남 ")
        await msg.channel.send(""f"{msg.author.mention}님이 시작한5초가 지났습니다")

    if msg.content == "!여친 생길 가능성":
        await msg.channel.send(""f"{msg.author.mention}")
        ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        if ran == 10:
            d = "당신은 여친이 생길겁니다."
        if ran == 9:
            d = "당신은 여친이 생길 가능성은 90%입니다."
        if ran == 8:
            d = "당신은 여친이 생길 가능성은 80%입니다."
        if ran == 7:
            d = "당신은 여친이 생길 가능성은 70%입니다."
        if ran == 6:
            d = "당신은 여친이 생길 가능성은 60%입니다."
        if ran == 5:
            d = "당신은 여친이 생길 가능성은 50%입니다."
        if ran == 4:
            d = "당신은 여친이 생길 가능성은 40%입니다."
        if ran == 3:
            d = "당신은 여친이 생길 가능성은 30%입니다."
        if ran == 2:
            d = "당신은 여친이 생길 가능성은 20%입니다."
        if ran == 1:
            d = "당신은 여친이 생길 가능성은 10%입니다."
        if ran == 0:
            d = "당신은 여친이 생길 가능성은 00%입니다."
        embed = discord.Embed(colour=discord.Colour.red(), title=d)
        await msg.channel.send(embed=embed)


    if msg.content == "!오늘의 운세":
        await msg.channel.send(""f"{msg.author.mention}")
        ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        if ran == 10:
            d = "`당신은 운좋은 가능성 100%`"
        if ran == 9:
            d = "`당신은 운좋은 가능성 90%`"
        if ran == 8:
            d = "`당신은 운좋은 가능성 80%`"
        if ran == 7:
            d = "`당신은 운좋은 가능성 70%`"
        if ran == 6:
            d = "`당신은 운좋은 가능성 60%`"
        if ran == 5:
            d = "`당신은 운좋은 가능성 50%`"
        if ran == 4:
            d = "`당신은 운좋은 가능성 40%`"
        if ran == 3:
            d = "`당신은 운좋은 가능성 30%`"
        if ran == 2:
            d = "`당신은 운좋은 가능성 20%`"
        if ran == 1:
            d = "`당신은 운좋은 가능성 10%`"
        if ran == 0:
            d = "`당신은 운좋은 가능성 00%`"
        await msg.channel.send(d)


    if msg.content == "!보":
        ran = random.choice([1, 2, 3])
        if ran == 1:
            d = "가위 (내가 이겼어!!인간은 역시 못해!!)"
        if ran == 2:
            d = "바위 (내가 졌군..인간..잘해..)"
        if ran == 3:
            d = "보 (흠..비겼군)"
        embed = discord.Embed(colour=discord.Colour.dark_magenta(), title=d)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "!가위":
        ran = random.choice([1, 2, 3])
        if ran == 1:
            d = "바위 (내가 이겼어!!인간은 역시 못해!!)"
        if ran == 2:
            d = "보 (내가 졌군..인간..잘해..)"
        if ran == 3:
            d = "가위 (흠..비겼군)"
        embed = discord.Embed(colour=discord.Colour.dark_magenta(), title=d)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "!바위":
        ran = random.choice([1, 2, 3])
        if ran == 1:
            d = "보 (내가 이겼어!!인간은 역시 못해!!)"
        if ran == 2:
            d = "가위 (내가 졌군..인간..잘해..)"
        if ran == 3:
            d = "바위 (흠..비겼군) "
        embed = discord.Embed(colour=discord.Colour.dark_magenta(), title=d)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


    if msg.content == "!제작자":
        embed = discord.Embed(colour=discord.Colour.red(), title="근짱", description="근짱#1339")
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


#봇 알림
    if msg.content == "tong start":
        embed = discord.Embed(title="봇이 시작 되었어요", description="봇이 시작됨.", color=0x62c1cc)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send("봇이 시작됨.", embed=embed)

    if msg.content == "tong stop":
        embed = discord.Embed(colour=discord.Color.greyple(), title="봇이 켜집니다", description="빨리 봇을 사용해보세요!")
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)


#통이가 싫어하는 것
    if msg.content == "!싫어하는 모든 것":        
        embed = discord.Embed(colour=discord.Color.dark_gray(), title="제가 싫어 하는 것은요...", description='''
        리플릿이에요...
        이유는요.. ||리플릿으로 돌리면 자꾸 저를 죽여서에요...||
        그리고요...
        저는 마냥이 너무 싫어요...
        이유는요.. ||뭐라하면 자꾸 마냥이 답해서에요...||''')
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)
   

#낚시
    if msg.content == "!낚시":
        await msg.channel.send("배타고 지금 바다에 가고있어요")
        await asyncio.sleep(5)
        await msg.channel.send("배타고 바다에 도착했어요! 낚시대를 바다에 넣었어요.")
        await asyncio.sleep(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 60, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]))
        ran = random.choice([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])
        if ran == 1:
            d = ""f"{msg.author.mention}님! 갈치를 낚았어요! 맛있게 드세요!"
        if ran == 2:
            d = ""f"{msg.author.mention}님! 명태를 낚았어요! 맛있게 드세요!"
        if ran == 3:
            d = ""f"{msg.author.mention}님! 신발을 낚았어요! (사용자 여러분 절때 따라하지 마세요!)우걱우걱 꼭꼭 씹어서 드세요!"
        if ran == 4:
            d = ""f"{msg.author.mention}님! 바다 쓰래기를 낚았어요! (사용자 여러분 절때 따라하지 마세요!)우걱 우걱 꼭꼭 씹어서 드세요!"
        if ran == 5:
            d = ""f"{msg.author.mention}님! 사람을 낚았어요! 일손이 부족했는데! 잘됬네요! 저한테 팔래요?"
        if ran == 6:
            d = ""f"{msg.author.mention}님! 코딩을 낚았어요 코딩 기술력이 오른거같아요! 통큰봇을 응원해 주세요!"
        if ran == 7:
            d = ""f"{msg.author.mention}님! 새를 낚았어요 이게 바다새일까요?"
        if ran == 8:
            d = ""f"{msg.author.mention}님! 복어을 낚았어요 으악! 가시다!"
        if ran == 9:
            d = ""f"{msg.author.mention}님! 제 주인을 낚았어요 저한테 주실래요? (오류는 근짱#1339!)"
        if ran == 10:
            d = ""f"{msg.author.mention}님! 상어을 낚았어요! 잘가요!"
        await msg.channel.send(d)


#테스트
    
    if msg.content == "!테스트":
        await msg.channel.send(
        """
        ```re
        테스트입니다.
        테스트2입니다.
        테스트3입니다.
        테스트4입니다.
        ```
        """
        )


#검색
    if msg.content.startswith(f"!유튜브검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            await msg.channel.send(f"""
            검색할 내용을 입력해주세요!

검색방법
!유튜브검색 (검색할 내용)
            """)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="YOUTUBE 검색결과 링크", value=f"[검색결과 확인하기!](https://www.youtube.com/results?search_query={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)

    if msg.content.startswith(f"!네이버검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            embed = discord.Embed(title=":warning:bug", description="알수없는 오류..", color=0xFFE600)
            embed.add_field(name="!네이버검색 (검색 내용)", value="알수없는 오류가 일어났습니다. \n!네이버검색 (검색내용)을 다시 입력해보세요.", inline=True)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=embed)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="NAVER 검색결과 링크", value=f"[검색결과 확인하기!](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)

    if msg.content.startswith(f"!네이버블로그검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            embed = discord.Embed(title=":warning:bug", description="알수없는 오류..", color=0xFFE600)
            embed.add_field(name="!네이버블로그검색 (검색 내용)", value="알수없는 오류가 일어났습니다. \n!네이버블로그검색 (검색내용)을 다시 입력해보세요.", inline=True)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=embed)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="NAVER BLOG검색결과 링크", value=f"[검색결과 확인하기!](https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)

    if msg.content.startswith(f"!네이버카페검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            embed = discord.Embed(title=":warning:bug", description="알수없는 오류..", color=0xFFE600)
            embed.add_field(name="!네이버카페검색 (검색 내용)", value="알수없는 오류가 일어났습니다. \n!네이버카페검색 (검색내용)을 다시 입력해보세요.", inline=True)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=embed)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="NAVER CAFE검색결과 링크", value=f"[검색결과 확인하기!](https://m.cafe.naver.com/ca-fe/home/search/articles?q={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)

    if msg.content.startswith(f"!아프리카tv검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            embed = discord.Embed(title=":warning:bug", description="알수없는 오류..", color=0xFFE600)
            embed.add_field(name="!아프리카tv검색 (검색 내용)", value="알수없는 오류가 일어났습니다. \n!아프리카tv검색 (검색내용)을 다시 입력해보세요.", inline=True)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=embed)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="아프리카tv 검색결과 링크", value=f"[검색결과 확인하기!](https://www.afreecatv.com/total_search.html?szSearchType=total&szStype=di&szKeyword={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)

    if msg.content.startswith(f"!페이스북검색"):
        a = str(msg.content).split()
        if len(a) < 2:
            embed = discord.Embed(title=":warning:bug", description="알수없는 오류..", color=0xFFE600)
            embed.add_field(name="!페이스북검색 (검색 내용)", value="알수없는 오류가 일어났습니다. \n!페이스북검색 (검색내용)을 다시 입력해보세요.", inline=True)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=embed)
        else:
            c = ""
            for i in range(1, len(a)):
                c = c + a[i]
                if i != len(a) - 1:
                    c = c + "+"
            holed = discord.Embed(title="", description="", color=0xFF0000)
            holed.add_field(name="페이스북 검색결과 링크", value=f"[검색결과 확인하기!](https://www.facebook.com/search/top?q={c})", inline=False)
            await msg.channel.send(""f"{msg.author.mention}")
            await msg.channel.send(embed=holed)



#안내

    if msg.content == "!봇 초대":
        embed = discord.Embed(title="<봇 초대>", description="통큰봇 봇 초대", color=0x62c1cc)
        embed.add_field(name="이곳에 들어간다.", value=f"[클릭!](https://koreanbots.dev/bots/866196608752418836)", inline=True)
        await msg.channel.send(""f"{msg.author.mention}")
        await msg.channel.send(embed=embed)

    if msg.content == "!이름":
        embed = discord.Embed(title=""f"{msg.author.name}의 이름", description="당신의 이름은는 "f"{msg.author.name}", color=0x62c1cc)
        await msg.channel.send(""f"{msg.author.mention}",embed=embed)

    if msg.content == "!id":
        embed = discord.Embed(title=""f"{msg.author.name}의 ID", description="당신의 ID는 "f"{msg.author.id}", color=0x62c1cc)
        await msg.channel.send(""f"{msg.author.mention}",embed=embed)


    if msg.content.startswith("!따라해"):
        mee = msg.content[5:]
        await msg.channel.send(mee)
        await msg.channel.send("```"f"{msg.author.name}님이 시켰어요!```")
        


#테스트


#청소
    if msg.content.startswith ("!청소"):
        if msg.author.guild_permissions.administrator:
            amount = msg.content[4:]
            await msg.delete()
            await msg.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, msg.author), color=0x000000)
            await msg.channel.send(embed=embed)
        
        else:
            await msg.delete()
            await msg.channel.send("{}, 당신은 !청소명령어를 사용할 수 있는 권한이 없습니다".format(msg.author.mention))


    if msg.content == "!테스트": # 메세지 감지
        await msg.channel.send ("{} | {}, Hello".format(msg.author, msg.author.mention))
        await msg.author.send ("{} | {}, User, Hello".format(msg.author, msg.author.mention))

    if msg.content.startswith ("!공지"):
        await msg.delete()
        if msg.author.guild_permissions.administrator:
            notice = msg.content[4:]
            channel = client.get_channel(875407101390909511)
            embed = discord.Embed(title="**!공지사항!**", description="공지사항 내용은 항상 확인 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n "f"{notice} \n\n――――――――――――――――――――――――――――", color=0x00ff00)
            embed.set_thumbnail(url="https://yt3.ggpht.com/EVCGgYu3azcS5EvjCJoxeOZ7NSObwaFbSxukijjwQlWWwdVo7L1oG03J6H3klbWWRijj_rVwQQ=s108-c-k-c0x00ffffff-no-rj")
            await channel.send ("@everyone", embed=embed)
            embed = discord.Embed(title="**[BOT 자동 알림]**", description="정상적으로 공지가 채널에 작성이 완료되었습니다 :)", color=0xff0000)
            embed.add_field(name="기본 작성 설정 채널", value="{}", inline=False)
            embed.add_field(name="공지 발신자", value=""f"{msg.author.name}", inline=False)
            embed.add_field(name="내용", value=""f"{notice}", inline=False)
            await msg.author.send(embed=embed)
 
        else:
            await msg.channel.send("{}, 당신은 관리자가 아닙니다".format(msg.author.mention))





#런
client.run(token)
