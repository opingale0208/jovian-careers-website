from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India`',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': 'Pune, India',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id':3,
        'title': 'SDE - FrontEnd',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 7,00,000'
    },
    {
        'id':4,
        'title': 'SDE - BackendEnd',
        'location': 'Chicago, USA',
    }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs = jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__=="__main__":
    app.run(host = '0.0.0.0', debug = True)