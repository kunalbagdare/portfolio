from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv','a') as f:
        w = csv.writer(f)
        w.writerow(data.values())




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #print(data)
        write_to_csv(data)
        return render_template('index.html')
        
    else:
        return "Something went wrong !!!"


if __name__ == "__main__":
    app.run(debug=True)