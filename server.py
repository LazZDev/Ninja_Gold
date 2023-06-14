from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    # Check if 'total_gold' key exists in the session
    if 'total_gold' not in session:
        # Initialize 'total_gold' to 0 and create an empty list for 'activities'
        session['total_gold'] = 0
        print("Total Gold = 0")
        session['activities'] = []
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():  # Process the form submission based on the selected building

    if request.form['building'] == 'farm':
        session['message'] = ''
        number = random.randrange(10, 21)  # Generate a random number between 10 and 20
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")  # Get the current timestamp
        session['total_gold'] += number  # Increase 'total_gold' by the generated number
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")

        # Iterate through 'activities' list in reverse order and concatenate the entries into 'message'
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]

    elif request.form['building'] == 'cave':
        session['message'] = ''
        number = random.randrange(5, 11)  # Generate a random number between 5 and 10
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['total_gold'] += number
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the cave! ({time})</div>")

        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]

    elif request.form['building'] == 'house':
        session['message'] = ''
        number = random.randrange(2, 6)  # Generate a random number between 2 and 5
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['total_gold'] += number
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the house! ({time})</div>")

        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]

    elif request.form['building'] == 'casino':
        if session['total_gold'] > 0:
            session['message'] = ''
            number = random.randrange(-50, 51)  # Generate a random number between -50 and 50
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            session['total_gold'] += number
            if number > 0:
                print(f"Gold increased by {number}.")
                session['activities'].append(f"<div class='won'>Earned {number} gold from the casino! ({time})</div>")
            if number < 0:
                print(f"Gold decreased by {abs(number)}.")
                session['activities'].append(
                    f"<div class='lost'>Entered a casino and lost {abs(number)} gold....Ouch! ({time})</div>")
            print(f"Total Gold = {session['total_gold']}")
        else:
            session['message'] = ''
            session['activities'].append(
                "<div>You have no gold to gamble. Please come back to the casino when you have more money.</div>"
            )
            print(f"Total Gold = {session['total_gold']}")
            print("You have no gold to gamble. Please come back to the casino when you have more money.")

        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]

    return redirect('/')


@app.route('/reset')
def reset():
    # Clear the session and redirect to the homepage
    print("Current game is ending. Gold count will reset to 0.")
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
