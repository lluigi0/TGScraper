# The code was optimized using a tool from pyobfuscate.com.

_G='Scraping... Wait.'
_F='utf-8'
_E=False
_D='\n'
_C='Telegram'
_B=None
_A=True
import time,re,random,requests
from telethon.sync import TelegramClient
import os
from colorama import Fore as F
import threading,configparser,json
try:
	with open('banner.json','r')as banner_file:banner_data=json.load(banner_file)
except FileNotFoundError:print('File banner.json not found');banner_data={}
cc=banner_data.get('cc',_B)
scraper=banner_data.get('scraper',_B)
select=banner_data.get('select',_B)
the=banner_data.get('the',_B)
underground=banner_data.get('underground',_B)
lines=banner_data.get('lines',_B)
config=configparser.ConfigParser()
config.read('config.ini')
clear='cls'if os.name=='nt'else'clear'
RD=F.RED
W=F.WHITE
R=F.RESET
info=F.LIGHTMAGENTA_EX+'[¡]'+F.RESET
done=F.GREEN+'[+]'+F.RESET
error=F.RED+'[!]'+F.RESET
api_id=config[_C]['api_id']
api_hash=config[_C]['api_hash']
time_sleep=float(config[_C]['time.sleep'])
def print_slow(text,delay,add_new_line=_A):
	for A in text:print(A,end='',flush=_A);time.sleep(delay)
	if add_new_line:print(_D,end='',flush=_A)
def get_input(prompt):print_slow(prompt,.01,_E);return input()
def scrape_single_channel(client,channel_username,bin_to_scrape,num_messages):
	H=num_messages;G=bin_to_scrape;F=client;D=channel_username
	try:L=F.get_entity(D)
	except ValueError:print_slow(f"{error} Invalid channel name",.01,_A);return _B,0,0,0
	M=time.time();N=random.randint(1,999999);I=f"{D}_{N}.txt";J=set();C=0
	with open(I,'a',encoding=_F)as O:
		B=0
		for A in F.iter_messages(L):
			if A.text:
				if G.lower()==''or G.lower()in A.text.lower():
					print(_G,end='\r');P=re.findall('(\\d+\\|\\d+\\/\\d+\\|\\d+)',A.text);Q=re.findall('(\\d+\\|\\d+\\|\\d+\\|\\d+)',A.text);R=re.findall('(\\d+\\/\\d+\\/\\d+\\/\\d+)',A.text);S=re.findall('(\\d+\\ \\d+\\/\\d+\\ \\d+)',A.text);T=re.findall('(\\d+\\ \\d+\\|\\d+\\ \\d+)',A.text);U=re.findall('(\\d+\\ \\d+\\ \\d+\\ \\d+)',A.text)
					for E in P+Q+R+S+T+U:
						if E not in J:
							J.add(E);O.write(E+_D);B+=1
							if B==H:break
						else:C+=1
					if B==H:break
			time.sleep(time_sleep)
	V=time.time();K=V-M;print_slow(f"{done} Scraped {B} cc's from {D} in {K:.2f} seconds",.01,_A)
	if C>0:print_slow(f"{done} Removed {C} duplicate card(s)",.01,_A)
	return I,B,C,K
def scrape_multiple_channels(client,channels_list):
	B=f"multi_{random.randint(1,999999)}.txt";C=0;D=0;E=0
	with open(B,'a',encoding=_F)as G:
		for F in channels_list:
			try:H=int(get_input(f"{info} Enter the number of CCs to scrape from @{F}: "))
			except ValueError:print_slow(f"{error} Invalid input for the number of CCs",.01,_A);return _B,0,0,0
			print(_G,end='\r');A,I,J,K=scrape_single_channel(client,F,'',H)
			if A is _B:return
			C+=I;D+=J;E+=K
			with open(A,'r',encoding=_F)as L:G.write(L.read())
			os.remove(A)
	return B,C,D,E
