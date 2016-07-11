__author__ = 'feng'
import requests
import json


class http:
    def post(self,url,data):
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
            ret = r.json()

        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}

        return ret

