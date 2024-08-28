from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "location": "New York",
        "position": "Data Analyst",
    },
    {
        "id": 2,
        "location": "San Francisco",
        "position": "Data Scientist",
        "salary": "$120,000"
    },
    {
        "id": 3,
        "location": "Chicago",
        "position": "Frontend Developer",
        "salary": "$85,000"
    },
    {
        "id": 4,
        "location": "Austin",
        "position": "Backend Developer",
        "salary": "$95,000"
    }
]

@app.route("/")
def hellomeenu():
  return render_template("home.html",jobs=JOBS,company_name="microsoft")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

