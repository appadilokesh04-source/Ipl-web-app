from flask import Flask,render_template
import requests

app=Flask(__name__)
@app.route('/')
def home():
    response=requests.get('uRl of teams')
    teams=response.json()['teams']
   
    return render_template('index.html',temas=teams)
@app.route('/teamvteam')
def team_vs_team():
    team1=requests.args.get('team1')
    team2=requests.args.get('team2')
    
    respone=requests.get('url')
    response=response.json()
    print(respone)
    return 
app.run(debug=True,port=5500)