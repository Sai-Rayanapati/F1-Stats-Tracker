import requests
import json
from model import db, Race, Driver, Result


def fetch_and_save_data():
    F1_data_URL = 'https://ergast.com/api/f1/2024/results.json'

    response = requests.get(F1_data_URL)

    data = response.json()

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    return data


def store_race_data(data):
    for race in data['MRData']['RaceTable']['Races']:
        race_record = Race(
            season = race['season'],
            round = race['round'],
            race_name = race['raceName'],
            circuit_name = race['Circuit']['circuitName']
        )
        db.session.add(race_record)
        db.session.commit()

        for result in race['Results']:
            driver_name = f"{result['Driver']['givenName']} {result['Driver']['familyName']}"
            driver = Driver.query.filter_by(name = driver_name).first()

            if not driver:
                driver = Driver(name = driver_name, nationality = result['Driver']['nationality'])
                db.session.add(driver)
                db.session.commit()

            result_record = Result(
                position = result['position'],
                time = result.get('Time',{}).get('Time','N/A'),
                race_id = race_record.id,
                driver_id = driver.id
            )
            db.session.add(result_record)
        db.session.commit()

if __name__ == '__main__':
    fetch_and_save_data()