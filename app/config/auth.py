import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from flask_restful import abort
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidSignatureError

load_dotenv()


class Token:
    @staticmethod
    def generate_token(user_id, username):
        """
        Generates an Auth Token issued with an user_id and username
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(
                    days=0,
                    minutes=30  # default expires in 30 minutes
                ),
                'iat': datetime.utcnow(),
                'sub': user_id,
                'name': username
            }

            return jwt.encode(
                payload=payload,
                key=os.getenv('SECRET'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def check_token(token):
        """Check if the Auth token is valid"""
        try:
            return jwt.decode(
                token,
                os.getenv('SECRET'),
                algorithms=['HS256']
            )
        except ExpiredSignatureError as e:
            abort(401, message='Token Expired')
        except InvalidTokenError as e:
            abort(401, message='Token is invalid')
        except InvalidSignatureError as e:
            abort(401, message='Token fails his validation')
