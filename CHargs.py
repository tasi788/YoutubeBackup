import os
import sys
import youtube_dl
import subprocess
ydl_opts = {
	'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
	'ignoreerrors': True
}
os.system('rm *.mp4')
x = sys.argv[1]
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	result = ydl.extract_info(x,download=False)
	try:
		for y in result['entries']:
			x = y['id']
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
	except KeyboardInterrupt:
		print('\x1b[38;96m\n被你關掉惹')
	except:
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
