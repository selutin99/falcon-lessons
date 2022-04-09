import json
import falcon


class Authorize:
    def __init__(self, roles):
        self._roles = roles

    def __call__(self, req, resp, resource, params):
        if 'admin' in self._roles:
            req.user_id = 5
        else:
            raise falcon.HTTPBadRequest('Bad request', 'You are not admin')


class ObjRequestClass:
    @falcon.before(Authorize(['admin', 'user', 'guest']))
    def on_get(self, req, resp):
        print('trigger GET')

        output = {
            'method': 'get',
            'user-id': req.user_id
        }

        resp.media = output

    @falcon.before(Authorize(['user', 'guest']))
    def on_post(self, req, resp):
        print('trigger POST')

        output = {
            'method': 'post',
            'user-id': req.user_id
        }

        resp.media = output


api = falcon.API()
api.add_route("/test6", ObjRequestClass())
