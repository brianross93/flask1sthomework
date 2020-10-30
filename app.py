
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask
app= Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<dessert>')
def favorite_desserts(dessert):
    """Display favorite dessert"""
    return f'My fav dessert is {dessert} too!'

@app.route('/madlibs/<noun>/<adjective>')
def do_madlibs(noun, adjective):
    """Display Madlib"""
    return f'I have a {noun} that has a {adjective} aura'

@app.route('/multiply/<number1>/<number2>')
def do_multiply(number1, number2):
    """Multiply numbers"""
    if number1.isdigit() & number2.isdigit():
        sum_num = int(number1) * int(number2)
        return str(sum_num)
    else:
        f"Please put in numbers"


if __name__ == '__main__':
    app.run(debug=True)