from pyramid.config import Configurator
from pyramid_jwt import JWTAuthenticationPolicy
from pyramid.security import Allow, Everyone

def groupfinder(userid, request):
    # Asumsikan fungsi ini mengembalikan list role dari user
    return ['group:admin', 'group:user']

class RootFactory(object):
    __acl__ = [
        (Allow, 'group:admin', 'admin'),
        (Allow, 'group:user', 'view'),
    ]

    def __init__(self, request):
        pass

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')
        config.scan()

        # Konfigurasi JWT
        config.include('pyramid_jwt')
        config.set_jwt_authentication_policy('your_jwt_secret', http_header='Authorization', auth_type='Bearer')

        # Lanjutan konfigurasi Pyramid...
    return config.make_wsgi_app()   
