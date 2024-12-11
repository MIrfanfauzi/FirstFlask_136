
from flask import Flask, render_template, request

app = Flask(__name__)  # Gunakan __name__, bukan _name_

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')  # Ambil nama dari form
    return render_template('index.html', name=name)  # Kirim nama ke template

if __name__ == '__main__':  # Gunakan __name__, bukan _name_
    app.run(debug=True)
