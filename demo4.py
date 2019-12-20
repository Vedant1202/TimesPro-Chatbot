

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from book_centre_adapter import retrieveCentreBot
from utils import *

def main():
    chatbot = ChatBot('Example Bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'book_place_adapter.CityAdapter'
                },
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand. Please try again.',
                    'maximum_similarity_threshold': 0.90
                }
            ],
            preprocessors=['chatterbot.preprocessors.clean_whitespace']
    )


    while True:
        try:
            print('\n')
            text = input("What would you like to do?\n")
            response = chatbot.get_response(text)
            if not str(response).strip().startswith("{'"):
                print(response)
            else:
                response = eval(str(response))
                if response['found']:
                    if response['datetime']:
                        data = response['data']
                        place = retrieveCentreBot(data['place'].lower())
                        if place['found']:
                            if str(data['datetime'][1]) == "00:00:00":
                                print("Booking at {} at date {} done".format(place['centre'], data['datetime'][0]))
                            else:
                                print("Booking at {} at date {} at time {} done".format(place['centre'], data['datetime'][0], data['datetime'][1]))
                        else:
                            print("I am sorry I did not get you.")
                    else:
                        data = response['data']
                        place = retrieveCentreBot(data['place'].lower())
                        if place['found']:
                            dateQuery = input("What date do you want to book?\n")
                            date = getDate(dateQuery)
                            if str(date.split(' ')[1]) == "00:00:00":
                                if checkIfAvailableSeats(df=getDataFrame('locations.csv'), centreName=place['centre'])['seatsAvailable']:
                                    print("Booking at {} on {} done.".format(place['centre'], date.split()[0]))
                                else:
                                    print("Booking at {} on {} could not be done. The seats are full.".format(place['centre'], date.split()[0]))
                            else:
                                if checkIfAvailableSeats(df=getDataFrame('locations.csv'), centreName=place['centre'])['seatsAvailable']:
                                    print("Booking at {} on {} at {} done.".format(place['centre'], date.split()[0], date.split()[1]))
                                else:
                                    print("Booking at {} on {} at {} could not be done. The seats are full.".format(place['centre'], date.split()[0], date.split()[1]))
                        else:
                            print("I am sorry I did not get you.")
                else:
                    print("I am sorry I did not get you.")

        except Exception as e:
            raise e


if __name__ == '__main__':
    main()





#
