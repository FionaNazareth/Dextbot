from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
answers = []
count = 0

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/reply', methods=['POST'])
def reply():
    
    global count
    print(answers)
    
    if count == 0:
        answers.append(english_bot)
        count = 1

    query = request.form.get('query')
    answers.append(("Human", query))
    print("User query:", query)

    response = answers[0].get_response(query)
    print("Bot response:", response)
    answers.append(("Bot", response))

    return render_template('index.html', response=answers[1:])



if __name__ == "__main__":
    app.run()
