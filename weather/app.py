from ctypes.wintypes import FLOAT
import requests
from flask import Flask, request
app = Flask(__name__)
  
@app.route('/hello/<name>')
def hello_name(name):
       return 'Hello %s!' % name

@app.route('/<city>')
def api(city):
    req=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=2ddd9887dec3187dea8956f38d9ea07e')
    data=req.json()
    ktemp=float(data['main']['temp'])
    humidity=float(data['main']['humidity'])
    
    print(ktemp)
    print(humidity)
    return "landing page "
  
if __name__ == '__main__':     
   app.run(debug=True)