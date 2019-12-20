from chatterbot.logic import LogicAdapter
from utils import *
import spacy

class CityAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.dest_city = False
        self.dest_date = False

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        words = ['booking', 'book', 'centre', 'center']
        if any(x in statement.text.split() for x in words):
            self.dest_city = True

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(str(statement.text))

        for ent in doc.ents:
            if ent.label_ == 'DATE':
                self.dest_date = True

        if self.dest_city or self.dest_date:
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        try:
            from chatterbot.conversation import Statement

            place = None
            cities = getPlaces(getDataFrame('locations.csv'), city=True)
            words = str(input_statement).lower().split(' ')
            for i in words:
                if i in cities:
                    place = i
                    break

            datetime = getDate(str(input_statement))
            # date = datetime.split(' ')[0]
            # time = time.split(' ')[1]

            if self.dest_date and place:
                return Statement(text=str(dict({
                    'found': True,
                    'datetime': True,
                    'data': {
                        'datetime': datetime.split(' '),
                        'place': place.capitalize()
                    }
                })))

            else:
                if place:
                    return Statement(text=str(dict({
                        'found': True,
                        'datetime': False,
                        'data': {
                            'place': place.capitalize()
                        }
                    })))
                else:
                    return Statement(text=str(dict({
                        'found': False,
                        'datetime': False,
                    })))


        except Exception as e:
            raise
