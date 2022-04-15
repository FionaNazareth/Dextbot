# Importing Libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

# variables
name = None
flag = 0
# bot = None
answers = []

# main
app = Flask(__name__)


@app.route('/')
def home():
#     bot = BotInit()
    return render_template('index.html', ans=answers)


@app.route('/answer', methods=['POST'])
def answer():
    if flag == 0:
        bot = BotInit()
        flag = 1
        
    answers.append(("Human", request.form.get('query')))
    if request.form.get('query').lower().startswith("bye"):
        home()
    else:
        response = bot.get_response(request.form.get('query'))
        answers.append(
            (
                "Dexter",
                response
            )
        )
    return render_template('index.html', ans=answers)


def BotInit():
    # Intialize the bot
    bot_1 = ChatBot("Dexter",
                  logic_adapters=['chatterbot.logic.BestMatch',
                                  'chatterbot.logic.MathematicalEvaluation'])
    # Training bot
    #trainer = ChatterBotCorpusTrainer(bot)
    #trainer.train("chatterbot.corpus.english")
    bot_1.set_trainer(ChatterBotCorpusTrainer)
    bot_1.train("chatterbot.corpus.english")
    print(bot_1)
    return bot_1

if __name__ == '__main__':
    app.run(debug=True)
