import discord, os, json, random, ast, asyncio, datetime
from discord.ext import commands


#이 프로젝트는 디스코드 haziel의 저작문서이므로 무단 복제를 금지합니다

token = "token code" #봇 토큰 설정하기

client = commands.Bot(command_prefix= "/")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready(): #봇이 준비되었을때 뭐라고하기
    print("봇 작동 준비가 완료되었습니다.명령어 주세요!")
    print(client.user)
    print("============================")
    import asyncio
    user = len(client.users)
    server = len(client.guilds)
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    message = ["/도움말 과 명령어 듣기", str(user) + "명과" + str(server) + "개의 서버에서 안전하게 보호되고 있어요!", "로라님이 만들어주셔서 열심히 일하는중","가입된 서버분들을 위해 열심히 일하는중" ]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(5)





@client.event
async def on_guild_join(server):
    await message.channel.send("저를 초대해 주셔서 감사해요!이제부터 이 서버를 열심히 보호도 하고 여려분과 열심히 놀게요(?)")
    print(server,"서버에 들어왔어요!헤이즐 서버 하나 늘었다")

@client.event
async def on_guild_remove(server):
    print(server,"서버에서 헤이즐이 나갔어요,,,ㅠㅠ")



@client.event
async def on_message(message): #사용자가 메세지를 입력했을때 반응하기
    if message.content.startswith("/킥"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[3:22]))
            reason = message.content[22:]
            await message.guild.kick(user)
            embed = discord.Embed(title="킥문구 작동", color=0xAAFFFF) 
            embed.add_field(name="킥된 유저", value=f"{user.mention}", inline=False)
            embed.add_field(name="킥 시킨 관리자", value=f"{message.author.mention}", inline=False)
            embed.add_field(name="사유", value=f"{reason}", inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
            return
            
    if message.content.startswith("/밴"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[3:21]))
            reason = message.content[22:]
            await message.guild.ban(user)
            embed = discord.Embed(title="밴문구 작동", color=0xAAFFFF) 
            embed.add_field(name="밴된 유저", value=f"{user.mention}", inline=False)
            embed.add_field(name="밴 시킨 관리자", value=f"{message.author.mention}", inline=False)
            embed.add_field(name="사유", value=f"{reason}", inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
            return
    if message.content.startswith("/청소"):
        if message.content == "/청소":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/청소 (청소할 개수)'에요", color=0xff0000))
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
                print(f"{message.author.mention}님이 {number}개의 메세지를 청소하는 코드를 사용했어요")
            elif message.author.id == 704535152763601007:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return
    if message.content.startswith("/긴청"):
        if message.author.id == 704535152763601007:
            number = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit=number)
            a = await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
            await asyncio.sleep(1)
            await a.delete()
        elif message.author.id == 800193013292335145:
            number = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit=number)
            a = await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
            await asyncio.sleep(1)
            await a.delete()
        else:
            await message.channel.send("이 명령어는 로라님만 사용할수 있어요!")
    if message.content == "/핑":
        ping = client.latency
        await message.channel.send(f'{str(round(ping * 1000))}ms 입니다!')
        print(f"{message.author.mention}님이 핑코드를 사용했어요")
    if message.content.startswith("/고정"):
        if message.content == "/고정":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/고정 (고정할 매세지)'에요", color=0xff0000))
            return
        else:
            if message.author.guild_permissions.administrator:
                await message.pin()
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return
#===========================================================관리기능==============================================================================================
    if message.content.startswith('/타이머'):
        if message.content == '/타이머':
            await message.channel.send(f"{message.author.mention} \n그래서 몇 초를 맞추라고요?\n올바른 명령어는 `/타이머 (숫자)` 에요!")
        else: #그렇지 않다면
            timer = int (message.content.split(" ")[1]) # 타이머를 숫자만큼 지정한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 설정되었습니다.\n시간이 끝나면 맨션해드릴게요!") # 설정 완료 메시지를 보낸다.
            await asyncio.sleep(timer) # 그 숫자만큼 대기한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 끝났어요!") # 타이머가 끝났음을 알린다.
            print(f"{message.author.mention}님이 타이머 코드를 사용했어요!")
    if message.content.startswith("/서버정보"):
        embed = discord.Embed(title=str(f"{message.guild}의 서버정보"), colour=discord.Colour.green(),description="선택하신 서버의 정보예요.")
        embed.add_field(name="서버 이름", value=f"{message.guild}", inline=True)
        embed.add_field(name="서버 아이디", value=f"{message.guild.id}", inline=True)
        embed.add_field(name="서버 생성일", value=(message.guild.created_at), inline=True)
        embed.add_field(name="서버인원", value=str(message.guild.member_count)+"명", inline=True)
        await message.channel.send(embed=embed)
        print(f"{message.author.mention}님이 서버정보 코드를 사용했어요")
    if message.content == "/주사위":
        await message.channel.send(random.randint(1, 6))
    if message.content.startswith == ("/디엠"):
        author = message.guild.get_member(int(message.conent[4:22]))
        msg = message.content[23:]
        await author.send(msg)
        await message.channel.send("성공적으로 전송되었습니다!")
    if message.content == '/내정보':
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{message.author.name}의 정보', color=0xAAFFFF)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="별명", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.author.send(embed=embed)
    if message.content.startswith("/투표"):
        if message.content == "/투표":
            embed = discord.Embed(title="명령어 오류", description="올바른 명령어는 '/투표 [제목]/항목1/항목2 ... 이에요", color=0xff0000)
        else:
            vote = message.content[4:].split("/")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                    choose = await message.channel.send("```" + vote[i] + "```")
                    await choose.add_reaction('👍')
                    print(f"{message.author.mention}님이 투표 코드를 사용했어요")
    if message.content.startswith("/말해"):
        tada = message.content[4:]
        embed = discord.Embed(title=(f"{message.author.name}님의 의해서 발생한 message"), description=(f"{tada}"), color=0xAAFFFF)
        embed.set_footer(text="출처(및 도와주신분):Dev. Hestia#5444")
        await message.channel.send(embed=embed)
    if message.content.startswith("/공지"):
        if message.author.id == 704535152763601007:
            tada = message.content[4:]
            await message.channel.send(f"{tada}")
        else:
            await message.channel.send("이 명령어는 Lora로라#3561님만 사용할수 있어요!")
    if message.content.startswith("/파티모집"):
        tada = message.content[6:]
        await message.channel.send(f'{message.author.mention}님과 같이 "{tada}"를 하실분을 찾습니다')
    if message.content.startswith("/채널매세지"):
        if message.author.id == 704535152763601007:
            channel = message.content[7:25]
            msg = message.content[25:]
            await client.get_channel(int(channel)).send(msg)
