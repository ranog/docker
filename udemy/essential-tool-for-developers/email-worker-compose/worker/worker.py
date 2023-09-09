import redis
import json
import os
from time import sleep
from random import randint


if __name__ == '__main__':
    redis_host = os.environ.get('REDIS_HOST', 'queue')
    r = redis.StrictRedis(host=redis_host, port=6379, db=0)
    print('####################################### Worker started! #######################################')
    while True:
        message = json.loads(r.blpop('sender')[1])
        # Simulating email sending...
        print(f'Sending email: {message["subject"]}')
        sleep(randint(15, 45))
        print(f'Email sent: {message["subject"]}')
