from flask import Flask, render_template

app = Flask(__name__)

@app.route('/my-page')
def my_page():
    #print("I am in my_page")
    return render_template('my-page.html')

if __name__ == '__main__':
    print("I am in my_page")
    app.run()
