"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
                <html>
                  Hi! This is the home page.
                  <div>
                    <a href="http://localhost:5000/hello">Say hello!</a>
                  </div>
                </html>
            """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          What kind of awesomeness are you?
            <select name="awesomeness">
                <option value = "awesome">Awesome</option>
                <option value = "teriffic">Teriffic</option>
                <option value = "fantastic">Fantastic</option>
                <option value = "smashing">Smashing</option>
                <option value = "ducky">Ducky</option>
            </select>
            <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          What kind of uncool are you?
            <select name="diss">
                <option value = "lame-o">Lame-o</option>
                <option value = "not-rad">Not Rad</option>
                <option value = "dry as a triscuit">Dry as a triscuit</option>
            </select>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  player = request.args.get("person")

  diss = request.args.get("diss")

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("awesomeness")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
