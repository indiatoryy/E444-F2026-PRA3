from flask import Flask, render_template

from flask_bootstrap import Bootstrap # supplies the navigation bar styling
from flask_moment import Moment # formats the timestamp in the browser
from datetime import datetime, timezone # gets the current time in UTC

# Create the web application.
app = Flask(__name__)

# Connect Bootstrap and Moment to this application.
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/') # The home page is http://127.0.0.1:5000/
def index():
    # Pass your name and the current time into the HTML template.
    return render_template('index.html', name='India', current_time=datetime.now(timezone.utc))


# A page that greets whatever name is written in the URL, such as /user/India.
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


# Start the server when this file is run directly.
if __name__ == '__main__':
    app.run(debug=True)
