from http.client import responses
from random import randint
import string,random,asyncio,logging,os,requests,json,stripe,re,time
import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, errors, events
from telethon import Button


api_id = '19084340'
api_hash = 'ddea16f6eecce0a0276c611086ff50f8'
bt = '5009768358:AAGNbzEfUldjFUvAeyhwpO07BnuJx1b58L4'
cc_regex = '(?:^|.*?[^\d])((\d+?)\|(\d{2})\|(\d{2,4}?)\|(\d{3,4}?))'
checkerkey=[]
superuser = [702792106,1687593507,5164193745] #whocan add sks and remove sks
count = 0
LOG_GROUP = -1001672970034
cclist=[]
credits=("\n\n**🧑🏽‍💻 Coded by: FS")

#CC_FILTER
def filter(q):
    cc = "None"
    cvv = "None"
    expm = "None"
    expy = "None"
    for x in q:
        if len(x) == 16: cc = x
        elif len(x) == 15: cc = x
        elif len(x) == 3: cvv = x
        elif len(x) == 2 and int(x) < 13: expm = x
        elif len(x) == 2 and int(x) > 21 and int(x) < 40: expy = x
        elif len(x) == 4 and int(x) > 2021 and int(x) < 2040: expy = x
        elif len(x) == 4: cvv = x
    return cc, expm, expy, cvv

#CC_LIVE_CHECK
def cvvcheck(ccn,ccm,ccy,cvv):
    try:
        tok = stripe.Token.create(
        card={
            "number": ccn,
            "exp_month": ccm,
            "exp_year": ccy,
            "cvc": cvv,
        },)
        custom = stripe.Customer.create(
        description="CustomerH",)
        cc = stripe.Customer.create_source(
        custom["id"],
        source=tok["id"],)
        msg =  (cc["cvc_check"])
        if (cc["cvc_check"]) == "unavailable" or (cc["cvc_check"]) == "pass":
            msg = "Live"
    except stripe.error.CardError as e:
        msg = e
    except stripe.error.RateLimitError as e:
        msg = e
    except stripe.error.InvalidRequestError as e:
        msg = e
    except stripe.error.AuthenticationError as e:
        msg = e
    except stripe.error.APIConnectionError as e:
        msg = e
    except stripe.error.StripeError as e:
        msg = e
    except Exception as e:
        msg = e
    bin = ccn[0:6]
    finaltxt = binck(bin)
       
            
    return msg,finaltxt

#FILTER_4_GEN
def filtergen(ccs):
    bin = "None"
    cvv = "None"
    expm = "None"
    expy = "None"
    for x in ccs:
        if 5 < len(x) < 16: bin = x
        elif len(x) == 3: cvv = x
        elif len(x) == 2 and int(x) < 13: expm = x
        elif len(x) == 2 and int(x) > 21 and int(x) < 40: expy = x
        elif len(x) == 4 and int(x) > 2021 and int(x) < 2040: expy = x
        elif len(x) == 4: cvv = x
    return bin, expm, expy, cvv


