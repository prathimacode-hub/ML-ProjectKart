import pickle as pkl
from flask import Flask, render_template, request, url_for, redirect
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_score', methods=['GET', 'POST'])
def predict_score():
    return render_template('predict_score.html')


@app.route('/score', methods=['GET', 'POST'])
def score():
    temp_array = list()

    if request.method == 'POST':

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        x = request.form['venue']
        if x == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif x == 'Feroz Shah Kotla':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Wankhede Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        elif x == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif x == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Eden Gardens':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Dr DY Patil Sports Academy':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Brabourne Stadium':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Sardar Patel Stadium, Motera':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif x == 'Himachal Pradesh Cricket Association Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Subrata Roy Sahara Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif x == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif x == 'Shaheed Veer Narayan Singh International Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif x == 'JSCA International Stadium Complex':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Maharashtra Cricket Association Stadium':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif x == 'Barabati Stadium':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        overs = float(request.form['overs'])
        runs_last_5 = int(request.form['runs_last_5'])
        wickets_last_5 = int(request.form['wickets_last_5'])

        temp_array = temp_array + [runs, wickets, overs, runs_last_5, wickets_last_5]

        data = np.array([temp_array]).reshape(1, -1)

        with open('score.pkl', 'rb') as f:
            regressor = pkl.load(f)

        if batting_team == bowling_team or runs < runs_last_5 or wickets < wickets_last_5 or wickets > 10 or overs < 5.0:
            return redirect(url_for('predict_score'))
        else:
            my_prediction = int(regressor.predict(data)[0])
            return render_template('score.html', lower_limit=my_prediction - 10, upper_limit=my_prediction + 5)


@app.route('/predict_winner', methods=['GET', 'POST'])
def predict_winner():
    return render_template('predict_winner.html')


@app.route('/winner', methods=['GET', 'POST'])
def winner():
    temp = [0, 0, 0, 0, 0]

    team1 = str(request.args.get('list1'))
    if team1 == 'Royal Challengers Bangalore':
        temp[0] = 0
    elif team1 == 'Kings XI Punjab':
        temp[0] = 1
    elif team1 == 'Delhi Capitals':
        temp[0] = 2
    elif team1 == 'Mumbai Indians':
        temp[0] = 3
    elif team1 == 'Rajasthan Royals':
        temp[0] = 4
    elif team1 == 'Chennai Super Kings':
        temp[0] = 5
    elif team1 == 'Kolkata Knight Riders':
        temp[0] = 6
    else:
        temp[0] = 7

    team2 = str(request.args.get('list2'))
    if team2 == 'Royal Challengers Bangalore':
        temp[1] = 0
    elif team2 == 'Kings XI Punjab':
        temp[1] = 1
    elif team2 == 'Delhi Capitals':
        temp[1] = 2
    elif team2 == 'Mumbai Indians':
        temp[1] = 3
    elif team2 == 'Rajasthan Royals':
        temp[1] = 4
    elif team2 == 'Chennai Super Kings':
        temp[1] = 5
    elif team2 == 'Kolkata Knight Riders':
        temp[1] = 6
    else:
        temp[1] = 7

    x = str(request.args.get('list3'))
    if x == 'M Chinnaswamy Stadium':
        temp[2] = 1
    elif x == 'Punjab Cricket Association Stadium, Mohali':
        temp[2] = 2
    elif x == 'Feroz Shah Kotla':
        temp[2] = 3
    elif x == 'Wankhede Stadium':
        temp[2] = 4
    elif x == 'Sawai Mansingh Stadium':
        temp[2] = 5
    elif x == 'MA Chidambaram Stadium, Chepauk':
        temp[2] = 6
    elif x == 'Eden Gardens':
        temp[2] = 7
    elif x == 'Dr DY Patil Sports Academy':
        temp[2] = 8
    elif x == 'Brabourne Stadium':
        temp[2] = 9
    elif x == 'Sardar Patel Stadium, Motera':
        temp[2] = 10
    elif x == 'Himachal Pradesh Cricket Association Stadium':
        temp[2] = 11
    elif x == 'Subrata Roy Sahara Stadium':
        temp[2] = 12
    elif x == 'Rajiv Gandhi International Stadium, Uppal':
        temp[2] = 13
    elif x == 'Shaheed Veer Narayan Singh International Stadium':
        temp[2] = 14
    elif x == 'JSCA International Stadium Complex':
        temp[2] = 15
    elif x == 'Maharashtra Cricket Association Stadium':
        temp[2] = 16
    elif x == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
        temp[2] = 17
    elif x == 'Barabati Stadium':
        temp[2] = 18
    else:
        temp[2] = 19

    toss_win = int(request.args.get('toss_winner'))
    temp[3] = toss_win

    choose = int(request.args.get('fb'))
    temp[4] = choose

    with open('winner.pkl', 'rb') as f:
        model = pkl.load(f)

    lst = np.array(temp).reshape(1, -1)
    prediction = model.predict(lst)

    if prediction == 0:
        team_win = team1
    else:
        team_win = team2

    if team1 == team2:
        return redirect(url_for('predict_winner'))
    else:
        return render_template('winner.html', data=team_win)


if __name__ == "__main__":
    app.run(debug=True,use_reloader = False)


