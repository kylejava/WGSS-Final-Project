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

@app.route('/impact' , methods = ['GET' , 'POST'])
def impact():
    return render_template('impact.html')

@app.route('/sources' , methods = ['GET' , 'POST'])
def sources():
    return render_template('sources.html')


if __name__ == "__main__":
    app.run(debug=True)
