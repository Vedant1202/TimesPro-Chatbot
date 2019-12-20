import pandas as pd

def getDataFrame(url):
    try:
        df = pd.read_csv(url)
        return df.applymap(lambda s:s.lower() if type(s) == str else s)
    except Exception as e:
        raise


def getPlaces(df, city=False, centre=False, cityName=None):
    citylabels = ['City', 'Cityalias1', 'Cityalias2', 'Cityalias3', 'Cityalias4', 'Cityalias5']
    centrelabels = ['Center', 'centeralias1', 'centeralias2', 'centeralias3']
    places = []

    if city:
        for j in citylabels:
            for i in df[j]:
                if str(i).lower() != 'nan':
                    places.append(i.lower())

        return list(set(places))


    elif centre and cityName:
        for i in centrelabels:
            temp = df.loc[(df['City'] == cityName) | (df['Cityalias1'] == cityName) | (df['Cityalias2'] == cityName) | (df['Cityalias3'] == cityName) | (df['Cityalias4'] == cityName) | (df['Cityalias5'] == cityName)][i]
            for j in temp:
                if str(j).lower() != 'nan' and str(j).startswith('tsw'):
                    places.append(j)

        return list(set(places))

    else:
        return False



def getDate(sentence):
    try:
        import datefinder
        matches = datefinder.find_dates(sentence)

        for match in matches:
            if match:
                return str(match)

    except Exception as e:
        raise



def checkIfAvailableSeats(df=None, centreName=None):
    centrelabel = 'Center'
    seatsLabel = 'Setspending'

    if centreName:
        for i in range(len(df[centrelabel]) - 1):
            if str(df[centrelabel][i]).strip() == str(centreName).strip():
                noOfSeats = df[seatsLabel][i]

        if int(noOfSeats) > 0:
            return dict({
                'seatsAvailable': True,
                'noOfSeats': noOfSeats
            })
        else:
            return dict({
                'seatsAvailable': False
            })

    else:
        return False









#
