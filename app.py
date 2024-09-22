from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# データベース接続用関数
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ホームページと評価入力ページ
@app.route('/')
def index():
    return render_template('index.html')

# 評価入力の処理
@app.route('/submit', methods=['POST'])
def submit_evaluation():
    team_name = request.form['team_name']
    evaluation = request.form['evaluation']
    comments = request.form['comments']

    # データベースに保存
    conn = get_db_connection()
    conn.execute('INSERT INTO evaluations (team_name, evaluation, comments) VALUES (?, ?, ?)',
                 (team_name, evaluation, comments))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# 評価一覧の表示
@app.route('/evaluations')
def evaluations():
    conn = get_db_connection()
    evaluations = conn.execute('SELECT * FROM evaluations').fetchall()
    conn.close()
    return render_template('evaluations.html', evaluations=evaluations)

if __name__ == '__main__':
    app.run(debug=True)