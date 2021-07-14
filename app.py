from flask import Flask, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def hello_world():

    try:

        # <----------------------World Data top countries only!------------------------------------------>

        r = requests.get('https://covid19.mathdro.id/api/confirmed')
        arr = list(r.json())

        confirmed_map = defaultdict(list)
        deaths_map = defaultdict(list)
        recovered_map = defaultdict(list)
        for i in range(len(arr)):
            confirmed_map[arr[i]['countryRegion']].append(arr[i]['confirmed'])
            recovered_map[arr[i]['countryRegion']].append(arr[i]['recovered'])
            deaths_map[arr[i]['countryRegion']].append(arr[i]['deaths'])

        for key, value in confirmed_map.items():
            confirmed_map[key] = sum(value)

        # US is having "None" type so deleting the key!
        del recovered_map['US']
        for key, value in recovered_map.items():
            recovered_map[key] = sum(value)

        recovered_map['US'] = 0

        for key, value in deaths_map.items():
            deaths_map[key] = sum(value)

        df = pd.DataFrame()
        df['Country'] = list(confirmed_map.keys())
        df['ConfirmedCases'] = list(confirmed_map.values())
        df['RecoveredCases'] = list(recovered_map.values())
        df['DeathCases'] = list(deaths_map.values())

        # Extracting the top15 effected countries

        countrylist = list(df['Country'].head(15))
        globalconfirmedcases = list(df['ConfirmedCases'].head(15))
        globalrecoveredcases = list(df['RecoveredCases'].head(15))
        globaldeathcases = list(df['DeathCases'].head(15))

        globalrecoverylist = []
        for i, j in zip(globalconfirmedcases, globalrecoveredcases):
            globalrecoverylist.append(round((j/i)*100, 2))

        # print(globalrecoverylist)

        # <--------------------------------India's Data---------------------------------------------------------->
        r = requests.get(
            'https://covid19.mathdro.id/api/countries/India/confirmed')
        arr = list(r.json())
        datetosend = arr[0]['lastUpdate']
        stateslist = []
        confirmed_map = {}
        deaths_map = {}
        active_map = {}
        recovered_map = {}
        for i in range(len(arr)):
            stateslist.append(arr[i]['provinceState'].lower())
            confirmed_map[arr[i]['provinceState'].lower()
                          ] = arr[i]['confirmed']
            deaths_map[arr[i]['provinceState'].lower()] = arr[i]['deaths']
            active_map[arr[i]['provinceState'].lower()] = arr[i]['active']
            recovered_map[arr[i]['provinceState'].lower()
                          ] = arr[i]['recovered']

        recoveryrate = []
        for i, j in zip(list(confirmed_map.values()), list(recovered_map.values())):
            recoveryrate.append(round((j/i)*100, 2))

        # print(recoveryrate)
        if request.method == 'POST':
            state = request.form.get('state')
            state = [state][0].lower()

            if state in stateslist:
                confirmed = confirmed_map[state]
                active = active_map[state]
                deaths = deaths_map[state]
                recovered = recovered_map[state]
                # print(active, confirmed, recovered, deaths)
                return render_template('index.html', active=active, confirmed=confirmed, deaths=deaths, recovered=recovered, activemap=list(active_map.values()),
                                       confirmedmap=list(
                                           confirmed_map.values()),
                                       recoveredmap=list(
                                           recovered_map.values()),
                                       deathsmap=list(deaths_map.values()),
                                       stateslist=stateslist, datetosend=datetosend, state=[state.capitalize()], showchart=True, recoveryrate=recoveryrate, isrecovery=True, countrylist=countrylist,
                                       globalconfirmedcases=globalconfirmedcases,
                                       globalrecoveredcases=globalrecoveredcases,
                                       globaldeathcases=globaldeathcases,
                                       globalrecoverylist=globalrecoverylist, showcards=True)

            else:
                # send an alert to please will the name clearly!
                return render_template('dashboarderror.html', statenotpresent=True)
    except:
        return render_template('exception.html')

    return render_template('index.html')


