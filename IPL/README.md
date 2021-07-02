# IPL Inning Score and Winner Prediction - Deployment
![Python 3.9](https://img.shields.io/badge/Python-3.9-brightgreen.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-yellow)

#### A glimpse of the web app:
 ![GIF](readme_resources/j.gif)

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)

## Demo
Link: [https://ipl-prediciton-1.herokuapp.com/](https://ipl-prediciton-1.herokuapp.com/)

## Overview
This is a Flask web app and it has 2 functionalities.
1) **Predicts the innings Score**
2) **Predicts the winner of the match**


## Motivation
What to do when you are at home due to this pandemic situation? I started to learn Machine Learning model to get most out of it. I came to know mathematics behind all supervised models. Finally it is important to work on application (real world application) to actually make a difference.

## Installation
The Code is written in Python 3.9.2 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── static 
    ├── a.png
    ├──csk.png
    ├──dc.png
    ├──rcb.png
    ├──kkr.png
    ├──rr.png
    ├──mi.png
    ├──srh.png
    ├──kxip.png
    ├──background.png
    ├──ipl-favicon.ico
├── template
    ├── index.html
    ├── predict_score.html
    ├── score.html
    ├── predict_winner.html
    ├── winner.html
├── readme_resources
    ├── ipl-first-innings-score-web-app.gif
    ├── application-error-heroku.png
├── README.md
├── app.py
├── score.pkl
├── score.ipynb
├── winner.pkl
├── winner.ipynb
├── requirements.txt
├── Procfile
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


## Bug / Feature Request

• If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/SuryanshNaugraiya/IPL/issues) here by including your search query and the expected result.<br />
• If you encounter this webapp as shown in the picture given below, it is occuring just because **free dynos for this particular month provided by Heroku have been completely used.** _You can access the webpage on 1st of the next month._<br />
• Sorry for the inconvenience.

![Heroku-Error](readme_resources/application-error-heroku.png)


## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End 

#### Please do ⭐ the repository, if it helped you in anyway.
