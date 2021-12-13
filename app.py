#!/usr/bin/python3 

from flask import Flask, render_template, redirect, url_for, session, request, Response
from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime
import json
import cv2
import time
import mediapipe as mp
from sqlalchemy.sql.elements import Null
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app = Flask(__name__)
app.secret_key = 'any random string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/members"

db = SQLAlchemy(app)                                                                  

class user(db.Model):
    UserID = db.Column(db.Integer, primary_key = True)
    UserName = db.Column(db.String(100), unique=True, nullable=False)
    UserPassword = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    CreateTime = db.Column(db.DateTime, nullable=False)
    LastModifyTime = db.Column(db.DateTime)

    def __init__(self, UserName, UserPassword, gender, birthday, height, weight, CreateTime, LastModifyTime):
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.gender = gender
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.CreateTime = CreateTime
        self.LastModifyTime = LastModifyTime

# ============== from Claude =================
class score_imin(db.Model):
    GameID = db.Column(db.Integer, primary_key = True)
    UserName = db.Column(db.String(100), nullable=False)
    GameTime = db.Column(db.DateTime, nullable=False)
    GameScore = db.Column(db.Integer, nullable=False)

    def __init__(self, UserName, GameTime, GameScore):
        self.UserName = UserName
        self.GameTime = GameTime
        self.GameScore = GameScore

class score_flash(db.Model):
    GameID = db.Column(db.Integer, primary_key = True)
    UserName = db.Column(db.String(100), nullable=False)
    GameTime = db.Column(db.DateTime, nullable=False)
    GameScore = db.Column(db.Integer, nullable=False)

    def __init__(self, UserName, GameTime, GameScore):
        self.UserName = UserName
        self.GameTime = GameTime
        self.GameScore = GameScore
# ============== from Claude end =================

db.create_all()

@app.route('/')
def index():
    if 'UserName' in session:
        UserName = session['UserName']
        return render_template("index.html", page = 'member_center', pagename = '會員中心', logout = '登出') 
    return render_template('index.html', page = 'login', pagename = '登入', logout = '')

@app.route('/game')
def game():
    if 'UserName' in session:
        UserName = session['UserName']
        return render_template("game.html", page = 'member_center', pagename = '會員中心', logout = '登出') 
    return render_template("game.html", page = 'login', pagename = '登入')

@app.route('/imin', methods = ['GET', 'POST'])
def imin():
    iminscore = 0
    if 'UserName' not in session:
        return redirect(url_for("login"))
   
    from gamepackage.imin2 import imin
    iminscore = imin()
    game_score = score_imin(GameTime = datetime.now(), UserName = session['UserName'], GameScore = iminscore)
    db.session.add(game_score)
    db.session.commit()
    
    return redirect(url_for("game"))


@app.route('/flash', methods = ['GET', 'POST'])
def flash():
    flashscore = 0
    if 'UserName' not in session:
        return redirect(url_for("login"))

    from gamepackage.flash import flash
    flashscore = flash()
    if flashscore < 0: 
        flashscore = 0
    game_score = score_flash(GameTime = datetime.now(), UserName = session['UserName'], GameScore = flashscore)
    db.session.add(game_score)
    db.session.commit()
    return redirect(url_for("game"))
   

@app.route('/rank')
def rank():
    imin_rank = []
    rank_imin = score_imin.query.order_by(score_imin.GameScore.desc()).all()
    for i in range(1, 11):
        dic = {}
        dic['rank'] = i
        dic['user'] = rank_imin[i].UserName
        dic['score'] = rank_imin[i].GameScore
        imin_rank.append(dic)
   
    flash_rank = []
    rank_flash = score_flash.query.order_by(score_flash.GameScore.desc()).all()
    for i in range(1, 11):
        dic = {}
        dic['rank'] = i
        dic['user'] = rank_flash[i].UserName
        dic['score'] = rank_flash[i].GameScore
        flash_rank.append(dic)

    if 'UserName' in session:
        UserName = session['UserName']
        return render_template("rank.html", page = 'member_center', pagename = '會員中心', logout = '登出', imin_rank = imin_rank, flash_rank = flash_rank)
    return render_template("rank.html", page = 'login', pagename = '登入', imin_rank = imin_rank, flash_rank = flash_rank)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        users = user.query.all()
        for person in users: 
            if request.form['usr'] == person.UserName and request.form['pwd'] == person.UserPassword: 
                session['UserName'] = request.form['usr']
                return redirect(url_for('index'))
                break
            error = '使用者名稱或密碼錯誤!'   
    return render_template("login.html",  error = error)

