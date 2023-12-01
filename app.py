from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bangalore, India',
    'Sallary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bangalore, India',
    'Sallary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Engeneer',
    'location': 'Remote',
    'Sallary': 'Rs. 20,00,000'
}, {
    'id': 4,
    'title': 'Backend',
    'location': 'Bangalore, India',
    'Sallary': 'Rs. 18,00,000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
