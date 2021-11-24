from flask import Flask, render_template, flash, request
app = Flask(__name__)


@app.route('/' , methods = ['GET' , 'POST'])
def home():
    return render_template('index.html')

@app.route('/introduction' , methods = ['GET' , 'POST'])
def introduction():
    return render_template('introduction.html')

@app.route('/history' , methods = ['GET' , 'POST'])
def history():
    return render_template('history.html')


if __name__ == "__main__":
    app.run(debug=True)
