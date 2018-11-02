from urllib.request import Request,urlopen
import json

username = ""
password = ""
api_type = ""
data = {'username':username,'password':password,'api_type':api_type}

headers = {}

def login(username,password):
    global data
    data = json.dumps(data)
    data = str(data)
    data = data.encode('utf-8')
    api_login = "https://www.reddit.com/login"
    request = Request(api_login,data=data)
    data = urlopen(request).read()
    print(data)
    
login(username,password)

##
##def get_api_info():
##    pass
##
##api_info = "https://www.reddit.com/api/me.json"
##
##secret_url = ""
##modhash = "uwu"
##
##while True:
##    try:
##        request = Request(secret_url,headers={"X-Modhash":modhash})
##        data = urlopen(request).read()
##        result = json.loads(data)
##        modhash = result['data']['modhash']
##        print(result['data']['modhash'])
##    except:
##        print("uwu I made a lil muckie wuckie, don't worry! the code monkies are getting onto it now")
