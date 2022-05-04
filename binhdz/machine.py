
import datetime,hashlib
from tabnanny import check
from tkinter import messagebox
from webbrowser import get
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.proxy import *
import anycaptcha
from anycaptcha import *
import requests,json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui,pickle
os.system('title Machine-Liker Bybass Cloudflare + Captcha Version 2.2 By Hoàng Đình Thanh Bình')
def logo():
    os.system('cls')
    log=""""""
    print(log)
def cre_mã():
    số_kí_tự_in_chuỗi = 8
    kí_tự_số = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    kí_tự_chữ = ['A', 'B', 'Y',
                        'Z']
    set_chuỗi = kí_tự_số + kí_tự_chữ
    random_số = random.choice(kí_tự_số)
    random_chữ = random.choice(kí_tự_chữ)
    ghép = random_số + random_chữ
    for x in range(số_kí_tự_in_chuỗi):
        ghép = ghép + random.choice(set_chuỗi)
        import array
        ghép_list = array.array('u', ghép)
        random.shuffle(ghép_list)
    password = "Team-Py-"
    for x in ghép_list:
            password = password + x
    return password
    logo()
fol_mã=r"C:\System\AppData\Win32\Team-Py\Program\Auto-TDS-TTC-YTB"
if os.path.exists(fol_mã) == False:
    os.makedirs(fol_mã, mode=0o777, exist_ok=True)
elif os.path.exists(fol_mã) == True:
    pass
if os.path.exists(f'{fol_mã}\device.txt')==False:
    mã_máy=cre_mã()
    filea=open(f'{fol_mã}\device.txt', "w+")
    filea.write(mã_máy)
    filea.close()
dev=open(f'{fol_mã}\device.txt', "r")
device=dev.read()
dev.close()
dev=open(f'{fol_mã}\device.txt', "r")
device=dev.read()
dev.close()
if os.path.exists(fol_mã) == False:
    os.makedirs(fol_mã, mode=0o777, exist_ok=True)
elif os.path.exists(fol_mã) == True:
    pass
he=hashlib.md5(bytes('HDTB - '+str(device), 'utf-8-sig')).hexdigest()
device='HDTB - '+str(he[0:14])
try:
    check_key=requests.get('https://pastebin.com/raw/uVs0hXUZ').text
except:
    check_key=requests.get('https://pastebin.com/raw/uVs0hXUZ').text
if device in check_key:
    pass
else:
    print( f'\033[1;36m[ ● ] Mã Máy: {device}')
    print("\033[1;36m[ ● ] Tool Miễn Phí Nhưng Key Mất Phí")
    print("\033[1;36m[ ● ] Vui Lòng Liên Hệ Zalo : 0869161198 Để Kích Hoạt Key!! ")
    time.sleep(1000)
    quit()
os.system("clear")
logo()
us=input(''' \033[1;37m➻\033[1;96m❥ Vui lòng viết thường
 \033[1;37m➻\033[1;96m❥ Very Mã Code Thủ Công Hay Auto (tay/auto): ''')
if us == 'tay':
    pass
else:
    print('\033[1;31m[\033[1;33m WARRING\033[1;31m]\033[1;36m Lây cookie bằng m.facebook.com/profile.php')
    cookie_fb=input(' \033[1;37m➻\033[1;96m❥\033[1;32m Nhập cookie Facebok: ')
