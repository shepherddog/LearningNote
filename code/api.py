#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import requests

for i in range(244,499):   
    url="http://scfriskadminneibu.haiziwang.com/scf-risk-admin/credit/syncCredit.do?core_id=1&uid="+str(i)
    print(url)
    r=requests.get(url)
    print(time.asctime( time.localtime(time.time())))
    print(r.status_code)
    time.sleep(3000)


