# Importing Libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

# variables
name = None
flag = 0
bot = None
answers = []

# main
app = Flask(__name__)

bot = ChatBot("Dexter", logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'])

# Training bot
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")


@app.route('/')
def home():
    answers = []
    return render_template('index.html', ans=answers)


@app.route('/answer', methods=['POST'])
def answer():
    answers.append(("Human", request.form.get('query')))
    if request.form.get('query').lower().startswith("bye"):
        home()
    else:
        # response = Chatbot(request.form.get('query'))
        response = bot.get_response(request.form.get('query'))
        answers.append(
            (
                "Dexter",
                response
            )
        )
    return render_template('index.html', ans=answers)

if __name__ == '__main__':
    app.run(debug=True)
