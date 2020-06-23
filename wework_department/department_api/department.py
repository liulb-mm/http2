"""
description：部门API，涉及增删改查
@author:liulb
"""
import requests

from wework_department.baseapi.base_api import BaseApi


class DepartmentApi(BaseApi):
    # 创建部门
    def department_creat(self, name, parentid, **kwargs):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": self.setup()},
                          json={"name": name, "parentid": parentid})
        return r.json()

    def department_update(self, id, name):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                          params={"access_token": self.setup()},
                          json={"id": id, "name": name})
        return r.json()

    def department_delete(self, id):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                         params={"access_token": self.setup(), "id": id})
        return r.json()

    def department_select(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": self.setup()})
        return r.json()
