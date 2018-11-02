from urllib.request import Request,urlopen
import json
from bs4 import BeautifulSoup
import requests
from time import sleep,time,ctime #to prevent too many requests
import hashlib


#adjust these
username = ""
password = ""



#don't touch these
session = requests.session()
headers={'User-Agent':'windows:frontpagechecker:v1.0.0 (by /u/sleepingonline)'}
hash_list = []
secret_feedlink = ""

def divider():
    timestamp = ctime(time())
    print("--------------------","("+str(timestamp)+")")

def login(username,password):
    global session,headers,secret_feedlink
    print("Attempting Login...","("+str(ctime(time()))+")")
    headers = []
    api_login = "https://www.reddit.com/login"
    response = session.get(api_login, headers=headers)
    page = response.text
    sleep(2)
    soup = BeautifulSoup(page, "lxml")
    try:
        csrf_token = soup.find("input", attrs={"name": "csrf_token"}).get("value")
        print("Acquired Secret Validation Code...","("+str(ctime(time()))+")")
        data = {'csrf_token':csrf_token,'otp':'','dest':'https%3A%2F%2Fwww.reddit.com%2F','password':password,'username':username}
        api_login = "https://www.reddit.com/login"
        response2 = session.post(api_login, headers=headers, data=data)
        sleep(2)
        print("Logged Into u/",str(username)+"...","("+str(ctime(time()))+")")
        api_feed_url = "https://www.reddit.com/prefs/feeds/"
        response3 = session.get(api_feed_url, headers=headers)
        page2 = response3.text
        soup2 = BeautifulSoup(page2, "lxml")
        secret_feedlink = soup2.find("a", attrs={"class": "feedlink json-link"}).get("href")
        print("Acquired Secret Feedlink...","("+str(ctime(time()))+")")
    except:
        sleep(2)
        login(username,password)
    
login(username,password)

while True:
    try:
        response = session.get(secret_feedlink, headers=headers)
        data = response.text
        result = json.loads(data)
        threads = result['data']['children']
        flag = False
        new_threads = []
        for thread in threads:
            upvotes = thread['data']['ups']
            if upvotes >= 1000:
                string = " r/"+str(thread['data']['subreddit'])+"/"+str(thread['data']['title'])
                hasher = hashlib.sha1(str(string).encode("utf-8"))
                unique_hash = hasher.hexdigest()
                if unique_hash not in hash_list:
                    new_threads.append("upvotes: "+str(upvotes)+string)
                    hash_list.append(unique_hash)
                    flag = True
                else:
                    pass
        if flag:
            divider()
            for i in new_threads:
                print(i)
                
    except:
        print("uwu I made a lil muckie wuckie, don't worry! the code monkies are getting onto it now")
    sleep(2)
