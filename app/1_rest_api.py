import json
import falcon


class ObjRequestClass:
    def on_get(self, req, resp):
        content = {
            'name': 'Alex',
            'age': '22',
            'country': 'Russia'
        }

        resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/test', ObjRequestClass())
