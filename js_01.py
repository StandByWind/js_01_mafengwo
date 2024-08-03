import hashlib
import requests
import execjs
import json


def encrypt(go_dict,ture__jsl_clearance_s):

    if go_dict['ha'] == 'md5':
        string = hashlib.md5(ture__jsl_clearance_s.encode('utf-8')).hexdigest()
        return string
    elif go_dict['ha'] == 'sha1':
        string = hashlib.sha1(ture__jsl_clearance_s.encode('utf-8')).hexdigest()
        return string
    elif go_dict['ha'] == 'sha256':
        string = hashlib.sha256(ture__jsl_clearance_s.encode('utf-8')).hexdigest()
        return string


def get_ture__jsl_clearance_s(go_dict):
    for i in range(len(go_dict['ct']) + 1):
        for j in range(len(go_dict['ct']) + 1):
            ture__jsl_clearance_s = go_dict['bts'][0] + go_dict['chars'][i - 1:i] + go_dict['chars'][j - 1:j] + go_dict['bts'][1]
            if encrypt(go_dict, ture__jsl_clearance_s) == go_dict['ct']:
                return ture__jsl_clearance_s


cookies = {}
resp_first = requests.get(url='',
                          headers={'User-Agent': ''}
                          )
__jsluid_s = requests.utils.dict_from_cookiejar(resp_first.cookies)
cookies.update(__jsluid_s)
__jsl_clearance = resp_first.text[resp_first.text.find('=') + 1:resp_first.text.rfind(';')]
__jsl_clearance_ = execjs.eval(__jsl_clearance)
__jsl_clearance_s = __jsl_clearance_[__jsl_clearance_.find('=')+1:__jsl_clearance_.find(';')]
cookies['__jsl_clearance_s'] = __jsl_clearance_s
resp_second = requests.get(url='',
                           headers={'User-Agent': ''},
                           cookies=cookies
                           )
go_dict = json.loads(resp_second.text[resp_second.text.rfind('{'):resp_second.text.rfind('}')+1])
ture__jsl_clearance_s = get_ture__jsl_clearance_s(go_dict)
cookies['__jsl_clearance_s'] = ture__jsl_clearance_s
resp_third = requests.get(url='',
                          headers={'User-Agent': ''},
                          cookies=cookies
                          )
print(resp_third.text)










