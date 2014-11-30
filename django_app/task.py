# Starting rabbitmq-server /usr/local/sbin/rabbitmq-server
# To run task, run Python in terminal, from task import add (import module) & add.delay(x,y)
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from celery import Celery

app = Celery('task', broker='amqp://localhost//')

@app.task
def add(x,y):
	return x + y

