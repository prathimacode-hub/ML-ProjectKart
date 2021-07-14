from flask import Flask, render_template, request

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = load_model('iplmodel.h5')


@app.route('/Orangecapdashboard', methods=['GET', 'POST'])
def orangecapdashboard():

    return render_template('orange.html')


@app.route('/Purplecapdashboard', methods=['GET', 'POST'])
def purplecapdashboard():

    return render_template('purple.html')


@app.route('/', methods=['GET', 'POST'])
def getdata():

    if request.method == 'POST':
        cap = request.form['cap']
        # print(cap, season)
        if cap == 'OrangeCap':
            return render_template('Orangecapdashboard.html', cap=cap)

        elif cap == 'PurpleCap':
            return render_template('Purplecapdashboard.html', cap=cap)

    return render_template('index.html')


# <!-- consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
#                     'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
#                     'Delhi Daredevils', 'Sunrisers Hyderabad'] -->

@app.route('/predict', methods=['GET', 'POST'])
def hello_world():

    try:

        team_dict = {1: 'Kolkata Knight Riders', 2: 'Chennai Super Kings', 3: 'Rajasthan Royals', 4: 'Mumbai Indians',
                     5: 'Kings XI Punjab', 6: 'Royal Challengers Bangalore', 7: 'Delhi Daredevils', 8: 'Sunrisers Hyderabad'}

        final_array = []
        temp_array = []
        batting_team = [0]*8
        bowling_team = [0]*8
        wickets_array = [0]*10
        overs_array = [0]*10

        if request.method == 'POST':

            # Batting team
            team_bat = request.form['batting']
            team_bowl = request.form['bowling']
            current_wicket = request.form['currentwickets']
            current_overs = request.form['currentovers']
            current_score = int(request.form['currentruns'])

            if team_bat == team_bowl:
                return render_template('error.html')

            else:

                # Batting team
                for key, val in team_dict.items():
                    if team_bat == val:
                        batting_team[key-1] = 1

                # Bowling team

                for key, val in team_dict.items():
                    if team_bowl == val:
                        bowling_team[key-1] = 1

                # Wickets array

                for i in range(1, len(wickets_array)):
                    if int(current_wicket) == i:
                        wickets_array[i-1] = 1

                # print(f' Wickets array : {wickets_array}')

                # Current overs

                for i in range(1, len(overs_array)):
                    if int(current_overs) == i:
                        overs_array[i-1] = 1

                final_array = final_array+batting_team+bowling_team+wickets_array+overs_array
                final_array.append(current_score)

                mm = MinMaxScaler()
                final_array = np.array([final_array])
                # print(final_array)

                # trained_scaled = mm.fit_transform(final_array)
                # print(trained_scaled)

                predictions = model.predict(final_array)
                value = int(int(predictions[0][0])//100)

                if current_score > 100 and int(current_wicket) <= 5:
                    value = value-50
                    return render_template('result.html', value=value)

                elif current_score > 100 and int(current_wicket) >= 5 and int(current_overs) >= 10:
                    value = value-75
                    return render_template('result.html', value=value)

                elif int(current_wicket) == 9 or int(current_wicket) == 8:
                    value = current_score+10
                    return render_template('result.html', value=value)

                else:
                    return render_template('result.html', value=value)

                # print(value)

        return render_template('predict.html')

    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
