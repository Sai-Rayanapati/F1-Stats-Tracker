from flask import Flask,render_template
from model import db, Race, Result, Driver
from fetch_data import fetch_and_save_data, store_race_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///f1.db'
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    data = fetch_and_save_data()
    store_race_data(data)

@app.route('/')
def home():
    races = Race.query.all()
    results = Result.query.join(Driver).join(Race).all()
    return render_template('home.html', races=races, results=results)

if __name__ == '__main__':
    app.run(debug=True)