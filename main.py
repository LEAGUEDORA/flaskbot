from flask import Flask, render_template

from database import ans

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/main.html')
def home():
    return render_template('main.html')


@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')


@app.route('/contact_us.html')
def contact_us():
    return render_template('contact_us.html')


@app.route('/report.html')
def report():
    return render_template('report.html', id = "")

@app.route('/details.html')
def details():
    name = ans.ans()
    name = ['','','','','','','']
    return render_template ("details.html", title = "Profile", image = "https://i.ibb.co/ZLqQ6L1/conq-removebg-preview.png", name = name  )


@app.route('/report.html/<id>')
def report_with_id(id):
    return render_template('report.html', id = id)


@app.route('/details.html/<id>')
def profile(id):
    name = ans.ans()
    name[1] = id
    dict_of_tiers = {
        "CONQUERER":"https://i.ibb.co/ZLqQ6L1/conq-removebg-preview.png",
        "ACE":"https://i.ibb.co/JyBMYw3/ace-removebg-preview-1.png",
        "CROWN":"https://i.ibb.co/z6kPWdg/cr-removebg-preview.png",
        "DIAMOND":"https://i.ibb.co/T1bkZVV/dia-removebg-preview.png",
        "PLATINUM":'https://i.ibb.co/FnRQRbC/lat-removebg-preview-1.png',
        "GOLD":'https://i.ibb.co/0yQ5TXq/gold-removebg-preview.png',
        "SILVER":'https://i.ibb.co/mCMqswG/silver-removebg-preview-1.png',
        "BRONZE":'https://i.ibb.co/Ht7WKz1/bronze-removebg-preview.png',

        }
    return render_template('details.html', title = "name", image = dict_of_tiers[name[3]], name = name)


if __name__ == "__main__":
    app.run(debug=True)



