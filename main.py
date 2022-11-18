import urllib.request, urllib.error, urllib.parse
from datetime import datetime
import time
import traceback
from pygame import mixer
import re

def get_site():
    url = 'https://maplelegends.com/'

    try:
        response = urllib.request.urlopen(url)
        webContent = response.read()
        f = open('maplelegends_homepage.txt', 'wb')

        f.write(webContent)
        f.close
        print("Scrape succeeded")

    except:
        traceback.print_exc()
        print("Scrape failed")
        


def comb_file():
    continue_running = True
    
    file = open('maplelegends_homepage.txt', 'r')
    line = file.readline()    

    while line != "" and 'id="server_status"' not in line:
        line = file.readline()

    if 'id="server_status"' in line:
        print("Found the tag")
    else:
        print("Well, this isn't supposed to happen.")

    if "offline" in line.lower():
        print("Still offline...",end=" ")
    elif "online" in line.lower():
        print("It's Online!",end=" ")
        is_online = True

        
        continue_running = False
    else:
        print("Well, this also shouldn't happen lol")
    show_date()

    while line != "" and 'class="online_users"' not in line:
        line = file.readline()
    
    players_online = [int(s) for s in re.findall(r'\b\d+\b', line)][0]    
    print("Players online:" , players_online)

    sufficient_amount_of_players = 25
    player_count_good = False
        
    if players_online > sufficient_amount_of_players:
        player_count_good = True
        print("There are enough players online")
    else:
        print("Not enough players online")
        
    if player_count_good and is_online:
        continue_running = False
        print("Verdict: Servers should be up and running")
    else:
        print("Verdict: Keep waiting")
    return continue_running
    
def show_date():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Time: ", current_time)



now = datetime.now()

start_time = now.strftime("%H:%M:%S")
attempts = 0

keep_trying = True
while keep_trying:
    attempts += 1

    get_site()
    keep_trying = comb_file()
    

    if keep_trying:
        time.sleep(30)
        print("----------------------------------")
        print("Attempt #{}, running since {}".format(attempts, start_time))
        print("----------------------------------")
time.sleep(2)




