from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Will You Go on a Date with Me?</title>
        <style>
            body {
                text-align: center;
                background-color: pink;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 50px;
                color: red;
            }
            button {
                font-size: 20px;
                padding: 10px 20px;
                margin: 20px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Will You Go on a Date with Me, Rashi? ❤️</h1>
        <img src="https://example.com/proposal_image.jpg" alt="Proposal Image" width="300px">
        <br>
        <button onclick="alert('No is not an option! 😜')">No</button>
        <button onclick="window.location.href='/pick-place'">Yes</button>
    </body>
    </html>
    '''

@app.route('/pick-place')
def pick_place():
    return '''
    <html>
    <head>
        <title>Pick a Place</title>
    </head>
    <body>
        <h1>Where should we go?</h1>
        <button onclick="window.location.href='/pick-time'">Hadoti Chaska</button>
        <button onclick="window.location.href='/pick-time'">Burg Cafe</button>
    </body>
    </html>
    '''

@app.route('/pick-time')
def pick_time():
    return '''
    <html>
    <head>
        <title>Pick a Time</title>
    </head>
    <body>
        <h1>What time should we meet?</h1>
        <button onclick="window.location.href='/final'">4:00 PM</button>
        <button onclick="window.location.href='/final'">5:00 PM</button>
    </body>
    </html>
    '''

@app.route('/final')
def final_page():
    return '''
    <html>
    <head>
        <title>See You There!</title>
    </head>
    <body>
        <h1>I Love You, Rashi! ❤️</h1>
        <h2>See You There! 😘</h2>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
import logging

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    logging.info('Home page accessed')
    return '''
    <html>
    <head>
        <title>Will You Go on a Date with Me?</title>
        <style>
            body {
                text-align: center;
                background-color: pink;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 50px;
                color: red;
            }
            button {
                font-size: 20px;
                padding: 10px 20px;
                margin: 20px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Will You Go on a Date with Me, Rashi? ❤️</h1>
        <img src="https://example.com/proposal_image.jpg" alt="Proposal Image" width="300px">
        <br>
        <button onclick="alert('No is not an option! 😜')">No</button>
        <button onclick="window.location.href='/pick-place'">Yes</button>
    </body>
    </html>
    '''

@app.route('/pick-place')
def pick_place():
    logging.info('Pick place page accessed')
    return '''
    <html>
    <head>
        <title>Pick a Place</title>
    </head>
    <body>
        <h1>Where should we go?</h1>
        <button onclick="window.location.href='/pick-time'">Hadoti Chaska</button>
        <button onclick="window.location.href='/pick-time'">Burg Cafe</button>
    </body>
    </html>
    '''

@app.route('/pick-time')
def pick_time():
    logging.info('Pick time page accessed')
    return '''
    <html>
    <head>
        <title>Pick a Time</title>
    </head>
    <body>
        <h1>What time should we meet?</h1>
        <button onclick="window.location.href='/final'">4:00 PM</button>
        <button onclick="window.location.href='/final'">5:00 PM</button>
    </body>
    </html>
    '''

@app.route('/final')
def final_page():
    logging.info('Final page accessed')
    return '''
    <html>
    <head>
        <title>See You There!</title>
    </head>
    <body>
        <h1>I Love You, Rashi! ❤️</h1>
        <h2>See You There! 😘</h2>
    </body>
    </html>
    '''