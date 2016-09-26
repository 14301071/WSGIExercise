import os

def application(environ, start_response):
  """A barebones WSGI application.
 
  This is a starting point for your own Web framework :)
  """
  status = '200 OK'
  response_headers = [('Content-Type', 'text/plain')]
  start_response(status, response_headers)
  if environ['PATH_INFO'][1:].endswith(".html"):
      filename = environ['PATH_INFO'][1:]

      if os.path.exists(filename):
          f = open(filename, "r")
          line = f.readline()
          message = line
          while line:
              line = f.readline()
              message = message + line

          status = '200 OK'
          response_headers = [('Content-Type', 'text/html')]
          start_response(status, response_headers)
          return [message]
      else:
          status = '404 NOT FOUND'
          response_headers = [('Content-Type', 'text/plain')]
          start_response(status, response_headers)
          return ['404 NOT FOUND']

  else:
    return  'Hello, %s!' % (environ['PATH_INFO'][1:] or 'world')