@app.route('/logout')
def logout():
    session.pop('UserName', None)
    return redirect(url_for('index'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        time = datetime.now()
        member = user(UserName = request.form['usr'], UserPassword = request.form['pwd'], gender = request.form['gender'], 
        birthday = request.form['bday'], height = request.form['height'], weight = request.form['weight'], CreateTime = time, LastModifyTime=None)
        db.session.add(member)
        db.session.commit()
        
        UserName = request.form['usr']
        f = request.files['photo']
        img_path = './static/profiles/' + UserName + '.jpg'
        f.save(img_path)
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/member_center', methods = ['GET', 'POST'])
def membercenter():
    UserName = session['UserName']
    member = user.query.filter_by(UserName=UserName).first()
    photo_path = '../static/profiles/' + UserName + '.jpg'

    if request.method == 'POST':
        time = datetime.now()
        member.UserName=request.form['usr']
        member.gender = request.form['gender']
        member.birthday = request.form['bday']
        member.height = request.form['height']
        member.weight = request.form['weight']
        member.LastModifyTime = time
        db.session.commit()
        
        session['UserName'] = request.form['usr']
        f = request.files['photo']
        img_path = './static/profiles/' + UserName + '.jpg'
        f.save(img_path)

        photo_path = '../static/profiles/' + UserName + '.jpg'

    return render_template("member_center.html", logout = '登出', UserName = member.UserName, UserPassword = member.UserPassword, gender = member.gender, birthday = member.birthday, 
    height = member.height, weight = member.weight, photo_path = photo_path)

@app.route('/plot1.png')
def plot_png_imin():
    fig = create_figure_imin()
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_imin():
    x = list()
    y = list()
    x_ticks = list()
    UserName = session['UserName']
    user_imin = score_imin.query.filter_by(UserName=UserName).order_by(score_imin.GameTime.asc()).all()
    for i, score, in enumerate(user_imin):
        s = score.GameScore
        t = score.GameTime
        x.append(i+1)
        y.append(s)
        x_ticks.append(t)

    fig = Figure(figsize=(9, 4.5))
    ax = fig.subplots()
    ax.plot(x, y, '-ro', color='tab:red')
    ax.set_title("I'm in", fontsize=32, color='purple', pad=20)
    ax.set_ylim(0, 200)
    ax.set_xticks(x)
    ax.set_xticklabels(x_ticks, rotation=350, fontsize=8)
    ax.spines["top"].set_alpha(0.0)    
    ax.spines["bottom"].set_alpha(0.3)
    ax.spines["right"].set_alpha(0.0)    
    ax.spines["left"].set_alpha(0.3)  
    fig.patch.set_facecolor('#E0E0E0')
    fig.patch.set_alpha(0)    
    ax.patch.set_facecolor('#E0E0E0')
    ax.patch.set_alpha(0.3) 
    fig.tight_layout()
    return fig

@app.route('/plot2.png')
def plot_png_flash():
    fig = create_figure_flash()
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_flash():
    x = list()
    y = list()
    x_ticks = list()
    UserName = session['UserName']
    user_fall = score_flash.query.filter_by(UserName=UserName).order_by(score_flash.GameTime.asc()).all()
    for i, score, in enumerate(user_fall):
        s = score.GameScore
        t = score.GameTime
        x.append(i+1)
        y.append(s)
        x_ticks.append(t)

    fig = Figure(figsize=((9, 4.5)))
    ax = fig.subplots()
    ax.plot(x, y, '-ro', color='tab:red')
    ax.set_title("Flash", fontsize=32, color='purple', pad=20)
    ax.set_ylim(0, 210)
    ax.set_xticks(x)
    ax.set_xticklabels(x_ticks, rotation=350, fontsize=8)
    ax.spines["top"].set_alpha(0.0)    
    ax.spines["bottom"].set_alpha(0.3)
    ax.spines["right"].set_alpha(0.0)    
    ax.spines["left"].set_alpha(0.3) 
    fig.patch.set_facecolor('#E0E0E0')
    fig.patch.set_alpha(0)    
    ax.patch.set_facecolor('#E0E0E0')
    ax.patch.set_alpha(0.3)  
    fig.tight_layout()
    return fig

@app.route('/set_password', methods = ['GET', 'POST'])
def set_password():
    if request.method == 'POST':
        UserName = request.form['usr']
        member = user.query.filter_by(UserName=UserName).first()
        if member.birthday == datetime.strptime(request.form['bday'],  "%Y-%m-%d"):
            member.UserPassword = request.form['pwd']
            db.session.commit()
            return redirect(url_for('login'))
        else:
            error = '使用者名稱或生日錯誤' 
            return render_template("set_password.html",  error = error)   
    return render_template("set_password.html")


# @app.route('/create_user', methods = ['POST'])
# def createuser():
#     input_json = request.get_json(force=True) 
#     member = user(UserName = input_json['UserName'], UserPassword = input_json['UserPassword'], gender = input_json['gender'], 
#     birthday = input_json['birthday'], height = input_json['height'], weight = input_json['weight'], CreateTime = input_json['CreateTime'], LastModifyTime=None)
#     db.session.add(member)
#     db.session.commit()
#     return 'OK'

# @app.route('/create_score_box', methods = ['POST'])
# def create_score_box():
#     input_json = request.get_json(force=True) 
#     game_score = score_box(UserName = input_json['UserName'], GameTime = input_json['GameTime'], GameScore = input_json['GameScore'])
#     db.session.add(game_score)
#     db.session.commit()
#     return 'OK'

# @app.route('/create_score_fall', methods = ['POST'])
# def create_score_fall():
#     input_json = request.get_json(force=True) 
#     game_score = score_fall(UserName = input_json['UserName'], GameTime = input_json['GameTime'], GameScore = input_json['GameScore'])
#     db.session.add(game_score)
#     db.session.commit()
#     return 'OK'


if __name__ == '__main__':
    app.run(debug = True)