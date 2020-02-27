import discord
import os
import requests
from bs4 import BeautifulSoup

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("존버")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # 봇 정보 / 명령어
    if message.content.startswith("!명령어"):
        embed = discord.Embed(
            title='☆★☆★☆★☆★탈붕이 등장☆★☆★☆★☆★',
            description='Version 0.3 last updated 2020.02.27\n'
                        ':: Last update log ::\n'
                        '필터 정보를 나명 필터 정보로 수정\n'
                        '탄 이미지 최신 탄약 차트로 수정\n'
                        '퀵 링크에 시세 확인 사이트 추가\n',
            colour=discord.Colour.orange()
        )
        embed.add_field(name='퀵 링크',
                        value='타르코프 공식사이트 [바로가기](https://www.escapefromtarkov.com/)\n'
                              '배틀스테이트 게임즈 트위터 [바로가기](https://twitter.com/bstategames?lang=ko/)\n'
                              '디시인사이드 타르코프 갤러리 [바로가기](https://gall.dcinside.com/mgallery/board/lists/?id=eft)\n'
                              '타르코프 위키 [바로가기](https://escapefromtarkov.gamepedia.com/Escape_from_Tarkov_Wiki)\n'
                              '플리 마켓 시세 확인 사이트 [바로가기](https://tarkov-market.com/)\n',
                        inline=False)
        embed.add_field(name='-----------------------------명령어 리스트-----------------------------',
                        value='모든 명령어는 느낌표를 붙입니다\n\n', inline=False)
        embed.add_field(name='[지도]', value='!커스텀\n!쇼어라인\n!리저브\n!인터체인지\n!우드\n!팩토리\n!랩\n', inline=False)
        embed.add_field(name='[모딩]', value='!모딩 - 총기 모딩 정보를 보여줍니다\n', inline=False)
        embed.add_field(name='[탄 정보]', value='!탄 - 탄 정보를 보여줍니다\n', inline=False)
        embed.add_field(name='[방어구 정보]', value='[바로가기](https://docs.google.com/spreadsheets/d/1FYTJlBVomct6-Fbh4'
                                               'ZQejR3CW9_e8U0ix_MEA2s52jw/edit#gid=1745411392)', inline=False)
        embed.add_field(name='[게임 필터 설정]', value='!필터 - 엔비디아 게임 필터 정보를 보여줍니다\n', inline=False)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791720498757646/674149913835208704/319px-Killa_Portrait.gif")

        await message.channel.send(embed=embed)

    # 아래는 맵 정보
    # if message.content.startswith('!지도'):
    #    embed = discord.Embed(
    #        title='',
    #        description='',
    #        colour=discord.Colour.orange()
    #    )
    #    embed.add_field(name='Map Information',
    #                    value='!커스텀\n'
    #                          '!쇼어라인\n'
    #                          '!리저브\n'
    #                          '!인터체인지\n'
    #                          '!우드\n'
    #                          '!팩토리\n'
    #                          '!랩\n', inline=False)
    #
    #    await message.channel.send(embed=embed)

    if message.content.startswith('!커스텀'):
        embed = discord.Embed(
            title='커스텀 지도',
            description='',
            colour=discord.Colour.orange()
        )
        # embed.set_image(
        #    url="https://mblogthumb-phinf.pstatic.net/MjAxOTAzMTBfMzcg/MDAxNTUyMTc5NzkxOTQ0.Hlt9Jyv_toEn0XTYAkpLyN8Ov"
        #        "UgsNxuRzNAVGhybD94g.hOkA_VByCxy5gWfMaChviQdjPElVQc6A7QD3k33ixckg.PNG.didwkqk2/qfqami7s4b90"
        #        "1.png?type=w800")

        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666780665244549180/674221773172113428/EFT_-_DC_v0.12.2.5485.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!쇼어라인'):
        embed = discord.Embed(
            title='쇼어라인 지도',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/666817363223511070/unknown-5.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!리저브'):
        embed = discord.Embed(
            title='리저브 지도',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666780665244549180/674221854956978177/EFT_-_v0.12.2.5485.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!인터체인지'):
        embed = discord.Embed(
            title='인터체인지 지도',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666780665244549180/674221802297229342/EFT_-_v0.12.2.5485.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!인터체인지'):
        embed = discord.Embed(
            title='인터체인지 - 히든 스태쉬',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/666818428400828416/32eddecc9fb6e631.jpg")

        await message.channel.send(embed=embed)

    if message.content.startswith('!우드'):
        embed = discord.Embed(
            title='우드 지도',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/666816583410384933/EFT_-__v0.12.2.5485.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!팩토리'):
        embed = discord.Embed(
            title='팩토리 지도',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/666817490533351436/unknown.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!랩'):
        embed = discord.Embed(
            title='랩 - 지하',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/671969633406025748/a0d9f7dd0435fefd.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!랩'):
        embed = discord.Embed(
            title='랩 - 1층',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/671969639734968320/1_Other_Version_v1.png")

        await message.channel.send(embed=embed)

    if message.content.startswith('!랩'):
        embed = discord.Embed(
            title='랩 - 2층',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/671969637784748062/2_final.png")

        await message.channel.send(embed=embed)

    # 탄 정보 모음
    if message.content.startswith('!탄'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.orange()
        )
        embed.add_field(name='Ammo Information',
                        value='탄종류 사이트\n\n'
                              '첫번째 사이트 [-클릭-](https://escapefromtarkov.gamepedia.com/Ballistics)\n\n'
                              '두번째 사이트 [-클릭-](https://docs.google.com/spreadsheets/d/1Pp8tKScb0jB66cOCJSAlNn'
                              '-iKERMXd9FVkSmSq83qn8/edit#gid=64053005)\n\n', inline=False)

        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/675746760752365609/80b24e11d2e0fe6b.png")

        await message.channel.send(embed=embed)

    # 게임 필터 정보
    if message.content.startswith('!필터'):
        embed = discord.Embed(
            title='NVIDIA Game Filter Information',
            description='인게임에서 Alt + F3으로 필터창 띄운 뒤 설정\n ※나명 필터입니다',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/680267449987629089/1.PNG")

        await message.channel.send(embed=embed)

    if message.content.startswith('!필터'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/680267465464479788/2.PNG")

        await message.channel.send(embed=embed)

    if message.content.startswith('!필터'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/680267474532302888/3.PNG")

        await message.channel.send(embed=embed)

    if message.content.startswith('!필터'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.orange()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/666791829148139551/680267486507171840/4.PNG")

        await message.channel.send(embed=embed)

    # 총기 모딩 정보
    if message.content.startswith('!모딩'):
        embed = discord.Embed(
            title='Modding Information',
            description='※참고용일 뿐, 개인 취향에 맞게 모딩하는 것이 가장 좋습니다\n',
            colour=discord.Colour.orange()
        )
        # 모딩 사이트
        embed.add_field(name='모딩 사이트',
                        value='[바로가기](https://docs.google.com/spreadsheets/d/1yHyVEVB5oN0qL_pR1qTNP1_ICmzJ3'
                              'SCFJQNb6XDM_DQ/htmlview#gid=0)',
                        inline=False)
        # AK 시리즈
        embed.add_field(name='AK Series',
                        value='[AK101](https://i.imgur.com/n0CUuSn.png) / [AK102](https://i.imgur.com/nFg6tEb.png) / '
                              '[AK103](https://i.imgur.com/HVCKzbP.png) / [AK104](https://i.imgur.com/dbWSRlM.png)\n'
                              '[AK105](https://i.imgur.com/x8fFt59.png) / [AK74M](https://i.imgur.com/z2Bpn6W.png) / '
                              '[AK74N](https://i.imgur.com/peQAba0.png) / [AKM](https://i.imgur.com/57LqVQM.png)\n'
                              '[AKMN](https://i.imgur.com/hBBnOu8.png) / [AKMSN](https://i.imgur.com/jIFiQ6M.png) / '
                              '[AKS-74U](https://i.imgur.com/D1ib4CU.png)',
                        inline=False)
        embed.add_field(name='Assault rifles',
                        value='[MDR](https://i.imgur.com/P9kyNHr.png) / [SA-58](https://i.imgur.com/RQpale8.png) / '
                              '[AS VAL](https://i.imgur.com/PKHVNZU.png) / [HK416](https://i.imgur.com/XWhQhaz.png) / '
                              '[M4A1](https://i.imgur.com/rbvZctq.png)',
                        inline=False)
        embed.add_field(name='Assault carbines',
                        value='[SKS](https://i.imgur.com/ci27SrM.png) / [TX-15](https://i.imgur.com/pXHbXFa.png) / '
                              '[Hunter](https://i.imgur.com/WO7s9uO.png) / [ADAR](https://i.imgur.com/uIM3tQa.png)\n',
                        inline=False)
        embed.add_field(name='Marksman rifles',
                        value='[SR-25](https://i.imgur.com/0GiQ4j4.png) / [SVD](https://i.imgur.com/6Gy6dLQ.png) / '
                              '[RSASS](https://i.imgur.com/ljsDAmk.png) / [M1A](https://i.imgur.com/xeYFZMu.png) / '
                              '[VSS](https://i.imgur.com/HmMg26i.png)',
                        inline=False)
        embed.add_field(name='Bolt-action rifles',
                        value='[T-5000](https://i.imgur.com/XSxmebO.png) / [SV-98](https://i.imgur.com/gM8SXP0.png) / '
                              '[Mosin-sniper rifle](https://i.imgur.com/kGrczhj.png) / [DVL-10](https://i.imgur.com/'
                              '9OqDlXI.png) / [Remington700](https://i.imgur.com/GRId0H1.png)',
                        inline=False)
        embed.add_field(name='SMGs',
                        value='[MP9](https://i.imgur.com/3fBrLp1.png) / [MP5 Kurz](https://i.imgur.com/kzQp0nv.png) / '
                              '[P90](https://i.imgur.com/c9Xh4go.png) / [MP5](https://i.imgur.com/mIzB46A.png)\n'
                              '[MPX](https://i.imgur.com/grRDc9S.png) / [MP7](https://i.imgur.com/ATjqIHy.png) / '
                              '[PP19](https://i.imgur.com/59PaubL.png)',
                        inline=False)
        embed.add_field(name='Shotguns',
                        value='[MP-153](https://i.imgur.com/epQfJmI.png) / [TOZ](https://i.imgur.com/0WNYBP4.png) / '
                              '[Saiga](https://i.imgur.com/ijdzN7K.png) / [M870](https://i.imgur.com/NB0KDPO.png)',
                        inline=False)
        embed.add_field(name='Machine guns',
                        value='[RPK-16](https://i.imgur.com/oVBDqzQ.png)', inline=False)

        await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

