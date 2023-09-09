import psycopg2
import redis
import json
from bottle import Bottle, request


DSN = 'dbname=email_sender user=postgres host=db'
SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'


class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)
        self.row = redis.StrictRedis(host='queue', port=6379, db=0)
        self.conn = psycopg2.connect(DSN)

    def register_message(self, subject, message):
        cur = self.conn.cursor()
        cur.execute(SQL, (subject, message))
        self.conn.commit()
        cur.close()
        msg = {'subject': subject, 'message': message}
        self.row.rpush('sender', json.dumps(msg))
        print('####################################### Message registered! #######################################')

    def send(self):
        subject = request.forms.get('subject')
        message = request.forms.get('message')

        self.register_message(subject, message)

        return f'Message queued! Subject: {subject} - Message: {message}'


if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)