#CC_GEN
def gen(bin, expm, expy, cvv):
    if 16 >len(str(bin)) > 0:
        try:
            cc_number = []
            multiplied_by_two = []
            remaining_numbers = []
            new_number = ''
            z = 0
            y = 0
            cccc=''
            while z < 10:
                binx = str(bin)
                cc = str(bin[0:-1])
                num = 15 - len(binx)
                ccend= randint(10**(num-1), (10**num)-1)
                cc = binx+str(ccend)
                starting_15 = cc
                for i in str(starting_15):
                    cc_number.append(int(i))
                    # extract all the numbers that have to be multiplied by 2

                for i in cc_number[0:16:2]:
                    i *= 2
                    if len(str(i)) == 2:        # check if the multiplied number is a two digit number
                        for x in str(i):        # if it is, separate them, and add them together
                            y += int(str(x))
                        i = y
                    multiplied_by_two.append(i)
                    y = 0

                for i in cc_number[1:15:2]:     # extract remaining numbers
                    remaining_numbers.append(i)

                # Luhn's algorithm
                last_digit = ((sum(multiplied_by_two) + sum(remaining_numbers)) * 9) % 10

                for i in cc_number:
                    new_number += str(i)
                if expm == "None":
                    ccm=str(randint(1, 12))
                else:
                    ccm = expm
                if expy == "None":                   
                    ccy=randint(2023, 2032)
                else:
                    ccy = expy
                if cvv == "None":
                    cvvs=str(randint(000, 999))
                else:
                    cvvs = cvv
                ccn= (new_number + str(last_digit))
                ccdetails = (f"{ccn}|{(ccm).zfill(2)}|{ccy}|{(cvvs).zfill(3)}")
                cc_number = []
                multiplied_by_two = []
                remaining_numbers = []
                new_number = ''
                starting_15 = int(starting_15) + randint(-15, 25)
                z += 1
                cccc=cccc+ccdetails+"\n"
        except Exception:
            cccc = "Invalid"
    else:
        cccc = "Invalid"
    return cccc

#CC_BIN_CHECK
def binck(bin):
    try:        
        bindata = requests.get(f'https://lookup.binlist.net/{bin}').json()
        try: 
                if bindata['scheme'] != []:Scheme = bindata['scheme'] 
        except: Scheme = "None"
        try:
                if bindata['type'] != []:Type = bindata['type']
        except: Type = "None"
        try:
                if bindata['brand'] != []:Brand = bindata['brand']
        except: Brand = "None"
        try:
                if bindata['country']['name'] != []:Country = bindata['country']['name']
        except: Country = "None"
        try:
                if bindata['country']['name'] != []:Currency = bindata['country']['currency']
        except: Currency = "None"
        try:
                if bindata['country']['emoji'] != []:Countryemo = bindata['country']['emoji']
        except: Countryemo = "None"
        try:
                if bindata['bank']['name'] != []:Bank = bindata['bank']['name']
        except: Bank = "None"

        bindata = '''BIN: {}
Scheme:  {}
Type:  {}
Brand: {}
Currency: {}
Country:   {} {}
Bank:  {}'''.format(bin,Scheme,Type,Brand,Currency,Country,Countryemo,Bank)

    except:
            bindata = bin

    return bindata

#CC_CHARGE
def charge(cc,expm,expy,cvv):
    
    r = stripe.Token.create(
    card={
        "number": cc,
        "exp_month": expm,
        "exp_year": expy,
        "cvc": cvv,
    },
    )
    tok = r.get("id")

    c = stripe.Charge.create(
    amount=60,
    currency="usd",
    source=tok,
    description="Fsociety Checker @USERID_Null",
    )
    bin = cc[0:6]
    finaltxt = binck(bin)
    
    return c,finaltxt
    

bot = TelegramClient('name', api_id, api_hash).start(bot_token=bt)

