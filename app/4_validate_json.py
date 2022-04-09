import json
import falcon


class ObjRequestClass:
    __json_content = {}

    def __validate_json_input(self, req) -> bool:
        try:
            self.__json_content = json.loads(req.stream.read())
            print('JSON from client is OK')
            return True
        except ValueError:
            self.__json_content = {}
            print('JSON from client is not OK')
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        validated: bool = self.__validate_json_input(req)
        output = {
            'status': 200,
            'msg': None
        }

        if validated:
            if 'name' in self.__json_content:
                output['msg'] = 'Hello {name}'.format(name=self.__json_content['name'])
        else:
            output['status'] = 400
            output['msg'] = 'Error input'

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test4', ObjRequestClass())
