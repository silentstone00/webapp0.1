from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {'id':1,
  'title':'Data Analyst',
  'location':'Bengaluru,India',
'salary':'RS 100000'},

{'id':2,
  'title':'Frontend Developer',
  'location':'Bengaluru,India',
'salary':'RS 100600'},

{'id':3,
  'title':'Backend Developer',
  'location':'Chennai,India',
'salary':'RS 60000'},

{'id':4,
  'title':' Machine Learnig',
  'location':'Delhi,India',
'salary':'RS 780000'}


]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)