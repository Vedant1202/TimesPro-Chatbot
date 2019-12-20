# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# chatbot = ChatBot(    'Exact Response Example Bot',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             'import_path': 'chatterbot.logic.BestMatch'
#         },
#         {
#             'import_path': 'chatterbot.logic.SpecificResponseAdapter',
#             'input_text': 'Help me!',
#             'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
#         }
#     ]
# )
#
# # Create a new trainer for the chatbot
# # trainer = ChatterBotCorpusTrainer(chatbot)
#
# # Train the chatbot based on the english corpus
# # trainer.train("chatterbot.corpus.english")
# # response = chatbot.get_response('Help me!')
#
# print("============================================\n")
#
# # Get a response to an input statement
# while True:
#     try: 
#         inp = input("Enter a query: \n")
#         print(chatbot.get_response(inp))
#     except Exception as e:
#         raise
#         break
