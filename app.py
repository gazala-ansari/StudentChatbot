#import files
from flask import Flask, render_template, request
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.trainers import ListTrainer
from c import *
app = Flask(__name__)

#bot = ChatBot("Candice")
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():   
    #return render_template("clerk_menu.html") 
    return render_template("index.html") 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    res=try1(userText)
    return str((res)) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