@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='\/addsk sk_(test|live)_[A-Za-z0-9]+'))
async def handler(event):
    sender = await event.get_sender()
    id = sender.id
    if id in superuser:
        msg=event.message.text
        msg= msg.replace("/addsk","")
        msglist = msg.split()
        for item in msglist:
            if 'sk_live_' in item:
                key=item
                try:

                    stripe.api_key=key
                    t = stripe.Source.create(
                    type='card',
                    card={
                    'number':'4373072001216886',
                    'cvc':'842' ,
                    'exp_month':'10' ,
                    'exp_year':'26'
                    }
                    )
                    pass
                    if t["card"]["exp_month"]==10:
                        await event.reply("**SK Added** 😈")
                        checkerkey.clear()
                        checkerkey.append(msg)
                        return checkerkey
                    pass  
                except stripe.error.CardError as e:
                    await event.reply("**DEAD SK** 💩")
                    pass
                except stripe.error.RateLimitError as e:
                    await event.reply("**DEAD SK, RATE LIMITED** 🫠")
                    pass
                except stripe.error.InvalidRequestError as e:
                    if 'Your card was declined.' in e.user_message:
                        await event.reply("**SK Added** 😈")
                        checkerkey.clear()
                        checkerkey.append(msg)
                    else:
                        await event.reply("**DEAD SK** 💩")
                    pass
                except stripe.error.AuthenticationError as e:
                    await event.reply("**DEAD SK** 💩")
                    pass
                except stripe.error.APIConnectionError as e:
                    await event.reply("**DEAD SK** 💩")
                    pass
                except stripe.error.StripeError as e:
                    await event.reply("**DEAD SK** 💩")
                    pass
                except Exception as e:
                    if t["card"]["exp_month"]==10:
                        await event.reply("**SK Added** 😈")
                        checkerkey.clear()
                        checkerkey.append(msg)
                        return checkerkey
                    else:
                        await event.reply("**DEAD SK** 💩")
                    pass


@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='\/chg'))
async def runnr(event):
    if event.is_reply:
        ms = await event.get_reply_message()
        msg = ms.message
    else:
        msg = event.message.text
    sender = await event.get_sender()
    id = sender.id
    ccs = re.findall(cc_regex, msg)
    if len(ccs) == 0:
        return
    if checkerkey == []:
        await event.reply("No SK Found\nUse /addsk to add a live SK")
    else:
        log = "Please wait"
        usr_msg = await event.reply(log)
        reply=""
        log=''
        ratelimitcount = 0
        for cc in ccs:
            cc, expm, expy, cvv = filter(cc)
            f_cc = (f'''{cc}|{expm}|{expy}|{cvv}''')
            try:
                stripe.api_key = checkerkey[0]
                c,finaltxt = charge(cc,expm,expy,cvv)
                suc_response = c
                seller_message = suc_response.outcome.get("seller_message")
                risk_level = suc_response.outcome.get("risk_level")
                risk_score = suc_response.outcome.get("risk_score")
                receipt = suc_response.get("receipt_url")
                country = suc_response.payment_method_details.card.get("country")
                funding = suc_response.payment_method_details.card.get("funding")
                reply =(f'''**#Charged 0.6 $✅**\n{f_cc}\n
**MESSAGE** : {seller_message} ✪ **FUNDING** : {funding}   ✪ **COUNTRY** : {country}   ✪ **RISK LEVEL** : {risk_level}   ✪ **RISK SCORE** : {risk_score}   ✪ [RECEIPT]({receipt}){finaltxt}
=====================================\n''')            
                log = log+"\n"+reply
                if(len(log) > 4000):
                    log = reply
                    usr_msg = await event.reply(log)
                else:
                    await usr_msg.edit(log)


            except Exception as e:
                try:
                    code = (e.code)
                except:
                    code = ("Error")
                message = (e.user_message)
                if 'rate limit' in message:
                    ratelimitcount = ratelimitcount + 1
                if ratelimitcount == 5:
                    await event.reply("Sk rate limited process terminated")
                    break
                reply=(f'''**#DECLINED ❌** \n```{f_cc}```\n ✪ **RESPONSE** : {code}   ✪ **MESSAGE** : {message[0:48]}\n''')
                log = log+"\n"+reply
                if(len(log) > 4000):
                    log = reply
                    usr_msg = await event.reply(log)
                else:
                    await usr_msg.edit(log)