def main():
	U='document';T='chat_id';S='bot_token';Q='━━━━━━━━━━━━';P='━━━━━━━━━━━━\n'
	while _A:
		os.system(clear);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);print(F.CYAN+select+F.WHITE);print_slow(F.LIGHTMAGENTA_EX+lines+W,.0085,_A);print_slow('Choose scraping mode:\n',.01,_E);print_slow('1. Single scrape\n',.01,_E);print_slow('2. Multi-scrape\n',.01,_E);print_slow('99. About us\n',.01,_E);G=get_input('> ');B=TelegramClient('session_name',api_id,api_hash);B.start()
		if G=='1':
			os.system(clear);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);print(F.CYAN+cc+_D+scraper+F.WHITE);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);L=get_input(f"{info} Enter the name of the channel you want to scrape the CCs from: ");V=get_input(f"{info} Enter a custom BIN to scrape (enter to skip): ")
			try:M=int(get_input(f"{info} Enter the number of CCs to scrape: "))
			except ValueError:print_slow(f"{error} Invalid input for the number of CCs",.01,_A);return _B,0,0,0
			D,X,Y,Z=scrape_single_channel(B,L,V,M)
			if D is not _B:
				A=f"Scrapped in {Z:.2f} Sec  ✅\n";A+=P;A+=f"Scraped From  » @{L}\n";A+=f"CC Asked  » {M}\n";A+=f"CC Found  » {X} Cards\n";A+=f"Removed  » {Y} Duplicate Card(s)\n";A+=f"Script Created by @itz_lluigi\n";A+=Q;H=config[_C][S];I=config[_C][T];J={U:open(D,'rb')};K=requests.post(f"https://api.telegram.org/bot{H}/sendDocument?chat_id={I}&caption={A}",files=J)
				if K.status_code==200:print_slow(f"{done} File '{D}' sent to Telegram bot successfully!",.01,_A)
				else:print_slow(f"{error} Failed to send file '{D}' to Telegram bot.",.01,_A)
			B.disconnect()
		elif G=='2':
			os.system(clear);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);print(F.CYAN+cc+_D+scraper+F.WHITE);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);a=get_input(f"{info} Enter channel names in this format 'channel1, channel2, channel3': ");N=[A.strip()for A in a.split(',')];C,O,b,c=scrape_multiple_channels(B,N)
			if C is not _B:
				A=f"Scrapped in {c:.2f} Sec  ✅\n";A+=P;A+=f"Scraped From  » @{', @'.join(N)}\n";A+=f"CC Asked  » {O}\n";A+=f"CC Found  » {O} Cards\n";A+=f"Removed  » {b} Duplicate Card(s)\n";A+=f"Script Created by @itz_lluigi\n";A+=Q;H=config[_C][S];I=config[_C][T];J={U:open(C,'rb')};K=requests.post(f"https://api.telegram.org/bot{H}/sendDocument?chat_id={I}&caption={A}",files=J)
				if K.status_code==200:print_slow(f"{done} File '{C}' sent to Telegram bot successfully!",.01,_A)
				else:print_slow(f"{error} Failed to send file '{C}' to Telegram bot.",.01,_A)
				os.remove(C)
			B.disconnect()
		elif G=='99':
			os.system(clear);print_slow(F.LIGHTMAGENTA_EX+lines,.0085,_A);print(RD+the+_D+underground+R);print_slow(F.LIGHTMAGENTA_EX+lines+W,.0085,_A);print_slow(f"Choose link to get: ",.01,_A);print_slow(f"1. Channel",.01,_A);print_slow(f"2. Group Chat",.01,_A);print_slow(f"3. Channel News",.01,_A);print_slow(f"4. All",.01,_A);E=get_input('> ')
			if E=='1':print_slow(f"Channel » ////Closed",.01,_A)
			elif E=='2':print_slow(f"Group Chat » t.me/+4atVullEWwsxYTA0",.01,_A)
			elif E=='3':print_slow(f"Channel News » t.me/TheUndergroundLink",.01,_A)
			elif E=='4':print_slow(f"Channel » ////Closed",.01,_A);print_slow(f"Group Chat » t.me/+HWm-i0PhYhdmNTQy",.01,_A);print_slow(f"Channel News » t.me/TheUndergroundLink",.01,_A)
			else:print_slow(f"{error} invalid choice. Please choose between 1, 2, 3 or 4.",.01,_A)
			return
		else:print_slow(f"{error} Invalid choice. Please choose either 1, 2 or 99.",.01,_A);return
		d=input(f"{info} Do you want to continue scraping? (y/n): ").lower()
		if d!='y':break
if __name__=='__main__':main()