import unittest
from mock import Mock
import jwt
import main.service.auth_service as service

class AuthServiceTestCase(unittest.TestCase):
    def test_login_raise_error_when_auth_token_empty(self):
        with self.assertRaises(AttributeError):
            service.login(None)
    
    def test_login_return_jwt_token_when_auth_token_provided(self):
        token='test'
        expected_result='some value'
        service.jwt.encode = Mock(return_value=expected_result)

        jwt_token=service.login(token)
        self.assertIsNotNone(jwt_token)
        self.assertEqual(expected_result,jwt_token)

    def test_validate_raise_error_when_auth_token_empty(self):
        with self.assertRaises(AttributeError):
            service.validate(None)   

    def test_validate_return_true_when_auth_token_provided(self):
        token='test'
        service.jwt.decode = Mock()

        result=service.validate(token)
        self.assertTrue(result)  

    def test_validate_raide_expired_signature_error_when_expired_auth_token_provided(self):
        token='test'
        service.jwt.decode = Mock(side_effect=jwt.ExpiredSignatureError('Test'))

        with self.assertRaises(ValueError):
            result=service.validate(token)

    def test_validate_raide_invalid_token_error_when_invalid_auth_token_provided(self):
        token='test'
        service.jwt.decode = Mock(side_effect=jwt.InvalidTokenError('Test'))

        with self.assertRaises(ValueError):
            result=service.validate(token)
    
        