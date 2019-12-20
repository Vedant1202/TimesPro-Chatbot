from chatterbot.logic import LogicAdapter
from utils import *
import spacy

def can_process(sentence):
    """
    Return true if the input statement contains
    'what' and 'is' and 'temperature'.
    """
    if len(str(sentence)) > 0:
        return True
    else:
        return False

def retrieveCentreBot(cityName=None):
    try:
        if cityName:

            place = None
            centres = getPlaces(getDataFrame('locations.csv'), centre=True, cityName=cityName)

            print("The list of centres in {} are: ".format(cityName.capitalize()))
            for i in centres:
                if i.strip().startswith('tsw'):
                    print(i)

            sentence = input("Enter your choice: \n")
            if not can_process(sentence):
                return False

            else:
                words = str(sentence).lower().split(' ')
                for i in words:
                    if i in centres:
                        place = i
                        break
                    for j in centres:
                        if i.strip() in j.split('-')[2].strip():
                            place = j
                            break

                if place:
                    return dict({
                        'found': True,
                        'centre': place,
                    })

                else:
                    return dict({
                        'found': False,
                    })

        else:
            return False

    except Exception as e:
        raise
