from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
  a = 'Hello'
  b = 'World'
  return a+' '+b
  
@app.route('/goodbye')
def goodbye():
  a = 'Goodbye'
  b = 'World'
  return a+' '+b
  
  
@app.route('/tree')
def tree():
  return 'oak'
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)  f a   