#========================================================편의기능=================================================================================================
    if message.content == "/가위" or message.content == "/바위" or message.content == "/보":
        random_ = random.randint(1, 3)
               
        if random_ == 1: # random 에 저장된 변수가 1일때 (가위 일때)
            if message.content == "/가위":        
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 가위!")
                await message.channel.send(f"{message.author.mention}님 비겼습니다.")
            elif message.content == "/바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 가위!")
                await message.channel.send(f"{message.author.mention}님 제가 졌습니다.")
            elif message.content == "/보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 가위!")
                await message.channel.send(f"{message.author.mention}님 제가 이겼습니다.")
        elif random_ == 2: # random 에 저장된 변수가 2일때 (바위 일때)
            if message.content == "/가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 바위!")
                await message.channel.send(f"{message.author.mention}님 제가 이겼습니다.")
            elif message.content == "/바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 바위!")
                await message.channel.send(f"{message.author.mention}님 비겼습니다.")
            elif message.content == "/보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 바위!")
                await message.channel.send(f"{message.author.mention}님 제가 졌습니다.")
        elif random_ == 3: # random 에 저장된 변수가 1일때 (보 일때)
            if message.content == "/가위":        
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 보!")
                await message.channel.send(f"{message.author.mention}님 제가 졌습니다.")
            elif message.content == "/바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 보!")
                await message.channel.send(f"{message.author.mention}님 제가 이겼습니다.")
            elif message.content == "/보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 보!")
                await message.channel.send(f"{message.author.mention}님 비겼습니다.")
    if message.content == "/금붕어 키우기":
        if message.guild.id == 787278470630604800:
            random_ = random.randint(1, 4)


            if random_ == 1: # random 에 저장된 변수가 1일때 (스트레스때문에 죽었을때)
                if message.content == "/금붕어 키우기":
                    await message.channel.send(f"{message.author.mention}님 아쉽게도 금붕어가 스트레스를 많이 받아서 죽었어요")
                   
            if random_ == 2: # random 에 저장된 변수가 2일때 (먹이를 너무 많이 먹어서)
                if message.content == "/금붕어 키우기":
                    await message.channel.send(f"{message.author.mention}님 아쉽게도 금붕어가 먹이를 너무 많이 먹어서 죽었어요")

            if random_ == 3: #random 에 저장된 변수가 3일때 (먹이를 너무 조금 먹어서)
                if message.content == "/금붕어 키우기":
                    await message.channel.send(f"{message.author.mention}님 아쉽게도 금붕어가 먹이를 너무 조금 먹어서 죽었어요")
        
            if random_ == 4: #random 에 저장된 변수가 4일때 (금붕어 성공)
                if message.content == "/금붕어 키우기":
                    await message.channel.send(f"{message.author.mention}님 금붕어가 성공적으로 잘았어요! <@&787278945392525312>님 {message.author.mention}님한테 보상으로 금붕어 달인 역할을 주세요")
        else:
            embed = discord.Embed(title="오류", description="이 명령어는 저의 서포트 체널에서만 사용가능해요 [여기](https://discord.gg/c3fjR4Kmvh) 를 눌러 바로 서포트 채널로 이동 하실수 있어요!", color=0xAAFFFF)
            await message.channel.send(embed=embed) 
