from chatterbot import ChatBot
import pyttsx3
engine=pyttsx3.init()
voice=engine.getProperty('voices')
bot=ChatBot('fibo')

#from chatterbot.trainers import ChatterBotCorpusTrainer
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train('chatterbot.corpus.english')

while(True):
    message=input('You: ')
    if(message=='BYE' or message=='bye'):
        print('{}: Bye, see you later!'.format(bot.name))
        engine.say('Bye, see you later!')
        engine.runAndWait()
        break
    if(message=='What is your name'or message=='what is your name'):
        print('{}:I am fibo'.format(bot.name))
        engine.say('I am fibo.')
        engine.runAndWait()
    if(message!='BYE' or message!='bye'):
        reply=bot.get_response(message)
        print('{}: {}'.format(bot.name,reply))
        engine.say(reply)
        engine.runAndWait()
