import requests
import psutil
import time

ALLOWED_USAGE = 80

def get_ram_usage():
    return psutil.virtual_memory().percent

def send_alarm(message):
    url = 'http://exampleapi.com'
    payload = {'message':message}
    r = requests.post(url=url,json=payload)
    if r.status_code == 200:
        print('Alert sent sucessfully')
    else: 
        print('Failed to send alert')


while True:
    usage = get_ram_usage()
    if usage > ALLOWED_USAGE:
        send_alarm(f'Warning! RAM usage is over {ALLOWED_USAGE}')
    time.sleep(60)