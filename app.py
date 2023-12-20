from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "suchSecret"

from routes import *

# app.py
from flask import session


# Secure session management
# Prevent unauthorized access // added this code
if not session.get('logged_in'):
    render_template('403.html')



if __name__ == '__main__':
    app.run(debug=True)