"""
description：部门API，涉及增删改查
@author:liulb
"""
import requests

from wework_department.baseapi.base_api import BaseApi


class DepartmentApi(BaseApi):
    corpsecret = "ENyEkc1Y1QQcLLUABVGr0eRvRArJOoIS06cPYi72E8A"

    # 创建部门
    def department_creat(self, name, parentid, **kwargs):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": name, "parentid": parentid}
        data.update(kwargs)
        r = requests.post(base_url, params={"access_token": self.get_token(self.corpsecret)}, json=data)
        return r.json()

    # 更新部门
    def department_update(self, id, name, **kwargs):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {"id": id, "name": name}
        data.update(kwargs)
        r = requests.post(base_url, params={"access_token": self.get_token(self.corpsecret)},
                          json=data)
        return r.json()

    # 删除部门
    def department_delete(self, id):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(base_url, params={"access_token": self.get_token(self.corpsecret), "id": id})
        return r.json()

    # 查询部门
    def department_select(self, id=None):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(base_url, params={"access_token": self.get_token(self.corpsecret), "id": id})
        return r.json()
