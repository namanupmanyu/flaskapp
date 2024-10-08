from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Dummy user for demonstration
USER = {'username': 'admin', 'password': 'password'}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            session['logged_in'] = True
            return redirect(url_for('hill_stations'))
    return render_template('login.html')

@app.route('/hill_stations')
def hill_stations():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    data = [
        {'name': 'Shimla', 'state': 'Himachal Pradesh', 'description': 'Known for its colonial architecture and scenic views.'},
        {'name': 'Manali', 'state': 'Himachal Pradesh', 'description': 'Famous for its beautiful landscapes and adventure sports.'},
        {'name': 'Nainital', 'state': 'Uttarakhand', 'description': 'A popular hill station known for its lake.'},
    ]
    return render_template('hill_stations.html', stations=data)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Ensure app runs only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)

