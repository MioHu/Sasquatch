from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    # class
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE id=%(uid)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user
    
    @classmethod
    def get_by_email(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE email=%(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user
    

    # static
    @staticmethod
    def create(data:dict) -> int:
        query = 'INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);'
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id
    
    @staticmethod
    def valid_regis(data:dict) -> bool:
        is_valid = True

        if len(data['first_name']) <= 0:
            flash('Need first name.', 'regis_first_name')
            is_valid = False
        elif len(data['first_name']) < 2:
            flash('First name need to be at least 2 characters.', 'regis_first_name')
            is_valid = False

        if len(data['last_name']) <= 0:
            flash('Need last name.', 'regis_last_name')
            is_valid = False
        elif len(data['last_name']) < 2:
            flash('Last name need to be at least 2 characters.', 'regis_last_name')
            is_valid = False

        if len(data['email']) <= 0:
            flash('Need email address.', 'regis_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email address.', 'regis_email')
            is_valid = False
        elif User.get_by_email({'email': data['email']}):
            flash('Email already exists.', 'regis_email')
            is_valid = False

        if len(data['pw']) <= 0:
            flash('Need password.', 'regis_pw')
            is_valid = False
        elif len(data['pw']) < 8:
            flash('Password need to be at least 8 characters.', 'regis_pw')
            is_valid = False
        
        if len(data['confirm_pw']) <= 0:
            flash('Need confirm password.', 'regis_confirm_pw')
            is_valid = False
        elif data['pw'] != data['confirm_pw']:
            flash("Passwords don't match.", 'regis_confirm_pw')
            is_valid = False
        
        return is_valid

    @staticmethod
    def valid_login(data:dict) -> bool:
        is_valid = True
        user = User.get_by_email({'email': data['email']})

        if len(data['email']) <= 0:
            flash('Need email address.', 'login_email')
            is_valid = False
        elif not user:
            flash("Invlid email.", 'login_email')
            is_valid = False

        if len(data['pw']) <= 0:
            flash('Need password.', 'login_pw')
            is_valid = False
            
        if is_valid:
            if not bcrypt.check_password_hash(user.pw, data['pw']):
                flash('Invalid password', 'login_pw')
                is_valid = False
        
        return is_valid