import json
import falcon


class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        output = {
            'name': req.params['name'],
            'age': req.params['age']
        }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test5', ObjRequestClass())
