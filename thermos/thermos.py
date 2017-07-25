from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """render_template takes an optional argument, template that can be used to pass data to the front end"""
    return render_template('index.html', title="This title has been passed from a view to template", text=["first","second","third"])


@app.route('/add')
def add():
    return render_template('add.html')

if __name__=="__main__":
    app.run(debug=True)