#===============================================================재미기능===============================================================================
    if message.content.startswith("/개발자"):
        embed = discord.Embed(title="Haizel의 개발자 정보", description="저를 만들어주신분 정보에요!", color=0xAAFFFF) 
        embed.add_field(name="닉네임", value="Lora로라#3561", inline=False)
        embed.add_field(name="아이디", value="704535152763601007", inline=False)
        embed.add_field(name="프로필 사진 그려주신분", value="/디자이너 를 하세요", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith("/디자이너"):
        embed = discord.Embed(title="Haizel의 디자이너 정보", description="저의 프사를 만들어주신분 정보에요!", color=0xAAFFFF) 
        embed.add_field(name="닉네임", value="SineSok#0001", inline=False)
        embed.add_field(name="아이디", value="789371145018277898", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/봇정보"):
        users = len(client.users)
        servers = len(client.guilds)
        await message.channel.send(f"봇이 있는 서버 수: {servers}, 봇이 있는 서버에 있는 유저 수의 합: {users}")
        print(f"{message.author.mention}님이 봇정보 코드를 사용했어요")
    if message.content.startswith("헤이즐 뒤져"):
        await message.channel.send("https://cdn.discordapp.com/attachments/763326924717293598/797005508363157514/unknown.png")
        print(f"{message.author.mention}님이 헤이즐 뒤져라고 사용했어요")
    if message.content == "/초대링크":
        embed=discord.Embed(title="haziel 초대링크", description = "[여기](https://discord.com/oauth2/authorize?client_id=800193013292335145&scope=bot&permissions=1610607742) 를 눌러 바로 초대 하실수 있어요!", color=0x00ff00)
        await message.channel.send(embed=embed)
    if message.content == ("/서포트 서버"):
        embed = discord.Embed(title="Haizel의 서포트 서버", description="[여기](https://discord.gg/xEBEpw7uQs)를 클릭하여 바로 갈수 있어요!", color=0xAAFFFF) 
        await message.channel.send(embed=embed)
    if message.content == "/링크":
        await message.channel.send(embed=discord.Embed(title="한국 봇 리스트 링크", description = "[여기](https://koreanbots.dev/bots/800193013292335145)를 눌러 바로 접속하실수 있어요!\n하트 부탁드려요!", color=0x00ff00))
        print(f"{message.author.mention}님이 한국 봇 리스트 링크 코드를 사용했어요")
        return
    if message.content.startswith('/봇공지'):
        if message.author.id == 704535152763601007:
            msg = message.content[5:]
            for i in client.guilds:
                for j in i.channels:
                    if ['봇', '공지'] in j.name:
                        await j.send(msg)
                        return


#===========================================================봇정보===========================================================================
    
    
    if message.content.startswith("씨발"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("지랄"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("존나"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("좆같은"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("니애미"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("개새끼"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("개같은"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if  message.content.startswith("ㅆㅂ"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("ㅗ"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("Tlqkf"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("<@704535152763601007> 바보"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("𝙎𝙎𝙄𝘽𝘼𝙇"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("ㅈㄴ"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("니 엄마가"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith(":middle_finger"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("병신"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("젠장"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("씨1발"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content == "/기모띠":
        await message.channel.send("그거 <@789371145018277898>님이 자주하시는 말이에요.시네님이 그거하고 싶나봐여")
    if message.content.startswith("씻팔"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("쓰으래기"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith("개애쌔끼"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)




#============================================================검열 시스템===========================================================================================
    if message.content.startswith(f'/eval'):
        if message.author.id == 704535152763601007:

            def insert_returns(body): # [1]
            # insert return stmt if the last expression is a expression statement
                if isinstance(body[-1], ast.Expr):
                    body[-1] = ast.Return(body[-1].value)
                    ast.fix_missing_locations(body[-1])

            # for if statements, we insert returns into the body and the orelse
                if isinstance(body[-1], ast.If):
                    insert_returns(body[-1].body)
                    insert_returns(body[-1].orelse)

            # for with blocks, again we insert returns into the body
                if isinstance(body[-1], ast.With):
                    insert_returns(body[-1].body)

            cmd = message.content.split(" ")[1:]
            _cmd = cmd
            print(cmd)
            msg = await message.channel.send(embed = discord.Embed(title='Code Compiling').add_field(
                name='📥 Input',
                value=f'```py\n{cmd}```',
                inline=False
            ))
            await asyncio.sleep(1.5)

        #banword checking
            banword = ['token', 'file=', 'file ='] 
        # 본인이 원하는걸 넣으심 됩니다  # banword에 있는 단어가 있으면 return None으로 처리됩니다.
    
            if cmd in banword: # [2]
                embed = discord.Embed(title='Code Compiling')
                embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
                embed.add_field(name = '📤 Output', value = f'`{cmd}`에는 eval에서 사용 금지된 단어가 포함되어 있습니다.')
                await msg.edit(embed=embed)
                await ctx.send(f'{ctx.message.content}는 사용 금지된 단어가 포함되어 있습니다.')
                return None # [3]
            else:
                try:
                    code = message.content[6:]
                    cmd = code
                    fn_name = "_eval_expr"
                    cmd = cmd.strip("` ")
                    # add a layer of indentation
                    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
                    # wrap in async def body
                    body = f"async def {fn_name}():\n{cmd}"
                    parsed = ast.parse(body)
                    body = parsed.body[0].body
                    insert_returns(body)
                    env = {
                        'client': client,
                        'discord': discord,
                        'message': message,
                        '__import__': __import__
                    }
                    exec(compile(parsed, filename="<ast>", mode="exec"), env)
                    result = (await eval(f"{fn_name}()", env))
                    embed=discord.Embed(title="실행 성공", colour=discord.Colour.green(), timestamp=message.created_at)
                    embed.add_field(name="`📥 Input (들어가는 내용) 📥`", value=f"```py\n{code}```", inline=False)
                    embed.add_field(name="`📤 Output (나오는 내용) 📤`", value=f"```py\n{result}```", inline=False)
                    embed.add_field(name="`🔧 Type (타입) 🔧`",value=f"```py\n{type(result)}```", inline=False)
                    embed.add_field(name="`🏓 Latency (지연시간) 🏓`",value=f"```py\n{str((datetime.datetime.now()-message.created_at)*1000).split(':')[2]}```", inline=False)
                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f"{message.author.mention}, 실행 중 오류가 발생하였습니다.\n\n```py\n{e}```")
        else:
            await message.channel.send("이 명령어는 저의 개발자만 사용할수 있어요!")
            embed = discord.Embed(title="Haizel의 개발자 정보", description="저를 만들어주신분 정보에요!", color=0xAAFFFF) 
            embed.add_field(name="닉네임", value="Lora로라#3561", inline=False)
            embed.add_field(name="아이디", value="704535152763601007", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/800255202535014420/800922645733310505/KakaoTalk_20201001_105019614.jpg")
            await message.channel.send(embed=embed)

#====================================================eval코드===============================================================================
    
    

    if message.content == '/도움말' or message.content == '/도움' or message.content == '/help':
        n = 0
        helps = [discord.Embed(title='목차', description='**페이지 2**\n 관리기능\n**페이지 3**\n편의기능\n**페이지 4**\n재미기능\n**페이지 5**\n봇정보', color=0x00ffff),
                 discord.Embed(title='관리기능', description='**/킥 [사용자 ID] [사유]**\n특정사용자를 서버에서 킥시켜요\n**/밴 [사용자 ID] [사유]\n특정사용자를 서버에서 밴시켜요\n **/고정 [고정할 매세지]** \n매세지를 고정해요\n **/핑** \n현재 핑을 측정해서 알려줘요', color=0x00fffff),
                 discord.Embed(title='편의기능', description='**/타이머 [시간(초기준)]**\n몇초의 타이머를 설정하고 끝나면 맨션해 드려요\n **/주사위**1부터 6까지 중에서 랜덤 숫자를 불러주어요\n**/서버정보**\n현재 서버의 정보를 알려줘요\n**/투표 [제목]/[항목 1]/[항목 2]....**투표를 할수있어요!예:"/투표 헤이즐은 유용하다/yes/no"같이 사용할수 있어요!\n**/내정보**\n디엠으로 내 정보를 알려줘요\n**/말해 [말할 내용]**\n봇으로 말을 할 수 있어요', color=0x00fffff),
                 discord.Embed(title='재미기능', description='**/금붕어 키우기**\n금붕어 키우기 미니게임을 해요\n**/가위(또는 /바위 또는 /보)**\n가위바위보 게임을 해요', color=0x00fffff),
                 discord.Embed(title='봇정보', description='**/링크**\n한국 봇 리스트 링크를 줘요\n**/초대링크**\n저의 초대링크를 드려요\n**/개발자**\n저를 만들어주신분을 알려드려요!\n**/디자이너**\n저의 프사를 만들어주신분을 알려드려요', color=0x00fffff),]
        help_msg = await message.channel.send(embed=helps[n])
        for i in ['⏪', '◀️', '⏹️', '▶️', '⏩']:
            await help_msg.add_reaction(i)
        def check(reaction, user):
        	return user == message.author and reaction.message.channel == message.channel
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=120)
            except asyncio.TimeoutError:
                break
            if reaction.emoji == '⏪':
                n = 0
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏩':
                n = len(helps)-1
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '◀️':
                if n != 0:
                    n -= 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '▶️':
                if n != len(helps)-1:
                    n += 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏹️':
                await help_msg.delete()
                break
                                    
                                    
client.run(token)
