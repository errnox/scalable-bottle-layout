import datetime
# import webbrowser  # Allows opening the browser automatically

import bottle


class WebApp(object):
  def __init__(self):
    self.color = 'red'
    self.user_name = 'John'
    self.password = '123'

  @bottle.error(404)
  def get_error_404(error):
    return '<center><pre><b>404</b> Error. Sorry.</pre></center>'

  def get_index(self):
    return bottle.template('index.html.tpl')

  def get_hello(self, name='John'):
    return 'Hello there, {}! \nYour color: {}'.format(name, self.color)

  def get_time(self):
    return 'The time is: {}'.format(datetime.datetime.now())

  def get_login(self):
    return '''
<form action="/login" method="post">
  <label for="username">Username:</label>
  <input name="username" type="text">
  <label for="password">Password:</label>
  <input name="password" type="password">
  <button type="submit">Sign in</button>
</form>
'''

  def post_login(self):
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    if (username == self.user_name) and (password == self.password):
      return '''
<p>Welcome!</p>
<p><a href="/login">Sign out</a></p>
'''
    else:
      return '''
<p>Wrong username and/or password. Sorry.</p>
<p><a href="/login">Try again</a></p>
'''

  def get_static(self, filename):
    return bottle.static_file(filename, root='static/')

  def get_json(self):
    response = {'one': 111, 'two': 222, 'list': ['abc', 'def', 'ghi']}
    for k, v in bottle.request.query.items():
      response[k] = v
    return response

  def get_template(self):
    name = bottle.request.query.name or 'John Doe'
    color = bottle.request.query.color or 'red'
    n = bottle.request.query.n or 3
    n = int(n)
    return bottle.template('example_template.html.tpl',
                           name=name, color=color, n=n)


if __name__ == '__main__':
  web_app = WebApp()

  app = bottle.default_app()
  # Routes
  #
  app.get('/', name='get_index',
             callback=web_app.get_index)

  app.get('/hello', name='get_hello',
               callback=web_app.get_hello)
  app.get('/hello/', name='get_hello_slash',
               callback=web_app.get_hello)
  app.get('/hello/<name>', name='get_hello',
               callback=web_app.get_hello)

  app.route('/time')(web_app.get_time)

  app.get(['/login', '/login/'], name='get_login',
             callback=web_app.get_login)
  app.post(['/login', '/login/'], name='post_login',
              callback=web_app.post_login)

  app.get('/static/<filename:path>', name='get_static',
             callback=web_app.get_static)

  app.get(['/json', '/json/'], name='get_json',
             callback=web_app.get_json)

  app.get(['/template', '/template/'], name='get_template',
             callback=web_app.get_template)

  # Production
  #
  # app.run(host='localhost', port=4321)

  print('--------------------')
  # print(app.get_url('/hello'))
  print(filter((lambda route : route.name == 'get_static'), app.routes)[0].rule)

  # webbrowser.open("http://localhost:4022")

  # Development
  #
  app.run(host='localhost', port=4321, reloader=True, debug=True)
