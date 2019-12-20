

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot ListTrainer.
'''

chatbot2 = ChatBot('Example Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.90
        },
        {
        'import_path': 'chatterbot.logic.MathematicalEvaluation',
        }
        ],
        preprocessors=['chatterbot.preprocessors.clean_whitespace']
)

# Start by training our bot with the ChatterBot corpus data
trainer = ListTrainer(chatbot2)

trainer.train([
    'Hello, how are you?',
    'I am doing well.',
    'That is good to hear.',
    'Thank you'
])

# You can train with a second list of data to add response variations

trainer.train([
    'Hello, how are you?',
    'I am great.',
    'That is awesome.',
    'Thanks'
])

# Now let's get a response to a greeting
while True:
    try:
        text = input("Enter Query: ")
        response = chatbot2.get_response(text)
        print(response)
        # print("\n")
        
    except Exception as e:
        raise e
        break
