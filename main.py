#!/usr/bin/env python3
# SRC_BUY_ARAFAT
# Ethekal_Hacked LOADED — Telegram Bot

import os
import sys
import re
import random
import string
import time
import json
import uuid
import platform
import requests
import subprocess
import logging
import hashlib
import asyncio
from typing import Set, Optional, Dict

# ---------- AUTO INSTALL ----------
def _ensure(pkg, mod=None):
    try:
        __import__(mod or pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

for _p, _m in [("beautifulsoup4","bs4"), ("fake-useragent","fake_useragent"),
               ("faker","faker"), ("pyotp","pyotp"),
               ("python-telegram-bot","telegram")]:
    _ensure(_p, _m)

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker
import pyotp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters, ContextTypes
)

# ================= BOT CONFIG =================
BOT_TOKEN = "8864774866:AAGCGEPBwlS3jCmoHagUuYr3dMUakXIz3bo"
ADMIN_ID  = None

# ================= LOGGING =================
logging.basicConfig(level=logging.INFO, filename="app.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ANSI
W = '\033[97m'; G = '\033[92m'; R = '\033[91m'; V = '\033[1;34m'; B = '\033[1;30m'; RESET = '\033[0m'

fake = Faker()
ua = UserAgent()

CONFIG = {
    "output_dir": os.path.expanduser("~/PREMIUM") if platform.system().lower() != 'android' else "/sdcard/PREMIUM-XD",
}
os.makedirs(CONFIG["output_dir"], exist_ok=True)


def install_dependencies():
    try:
        import pyotp  # noqa
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyotp"])
        except Exception as e:
            logging.error(f"Failed to install pyotp: {e}")
            sys.exit(1)


def clear_screen():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')


def linex():
    print(f"{W}─────────────────────────────────────────────{W}")


def banner():
    clear_screen()
    print(f"""{G}
      PREMIUM  PREMIUM  PREMIUM
{W}─────────────────────────────────────────────{W}
{W}[{G}•{W}]{G} DEVELOPER {W}:{G} PREMIUM USER
{W}[{G}•{W}]{G} VERSION   {W}:{G} PREMIUM VIP
{W}[{G}•{W}]{G} TOOL      {W}:{G} Auto Create FB
{W}─────────────────────────────────────────────{W}""")


# ================= USER-AGENT GENERATOR =================
ua = UserAgent()


def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))


ugen = []
for xd in range(5000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen.append(um2); ugen.append(um3); ugen.append(um1); ugen.append(um4)

for xhd in range(500):
    a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
    b = random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    c = random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    b2 = random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    c2 = random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
    ugen.append(d)

for xd in range(500):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39', 'JZO54K']
    oppo = ["CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805","CPH1809","CPH1851","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH2061","CPH2069","CPH2127","CPH2131","CPH2139","CPH2135","CPH2239","CPH2195","CPH2273","CPH2325","CPH2309","CPH1701","CPH2387","CPH1909","CPH1920","CPH1912","CPH1901","CPH1903","CPH1905","CPH1717","CPH1801","CPH2067","CPH2099","CPH2161","CPH2219","CPH2197","CPH2263","CPH2375","CPH2339","CPH1715","CPH2385","CPH1729","CPH1827","CPH1938","CPH1937","CPH1939","CPH1941","CPH2001","CPH2021","CPH2059","CPH2121","CPH2123","CPH2203","CPH2333","CPH2365","CPH1913","CPH1911","CPH1915","CPH1969","CPH2209","CPH1987","CPH2095","CPH2119","CPH2285","CPH2213","CPH2223","CPH2363","CPH1609","CPH1613","CPH1723","CPH1727","CPH1725","CPH1819","CPH1821","CPH1825","CPH1881","CPH1823","CPH1871","CPH1875","CPH2023","CPH2005","CPH2025","CPH2207","CPH2173","CPH2307","CPH2305","CPH2337","CPH1955","CPH1707","CPH1719","CPH1721","CPH1835","CPH1831","CPH1833","CPH1879","CPH1893","CPH1877","CPH1607","CPH1611","CPH1917","CPH1919","CPH1907","CPH1989","CPH1945","CPH1951","CPH2043","CPH2035","CPH2037","CPH2036","CPH2009","CPH2013","CPH2113","CPH2091","CPH2125","CPH2109","CPH2089","CPH2065","CPH2159","CPH2145","CPH2205","CPH2201","CPH2199","CPH2217","CPH1921","CPH2211","CPH2235","CPH2251","CPH2249","CPH2247","CPH2237","CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979"]
    redmi = ["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG ","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C","M2012K11C","22021211RC"]
    infinix = ["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624","X655F","X689C","X608","X698","X682B","X682C","X688C","X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675","X6812B","X6812","X6817B","X6817","X6816C","X6816","X6816D","X668C","X665B","X665E","X510","X559C","X559F","X559","X606","X606C","X606D","X623","X624B","X625C","X625D","X625B","X650D","X650B","X650","X650C","X655C","X655D","X680B","X573","X573B","X622","X693","X695C","X695D","X695","X663B","X663","X670","X671","X671B","X672","X6819","X572","X572-LTE","X571","X604","X610B","X690","X690B","X656","X692","X683","X450","X5010","X501","X401","X626","X626B","X652","X652A","X652B","X652C","X660B","X660C","X660","X5515","X5515F","X5515I","X609B","X5514D","X5516B","X5516C","X627","X680","X653","X653C","X657","X657B","X657C","X6511B","X6511E","X6511","X6512","X6823C","X612B","X612","X503","X511","X352","X351","X530","X676C","X6821","X6823","X6827","X509","X603","X6815","X620B","X620","X687B","X6811B","X6810","X6811"]
    samsung = ["E025F","G996B","A826S","E135F","G781B","G998B","F936U1","G361F","A716S","J327AZ","E426B","A015F","A015M","A013G","A013M","A013F","A022M","A022G","A022F","A025M","S124DL","A025U","A025A","A025G","A025F","A025AZ","A035F","A035M","A035G","A032F","A032M","A037F","A037U","A037M","S134DL","A037G","A105G","A105M","A105F","A105FN","A102U","S102DL","A102U1","A107F","A107M","A115AZ","A115U","A115U1","A115A","A115M","A115F","A125F","A127F","A125M","A125U","A127M","A135F","A137F","A135M","A136U","A136U1","A136W","A260F","A260G","A205GN","A205U","A205F","A205G","A205FN","A202F","A2070","A207F","A207M","A215U","A215U1","A217F","A217M","A225F","A225M","A226B","A226BR","A235F","A235M","A300FU","A300F","A300H","A310F","A310M","A320FL","A320F","A305G","A305GT","A305N","A305F","A307FN","A307G","A307GN","A315G","A315F","A325F","A325M","A326U","A326W","A336E","A336B","A430F","A405FN","A405FM","A3051","A3050","A415F","A426U","A426B","A5009","A500YZ","A500Y","A500W","A500L","A500X","A500XZ","A510F","A510Y","A520F","A520W","A500F","A500FU","A500H","S506DL","A505G","A505FN","A505U","A505GN","A505F","A507FN","A5070","A515F","A515U","A515U1","A516U","A516V","A516N","A516B","A525F","A525M","A526U","A526U1","A526B","A526W","A528B","A536B","A536U","A536E","A536V","A600FN","A600G","A605FN","A605G","A605GN","A605F","A6050","A606Y","A6060","G6200","A700FD","A700F","A7000","A700H","A700YD","A710F","A710M","A720F","A750F","A750FN","A750GN","A705FN","A705F","A705MN","A707F","A715F","A715W","A716U","A716V","A716U1","A716B","A725F","A725M","A736B","A530F","A810YZ","A810F","A810S","A530W","A530N","G885F","G885Y","G885S","A730F","A805F","G887F","G8870","A9000","A920F","G887N","A910F","G8850","A908B","A908N","A9080"]
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugen.append(strvoppo); ugen.append(strvredmi); ugen.append(strvoppo1)
    ugen.append(strvinfinix); ugen.append(strvsamsung); ugen.append(strvredmi1); ugen.append(strvnokiax)

for op in range(500):
    rr = random.randint; rc = random.choice
    bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000,39000))}/{str(rr(190,199))}.{str(rr(270,290))}; U; {bahasa}) Presto/2.{str(rr(4,20))}.{str(rr(420,490))} Version/12.16"
    ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000,39000))}/{str(rr(190,199))}.{str(rr(270,290))}; U; {bahasa}) Presto/2.{str(rr(4,20))}.{str(rr(420,490))} Version/12.16"
    ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000,39000))}/{str(rr(190,199))}.{str(rr(270,290))}; U; {bahasa}) Presto/2.{str(rr(4,20))}.{str(rr(420,490))} Version/12.16"
    ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000,39000))}/{str(rr(190,199))}.{str(rr(270,290))}; U; {bahasa}) Presto/2.{str(rr(4,20))}.{str(rr(420,490))} Version/12.16"
    ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000,39000))}/{str(rr(190,199))}.{str(rr(270,290))}; U; {bahasa}) Presto/2.{str(rr(4,20))}.{str(rr(420,490))} Version/12.16"
    ugen.append(ua1); ugen.append(ua2); ugen.append(ua3); ugen.append(ua4); ugen.append(ua5)

