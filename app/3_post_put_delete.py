import json
import falcon


class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream().read())

        output = {
            'msg': 'Hello {0}'.format(data['name'])
        }
        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        total_count = int(data['x']) + int(data['y'])
        output = {
            'msg': 'x: {0} + y: {1} is {2}'.format(data['x'], data['y'], total_count)
        }
        resp.body = json.dumps(output)

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_405

        output = {
            'msg': 'put not supported now, sorry'
        }
        resp.body = json.dumps(output)

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_405

        output = {
            'msg': 'delete not supported now, sorry'
        }
        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test3', ObjRequestClass())
