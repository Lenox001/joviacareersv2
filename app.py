from flask import Flask,render_template,jsonify

app=Flask(__name__)
JOBS=[{
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'55,000 USD'
},
{
    'id':2,
    'title':'Data Scientist',
    'location':'San Francisco,USA',
    'salary':'100,000 USD'
},
{
    'id':3,
    'title':'Frontend Developer',
    'location':'Remote',
    'salary':'65,000 USD'
},
{
    'id':4,
    'title':'Backend Developer',
    'location':'Remote',
    'salary':'72,000 USD'
}
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(debug=True)