#cookie_fb='sb=4mYQYsw1R8qwxHHYD9XJ-zO-;datr=4mYQYroRpk87Nu4I5VTo2Che;c_user=100046543398712;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1645959175560%2C%22v%22%3A1%7D;xs=31%3AvybBVaZAAoMkog%3A2%3A1645328289%3A-1%3A6319%3A%3AAcUzAZkKZBIEj3Z9R7eit-5osAqFbkrBRl030sgLfKs;fr=0aXuV7q1A8pPK8cKg.AWVNQunA3Zp_rbkDUvn4G1rz94M.BiG4ZF.ct.AAA.0.0.BiG4ZF.AWXK3bm_iP4;'
url_post=input(" \033[1;37m➻\033[1;96m❥\033[1;32m Nhập Link Cần Buff Cảm Xúc:\033[1;33m ")
logo()
import sys
o=""" \033[1;37m[\033[1;31m1\033[1;37m] \033[1;31m=> \033[1;32mBUFF LIKE
 \033[1;37m[\033[1;31m2\033[1;37m] \033[1;31m=> \033[1;32mBUFF LOVE
 \033[1;37m[\033[1;31m3\033[1;37m] \033[1;31m=> \033[1;32mBUFF WOW
 \033[1;37m[\033[1;31m4\033[1;37m] \033[1;31m=> \033[1;32mBUFF HAHA
 \033[1;37m[\033[1;31m7\033[1;37m] \033[1;31m=> \033[1;32mBUFF BUỒN
 \033[1;37m[\033[1;31m8\033[1;37m] \033[1;31m=> \033[1;32mBUFF PHẪN NỘ
 \033[1;37m[\033[1;31m16\033[1;37m] \033[1;31m=> \033[1;32mBUFF THƯƠNG THƯƠNG
 \033[1;37m[\033[1;31m999\033[1;37m] \033[1;31m=> \033[1;32mBUFF ALL
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
for oo in o:
    sys.stdout.write(oo)
    sys.stdout.flush()
    sleep(0.003)
print(' \033[1;37m➻\033[1;96m❥ Mỗi Số Ngăn Cách Bởi Dấu \033[1;37m"\033[1;33m,\033[1;37m" \033[1;31m[\033[1;32m 1,2,3\033[1;31m ]')
pick=input(' \033[1;37m➻\033[1;96m❥ Nhập Loại Cảm Xúc: \033[1;33m')
if pick == '999':
    pick="1,2,3,4,7,8,16"
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--window-size=580,800")
chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
chromeoptions.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_setting_values.notifications" : 2}
chromeoptions.add_experimental_option('useAutomationExtension', False)
#chromeoptions.add_argument(f"--user-data-dir=D:\python\datachrome")
chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
#chromeoptions.add_argument('--incognito')
chromeoptions.add_experimental_option("prefs",prefs) 
driver = webdriver.Chrome(options=chromeoptions)
driver.set_window_position(0, 0)
driver.get('https://www.machine-liker.com/login/');sleep(2)
driver.execute_script("""window.open('https://www.machine-liker.com/login/')""")
sleep(7)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.execute_script("""window.open('https://www.machine-liker.com/login/')""")
sleep(7)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.refresh()
time.sleep(3)
try:
    code=driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[1]/div/input').get_attribute("value")
except:
    print('\033[1;31m Bybass Cloud Flare Thất Bại')
    time.sleep(1000)
    quit()
if us == "tay":
    print('''Nhập link lên trình duyệt có sẵn Facebook và xác nhận''')
    print(f'''Link: https://facebook.com/device?user_code={code}
    ''')
    input('Xác nhận xong quay lại đây ân ENTER')
else:
    try:
        print(f'\033[1;32m Đang Veri Code {code} Auto Bằng Cookie...   ', end="\n")
        headers = {
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                'sec-ch-ua-mobile': '?1',
                'save-data': 'on',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cookie': cookie_fb
        }
        check_dv = requests.get(f'https://mbasic.facebook.com/device?user_code={code}', headers=headers).text
        try:
                    fb_dtsg = check_dv.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
                    jazoest = check_dv.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
                    qr = check_dv.split('name="qr" value="')[1].split('"')[0]
        except:
                    print('Cookie die')
        headers = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?1',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'save-data': 'on',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': cookie_fb
                }
        data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'qr': qr,
                    'user_code': code
                }
        url_c = requests.post('https://mbasic.facebook.com/device/redirect/', headers=headers, data=data).url
        from urllib.parse import unquote
        for x in range(10):
            try:
                url_f = unquote(url_c).split('&next=')[1]
                break
            except:
                time.sleep(0.8)
        headers = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'save-data': 'on',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?1',
                    'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': cookie_fb
                }
        find_data = requests.get(url_f, headers=headers).text
        fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
        scope = find_data.split('name="scope" value="')[1].split('"')[0]
        jazoest = find_data.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
        logger_id = find_data.split('name="logger_id" value="')[1].split('"')[0]
        user_code = find_data.split('name="user_code" value="')[1].split('"')[0]
        encrypted_post_body = find_data.split('name="encrypted_post_body" value="')[1].split('"')[0]
        headers = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'origin': 'https://mbasic.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'referer': url_f,
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': cookie_fb
                }
        data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'from_post': '1',
                    'deduplicate': '',
                    'link_customer_account': '',
                    'read': '',
                    'link_news_subscription': '',
                    'write': '',
                    'extended': '',
                    'confirm': '',
                    'reauthorize': '',
                    'user_messenger_contact': '',
                    'seen_scopes': '',
                    'response_type': 'code',
                    'auth_type': 'rerequest',
                    'auth_nonce': '',
                    'calling_package_key': '',
                    'default_audience': '',
                    'dialog_type': 'gdp_v4',
                    'fbapp_pres': '',
                    'ret': '',
                    'return_format': 'code',
                    'domain': '',
                    'scope': scope,
                    'sso_device': '',
                    'logger_id': logger_id,
                    'sheet_name': 'initial',
                    'fallback_redirect_uri': '',
                    'sdk': '',
                    'facebook_sdk_version': '',
                    'sdk_version': '',
                    'user_code': user_code,
                    'logged_out_behavior': '',
                    'install_nonce': '',
                    'l_nonce': '',
                    'original_redirect_uri': '',
                    'loyalty_program_id': '',
                    'messenger_page_id': '',
                    'reset_messenger_state': '',
                    'aid': '',
                    'deferred_redirect_uri': '',
                    'code_redirect_uri': '',
                    'extras': '',
                    'tp': 'unspecified',
                    'fx_app': '',
                    'is_promote_auth': '',
                    'encrypted_post_body': encrypted_post_body,
                    'cbt': '',
                    '__CONFIRM__': 'Tiếp+tục'
                }
        do = requests.post('https://mbasic.facebook.com/v2.0/dialog/oauth/confirm/', headers=headers, data=data)
        url_z = unquote(do.url).split('next=')[1]
        headers = {
                    'Host': 'mbasic.facebook.com',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?1',
                    'save-data': 'on',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'none',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': cookie_fb
                }
        don = requests.get(url_z, headers=headers)
        if 'Bạn hiện được kết nối với' in don.text:
            print('Success')
            
        else:
            quit()
    except:
        print('\033[1;31m Cookie lỗi rồi....')
        time.sleep(100)
        quit()
user_agent = driver.execute_script("return navigator.userAgent;")
def check_cookie(cookie):
  headers={
    "Host":"www.machine-liker.com",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":user_agent,
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "cookie":cookie
  }
  check_ck=requests.get("http://www.machine-liker.com/dashboard/",headers=headers, verify=False, allow_redirects=True, timeout=50).text
  return check_ck
ckkk=[]
list_ck=[]

for x in driver.get_cookies():
    ckkk.append(x['name']+'='+x['value'])
ck=';'.join(ckkk)+';'
list_ck.append(ck)

def get_ck():
    list_ck.clear()
    driver.refresh()
    time.sleep(3)
    driver.execute_script("""window.open('https://www.machine-liker.com/')""")
    sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    driver.execute_script("""window.open('https://www.machine-liker.com/')""")
    sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(3)
    ckkk.clear()
    for x in driver.get_cookies():
        ckkk.append(x['name']+'='+x['value'])
    cok=';'.join(ckkk)+';'
    list_ck.append(cok)
try:
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div[4]/button').click()
except:
    pass
import os
os.system('cls')
driver.set_page_load_timeout(100)
time.sleep(5)
for x in range(10):
    try:
        keyy=driver.page_source.split('data-sitekey="')[1].split('"')[0]
        url=driver.current_url
        break
    except:
        pass
    time.sleep(1)
if 'verify' not in url:
    quit('có lỗi')
print('\033[1;32mĐang giải captcha   ', end='\r')
key_any='e85ab42de4da462e950d905082136396'
gg=anycaptcha.captcha(url, keyy, key_any)
try:
    driver.execute_script(f'''document.getElementById("g-recaptcha-response").innerHTML="{gg}"''')
except:
    print('\033[1;31m Giải captcha thất bại...')
print('\033[1;32m Giải captcha thành công...')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/button').click()
login=check_cookie(ck)
logo()
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
if 'User ID' in login:
    id_fb=login.split('User ID:</strong> ')[1].split('</h5>')[0]
    namefb=login.split('="true" aria-expanded="false"><i class="fas fa-user"></i> ')[1].split('</a>')[0]
    print(f' \033[1;37m➻\033[1;96m❥\033[1;32m Login Thành Công Với FB: \033[1;33m{namefb} \033[1;32m ID: \033[1;37m{id_fb}')
    print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
else:
    print('\033[1;31m Login Fald')
    time.sleep(100)


stt=0
while(True):
    for ck in list_ck:
        for x in range(10):
            try:
                while(True):
                    headers_new={
                    "Host":"www.machine-liker.com",
                    "x-requested-with":"XMLHttpRequest",
                    "user-agent":user_agent,
                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                    "cookie":ck
                    }
                    
                    
                    data={

                    "url":url_post
                    }

                    info=requests.post("https://www.machine-liker.com/api/get-post-info/",data=data,headers=headers_new,allow_redirects=False,timeout=60).json()
                    check_status=info['status']
                    if check_status == 'fail':
                        if info['error']['message'] == 'The post is either invalid or not public, please check and try again.':
                            exit("\033[1;31m Bật Công Khai Bài Viết Lên ĐCM =)")
                    elif check_status == 'ok':
                        id=info["post"]["id"]
                        story=info["post"]["story"]
                    sleep(2)
                    link=requests.get(f"https://www.machine-liker.com/send-reactions/?post_id={id}&story={story}",headers=headers_new).text
                    pr=link.split('name="object_id" value="')[1].split('"')[0]
                    data2={
                        "object_id":pr,
                        "reactions":pick,
                        "limit":"150"
                    }
                    stt+=1
                    send=json.loads(requests.post("https://www.machine-liker.com/api/send-reactions/",data=data2,headers=headers_new).text)
                    if send['status'] == 'ok':
                        so_rec=send['info']['message'].split(' ')[0]
                        tổng=send['info']['total_reactions']
                        from datetime import datetime
                        tg=datetime.now().strftime('%H:%M:%S')
                        print(f"\033[1;31m [ \033[1;33m{tg}\033[1;31m ] <> \033[1;31m[ \033[1;33mH D T B\033[1;31m ] \033[1;37m=> \033[1;32mTăng Thành Công \033[1;33m{so_rec} \033[1;37mReactions => Tổng: \033[1;33m{tổng} \033[1;32mReactions")
                        for a in range(600,0,-1):
                            print(f' \033[1;37m➻\033[1;96m❥ Tiếp Tục Buff Sau {a} Giây   ',end='\r')
                            sleep(1)
                            print(f' \033[1;37m➻\033[1;96m❥ Tiếp Tục Buff Sau {a} Giây   ',end='\r')
                    else:
                        for a in range(600,0,-1):
                            print(f' \033[1;37m➻\033[1;96m❥ Tiếp Tục Buff Sau {a} Giây   ',end='\r')
                            sleep(1)
                            print(f' \033[1;37m➻\033[1;96m❥ Tiếp Tục Buff Sau {a} Giây   ',end='\r')
                    break
            except:
                sleep(0.5)
        get_ck()
        continue
