import discord, os, json, random, ast, asyncio, datetime
from discord.ext import commands


#이 프로젝트는 디스코드 haziel의 저작문서이므로 무단 복제를 금지합니다

token = "token" #봇 토큰 설정하기

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready(): #봇이 준비되었을때 뭐라고하기
    print("봇 작동 준비가 완료되었습니다.명령어 주세요!")
    print(client.user)
    print("============================")
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    while True:
        user = len(client.users)
        server = len(client.guilds)
        message = ["/도움말 과 명령어 듣기", f"{user}명과 {server}개의 서버에서 안전하게 보호되고 있어요!", "로라님이 만들어주셔서 열심히 일하는중", "가입된 서버분들을 위해 열심히 일하는중" ]
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(5)


@client.event
async def on_guild_join(server):
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
            user = await client.fetch_user(int(message.content[3:22]))
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
                number = int(message.content.split()[1])
                await message.channel.purge(limit=number)
                await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
                print(f"{message.author.mention}님이 {number}개의 메세지를 청소하는 코드를 사용했어요")
            elif message.author.id == 704535152763601007:
                number = int(message.content.split(" ")[1])
                await message.channel.purge(limit=number)
                await message.channel.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return
            return
     
    if message.content == "/핑":
        la = client.latency
        await message.channel.send(f'{str(round(la * 1000))}ms 입니다!')
        return
    #=============================================================관리기능=====================================================================================
    
    if message.content.startswith('/타이머'):
        if message.content == '/타이머':
            await message.channel.send(f"{message.author.mention} \n그래서 몇 초를 맞추라고요?\n올바른 명령어는 `/타이머 (숫자)` 에요!")
        else: #그렇지 않다면
            timer = int(message.content.split(" ")[1]) # 타이머를 숫자만큼 지정한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 설정되었습니다.\n시간이 끝나면 맨션해드릴게요!") # 설정 완료 메시지를 보낸다.
            await asyncio.sleep(timer) # 그 숫자만큼 대기한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 끝났어요!") # 타이머가 끝났음을 알린다.
        return
            
    if message.content == "/주사위":
        await message.channel.send(random.randint(1, 6))
        return
    
    if message.content.startswith("/서버정보"):
        embed = discord.Embed(title=str(f"{message.guild}의 서버정보"), colour=discord.Colour.green(),description="선택하신 서버의 정보예요.")
        embed.add_field(name="서버 이름", value=message.guild.name)
        embed.add_field(name="서버 아이디", value=f"{message.guild.id}")
        embed.add_field(name="서버 생성일", value=message.guild.created_at)
        embed.add_field(name="서버인원", value=str(message.guild.member_count)+"명")
        await message.channel.send(embed=embed)
        return   
                
    if message.content == "/투표":
        embed = discord.Embed(title="명령어 오류", description="올바른 명령어는 '/투표 [제목]/항목1/항목2 ... 이에요", color=0xff0000)
        return
    
    if message.content.startswith("/투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')
            print(f"{message.author.mention}님이 투표 코드를 사용했어요")
        return
    
    if message.content == '/내정보':
        date = datetime.datetime.utcfromtimestamp(((message.author.id >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{message.author.name}의 정보', color=0xAAFFFF)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="별명", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.author.send(embed=embed)
        return
        
    if message.content.startswith("/말해"):
        tada = message.content[4:]
        embed = discord.Embed(title=f"{message.author.name}님에 의해서 발생한 message", description=tada, color=0xAAFFFF)
        embed.set_footer(text="출처(및 도와주신분):Dev. Hestia#5444")
        await message.channel.send(embed=embed)
        return
            
    #=============================================================편의기능=====================================================================================    
    if message.content in ["/가위", "/바위", "/보"]:
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
        return
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
                    await message.channel.send(f"{message.author.mention}님 금붕어가 성공적으로 잘았어요! <@&787278945392525312>님 {message.author.mention}님한테 보상으로 금붕어 달인 역할을 드릴게요")
        else:
            embed = discord.Embed(title="오류", description="이 명령어는 저의 서포트 체널에서만 사용가능해요 [여기](https://discord.gg/c3fjR4Kmvh) 를 눌러 바로 서포트 채널로 이동 하실수 있어요!", color=0xAAFFFF)
            await message.channel.send(embed=embed) 
    #===============================================재미기능(금붕어 키우기는 오류나서 안 올립니다)=======================================================================
    if message.content == "/링크":
        await message.channel.send(embed=discord.Embed(title="한국 봇 리스트 링크", description = "[여기](https://koreanbots.dev/bots/800193013292335145)를 눌러 바로 접속하실수 있어요!\n하트 부탁드려요!", color=0x00ff00))
        return
    
    if message.content == "/초대링크":
        embed=discord.Embed(title="haziel 초대링크", description = "[여기](https://discord.com/oauth2/authorize?client_id=800193013292335145&scope=bot&permissions=1610607742) 를 눌러 바로 초대 하실수 있어요!", color=0x00ff00)
        await message.channel.send(embed=embed)
        return
    
    if message.content == "/패치노트":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="패치노트\n 베타Ver. 0.1.4", description="1.가위바위보 미니게임 추가!\n2.욕 검열 시스템 수정\n3.패치노트 추가\n4.킥문구 수정\n5.밴문구 수정\n6.타이머 기능 추가\n7.서버정보 기능 추가\n8.계산문구 제거")
        await message.channel.send(embed=embed)
        return
    
    if message.content.startswith("/개발자"):
        embed = discord.Embed(title="Haizel의 개발자 정보", description="저를 만들어주신분 정보에요!", color=0xAAFFFF) 
        embed.add_field(name="닉네임", value="Lora로라#3561", inline=False)
        embed.add_field(name="아이디", value="704535152763601007", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/800255202535014420/800922645733310505/KakaoTalk_20201001_105019614.jpg")
        await message.channel.send(embed=embed)
        return
    
    if message.content == ("/서포트 서버"):
        embed = discord.Embed(title="Haizel의 서포트 서버", description="[여기](https://discord.gg/xEBEpw7uQs)를 클릭하여 바로 갈수 있어요!", color=0xAAFFFF) 
        await message.channel.send(embed=embed)
        return
    
    #===============================================봇정보==================================================================================================
    
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

            cmd = message.content.split()[1:]
            _cmd = cmd
            print(cmd)
            msg = await message.channel.send(embed = (discord.Embed(title='Code Compiling')).add_field(
                name='📥 Input',
                value=f'```py\n{cmd}```',
                inline=False
            ))
            await asyncio.sleep(1.5)

        #banword checking
            banword = ['file=', 'file ='] 
        # 본인이 원하는걸 넣으심 됩니다  # banword에 있는 단어가 있으면 return None으로 처리됩니다.
    
            if cmd in banword: # [2]
                embed = discord.Embed(title='Code Compiling')
                embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
                embed.add_field(name = '📤 Output', value = f'`{cmd}`에는 eval에서 사용 금지된 단어가 포함되어 있습니다.')
                await msg.edit(embed=embed)
                await ctx.send(f'{ctx.message.content}는 사용 금지된 단어가 포함되어 있습니다.')
                return
            
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
                    embed.add_field(name="`🔧 Type (타입) 🔧`", value=f"```py\n{type(result)}```", inline=False)
                    embed.add_field(name="`🏓 Latency (지연시간) 🏓`", value=f"```py\n{str((datetime.datetime.now()-message.created_at)*1000).split(':')[2]}```", inline=False)
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
        return
   #========================================================eval코드============================================================================================
    if message.content == "/도움말":
        if message.author.id == 704535152763601007:
            embed = discord.Embed(title="Haizel의 명령어 도움말", description="Haizel은 관리기능 편의기능 재미기능 등이 있어요!", color=0xAAFFFF) 
            embed.add_field(name="관리기능", value="ㅤ", inline=False)
            embed.add_field(name="/킥 [사용자 ID] [사유]", value="특정사용자를 서버에서 킥시켜요", inline=True)
            embed.add_field(name="/밴 [사용자 ID] [사유]", value="특정사용자를 서버에서 밴시켜요", inline=True)
            embed.add_field(name="/청소 [개수]", value="매세지를 청소해요(요구 권한=관리자)", inline=True)
            embed.add_field(name="/핑", value="현재 핑을 측정해서 알려줘요", inline=True)
            embed.add_field(name="편의기능", value="ㅤ", inline=False)
            embed.add_field(name="/타이머 [시간(초기준)]", value="몇초의 타이머를 설정하고 끝나면 맨션해 드려요", inline=True)
            embed.add_field(name="/주사위", value="1부터 6까지 중에서 랜덤 숫자를 불러주어요", inline=True)
            embed.add_field(name="/서버정보", value="현재 서버의 정보를 알려줘요", inline=True)
            embed.add_field(name="/투표 [제목]/[항목 1]/[항목 2]....", value="투표를 할수있어요!예:'/투표 헤이즐은 유용하다/yes/no'같이 사용할수 있어요!", inline=True)
            embed.add_field(name="/내정보", value="디엠으로 내 정보를 알려줘요", inline=True)
            embed.add_field(name="/말해 [말할 내용]", value="봇으로 말을 할 수 있어요", inline=True)
            embed.add_field(name="재미기능", value="ㅤ", inline=False)
            embed.add_field(name="/금붕어 키우기[현재 오류남]", value="금붕어 키우기 미니게임을 해요", inline=True)
            embed.add_field(name="/가위(또는 /바위 또는 /보)", value="가위바위보 게임을 해요", inline=True)
            embed.add_field(name="봇 정보", value="ㅤ", inline=False)
            embed.add_field(name="/링크", value="한국 봇 리스트 링크를 줘요", inline=True)
            embed.add_field(name="/초대링크", value="저의 초대링크를 드려요", inline=True)
            embed.add_field(name="/패치노트", value="최근 패치노트를 불러주어요", inline=True)
            embed.add_field(name="/개발자", value="저를 만들어주신분을 알려드려요!", inline=True)
            embed.add_field(name="/도움말 페이지2", value="나머지 기능의 도움말이에요", inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(f"{message.author.mention}, 아래의 링크를 클릭하여 서포트서버에서 **#도움말**에 가보시면 되요!")
            embed = discord.Embed(title="Haizel의 서포트 서버", description="[여기](https://discord.gg/xEBEpw7uQs)를 클릭하여 바로 갈수 있어요!", color=0xAAFFFF)
            await message.channel.send(embed=embed)

client.run(token)
