from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        words = ['booking', 'book', 'centre', 'center']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import spacy
        # import requests

        # Make a request to the temperature API
        # response = requests.post('http://localhost:5000/recommend/search', data={'query':'excel'})
        # data = response.json()


        nlp = spacy.load("en_core_web_sm")
        doc = nlp("Apple is looking at buying U.K. startup for $1 billion tomorrow and at December 17th")

        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)


        # print(response)
        # print(data['results'])

        # Let's base the confidence value on if the request was successful

        response_statement = Statement(text='The results are \n{}'.format(data))

        return response_statement
        # return confidence, str(data)
