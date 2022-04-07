import random,requests,random,os,time
E = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
zz = 0
print(E+' — '*15)
Banner = f"""{R}                                                                     \n88888888ba  88            88         \n88      \"8b \"\"            88         \n88      ,8P               88         \n88aaaaaa8P' 88  ,adPPYba, 88   ,d8   \n88\"\"\"\"88'   88 a8\"     \"\" 88 ,a8\"    \n88    `8b   88 8b         8888[      \n88     `8b  88 \"8a,   ,aa 88`\"Yba,   \n88      `8b 88  `\"Ybbd8\"' 88   `Y8a  \n                                     \n                                     \n{R}# {W}Coder : Rick {R}  #   {W}  -\n          {R}-{W} Telegram: https://t.me/KKKFF {R}-\n   {R  }               #{W}   The Best Rick {R} #\n\n"""
print(Banner)  
       
print(' — '*15)
ID = input(' \033[2;34m⌔ \033[1;33mYour \033[1;31mID : ')
print('— — — — — — — — —')
token = input(' \033[1;33m⌔ \033[1;31mYour \033[2;34mToken : ')
print('— — — — — — — — —')
rek = input(C+'⌔ Choose Shape User .\n— — — — — — — — —\n⌔ Ex 1: X1XX11\n⌔ Ex 2: X12BOT\n⌔ Ex 3: XXXX1X\n⌔ Ex 4: XXXX1XX\n⌔ Ex 5: X1XBOT\n⌔ Ex 6: X11X11\n⌔ Ex 7: XX1XX1\n⌔ Ex 8: X1112\n⌔ Ex 9: X11XX1\n⌔ Ex 10: X1222\n⌔ Ex 11: X1XX1\n⌔ Ex 12: X11X1\n⌔ Ex 13: X_X1X\n— — — — — — — — —\n⌔ Number Shape : '+A)
REK = '#Rick'
print('— — — — — — — — —')
pss = input('\x1b[1;37m [~]\x1b[2;36mENTER PASSWORD :  \x1b[1;31m')
if pss == REK:
    print('\x1b[1;32m          SUCCESS PASSWORD Sing In For Your Bot')
    time.sleep(1)
    os.system('clear')
else:
    exit('\x1b[1;31m             WORNG PASSWORD ')
tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- اشتغل البوت انتظر الصيد 😉.\n- Num : {zz}\n- Developers : @HrHrr .''')
i = requests.post(tlg)
oip = 'qwertyuioplkjhgfdsazxcvbnm'
upper = 'A'
number = '1234567890'
uu7 = '_'
all = number + upper + oip
length = 1

if rek == '1':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  o = ''.join(random.sample(oip, length))
  dev = h+s+h+h+s+s
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '2':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = l + h + s +'bot'
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '3':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+h+h+h+s+h
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
   
if rek == '4':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+h+h+h+s+h+h
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '5':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = s + h + s +'bot'
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '6':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = l + h + h + l + h + h 
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '7':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = l+l+s+l+l+s 
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
   
if rek == '8':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+s+s+s+l 
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
  
if rek == '9':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+s+s+h+h+s 
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
  
if rek == '10':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+s+l+l+l
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
   
if rek == '11':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+s+h+h+s
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '12':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+s+s+h+s
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)

if rek == '13':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  dev = h+'_'+h+h+s
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
   
if rek == 'rick':
 while True:
  s = ''.join(random.sample(all, length))
  l = ''.join(random.sample(all, length))
  h = ''.join(random.sample(all, length))
  o = ''.join(random.sample(oip, length))
  ss = '_'
  dev = 's'+s+l+'bot'
  us = f'https://t.me/{dev}'
  zz += 1
  req = requests.get(us)
  if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
   print(F+' ⌔ Done User : '+dev)
   tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌔ New Hit Users Baby .\n— — — — — — — — —\n⌔ User : @{dev}\n⌔ Number Hit : {zz}\n— — — — — — — — —\n⌔ Developers: @HrHrr''')
   i = requests.post(tlg)
  else:
   print(E+' ⌔ Error User : '+dev)