for generate in range(100):
    a = random.randrange(1, 9); b = random.randrange(1, 9)
    c = random.randrange(73, 100); d = random.randrange(4200, 4900); e = random.randrange(40, 150)
    ugen.append(f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36')


# ================= NAMES =================
first_names = [
    "Ayesha","Sumaiya","Mitu","Sharmin","Nusrat","Moushumi","Laboni","Rumana","Lamia","Sadia",
    "Farzana","Tania","Shanta","Nadia","Salma","Nargis","Shabnam","Mim","Jannat","Priya",
    "Afia","Jerin","Mahira","Sinthia","Oishee","Trisha","Rakhi","Puja","Ema","Sabrina",
    "Tahmina","Naznin","Rifat","Antora","Nilufa","Elma","Bonna","Sanjida","Riya","Mahi",
    "Sumi","Arpita","Tumpa","Pinky","Munia","Tuli","Runa","Rupsha","Nasima","Sharifa",
    "Kaniz","Taslima","Faria","Joya","Khadija","Fatema","Halima","Shorna","Ishita","Mou",
    "Sumona","Konika","Anika","Afroza","Sanjana","Nourin","Falguni","Reshma","Bonhi","Aklima",
    "Jerin","Salma","Tisha","Sinthi","Shimul","Nabila","Noshin","Tania","Minu",
    "Tanjina","Anjuman","Ruksana","Dilruba","Sumaira","Samia","Rashida","Nishat","Asma","Lubna",
    "Mahiya","Zinia","Tanima","Monira","Nilufa","Narmeen","Sabila","Jinnat","Mahbuba","Borsha",
    "Nadia","Sharmin","Rokeya","Nahida","Shathi","Anamika","Rokhshana","Mahinur","Sanjida","Morsheda",
    "Khadiza","Sayma","Rumana","Zakia","Suborna","Fariha","Sultana","Farzana","Tumpa","Sadia",
    "Nargis","Rodela","Sabrina","Shaima","Najma","Khaleda","Tanzila","Nushrat","Samira","Anisa",
    "Tanjila","Tasfia","Mim","Trina","Zara","Arifa","Khadija","Laila","Mahima","Fatima",
    "Afia","Sanjida","Sanjiya","Moyna","Dipa","Tanima","Nishita","Alifa","Nazira","Raisa",
    "Afsana","Rubina","Minara","Morium","Nila","Kanta","Sumona","Bithi","Moyna","Adiba",
    "Lopa","Elora","Rehana","Purnima","Aklima","Sharmin","Shaheda","Tanjuma","Pakhi","Afsari",
    "Mobina","Khadiza","Niloy","Sharmi","Jerin","Tumpa","Urmi","Sweety","Jumaiya","Shanta",
    "Arin","Taslima","Naznin","Samia","Fariha","Karishma","Zarifa","Asifa","Tani","Anonna",
    "Rokshana","Mousumi","Eshita","Tanisha","Moumita","Nusrat","Taniya","Oni","Marjia","Nashita",
    "Nashrin","Fozia","Sinthia","Tanjina","Nazma","Papia","Lubaba","Nilufa","Ashfia","Shama",
    "Sayda","Rahima","Masuma","Monika","Riyana","Jesmin","Humaira","Maisha","Sumita","Anjuli"
]
surnames = ["Akter","Begum","Khatun","Sultana","Haque","Rahman","Chowdhury","Islam","Jahan","Parvin"]


def get_bd_name():
    return random.choice(first_names), random.choice(surnames)


def extractor(data):
    soup = BeautifulSoup(data, "html.parser")
    data = {}
    for inputs in soup.find_all("input"):
        name = inputs.get("name"); value = inputs.get("value")
        if name:
            data[name] = value
    return data


def check_facebook_profile_picture(uid):
    pic_url = f"https://graph.facebook.com/{uid}/picture?type=normal"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"}
    try:
        response = requests.get(pic_url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            return "live" if "scontent" in redirect_url else "not_live"
        return None
    except requests.RequestException:
        return None


# ================= COOKIE FORMATTER =================
def get_all_cookies(session):
    cookie_dict = {}
    for cookie in session.cookies:
        cookie_dict[cookie.name] = cookie.value
    return cookie_dict

def build_exact_cookie(cookies_dict):
    datr = cookies_dict.get("datr", "WGLWamKwPlUwVU-RvGkDIc1o") 
    sb = cookies_dict.get("sb", "")
    c_user = cookies_dict.get("c_user", "")
    fr = cookies_dict.get("fr", "")
    xs = cookies_dict.get("xs", "")
    return f"datr={datr}; m_pixel_ratio=2; wd=360x806; sb={sb}; c_user={c_user}; fr={fr}; xs={xs}; ps_l=0; ps_n=0"
# ================= COOKIE FORMATTER END =================


# ================= PANEL & CHECKER =================
API_2OO9_BASE = "https://api.2oo9.cloud/MXS47FLFX0U/tnevs/@public/api"
API_2OO9_KEY = "MJMUGO5RU9O"
GRAPHQL_URL = "https://www.facebook.com/api/graphql/"

LSD = "AdS-QY2mYrCcHP7sVf7ynTA6vTc"
CIPHER_TEXT = ("AdAtB3O832KrYgWu2c7Jm2mNWOdAALA9wNFKJ_043RSsW27RSXXjhlBd0Cr8rGn-lIwgDuQU-CNQILiqKbqFW0GZop7nLgDVhClntKlePmNpHzT4ESf47v-lTUCNV3L-ikw70LhayHi30trSUJqk-Rvmaost-m0CTl60dFiIcbLNhGmQ8uggs-M1wfu04KQJvOQBDLwohSr7f_yRqkDGj98Ra-1S2N77k17Fqxu8N84cEWWTyv4qW6ySj7GI7CYYhD8QZDTzMxXcImxAr_Y")
JAZOEST = "22291"
DOC_ID = "27012969198380071"

MAX_NUM_ATTEMPTS = 15

PANEL_STATE = {"ranges": [], "selected_range": None, "create_version": None}
PANEL_USED = set()


def fetch_live_access():
    try:
        res = requests.get(f"{API_2OO9_BASE}/liveaccess", headers={"mauthapi": API_2OO9_KEY}, timeout=15)
        data = res.json()
        if data and data.get("meta", {}).get("code") == 200:
            return data.get("data", {}).get("services", []) or []
    except Exception:
        pass
    return []


def find_fb_services(services):
    return [s for s in services
            if "facebook" in str(s.get("sid", "")).lower()
            or str(s.get("sid", "")).lower().startswith("fb")
            or "meta" in str(s.get("sid", "")).lower()]


def get_unique_ranges(fb_services):
    seen = {}
    for service in fb_services:
        sid = service.get("sid", "Unknown")
        for r in service.get("ranges", []) or []:
            clean_r = str(r).replace("X", "").strip()
            if not clean_r:
                continue
            prefix = clean_r[:4] if len(clean_r) >= 4 else clean_r
            if prefix not in seen:
                seen[prefix] = {"range": r, "clean_range": clean_r, "sid": sid}
    return list(seen.values())


def fetch_live_number(rid):
    try:
        res = requests.post(f"{API_2OO9_BASE}/getnum",
                            headers={"mauthapi": API_2OO9_KEY, "Content-Type": "application/json"},
                            json={"rid": str(rid)}, timeout=15)
        data = res.json()
        if data and data.get("meta", {}).get("code") == 200:
            return data.get("data", {}) or {}
    except Exception:
        pass
    return None


def build_graphql_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua-full-version-list": '"Chromium";v="155.0.8059.43", "Not(A:Brand";v="24.0.0.0"',
        "sec-ch-ua-platform": '"Windows"',
        "x-fb-navigation-chain": "CAAFBAccountSearchRoot.react,comet.caa.account_recovery.account_search,via_cold_start,1792144816098,553013,,,",
        "sec-ch-ua": '"Chromium";v="155", "Not(A:Brand";v="24"',
        "x-fb-friendly-name": "CAAFBAccountSearchViewQuery",
        "sec-ch-ua-mobile": "?0",
        "x-asbd-id": "359341",
        "x-fb-lsd": LSD,
        "origin": "https://www.facebook.com",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
        "referer": "https://www.facebook.com/login/identify/",
        "accept-language": "en-US,en;q=0.9", "priority": "u=1, i",
    }


def build_graphql_payload(phone_number):
    variables = {"params": {"cipher_text": CIPHER_TEXT, "context": "recover",
                            "event_request_id": str(uuid.uuid4()), "friend_name": "",
                            "search_query": phone_number, "waterfall_id": str(uuid.uuid4())}}
    return {
        "av": "0", "__aaid": "0", "__user": "0", "__a": "1", "__req": "5",
        "__hs": "20742.HYP:comet_loggedout_pkg.2.1...0", "dpr": "2",
        "__ccg": "EXCELLENT", "__rev": "1050579926",
        "__comet_req": "15", "lsd": LSD, "jazoest": JAZOEST,
        "__spin_r": "1050579926", "__spin_b": "trunk",
        "__spin_t": str(int(time.time())),
        "__crn": "comet.fbweb.CometCAAAccountSearchRoute",
        "qpl_active_flow_ids": "516759801",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CAAFBAccountSearchViewQuery",
        "server_timestamps": "true",
        "variables": json.dumps(variables, separators=(',', ':')),
        "doc_id": DOC_ID,
        "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]',
    }


def check_number_graphql(phone_number, proxy=None):
    try:
        r = requests.post(GRAPHQL_URL, headers=build_graphql_headers(),
                          data=build_graphql_payload(phone_number), timeout=30, proxies=proxy)
    except Exception as e:
        return "error", str(e)[:40]
    if r.status_code != 200:
        return "error", f"HTTP {r.status_code}"
    try:
        js = r.json()
    except Exception:
        return "error", "Bad JSON"
    data = js.get("data", {}) or {}
    search = data.get("caa_ar_fb_account_search", {}) or {}
    accounts = search.get("accounts") or []
    error_content = search.get("error_content") or {}
    description = (error_content.get("description") or "").strip()
    if not accounts and "No account found" in description:
        return "free", description
    if accounts:
        return "taken", f"{len(accounts)} account(s)"
    if description:
        return "taken", description
    return "unknown", "No clear result"


def acquire_checked_number(rid, proxy=None):
    fallback = None
    for attempt in range(1, MAX_NUM_ATTEMPTS + 1):
        nd = fetch_live_number(rid)
        if not nd:
            time.sleep(1.2)
            continue
        full_number = str(nd.get("full_number", "")).strip().lstrip("+")
        if not full_number or full_number in PANEL_USED:
            time.sleep(1.0)
            continue
        try:
            status, desc = check_number_graphql(f"+{full_number}", proxy=proxy)
        except Exception:
            status, desc = "error", "checker exception"
        if status == "free":
            PANEL_USED.add(full_number)
            return full_number, status, desc
        if status == "taken":
            PANEL_USED.add(full_number)
            time.sleep(0.6)
            continue
        if fallback is None:
            fallback = (full_number, status, desc)
        time.sleep(0.6)
    if fallback:
        PANEL_USED.add(fallback[0])
        return fallback
    return None, None, None


# ================= OTP (Memory Only) =================
WATCH_TIMEOUT = 20 * 60
OTP_SEEN = set()
OTP_SEEN_MAX = 2000
LOGIN_RESULTS: Dict[str, dict] = {}


def otp_fingerprint(number, msg, sid=""):
    raw = f"{number}|{sid}|{msg}".strip()
    return hashlib.sha1(raw.encode("utf-8", "ignore")).hexdigest()[:16]


def otp_is_new(number, msg, sid=""):
    fp = otp_fingerprint(number, msg, sid)
    if fp in OTP_SEEN:
        return False
    OTP_SEEN.add(fp)
    if len(OTP_SEEN) > OTP_SEEN_MAX:
        trimmed = list(OTP_SEEN)[-OTP_SEEN_MAX // 2:]
        OTP_SEEN.clear()
        OTP_SEEN.update(trimmed)
    return True


def fetch_success_otps():
    try:
        res = requests.get(f"{API_2OO9_BASE}/success-otp",
                           headers={"mauthapi": API_2OO9_KEY, "Content-Type": "application/json"},
                           timeout=15)
        if res.status_code != 200:
            return []
        data = res.json()
        if isinstance(data, dict):
            if isinstance(data.get("data"), list):
                return data["data"]
            if isinstance(data.get("data"), dict):
                return data["data"].get("otps", data["data"].get("hits", []))
            return data.get("otps", data.get("hits", []))
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def login_with_otp(phone, otp, proxy=None):
    print(f"\n{W}[{G}•{W}]{G} Sending Auto-Login Request for: {phone} with OTP: {otp}{W}")
    url = "https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=9d9579f00d6cb02f0045464322c6b9ce85cccd48aef3d7454ac1090aaed41b5e"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "sec-ch-ua-full-version-list": '"Chromium";v="155.0.8059.43", "Not(A:Brand";v="24.0.0.0"',
        "sec-ch-ua-platform": '"iOS"',
        "sec-ch-ua": '"Chromium";v="155", "Not(A:Brand";v="24"',
        "sec-ch-ua-model": '"itel S665L"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-prefers-color-scheme": "light",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "sec-ch-ua-platform-version": '"12.0.0"',
        "origin": "https://m.facebook.com",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.facebook.com/login/",
        "accept-language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
        "priority": "u=1, i",
        "Cookie": "datr=S_zVajF1XZhQSboPh6fLPtPk; m_pixel_ratio=2; wd=360x806; sb=VvzVatcF4de2L3weuwCVQGiI; fr=0099a8H8hxjYZOYxm..Bq1fxN..AAA.0.0.Bq1fxk.AWfj549aeJXIj1-Kzap92dsy5Hc"
    }
    formatted_password = f"#PWD_BROWSER:0:{int(time.time())}:{otp}"
    server_params = {
        "credential_type": "password",
        "username_text_input_id": "5u2xie:65",
        "password_text_input_id": "5u2xie:66",
        "login_source": "Login",
        "login_credential_type": "none",
        "server_login_source": "login",
        "ar_event_source": "login_home_page",
        "should_trigger_override_login_success_action": 0,
        "should_trigger_override_login_2fa_action": 0,
        "is_caa_perf_enabled": 0,
        "reg_flow_source": "login_home_native_integration_point",
        "caller": "gslr",
        "is_from_landing_page": 0,
        "is_from_empty_password": 0,
        "is_from_aymh": 0,
        "is_from_password_entry_page": 0,
        "is_from_assistive_id": 0,
        "is_from_msplit_fallback": 0,
        "two_step_login_type": "one_step_login",
        "left_nav_button_action": "NONE",
        "INTERNAL__latency_qpl_marker_id": 36707139,
        "INTERNAL__latency_qpl_instance_id": "35285610200187",
        "device_id": None,
        "family_device_id": None,
        "waterfall_id": str(uuid.uuid4()),
        "offline_experiment_group": None,
        "layered_homepage_experiment_group": None,
        "is_platform_login": 0,
        "is_from_logged_in_switcher": 0,
        "is_from_logged_out": 0,
        "access_flow_version": "pre_mt_behavior",
        "login_surface": "login_home",
        "login_entry_point": "logged_out"
    }
    client_input_params = {
        "machine_id": "",
        "cloud_trust_token": None,
        "block_store_machine_id": "",
        "zero_balance_state": "",
        "contact_point": phone,
        "password": formatted_password,
        "accounts_list": [],
        "fb_ig_device_id": [],
        "secure_family_device_id": "",
        "encrypted_msisdn": "",
        "headers_infra_flow_id": "",
        "try_num": 2,
        "login_attempt_count": 1,
        "event_flow": "login_manual",
        "event_step": "home_page",
        "openid_tokens": {},
        "auth_secure_device_id": "",
        "client_known_key_hash": "",
        "has_whatsapp_installed": 0,
        "sso_token_map_json_string": "",
        "should_show_nested_nta_from_aymh": 0,
        "gms_incoming_call_retriever_eligibility": "client_not_supported",
        "password_contains_non_ascii": "false",
        "has_granted_read_contacts_permissions": 0,
        "has_granted_read_phone_permissions": 0,
        "app_manager_id": "",
        "aymh_accounts": [
            {
                "id": "",
                "profiles": {
                    "id": {
                        "user_id": "",
                        "name": "",
                        "profile_picture_url": "",
                        "small_profile_picture_url": None,
                        "notification_count": 0,
                        "credential_type": "none",
                        "token": "",
                        "last_access_time": 0,
                        "is_derived": 0,
                        "username": "",
                        "password": "",
                        "has_smartlock": 0,
                        "account_center_id": "",
                        "account_source": "",
                        "credentials": [],
                        "nta_eligibility_reason": None,
                        "from_accurate_privacy_result": 0,
                        "dbln_validated": 0
                    }
                }
            }
        ],
        "sso_accounts_auth_data": [],
        "blocked_uids": [],
        "network_bssid": None,
        "lois_settings": {"lois_token": ""},
        "aac": ""
    }
    params_inner = {
        "server_params": server_params,
        "client_input_params": client_input_params
    }
    final_params = {"params": json.dumps(params_inner)}
    payload = {
        "__aaid": "0",
        "__user": "0",
        "__a": "1",
        "__req": "e",
        "__hs": "20745.BP:wbloks_caa_pkg.2.0...0",
        "dpr": "3",
        "__ccg": "EXCELLENT",
        "__rev": "1050809078",
        "__s": "umgqvz:lggb1e:lrquoi",
        "__hsi": "7698336542943283940",
        "__dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-0Co1kU1bo8Xw8S0QU3yw",
        "fb_dtsg": "NAfzR9onYhQkdESpmTUaq1G26_d2YUOpfnKIOoPCce0KkZl3tnLtyrw:0:0",
        "jazoest": "25154",
        "lsd": "AdSSKmcqetqo8sz37bemyKqyUEQ",
        "params": json.dumps(final_params)
    }
    try:
        session = requests.Session()
        response = session.post(url, headers=headers, data=payload, timeout=30, proxies=proxy)
        cookies = get_all_cookies(session)
        if "c_user" in cookies:
            uid = cookies["c_user"]
            print(f"\n{G}[✔] OTP LOGIN SUCCESSFUL!{W}")
            print(f"{W}┌─────────────────────────────────────────────┐{W}")
            print(f"{W}│{G} UID (c_user): {uid}{W}")
            print(f"{W}│{G} Phone: {phone}{W}")
            cookie_str = build_exact_cookie(cookies)
            print(f"{W}└─────────────────────────────────────────────┘{W}")
            print(f"{W}[•] Full Cookie:\n{G}{cookie_str}{W}\n")
            LOGIN_RESULTS[phone] = {"success": True, "uid": uid, "cookie": cookie_str, "otp": otp}
            return True
        else:
            print(f"\n{R}[✖] OTP LOGIN FAILED!{W}")
            print(f"{R}[•] Response: {response.text[:200]}...{W}\n")
            LOGIN_RESULTS[phone] = {"success": False, "reason": response.text[:200] or "NO_C_USER"}
            return False
    except Exception as e:
        print(f"\n{R}[✖] OTP Login Error: {e}{W}")
        LOGIN_RESULTS[phone] = {"success": False, "reason": str(e)}
        return False


# ================= CREATE V1 (verbatim) =================
V1_UA = ("Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
         "(KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36")
V1_GET_URL = "https://limited.facebook.com/reg/?cid=103&refsrc=deprecated&soft=hjk"
V1_SUBMIT_URL = ("https://limited.facebook.com/reg/submit/"
                 "?app_id=103&multi_step_form=1&skip_suma=0&shouldForceMTouch=1")
V1_LSD = "AdR_ZsMKEdbWR9Bzgszds2hpIuU"
V1_FB_DTSG = "NAfw6nPbOeh56pD4St7KJqdHVSgFSi01b6uYYswWA5UW2xmeQce2yrw:0:0"
V1_JAZOEST = "24979"
V1_DYN = "0wzpawlEnwm8_Bg9ppoW5UdE4a2i5U4e0C86u7E39x60zU3ex608ewk9E4W0pKq0FE6S0x81vohw73wGwcq1GwqU2YwbK0oi0zE1jU1soG0hi0Lo6-0Co1kU1UU3jwea"
V1_A = "AY2cwwFP8tCEAJI_5xp5JzsmX9z6vZS4sOk6jDcfM6HmjcPjAO98qt-vyyK-OjqQYfbA165stXgz7yp_DqEoanccwO0brSu3GpY"


def _extract_fb_tokens(html):
    tokens = {}
    try:
        soup = BeautifulSoup(html, "html.parser")
        for inp in soup.find_all("input"):
            name = inp.get("name")
            value = inp.get("value")
            if name and value is not None and value != "":
                tokens[name] = value
    except Exception:
        pass

    def grab(key, *patterns):
        if tokens.get(key):
            return
        for p in patterns:
            try:
                m = re.search(p, html)
                if m and m.group(1):
                    tokens[key] = m.group(1)
                    return
            except Exception:
                continue

    grab("lsd",
         r'"LSD",\[\],\{"token":"([^"]+)"',
         r'"lsd"\s*:\s*"([^"]+)"',
         r'name="lsd"[^>]*value="([^"]+)"')
    grab("fb_dtsg",
         r'"DTSGInitialData",\[\],\{"token":"([^"]+)"',
         r'"fb_dtsg"\s*:\s*"([^"]+)"',
         r'name="fb_dtsg"[^>]*value="([^"]+)"')
    grab("jazoest",
         r'"jazoest"\s*:\s*"(\d+)"',
         r'jazoest=(\d+)',
         r'name="jazoest"[^>]*value="(\d+)"')
    grab("__dyn",
         r'"__dyn"\s*:\s*"([^"]+)"',
         r'name="__dyn"[^>]*value="([^"]+)"')
    grab("__a",
         r'name="__a"[^>]*value="([^"]+)"',
         r'"__a"\s*:\s*"([^"]+)"')
    grab("__csr",
         r'name="__csr"[^>]*value="([^"]*)"',
         r'"__csr"\s*:\s*"([^"]*)"')
    grab("reg_instance", r'name="reg_instance"[^>]*value="([^"]+)"')
    grab("reg_impression_id", r'name="reg_impression_id"[^>]*value="([^"]+)"')
    grab("logger_id", r'name="logger_id"[^>]*value="([^"]+)"')
    return tokens


def fb_create_account_v1(number, password, proxy=None):
    try:
        ses = requests.Session()
        base_headers = {
            "User-Agent": V1_UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
            "sec-ch-ua": '"Android WebView";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "upgrade-insecure-requests": "1",
        }
        fresh_html = ""
        try:
            r = ses.get(V1_GET_URL, headers=base_headers, timeout=20, allow_redirects=True, proxies=proxy)
            fresh_html = r.text or ""
        except Exception:
            pass
        tokens = {}
        try:
            if fresh_html:
                tokens = _extract_fb_tokens(fresh_html)
        except Exception:
            pass
        lsd_token = tokens.get("lsd") or V1_LSD
        fb_dtsg_token = tokens.get("fb_dtsg") or V1_FB_DTSG
        jazoest_token = tokens.get("jazoest") or V1_JAZOEST
        dyn_token = tokens.get("__dyn") or V1_DYN
        a_token = tokens.get("__a") or V1_A
        csr_token = tokens.get("__csr", "")
        ck_get = get_all_cookies(ses)
        reg_instance = (tokens.get("reg_instance") or ck_get.get("datr", "") or "").strip()
        if not reg_instance:
            reg_instance = "rYnRag94NnjWBOYfFX7r8ce9"
            try:
                ses.cookies.set("datr", reg_instance, domain=".facebook.com")
                ses.cookies.set("sb", "ronRapOkErLEKH_4j_IvtMvz", domain=".facebook.com")
            except Exception:
                pass
        reg_impression_id = tokens.get("reg_impression_id") or str(uuid.uuid4())
        logger_id = tokens.get("logger_id") or str(uuid.uuid4())
        firstname, lastname = get_bd_name()
        bd_day = str(random.randint(15, 28))
        bd_month = str(random.randint(1, 12))
        bd_year = str(random.randint(1990, 2003))
        payload = [
            ('ccp', '2'), ('reg_instance', reg_instance), ('submission_request', 'true'),
            ('helper', ''), ('reg_impression_id', reg_impression_id), ('ns', '1'),
            ('zero_header_af_client', ''), ('app_id', '103'), ('logger_id', logger_id),
            ('field_names[0]', 'firstname'), ('firstname', firstname), ('lastname', lastname),
            ('field_names[1]', 'birthday_wrapper'), ('birthday_day', bd_day),
            ('birthday_month', bd_month), ('birthday_year', bd_year), ('age_step_input', ''),
            ('did_use_age', 'false'), ('field_names[2]', 'reg_email__'), ('reg_email__', number),
            ('field_names[3]', 'sex'), ('sex', '2'), ('preferred_pronoun', ''), ('custom_gender', ''),
            ('field_names[4]', 'reg_passwd__'), ('reg_passwd__', password),
            ('was_shown_name_suggestions', 'false'), ('did_use_suggested_name', 'false'),
            ('use_custom_gender', 'false'), ('guid', ''), ('pre_form_step', ''), ('submit', 'Sign up'),
            ('fb_dtsg', fb_dtsg_token), ('jazoest', jazoest_token), ('lsd', lsd_token),
            ('__dyn', dyn_token), ('__csr', csr_token), ('__hsdp', ''), ('__hblp', ''),
            ('__sjsp', ''), ('__req', '7'), ('__fmt', '1'), ('__a', a_token), ('__user', '0'),
        ]
        post_headers = {
            "User-Agent": V1_UA,
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua": '"Android WebView";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
            "x-response-format": "JSONStream",
            "sec-ch-ua-mobile": "?1",
            "x-asbd-id": "359341",
            "x-fb-lsd": lsd_token,
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://limited.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": V1_GET_URL,
            "accept-language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
            "priority": "u=1, i",
        }
        r2 = ses.post(V1_SUBMIT_URL, data=payload, headers=post_headers, timeout=30, proxies=proxy)
        login_coki = get_all_cookies(ses)
        result = {
            "firstname": firstname, "lastname": lastname,
            "number": number, "password": password,
            "uid": "", "cookie": "", "status": "failed",
            "dob": f"{bd_day}-{bd_month}-{bd_year}",
            "version": "v1",
        }
        if "c_user" in login_coki:
            uid = login_coki["c_user"]
            pstatus = check_facebook_profile_picture(uid)
            result["uid"] = uid
            result["cookie"] = build_exact_cookie(login_coki)
            result["status"] = "created"
            result["profile_status"] = pstatus or "unknown"
            return result, None
        if "checkpoint" in login_coki:
            return result, "CHECKPOINT"
        try:
            txt = (r2.text or "").strip()
            if txt.startswith("for(;;);"):
                txt = txt[len("for(;;);"):].strip()
            for line in txt.split("\n")[:6]:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if isinstance(obj, dict):
                    em = (obj.get("errorSummary") or obj.get("errorDescription") or obj.get("error"))
                    if em:
                        return result, f"FB_ERR: {str(em)[:60]}"
                    rd = obj.get("redirect")
                    if rd and "checkpoint" in str(rd).lower():
                        return result, "CHECKPOINT"
        except Exception:
            pass
        return result, "NO_C_USER"
    except requests.exceptions.Timeout:
        return None, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return None, "CONN_ERROR"
    except Exception as e:
        return None, f"EXC: {str(e)[:40]}"


# ================= CREATE V2 (verbatim) =================
def fb_create_account_v2(number, password, proxy=None):
    try:
        ses = requests.Session()
        response = ses.get("https://x.facebook.com/reg", timeout=30, proxies=proxy)
        form = extractor(response.text)
        firstname, lastname = get_bd_name()
        payload = {
            'ccp': "2",
            'reg_instance': form.get("reg_instance", ""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id", ""),
            'ns': "1",
            'logger_id': form.get("logger_id", ""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(20, 28)),
            'birthday_month': str(random.randint(5, 25)),
            'birthday_year': str(random.randint(1990, 2001)),
            'reg_email__': number,
            'sex': "1",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg", ""),
            'jazoest': form.get("jazoest", ""),
            'lsd': form.get("lsd", "")
        }
        headers = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ugenX(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }
        head1 = {
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ugenX()
        }
        merged_headers = {**headers, **head1}
        ses.post("https://www.facebook.com/reg/submit/", data=payload,
                 headers=merged_headers, timeout=30, proxies=proxy)
        login_coki = get_all_cookies(ses)
        result = {
            "firstname": firstname, "lastname": lastname,
            "number": number, "password": password,
            "uid": "", "cookie": "", "status": "failed",
            "dob": f"{payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}",
            "version": "v2",
        }
        if "c_user" in login_coki:
            uid = login_coki["c_user"]
            pstatus = check_facebook_profile_picture(uid)
            result["uid"] = uid
            result["cookie"] = build_exact_cookie(login_coki)
            result["status"] = "created"
            result["profile_status"] = pstatus or "unknown"
            return result, None
        if "checkpoint" in login_coki:
            return result, "CHECKPOINT"
        return result, "NO_C_USER"
    except requests.exceptions.Timeout:
        return None, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return None, "CONN_ERROR"
    except Exception as e:
        return None, f"EXC: {str(e)[:40]}"


# ================= CREATE V3 (verbatim) =================
V3_URL = "https://www.facebook.com/api/graphql/"
V3_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "sec-ch-ua-full-version-list": '"Chromium";v="155.0.8059.43", "Not(A:Brand";v="24.0.0.0"',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua": '"Chromium";v="155", "Not(A:Brand";v="24"',
    "x-fb-friendly-name": "useCAARegistrationFormSubmitMutation",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '"itel S665L"',
    "x-asbd-id": "359341",
    "x-fb-lsd": "AdQBHXQf_CpDXYrPBnVibCGFQyU",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua-platform-version": '"12.0.0"',
    "origin": "https://www.facebook.com",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.facebook.com/reg/?entry_point=login&next=",
    "accept-language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
    "priority": "u=1, i",
    "Cookie": "datr=Je3VakJWee5EYBLobwNP5C7b"
}
V3_STATIC_PAYLOAD = {
    "av": "0",
    "__user": "0",
    "__a": "1",
    "__req": "a",
    "__hs": "20745.HYP:comet_plat_default_pkg.2.1...0",
    "dpr": "1",
    "__ccg": "EXCELLENT",
    "__rev": "1050806504",
    "__s": "omt8qa:laskej:apje4u",
    "__hsi": "7698319890411026009",
    "__dyn": "7xe6E5q5U5ObwKBAg5S1Dxu13w8CewSwMwNw9G2S0lW4o0B-q1ew2io2awpUO0n24oaEd82lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1Lwqo15E6O1Fwce2eU5SEb87u0xE2Tw3C8doS1DwTw",
    "__csr": "l2cath-xknaD9Oj-yFfOnWHKCJtWnAqHHp9HOvJkBlPllqvWiRnOiHRpb8O9fOfjBFr_CDAVmu-HgDGJmsyHFGBifvWOWzFt9_AnQqhlylj9LpLHCR9AWyrFlKGCR4QbHClFfxibGegmAAnhA2C0CUCdwmouwKxK5U4a2maykEeUeE4K0lW0K85y4o2hwLKm0yoK0HE14HDG2u6E3Ow4Bwop40G-E3CAxy0j61YwbS4o9o39w41g0oNw1oK00yNU0caQ00r0u01-5o22w0T3w0Nqw0glm1hw",
    "__hsdp": "geN77CwOSCEmoK48sm3q1nwDxO0CC10w8CE1YA0ldy1M04Pe0ty0lO02N600V1o0rzw0yNw",
    "__hblp": "04Fw1hS1Xw76wio0c3o0T20qy0ty1jwdu320FE0xq06EU2zw4bw0DUw0kvo0eTo0xe020K0p209GU4W0ZE2Kw2cU4S02b60aYwLwn8d8",
    "__sjsp": "geN4Iqq3bqqxpyUgxNodE5u2u782qo420yqw7Og1kS870",
    "__comet_req": "102",
    "lsd": "AdQBHXQf_CpDXYrPBnVibCGFQyU",
    "jazoest": "22328",
    "__spin_r": "1050806504",
    "__spin_b": "trunk",
    "__spin_t": "1792404775",
    "qpl_active_flow_ids": "250359044,516759801",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "useCAARegistrationFormSubmitMutation",
    "server_timestamps": "true",
    "doc_id": "27029416779977343",
    "fb_api_analytics_tags": '["qpl_active_flow_ids=250359044,516759801"]'
}


def fb_create_account_v3(number, password, proxy=None):
    try:
        session = requests.Session()
        session.headers.update(V3_HEADERS)
        client_mutation_id = str(uuid.uuid4())
        waterfall_id = str(uuid.uuid4())
        formatted_password = f"#PWD_BROWSER:0:{int(time.time())}:{password}"
        firstname, lastname = get_bd_name()
        bd_day = str(random.randint(1, 28))
        bd_month = str(random.randint(1, 12))
        bd_year = str(random.randint(1990, 2003))
        variables = {
            "input": {
                "actor_id": "0",
                "client_mutation_id": client_mutation_id,
                "machine_id": "",
                "next_uri": None,
                "reg_data": {
                    "birthday_day": int(bd_day),
                    "birthday_month": int(bd_month),
                    "birthday_year": int(bd_year),
                    "contactpoint": {"sensitive_string_value": number},
                    "contactpoint_type": "PHONE",
                    "custom_gender": "",
                    "did_use_age": False,
                    "firstname": {"sensitive_string_value": firstname},
                    "fullname": {"sensitive_string_value": ""},
                    "ig_age_block_data": None,
                    "lastname": {"sensitive_string_value": lastname},
                    "preferred_pronoun": None,
                    "reg_passwd__": {"sensitive_string_value": formatted_password},
                    "sex": "FEMALE",
                    "use_custom_gender": False,
                    "username": {"sensitive_string_value": ""}
                },
                "sk_pipa_consent_given": None,
                "waterfall_id": waterfall_id
            }
        }
        payload = V3_STATIC_PAYLOAD.copy()
        payload["variables"] = json.dumps(variables, separators=(',', ':'))
        response = session.post(V3_URL, data=payload, timeout=30, proxies=proxy)
        cookies = get_all_cookies(session)
        result = {
            "firstname": firstname, "lastname": lastname,
            "number": number, "password": password,
            "uid": "", "cookie": "", "status": "failed",
            "dob": f"{bd_day}-{bd_month}-{bd_year}",
            "version": "v3",
        }
        if "c_user" in cookies:
            uid = cookies["c_user"]
            pstatus = check_facebook_profile_picture(uid)
            result["uid"] = uid
            result["cookie"] = build_exact_cookie(cookies)
            result["status"] = "created"
            result["profile_status"] = pstatus or "unknown"
            return result, None
        if "checkpoint" in cookies:
            return result, "CHECKPOINT"
        try:
            js = response.json()
            if "errors" in js:
                err_msg = js["errors"][0].get("summary", "GraphQL Error")
                return result, f"FB_ERR: {str(err_msg)[:40]}"
        except Exception:
            pass
        return result, "NO_C_USER"
    except requests.exceptions.Timeout:
        return None, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return None, "CONN_ERROR"
    except Exception as e:
        return None, f"EXC: {str(e)[:40]}"


# ================= CREATE V4 (verbatim, full reg_info) =================
def fb_create_account_v4(number, password, proxy=None):
    try:
        url = "https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.create.account.async&type=action&__bkv=9d9579f00d6cb02f0045464322c6b9ce85cccd48aef3d7454ac1090aaed41b5e"
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "sec-ch-ua-full-version-list": '"Chromium";v="155.0.8059.43", "Not(A:Brand";v="24.0.0.0"',
            "sec-ch-ua-platform": '"iOS"',
            "sec-ch-ua": '"Chromium";v="155", "Not(A:Brand";v="24"',
            "sec-ch-ua-model": '"itel S665L"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-prefers-color-scheme": "light",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-ch-ua-platform-version": '"12.0.0"',
            "origin": "https://m.facebook.com",
            "x-requested-with": "mark.via.gp",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/reg/?entry_point=login&next",
            "accept-language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
            "priority": "u=1, i",
            "Cookie": "datr=v_DVann8RekIaxiWOf6xHdNH"
        }
        firstname, lastname = get_bd_name()
        bd_day = str(random.randint(1, 28))
        bd_month = str(random.randint(1, 12))
        bd_year = str(random.randint(1990, 2003))
        dob_str = f"{bd_day}-{bd_month}-{bd_year}"
        reg_info = {
            "first_name": firstname,
            "last_name": lastname,
            "full_name": f"{firstname}+{lastname}",
            "contactpoint": number,
            "ar_contactpoint": None,
            "attempted_empty_last_name": False,
            "contactpoint_type": "phone",
            "is_using_unified_cp": False,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "is_cp_claimed": True,
            "confirmation_code": None,
            "birthday": dob_str,
            "birthday_derived_from_age": None,
            "age_range": "o18",
            "did_use_age": False,
            "os_shared_age_range": None,
            "gender": 2,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": f"#PWD_BROWSER:0:{int(time.time())}:{password}",
            "username": None,
            "username_prefill": None,
            "accounts_list_client": [],
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "fdid_available_on_start": None,
            "fdid_rid_available_on_start": None,
            "asdid_available_on_start": None,
            "user_id": None,
            "safetynet_token": None,
            "skip_slow_rel_check": False,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": [],
            "sign_in_with_google_email": None,
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "opt_out_source_account_reg_info_logging_only": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": str(uuid.uuid4()),
            "was_headers_prefill_available": False,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": False,
            "fb_access_token": None,
            "is_msplit_reg": None,
            "is_spectra_reg": None,
            "dema_account_consent_given": None,
            "spectra_entry_source": None,
            "spectra_reg_token": None,
            "spectra_reg_guardian_id": None,
            "spectra_reg_guardian_logged_in_context": None,
            "spectra_requester_user_id": None,
            "user_id_of_msplit_creator": None,
            "msplit_creator_nonce": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_ca_late_teen": None,
            "is_early_teen": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "should_show_rel_error": False,
            "ignore_suma_check": False,
            "dismissed_login_upsell_with_cna": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "suggested_gender": None,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": True,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "consent_jurisdiction_at_gate": None,
            "consent_jurisdiction_at_inflow": None,
            "pc_enforcement_outcome": None,
            "pc_inflow_decision": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "eligible_to_mo_sms_in_ig4a": False,
            "mo_sms_ent_id": None,
            "flash_call_permissions_status": None,
            "gms_incoming_call_retriever_eligibility": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "sk_pipa_consent_given": None,
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "client_known_key_hash": None,
            "flash_call_provider": None,
            "is_in_gms_experience": None,
            "flash_call_nonce_prefix_details": None,
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None,
            "user_opted_out_of_ntp": None,
            "is_from_registration_reminder": False,
            "show_youth_reg_in_ig_spc": False,
            "fb_suma_is_high_confidence": None,
            "screen_visited": [
                "bloks.caa.reg.birthday",
                "CAA_REG_CONTACT_POINT_PHONE",
                "CAA_REG_PASSWORD",
                "CAA_REG_SAVE_PASSWORD_CREDENTIALS"
            ],
            "fb_email_login_upsell_skip_suma_post_tos": False,
            "fb_suma_is_from_email_login_upsell": False,
            "fb_suma_is_from_phone_login_upsell": False,
            "should_prefill_cp_in_ar": True,
            "ig_partially_created_account_user_id": None,
            "ig_partially_created_account_nonce": None,
            "ig_partially_created_account_nonce_expiry": None,
            "force_sessionless_nux_experience": False,
            "has_seen_suma_landing_page_pre_conf": False,
            "has_seen_suma_candidate_page_pre_conf": False,
            "has_seen_confirmation_screen": False,
            "suma_on_conf_threshold": -1,
            "should_show_error_msg": True,
            "th_profile_photo_token": None,
            "attempted_silent_auth_in_fb": False,
            "attempted_silent_auth_in_ig": False,
            "sa_prefetch_callback_id": None,
            "cp_suma_results_map": None,
            "source_username": None,
            "next_uri": "",
            "should_use_next_uri": False,
            "linking_entry_point": None,
            "fb_encrypted_partial_new_account_properties": None,
            "starter_pack_name": None,
            "starter_pack_creator_user_ids": None,
            "wa_data_bundle": None,
            "bloks_controller_source": None,
            "airwave_registration_code": None,
            "is_sessionless_nux": None,
            "login_contactpoint": None,
            "login_contactpoint_type": None,
            "should_show_bday_after_name_suggestions": None,
            "should_override_back_nav": False,
            "ig_footer_variant": "control",
            "ig_gender": None,
            "device_network_info": None,
            "is_from_web_lite_reg_controller": True,
            "login_form_siwg_email": None,
            "account_setup_waterfall_id": None,
            "is_wanted_suma_user": None,
            "device_zero_balance_state": None,
            "wa_to_ig_merged_tos_variant": None,
            "is_in_nta_single_form": False,
            "source_account_image_asset_id": None,
            "passkey_eligible_device": None,
            "nta_ac_opted_out": None,
            "nta_control_reason": None,
            "nta_risk_type": None,
            "nta_single_form_variant": None,
            "enable_survey": None,
            "phone_prefetch_outcome": None,
            "tos_accepted_on_profile_info": None
        }
        server_params = {
            "event_request_id": str(uuid.uuid4()),
            "should_ignore_suma_check": 0,
            "app_id": 0,
            "bloks_controller_source": "bk_caa_reg_tos_screen",
            "sa_prefetch_callback_id": "",
            "reg_info": json.dumps(reg_info),
            "flow_info": json.dumps({"flow_name": "new_to_meta_fb_default", "flow_type": "ntf"}),
            "current_step": 7,
            "INTERNAL__latency_qpl_marker_id": 36707139,
            "INTERNAL__latency_qpl_instance_id": "24736761800087",
            "device_id": None,
            "family_device_id": None,
            "waterfall_id": str(uuid.uuid4()),
            "offline_experiment_group": None,
            "layered_homepage_experiment_group": None,
            "is_platform_login": 0,
            "is_from_logged_in_switcher": 0,
            "is_from_logged_out": 0,
            "access_flow_version": "pre_mt_behavior",
            "login_surface": "unknown"
        }
        client_input_params = {
            "device_id": "",
            "waterfall_id": str(uuid.uuid4()),
            "machine_id": "",
            "zero_balance_state": "",
            "ck_error": "",
            "ck_id": "",
            "ck_nonce": "",
            "has_dismissed_suma_pre_conf": 0,
            "should_ignore_existing_login": 0,
            "encrypted_msisdn": "",
            "headers_last_infra_flow_id": "",
            "reached_from_tos_screen": 1,
            "no_contact_perm_email_oauth_token": "",
            "failed_birthday_year_count": "{}",
            "ig_partially_created_account_user_id": 0,
            "ig_partially_created_account_nonce": "",
            "ig_partially_created_account_nonce_expiry": 0,
            "force_sessionless_nux_experience": 0,
            "passkey_eligible_device": 0,
            "cloud_trust_token": None,
            "network_bssid": None,
            "lois_settings": {"lois_token": ""},
            "aac": ""
        }
        params_inner = {"server_params": server_params, "client_input_params": client_input_params}
        final_params = {"params": json.dumps(params_inner)}
        payload = {
            "__aaid": "0",
            "__user": "0",
            "__a": "1",
            "__req": "s",
            "__hs": "20745.BP:wbloks_caa_pkg.2.0...0",
            "dpr": "3",
            "__ccg": "EXCELLENT",
            "__rev": "1050806504",
            "__s": "fpveuk:3dpw5y:2snaj4",
            "__hsi": "7698323847575319333",
            "__dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-0Co1kU1bo8Xw8S0QU3yw",
            "fb_dtsg": "NAfwkoUm61gjySCbh0SuweWU4ExIvX2f4Rzd7xd-QBSAC1psyBSNhZw:0:0",
            "jazoest": "25060",
            "lsd": "AdTXCNk3TBAdtpmAf0vFxtuEHNM",
            "params": json.dumps(final_params)
        }
        session = requests.Session()
        session.post(url, headers=headers, data=payload, timeout=30, proxies=proxy)
        cookies = get_all_cookies(session)
        result = {
            "firstname": firstname, "lastname": lastname,
            "number": number, "password": password,
            "uid": "", "cookie": "", "status": "failed",
            "dob": dob_str, "version": "v4",
        }
        if "c_user" in cookies:
            uid = cookies["c_user"]
            pstatus = check_facebook_profile_picture(uid)
            result["uid"] = uid
            result["cookie"] = build_exact_cookie(cookies)
            result["status"] = "created"
            result["profile_status"] = pstatus or "unknown"
            return result, None
        if "checkpoint" in cookies:
            return result, "CHECKPOINT"
        return result, "NO_C_USER"
    except requests.exceptions.Timeout:
        return None, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return None, "CONN_ERROR"
    except Exception as e:
        return None, f"EXC: {str(e)[:40]}"


# ============================================================================
#                          TELEGRAM BOT LAYER
# ============================================================================

USER_STATES: Dict[int, dict] = {}


def _get_state(chat_id: int) -> dict:
    if chat_id not in USER_STATES:
        USER_STATES[chat_id] = {
            "version": None,
            "range": None,
            "ranges": [],
            "password": None,
            "proxy": None,
            "await_state": None, 
            "creating": False,
        }
    return USER_STATES[chat_id]


def _authorized(update: Update) -> bool:
    if ADMIN_ID is None:
        return True
    u = update.effective_user
    return bool(u and u.id == ADMIN_ID)


def _mask_pw(pw):
    if not pw:
        return "❌ not set"
    return f"✅ set ({pw[:2]}***{pw[-1]})" if len(pw) > 3 else "✅ set"


def _menu_text(state: dict) -> str:
    v = state.get("version"); r = state.get("range"); pw = state.get("password")
    px = state.get("proxy")
    proxy_status = "❌ not set"
    if px and px.get("server") and px.get("port"):
        proxy_status = f"✅ {px['server']}:{px['port']}"

    return (
        "🤖 *FB Auto Creator — Bot*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"🔧 Version   : `{v.upper() if v else 'not set'}`\n"
        f"📞 Range     : `{r[:22] if r else 'not set'}`\n"
        f"🔑 Password  : `{_mask_pw(pw)}`\n"
        f"🌐 Proxy     : `{proxy_status}`\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "_Set version + range + password + proxy, then tap ▶️ Create._"
    )


def _menu_kb(state: dict) -> InlineKeyboardMarkup:
    v = state.get("version"); r = state.get("range"); pw = state.get("password")
    px = state.get("proxy")
    def m(x): return f"✅ {x.upper()}" if v == x else x.upper()
    kb = [
        [InlineKeyboardButton(m("v1"), callback_data="sv_v1"),
         InlineKeyboardButton(m("v2"), callback_data="sv_v2"),
         InlineKeyboardButton(m("v3"), callback_data="sv_v3"),
         InlineKeyboardButton(m("v4"), callback_data="sv_v4")],
        [InlineKeyboardButton(f"📞 {r[:16] if r else 'Select Range'}", callback_data="show_ranges")],
        [InlineKeyboardButton(f"🔑 {'Change Password' if pw else 'Set Password'}", callback_data="set_password")],
        [InlineKeyboardButton(f"🌐 {'Change Proxy' if px else 'Set Proxy'}", callback_data="set_proxy")],
    ]
    
    if px and px.get("server"):
        kb.append([InlineKeyboardButton("🧪 Test Proxy", callback_data="test_proxy")])
        
    kb.append([InlineKeyboardButton("▶️ Create Account", callback_data="create_now")])
    return InlineKeyboardMarkup(kb)


def _back_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Menu", callback_data="back")]])


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _authorized(update):
        await update.message.reply_text("🚫 Unauthorized.")
        return
    st = _get_state(update.effective_chat.id)
    await update.message.reply_text(_menu_text(st), reply_markup=_menu_kb(st), parse_mode="Markdown")


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    st = _get_state(update.effective_chat.id)
    st["await_state"] = None
    await update.message.reply_text("❌ Cancelled.", reply_markup=_menu_kb(st))


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if not _authorized(update):
        return
    data = q.data
    chat_id = update.effective_chat.id
    st = _get_state(chat_id)

    if data.startswith("sv_"):
        st["version"] = data.replace("sv_", "")
        await q.edit_message_text(_menu_text(st), reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    if data == "show_ranges":
        await q.edit_message_text("⏳ Fetching ranges from panel...", reply_markup=_back_kb())
        services = await asyncio.to_thread(fetch_live_access)
        fb = find_fb_services(services) if services else []
        ranges = get_unique_ranges(fb) if fb else []
        st["ranges"] = ranges
        if not ranges:
            await q.edit_message_text("❌ No ranges available. Try again later.", reply_markup=_back_kb())
            return
        kb = []
        for idx, r in enumerate(ranges[:40]):
            kb.append([InlineKeyboardButton(f"{idx+1}. {r['range'][:14]} ({r['sid'][:12]})", callback_data=f"pr_{idx}")])
        kb.append([InlineKeyboardButton("🔙 Back to Menu", callback_data="back")])
        await q.edit_message_text(f"📞 *Available Ranges* ({len(ranges)})\n_Pick one:_", reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")
        return

    if data.startswith("pr_"):
        idx = int(data.replace("pr_", ""))
        ranges = st.get("ranges", [])
        if 0 <= idx < len(ranges):
            st["range"] = ranges[idx]["range"]
        await q.edit_message_text(_menu_text(st), reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    if data == "back":
        await q.edit_message_text(_menu_text(st), reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    if data == "set_password":
        st["await_state"] = "set_password"
        pw = st.get("password")
        text = ("🔑 *Set New Password*\n\nSend the password you want to use for new accounts.\n"
                + (f"Current: `{_mask_pw(pw)}`\n" if pw else "")
                + "\n_Your message will be deleted automatically._")
        await q.edit_message_text(text, reply_markup=_back_kb(), parse_mode="Markdown")
        return
        
    if data == "set_proxy":
        st["await_state"] = "set_proxy_server"
        await q.edit_message_text("🌐 *Proxy Setup - Step 1/4*\n\nSend Server IP / Host:", reply_markup=_back_kb(), parse_mode="Markdown")
        return
        
    if data == "test_proxy":
        px = st.get("proxy")
        if not px:
            await q.edit_message_text("⚠️ Proxy not set.", reply_markup=_back_kb())
            return
            
        await q.edit_message_text("⏳ Testing proxy...", reply_markup=_back_kb())
        proxy_url = f"http://{px['user']}:{px['pass']}@{px['server']}:{px['port']}" if px['user'] else f"http://{px['server']}:{px['port']}"
        proxies = {"http": proxy_url, "https": proxy_url}
        
        try:
            res = await asyncio.to_thread(requests.get, "http://ipinfo.io/json", proxies=proxies, timeout=15)
            js = res.json()
            if res.status_code == 200:
                text = (f"✅ *Proxy Test Success!*\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"🌐 Server  : `{px['server']}`\n"
                        f"📍 IP      : `{js.get('ip')}`\n"
                        f"🏳️ Country : `{js.get('country')}`\n"
                        f"🏙 City    : `{js.get('city')}`\n"
                        f"🕒 Timezone: `{js.get('timezone')}`\n"
                        f"━━━━━━━━━━━━━━━━━━━━")
                await q.edit_message_text(text, parse_mode="Markdown", reply_markup=_back_kb())
            else:
                await q.edit_message_text(f"❌ Proxy Test Failed. API error.", reply_markup=_back_kb())
        except Exception as e:
            await q.edit_message_text(f"❌ Proxy Test Failed:\n`{str(e)[:100]}`", parse_mode="Markdown", reply_markup=_back_kb())
        return

    if data == "create_now":
        if not st.get("version"):
            await q.edit_message_text("⚠️ Select a version first.", reply_markup=_back_kb())
            return
        if not st.get("range"):
            await q.edit_message_text("⚠️ Select a range first.", reply_markup=_back_kb())
            return
        if not st.get("proxy") or not st["proxy"].get("server") or not st["proxy"].get("port"):
            await q.edit_message_text("⚠️ *Proxy Required!*\n\nPlease set proxy before creating account.", parse_mode="Markdown", reply_markup=_back_kb())
            return
        if st.get("creating"):
            await q.edit_message_text("⏳ Already creating.", reply_markup=_back_kb())
            return

        if not st.get("password"):
            st["await_state"] = "create_password"
            await q.edit_message_text(
                "🔑 *Password Required*\n\n"
                f"Version : `{st['version'].upper()}`\n"
                f"Range   : `{st['range'][:22]}`\n\n"
                "Send the password for the new account.\n"
                "_(This will be saved for future creations too.)_",
                parse_mode="Markdown", reply_markup=_back_kb())
            return

        st["creating"] = True
        await q.edit_message_text(
            f"⏳ *Starting...*\n"
            f"Version : `{st['version'].upper()}`\n"
            f"Range   : `{st['range'][:22]}`\n"
            f"Password: `{_mask_pw(st['password'])}`\n\n"
            f"Fetching & checking number...",
            parse_mode="Markdown", reply_markup=_back_kb())
        asyncio.create_task(_create_flow(context.bot, chat_id))
        return


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _authorized(update):
        return
    chat_id = update.effective_chat.id
    st = _get_state(chat_id)
    text = (update.message.text or "").strip()
    state = st.get("await_state")

    if state is None:
        await update.message.reply_text(_menu_text(st), reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    if not text:
        await update.message.reply_text("⚠️ Cannot be empty.")
        return
        
    try:
        await update.message.delete()
    except Exception:
        pass

    # --- Proxy Setup Steps ---
    if state == "set_proxy_server":
        if "proxy" not in st or st["proxy"] is None: st["proxy"] = {}
        st["proxy"]["server"] = text
        st["await_state"] = "set_proxy_port"
        await context.bot.send_message(chat_id, f"🌐 *Proxy Setup - Step 2/4*\n\nServer: `{text}`\n\nSend Port:", parse_mode="Markdown", reply_markup=_back_kb())
        return
        
    if state == "set_proxy_port":
        st["proxy"]["port"] = text
        st["await_state"] = "set_proxy_user"
        await context.bot.send_message(chat_id, f"🌐 *Proxy Setup - Step 3/4*\n\nServer: `{st['proxy']['server']}:{text}`\n\nSend Username (or type `skip`):", parse_mode="Markdown", reply_markup=_back_kb())
        return
        
    if state == "set_proxy_user":
        st["proxy"]["user"] = "" if text.lower() == "skip" else text
        if not st["proxy"]["user"]:
            st["proxy"]["pass"] = ""
            st["await_state"] = None
            await context.bot.send_message(chat_id, "✅ *Proxy Saved!* (No Auth)\n\nYou can test it.", reply_markup=_menu_kb(st), parse_mode="Markdown")
        else:
            st["await_state"] = "set_proxy_pass"
            await context.bot.send_message(chat_id, f"🌐 *Proxy Setup - Step 4/4*\n\nUser: `{text}`\n\nSend Password:", parse_mode="Markdown", reply_markup=_back_kb())
        return
        
    if state == "set_proxy_pass":
        st["proxy"]["pass"] = text
        st["await_state"] = None
        await context.bot.send_message(chat_id, f"✅ *Proxy Saved!*\n\n{st['proxy']['server']}:{st['proxy']['port']}", reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    # --- Password Setup ---
    if state == "set_password":
        st["password"] = text
        st["await_state"] = None
        await context.bot.send_message(chat_id, f"✅ *Password saved!*\n`{_mask_pw(text)}`", reply_markup=_menu_kb(st), parse_mode="Markdown")
        return

    # --- Create Password (if missing) ---
    if state == "create_password":
        st["password"] = text
        st["await_state"] = None
        if st.get("creating"):
            await context.bot.send_message(chat_id, "⏳ Already running.")
            return
        st["creating"] = True
        await context.bot.send_message(
            chat_id,
            f"⏳ *Starting...*\n"
            f"Version : `{st['version'].upper()}`\n"
            f"Range   : `{st['range'][:22]}`\n"
            f"Password: `{_mask_pw(text)}`\n\n"
            f"Fetching & checking number...",
            parse_mode="Markdown")
        asyncio.create_task(_create_flow(context.bot, chat_id))
        return


async def _create_flow(bot, chat_id: int):
    st = _get_state(chat_id)
    version = st["version"]
    selected_range = st["range"]
    password = st["password"]
    px = st["proxy"]
    proxy_url = f"http://{px['user']}:{px['pass']}@{px['server']}:{px['port']}" if px.get('user') else f"http://{px['server']}:{px['port']}"
    proxies = {"http": proxy_url, "https": proxy_url}

    try:
        phone, num_status, num_desc = await asyncio.to_thread(acquire_checked_number, selected_range, proxies)
        if not phone:
            await bot.send_message(chat_id, "❌ Failed to get usable number from panel (Proxy error?).", reply_markup=_menu_kb(st))
            return
        await bot.send_message(
            chat_id,
            f"📞 Number: `+{phone}`\n⚡ Status: *{num_status.upper()}*\n\n"
            f"Creating account via *{version.upper()}*...",
            parse_mode="Markdown")

        if version == "v1":
            res, err = await asyncio.to_thread(fb_create_account_v1, phone, password, proxies)
        elif version == "v3":
            res, err = await asyncio.to_thread(fb_create_account_v3, phone, password, proxies)
        elif version == "v4":
            res, err = await asyncio.to_thread(fb_create_account_v4, phone, password, proxies)
        else:
            res, err = await asyncio.to_thread(fb_create_account_v2, phone, password, proxies)

        if res and res.get("status") == "created":
            uid = res["uid"]; coki = res["cookie"]
            text = (
                "🎉 *ACCOUNT CREATED!*\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🔧 Version : `{version.upper()}`\n"
                f"👤 Name    : `{res['firstname']} {res['lastname']}`\n"
                f"📞 Number  : `+{phone}`\n"
                f"🎂 DOB     : `{res['dob']}`\n"
                f"👩 Gender  : `Female`\n"
                f"🔑 Pass    : `{password}`\n"
                f"🆔 UID     : `{uid}`\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🍪 *Cookie:*\n"
                "```\n" + coki + "\n```\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "💾 Memory Saved (No File)"
            )
            await bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=_menu_kb(st))
            asyncio.create_task(_otp_monitor(bot, chat_id, phone, proxies))

        elif err == "CHECKPOINT":
            await bot.send_message(
                chat_id,
                "⚠️ *Checkpoint Required*\n"
                f"📞 `+{phone}`\n🔑 `{password}`\n\n"
                "Account created but needs manual confirmation.",
                parse_mode="Markdown", reply_markup=_menu_kb(st))
        else:
            await bot.send_message(
                chat_id,
                f"❌ *Creation Failed*\n📞 `+{phone}`\n🔧 `{version.upper()}`\n"
                f"Reason: `{err or 'unknown'}`",
                parse_mode="Markdown", reply_markup=_menu_kb(st))
    except Exception as e:
        logging.exception("create_flow error")
        try:
            await bot.send_message(chat_id, f"❌ Error: `{str(e)[:180]}`", parse_mode="Markdown", reply_markup=_menu_kb(st))
        except Exception:
            pass
    finally:
        st["creating"] = False


async def _otp_monitor(bot, chat_id: int, phone: str, proxies: dict, timeout: int = WATCH_TIMEOUT):
    end_at = time.time() + timeout
    found = 0
    try:
        await bot.send_message(
            chat_id,
            f"🔔 *OTP Monitor Active*\n📞 `+{phone}`\n⏱ 20 minutes\n\n"
            "I'll notify + auto-login when OTP arrives.",
            parse_mode="Markdown")
        while time.time() < end_at:
            try:
                otps = await asyncio.to_thread(fetch_success_otps)
            except Exception:
                otps = []
            for otp_data in otps:
                try:
                    num = str(otp_data.get("number", otp_data.get("phone", "")))
                    if not num or phone not in num:
                        continue
                    msg = str(otp_data.get("message", otp_data.get("sms", otp_data.get("code", ""))))
                    sid = str(otp_data.get("sid", otp_data.get("service", "Unknown")))
                    if not otp_is_new(num, msg, sid):
                        continue
                    m = re.search(r'\b(\d{4,8})\b', msg)
                    code = m.group(1) if m else "N/A"
                    ts = time.strftime('%H:%M:%S')
                    found += 1

                    await bot.send_message(
                        chat_id,
                        f"⚡ *OTP Intercepted!*\n📞 `+{phone}`\n🔢 Code: `{code}`\n📱 Service: `{sid}`\n🕒 {ts}",
                        parse_mode="Markdown")

                    if code != "N/A":
                        await bot.send_message(chat_id, f"🔐 Auto-login with OTP `{code}`...", parse_mode="Markdown")
                        ok = await asyncio.to_thread(login_with_otp, phone, code, proxies)
                        info = LOGIN_RESULTS.get(phone, {})

                        if ok and info.get("success"):
                            # Live Check
                            live_status = "UNKNOWN"
                            try:
                                check_url = "https://check.fb.tools/api/check/facebook"
                                check_headers = {
                                    "User-Agent": "Mozilla/5.0 (Linux; Android 12; itel S665L Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.8010.39 Mobile Safari/537.36",
                                    "Content-Type": "application/json",
                                    "Accept": "application/x-ndjson",
                                    "Accept-Encoding": "gzip, deflate, br, zstd",
                                    "origin": "https://check.fb.tools",
                                    "referer": "https://check.fb.tools/",
                                    "accept-language": "en-US,en;q=0.9,my-MM;q=0.8,my;q=0.7,fr-FR;q=0.6,fr;q=0.5",
                                    "priority": "u=1, i",
                                    "x-requested-with": "mark.via.gp",
                                    "sec-ch-ua-platform": '"Windows"',
                                    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="153"',
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-fetch-site": "same-origin",
                                    "sec-fetch-mode": "cors",
                                    "sec-fetch-dest": "empty"
                                }
                                check_payload = {"inputData": [info["uid"]], "userLang": "en", "checkFriends": False}
                                r_check = requests.post(check_url, headers=check_headers, json=check_payload, timeout=15, proxies=proxies)
                                for line in r_check.text.strip().split("\n"):
                                    if line:
                                        try:
                                            js_line = json.loads(line)
                                            if js_line.get("event") == "result":
                                                st_name = js_line.get("data", {}).get("status", {}).get("name", "")
                                                st_msg = js_line.get("data", {}).get("status", {}).get("message", "")
                                                if st_name:
                                                    live_status = f"{st_name.upper()} ({st_msg})"
                                                    break
                                        except Exception:
                                            continue
                            except Exception as e:
                                live_status = f"CHECK FAILED: {str(e)[:50]}"

                            await bot.send_message(
                                chat_id,
                                "✅ *AUTO-LOGIN SUCCESSFUL!*\n"
                                "━━━━━━━━━━━━━━━━━━━━\n"
                                f"📞 Phone : `+{phone}`\n"
                                f"🔢 OTP   : `{code}`\n"
                                f"🆔 UID   : `{info['uid']}`\n"
                                f"🔍 Status: *{live_status}*\n"
                                "━━━━━━━━━━━━━━━━━━━━\n"
                                "🍪 *Cookie:*\n"
                                "```\n" + info["cookie"] + "\n```\n"
                                "━━━━━━━━━━━━━━━━━━━━\n"
                                "💾 Memory Saved (No File)",
                                parse_mode="Markdown",
                                reply_markup=_menu_kb(_get_state(chat_id)))
                        else:
                            reason = (info.get("reason") or "unknown")[:150]
                            await bot.send_message(
                                chat_id,
                                "❌ *AUTO-LOGIN FAILED*\n"
                                "━━━━━━━━━━━━━━━━━━━━\n"
                                f"📞 Phone : `+{phone}`\n"
                                f"🔢 OTP   : `{code}`\n"
                                f"⚠️ Reason: `{reason}`",
                                parse_mode="Markdown")
                except Exception:
                    continue
            await asyncio.sleep(3.0)

        await bot.send_message(
            chat_id,
            f"⏰ *OTP Monitor Ended*\n📞 `+{phone}`\nTotal OTPs: `{found}`",
            parse_mode="Markdown",
            reply_markup=_menu_kb(_get_state(chat_id)))
    except asyncio.CancelledError:
        raise
    except Exception as e:
        logging.exception("otp_monitor error")
        try:
            await bot.send_message(chat_id, f"⚠️ Monitor error: `{str(e)[:120]}`", parse_mode="Markdown")
        except Exception:
            pass


# ================= BOT ENTRY =================
def bot_main():
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Set BOT_TOKEN in the file!")
        return
    print("🚀 Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("menu", cmd_start))
    app.add_handler(CommandHandler("cancel", cmd_cancel))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    print("✅ Bot running.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    install_dependencies()
    bot_main()