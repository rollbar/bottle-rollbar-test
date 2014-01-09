import bottle
from rollbar.contrib.bottle import RollbarBottleReporter

rbr = RollbarBottleReporter(access_token='525247d699574ec187505f6c94993400', environment='test') #setup rollbar

bottle.install(rbr) #install globally

@bottle.get('/')
def index():
  '''
  When navigating to /, we'll get a regular 500 page from bottle, 
  as well as have the error below listed on Rollbar.
  '''
  return 'Hello World!'


@bottle.get('/error')
def error():
  raise Exception('error 1')


@bottle.get('/error/:num')
def error(num):
  raise Exception('error %s' % num)


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
