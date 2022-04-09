import base64
import falcon

accounts = {
    'test': 'test'
}


class Authorize:
    def __init__(self):
        pass

    def __auth_basic(self, username, password):
        if username in accounts and accounts[username] == password:
            print('OK')
        else:
            raise falcon.HTTPUnauthorized('Unauthorized', 'Not authorized')

    def __call__(self, req, resp, resource, params):
        print('Before trigger - class: Authorize')

        auth_exp = req.auth.split(' ') if req.auth is not None else (None, None, )
        if auth_exp[0] and auth_exp[0].lower() == 'basic':
            auth = base64.b64decode(auth_exp[1]).decode('utf-8').split(':')
            username = auth[0]
            password = auth[1]

            self.__auth_basic(username, password)
        else:
            raise falcon.HTTPBadRequest('Not implement', 'Only via basic auth')


class ObjRequestClass:
    @falcon.before(Authorize())
    def on_get(self, req, resp):
        print('trigger GET')

        output = {
            'method': 'get',
        }

        resp.media = output


api = falcon.API()
api.add_route("/test7", ObjRequestClass())
