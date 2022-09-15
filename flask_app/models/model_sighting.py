from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Sighting:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.location = data['location']
        self.happen = data['happen']
        self.date = data['date']
        self.num = data['num']
        self.user_id = data['user_id']
        self.user_fname = data['user_fname']
        self.user_lname = data['user_lname']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.skep_num = 0
        self.skep_peo_name = []
        self.skep_peo_id = []
    

    def skeptics_num(self) -> int:
        query = f'SELECT COUNT(*) AS cnt FROM sightings JOIN skeptics ON sightings.id=skeptics.sighting_id WHERE sightings.id={self.id};'
        result = connectToMySQL(DATABASE).query_db(query)
        self.skep_num = int(result[0]['cnt'])
    
    def skeptics_peo_name(self) -> list:
        query = f'SELECT * FROM skeptics JOIN users ON users.id=skeptics.user_id WHERE sighting_id={self.id};'
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return
        for row in results:
            self.skep_peo_name.append(f"{row['first_name']} {row['last_name']}")

    def skeptics_peo_id(self) -> list:
        query = f'SELECT user_id FROM skeptics WHERE sighting_id={self.id};'
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return
        for row in results:
            self.skep_peo_id.append(row['user_id'])


    # class
    @classmethod
    def get_all(cls) -> list:
        query = 'SELECT * FROM sightings;'
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        sightings = []
        for row in results:
            sightings.append(cls(row))
        return sightings
    
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM sightings WHERE id=%(sid)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    
    # static
    @staticmethod
    def create(data:dict) -> int:
        query = 'INSERT INTO sightings (location, happen, date, num, user_id, user_fname, user_lname) VALUES (%(location)s, %(happen)s, %(date)s, %(num)s, %(user_id)s, %(user_fname)s, %(user_lname)s);'
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id

    @staticmethod
    def edit(data:dict) -> None:
        query = 'UPDATE sightings SET location=%(location)s, happen=%(happen)s, date=%(date)s, num=%(num)s WHERE id=%(sid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def delete(data:dict) -> None:
        query = 'DELETE FROM sightings WHERE id=%(sid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data:dict) -> bool:
        is_valid = True

        if len(data['location']) <= 0:
            flash('Need location.', 'location')
            is_valid = False
        
        if len(data['happen']) <= 0:
            flash('Need to describe what happened.', 'happen')
            is_valid = False
        
        if len(data['date']) <= 0:
            flash('Need date of siting.', 'date')
            is_valid = False
        
        if len(data['num']) <= 0:
            flash('Need number.', 'num')
            is_valid = False
        elif int(data['num']) < 1:
            flash('Number of asquatches min 1.', 'num')
            is_valid = False
        
        return is_valid
    
    @staticmethod
    def believe(data:dict) -> None:
        query = 'DELETE FROM skeptics WHERE user_id=%(uid)s AND sighting_id=%(sid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def skeptic(data:dict) -> int:
        query = 'INSERT INTO skeptics VALUES (%(uid)s, %(sid)s);'
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id