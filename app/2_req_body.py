import json
import falcon


class ObjRequestClass:
    def on_get(self, req, resp):
        data = json.loads(req.stream.read())

        content = {
            'name': 'Alex',
            'age': '22',
            'country': 'Russia'
        }

        output = {}
        if 'method' not in data:
            resp.status = falcon.HTTP_400
            output['value'] = 'Error: no method found'
        else:
            if data.get('method') == 'get-name':
                resp.status = falcon.HTTP_200
                output['value'] = content['name']
            else:
                resp.status = falcon.HTTP_404
                output['value'] = None

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test2', ObjRequestClass())
