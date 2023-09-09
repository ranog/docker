import redis
import json
from time import sleep
from random import randint


if __name__ == '__main__':
    r = redis.StrictRedis(host='queue', port=6379, db=0)
    print('####################################### Worker started! #######################################')
    while True:
        message = json.loads(r.blpop('sender')[1])
        # Simulating email sending...
        print(f'Sending email: {message["subject"]}')
        sleep(randint(15, 45))
        print(f'Email sent: {message["subject"]}')
