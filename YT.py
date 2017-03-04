import os
import re
import youtube_dl
import subprocess
from colorama import Fore, Back, Style

ydl_opts = {
	'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
}
try:
	f = open('yt.html','r').read()
	v = re.findall('watch\?v=(\w+)',f)
	os.system('rm *.mp4')
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		for x in v:
			check = open('check.txt','r').read().split('\n')
			if x in check:
				pass
			else:
				try:
					ydl.download(['%s' % (x)])
					with open('check.txt','a') as f:
						f.write('%s\n'%(x))
					up = 'gdrive upload *.mp4 -p 0B6-vwxMTtzg_cG1XMWZHWGNwNEE'
					s = subprocess.check_output([up],stderr=subprocess.STDOUT,shell=True).decode('utf-8')
					if 'Uploaded' in s:
						tidy = s.split('Uploaded ')[1].split(' ')[0]
						os.system('rm *.mp4')
				except:
					with open('error','a') as err:
						err.write('%s\n' % (x))
except:
	print(Fore.RED + '找不到yt.html啦。')
