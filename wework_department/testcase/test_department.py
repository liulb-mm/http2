import json
import pytest

from wework_department.department_api.department import DepartmentApi

s = DepartmentApi()


@pytest.mark.parametrize("name,parentid", [("新增一个", 1), ("新增六个", 1)])
def test_department_creat(name, parentid):
    creat = s.department_creat(name, parentid)
    assert creat["errcode"] == 0


def test_department_update():
    update = s.department_update(14, "修改第一个")
    assert update["errcode"] == 0


def test_department_delete():
    delete = s.department_delete(18)
    assert delete["errmsg"] == "deleted"


def test_department_select():
    select = s.department_select()
    assert select["errcode"] == 0
    print(json.dumps(select, indent=5))
