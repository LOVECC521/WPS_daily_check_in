invite_userid = [583366194]

import requests

sids = [
    "V02SvzHCcsrLymMO1jul1JnqfG2GD_g00a3ba5d40047635f5d"
]

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
for i in sids:
    requests.post(invite_url, headers={'sid': i}, data={'invite_userid': invite_userid})
    
