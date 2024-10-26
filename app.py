from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """Display a madlib to the user that changes based on their adjective and noun they input."""
    return f'The {adjective} {noun} is attacking the town!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display the result of the multiplication of two numbers input by the user."""
    if(number1.isdigit() and number2.isdigit()):
        return f"{number1} times {number2} is {int(number1) * int(number2)}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def repeat_word(word, n):
    """Display a a string a given a number of times."""
    result = ""
    if(n.isdigit()):
        for i in range(int(n)):
            result += word + " "
    else:
        return "Invalid input. Please try again by entering a word and a number!"
    return result.strip()

@app.route('/dice')
def dice():
    """Display whether the user won or lost the dice game."""
    num = random.randint(1, 6)
    if num == 6:
        return f"You rolled a {num}. You won!"
    else:
        return f"You rolled a {num}. You lost!"

if __name__ == '__main__':
    app.run(debug=True)