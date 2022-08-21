import jwt
import datetime
from ..config import key


def login(authorizationToken):
    if authorizationToken is None:
        raise AttributeError('Invalid token')
    try:
        payload={
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1,seconds=5),
            'iat':datetime.datetime.utcnow(),
            'sub':authorizationToken
        }

        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
    except Exception as e:
        return e

def validate(jwt_token):
    if jwt_token is None:
        raise AttributeError('Invalid token')
    
    try:
        payload=jwt.decode(jwt_token,key)

        return True
    except jwt.ExpiredSignatureError:
        raise ValueError("Signatue expired. please login again")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


    
    