@app.route('/vaccine', methods=['GET', 'POST'])
def vaccine():

    try:
        url = 'https://en.wikipedia.org/wiki/COVID-19_vaccination_in_India#Andhra_Pradesh'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = []
        table = soup.find('table', attrs={"class": "plainrowheaders"})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            # Get rid of empty values
            data.append([ele for ele in cols if ele])

        data = data[2:]
        data = data[:-2]
        states = ['andaman and nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra and nagar haveli', 'daman and diu', 'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu and kashmir', 'jharkhand',
                  'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']

        population = [int(''.join(data[i][0].split(',')))
                      for i in range(len(data))]
        dose1 = [int(''.join(data[i][1].split(','))) for i in range(len(data))]
        dose2 = [int(''.join(data[i][2].split(','))) for i in range(len(data))]
        atmostonedose = [float(data[i][4].split('%')[0])
                         for i in range(len(data))]
        fullyvaccinated = [float(data[i][5].split('%')[0])
                           for i in range(len(data))]

        # creating maps
        populationmap = dict(list(
            (sorted(dict(zip(states, population)).items(), key=lambda x: x[1], reverse=True))))
        dose1_map = dict(list(
            (sorted(dict(zip(states, dose1)).items(), key=lambda x: x[1], reverse=True))))
        dose2_map = dict(list(
            (sorted(dict(zip(states, dose2)).items(), key=lambda x: x[1], reverse=True))))
        atmostonedose_map = dict(list((sorted(
            dict(zip(states, atmostonedose)).items(), key=lambda x: x[1], reverse=True))))
        fulldosemap = dict(list((sorted(
            dict(zip(states, fullyvaccinated)).items(), key=lambda x: x[1], reverse=True))))

        # segregating the top doses,top doses will give a value if compared to states which are having more pouplation instead of less,so i have segrated the dose results based on the highly populated states!

        def getnewmap(topstates, mapper):
            maps = {}
            for key, val in mapper.items():
                if key in list(topstates.keys()):
                    maps[key] = val

            return maps

        # segregating the top doses

        topstates = dict(list(populationmap.items())[:5])
        topdose1 = getnewmap(topstates, dose1_map)
        topdose2 = getnewmap(topstates, dose2_map)
        toponedose = getnewmap(topstates, atmostonedose_map)
        topfullvaccine = getnewmap(topstates, fulldosemap)

        # retriving the data from the form

        if request.method == 'POST':

            try:
                statename = request.form.get('state').lower()
                dose1 = dose1_map[statename]
                dose2 = dose2_map[statename]
                atmostonedose = atmostonedose_map[statename]
                fulldose = fulldosemap[statename]
                populationstate = populationmap[statename]

                print(dose1, dose2, atmostonedose, fulldose)
                return render_template('vaccine.html', showcards=True, dose1=dose1, dose2=dose2, atmostonedose=atmostonedose, fulldose=fulldose, state=[statename.capitalize()],
                                       topstates=list(topstates.keys()), population=list(topstates.values()),
                                       statedose1=list(topdose1.values()), statedose2=list(topdose2.values()),
                                       toponedose=list(toponedose.values()), tofulldose=list(topfullvaccine.values()), populationstate=populationstate,
                                       showchart=True, fullyvaccinatedstate=list(fulldosemap.keys()),
                                       fullyvaccinatedvalues=list(
                    fulldosemap.values()),
                    atmostonedosemapstate=list(
                    atmostonedose_map.keys()),
                    atmostonedosevalue=list(atmostonedose_map.values()),)
            except:
                return render_template('vaccineerror.html', statenotpresent=True)
    except:
        return render_template('exception.html')

    return render_template('vaccine.html')


@app.route('/covidtable', methods=['GET', 'POST'])
def gettable():

    try:
        r = requests.get(
            'https://covid19.mathdro.id/api/countries/India/confirmed')
        arr = list(r.json())
        datetosend = arr[0]['lastUpdate']
        stateslist = []
        confirmed_map = {}
        deaths_map = {}
        active_map = {}
        recovered_map = {}
        for i in range(len(arr)):
            stateslist.append(arr[i]['provinceState'])
            confirmed_map[arr[i]['provinceState']] = arr[i]['confirmed']
            deaths_map[arr[i]['provinceState']] = arr[i]['deaths']
            active_map[arr[i]['provinceState']] = arr[i]['active']
            recovered_map[arr[i]['provinceState']] = arr[i]['recovered']

        active = list(active_map.values())
        confirmed = list(confirmed_map.values())
        deaths = list(deaths_map.values())
        recovered = list(recovered_map.values())

        # recoveryrate = recovered/confirmed*100

        recoveryrate = [round(((i/j)*100), 2)
                        for i, j in zip(recovered, confirmed)]

        alltogether = []
        for state, i, j, k, l, m in zip(stateslist, active, confirmed, deaths, recovered, recoveryrate):
            alltogether.append([state, i, j, k, l, m])

        return render_template('covidtable.html', active=sum(active),
                               confirmed=sum(confirmed), deaths=sum(deaths), recovered=sum(recovered),
                               date=datetosend, details=alltogether)

    except:
        return render_template('exception.html')

    return render_template('home.html')


@app.route('/vaccinetable', methods=['GET', 'POST'])
def getvaccinetable():

    try:

        # Scrapping Date

        r = requests.get(
            'https://covid19.mathdro.id/api/countries/India/confirmed')
        arr = list(r.json())
        datetosend = arr[0]['lastUpdate']

        url = 'https://en.wikipedia.org/wiki/COVID-19_vaccination_in_India#Andhra_Pradesh'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = []
        table = soup.find('table', attrs={"class": "plainrowheaders"})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            # Get rid of empty values
            data.append([ele for ele in cols if ele])

        data = data[2:]
        data = data[:-2]
        states = ['andaman and nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra and nagar haveli', 'daman and diu', 'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu and kashmir', 'jharkhand',
                  'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
        population = [int(''.join(data[i][0].split(',')))
                      for i in range(len(data))]
        dose1 = [int(''.join(data[i][1].split(','))) for i in range(len(data))]
        dose2 = [int(''.join(data[i][2].split(','))) for i in range(len(data))]
        atmostonedose = [float(data[i][4].split('%')[0])
                         for i in range(len(data))]
        fullyvaccinated = [float(data[i][5].split('%')[0])
                           for i in range(len(data))]

        alltogether = []
        for i, j, k, l, m, n in zip(states, population, dose1, dose2, atmostonedose, fullyvaccinated):
            alltogether.append([i, j, k, l, m, n])

        # print(alltogether)
        return render_template('vaccinetable.html', date=datetosend,
                               totalpopulation=sum(population), totaldose1=sum(dose1), totaldose2=sum(dose2), totaldose=round(sum(fullyvaccinated)/len(fullyvaccinated), 2),
                               alltogether=alltogether)

    except:
        return render_template('exception.html')

    return render_template('vaccinetable.html')


if __name__ == '__main__':
    app.run(debug=True)
