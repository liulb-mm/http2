import json
import pytest

from wework_department.baseapi.base_api import BaseApi
from wework_department.department_api.department import DepartmentApi


class TestDepartment(DepartmentApi):

    def setup(self):
        self.dp = DepartmentApi()

    @pytest.mark.parametrize("name,parentid", [("新增七个", 1), ("新增八个", 1)])
    def test_department_creat(self, name, parentid):
        creat = self.dp.department_creat(name, parentid)
        assert creat["errcode"] == 0

    def test_department_update(self):
        update = self.dp.department_update(14, "修改第一个")
        assert update["errcode"] == 0

    def test_department_delete(self):
        delete = self.dp.department_delete(18)
        assert delete["errmsg"] == "deleted"

    def test_department_select(self):
        select = self.dp.department_select()
        assert select["errcode"] == 0
        print(json.dumps(select, indent=5))

    def test_get_token(self):
        r = BaseApi.get_token("ENyEkc1Y1QQcLLUABVGr0eRvRArJOoIS06cPYi72E8A")
        assert r["errmsg"] == "ok"
