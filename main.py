from flask import Flask, session, redirect, url_for, request, render_template, send_from_directory

app = Flask(__name__)

@app.route('/login')
def index():
    return "success"

@app.route('/', methods=['GET', 'POST'])
def login():
    title = []
    # POSTかどうか判定
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            # 例えば、ここでデータベース（MySQLなど）と接続するとします。

            # SQLでユーザーの情報があるかを取得します。

            # 例えば、セッションに情報を保持します
            return redirect(url_for('index'))
        else:
            title.append("入力内容が間違っているか、入力されていない値があります。")
            return render_template('login.html', message=title[0])
    #正しくなければもう一度loginページを表示します

    return render_template('login.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)