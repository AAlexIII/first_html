import requests
res = requests.post('https://kurso.herokuapp.com/api/add_message/1234', json={"mytext":"lalala"})
if res.ok:
    print (res.json())