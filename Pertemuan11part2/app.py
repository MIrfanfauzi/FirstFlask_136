from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', name=None)

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')  # Ambil nama dari form
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