#cvv check
@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='\/chk'))
async def runnr(event):
    if event.is_reply:
        ms = await event.get_reply_message()
        msg = ms.message
    else:
        msg = event.message.text
    sender = await event.get_sender()
    id = sender.id
    ccs = re.findall(cc_regex, msg)
    if len(ccs) == 0:
        return
    if checkerkey == []:
        await event.reply("No SK Found\nUse /addsk to add a live SK")
    else:
        log = "Please wait"
        usr_msg = await event.reply(log)
        reply=""
        log=''
        ratelimitcount = 0
        for cc in ccs:
            cc, expm, expy, cvv = filter(cc)
            f_cc = (f'''{cc}|{expm}|{expy}|{cvv}''')
            stripe.api_key = checkerkey[0]
            msg,finaltxt = cvvcheck(cc,expm,expy,cvv)
            if msg == "Live":
                reply =(f'''**#LIVE✅**\n{f_cc}
{finaltxt}
=====================================\n''')
            else:
                try:
                    msgs =(str(msg).split(':')[1])
                except:
                    msgs =(str(msg))
                    if 'rate-limits.' in msgs:
                        ratelimitcount = ratelimitcount + 1
                    if ratelimitcount == 5:
                        await event.reply("Sk rate limited process terminated")
                        break
                reply=(f'''**#Dead ❌** \n```{f_cc}```
{msgs}
{finaltxt}
=====================================''')           
            log = log+"\n"+reply
            if(len(log) > 4000):
                log = reply
                usr_msg = await event.reply(log)
            else:
                await usr_msg.edit(log)


@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='/rmkey'))
async def handler(event):
    sender = await event.get_sender()
    id = sender.id
    if id in superuser:
        msg=event.message.text
        await event.reply("**KEY DELETED**")
        checkerkey.clear()


@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='/gen (\d+)'))
async def handler(event):
    msg =event.message.text
    bin = msg.split(" ")[1]
    chatid =event.chat.id
    ccs = re.findall('(\d+)',bin)
    rid = event.id
    for digits in ccs:
        if len(digits)>15:
            await bot.send_file(chatid,"big.jpg",reply_to=rid,caption="Wow Thats So LONGGGG\nI Dont think i can handle that")
            return
    bin, expm, expy, cvv = filtergen(ccs)
    cccc=''
    log = await event.reply("Please wait")
    try:  
        if bin != "None":
            cccc = gen(bin, expm, expy, cvv)
            await log.edit(cccc)
    except:
        await log.edit('Error')

@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='/bin (\d+)'))
async def handler(event):
    msg =event.message.text
    bin = msg.split(" ")[1]
    if len(bin) < 6:
        await event.reply("Please Enter 6 or more")
    else:
        log = await event.reply("Please wait")        
        bin6 = bin[0:6]
        bindata =binck(bin6)
        await log.edit(bindata)
        


@bot.on(events.NewMessage(chats= LOG_GROUP,pattern='/addr'))
async def handler(event):
    r = requests.get('https://random-data-api.com/api/v2/users')
    responce_data = r.json()
    d1 = responce_data.get('id')
    d2 = responce_data.get('first_name')
    d3 = responce_data.get('last_name')
    d4 = responce_data.get('email')
    d5 = responce_data.get('avatar')
    d6 = responce_data.get('gender')
    d7 = responce_data.get('phone_number')
    d8 = responce_data.get('date_of_birth')
    d9 = responce_data.get('address').get('city')
    d10 = responce_data.get('address').get('street_address')
    d11 = responce_data.get('address').get('street_name')
    d12 = responce_data.get('address').get('zip_code')
    d13 = responce_data.get('address').get('state')
    d14 = responce_data.get('address').get('country')
    d15 = responce_data.get('social_insurance_number')
    d16 = responce_data.get('employment').get('title')

    addr = (f'''{d5}

**Name**
    {d2} {d3}
**DOB** 
    {d8}

**Address**
    {d10}
    {d11}
    {d9}
    {d13} {d12}
    {d14}

**Phone**
    {d7}

**Email**
    {d4}

**Gender**
    {d6}

**S.Insurance**
    {d15}

**Title**
    {d16}

**Code**
    {d1}''')

    await event.reply(addr)

    
print('Stripe_bot started')
bot.run_until_disconnected()
