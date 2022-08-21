from functools import wraps
from typing import Callable
from flask import request

from ..service.auth_service import validate
from .file_logger import error

def authorize(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args,**kwargs):
        try:
            jwt_token=request.headers.get('Authorization')

            if jwt_token is None:
                return 'Invalid token',401
            validate(jwt_token)

            return f(*args,**kwargs)
        except Exception as e:
            error(str(e))
            return str(e), 403
    
    return decorated

        
