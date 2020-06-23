import pytest

from wework_department.department_api.department import DepartmentApi

@pytest.mark.parametrize("name,parentid",[("新增三个",1),("新增四个",1)])
def test_department_creat(name,parentid):
    s = DepartmentApi().department_creat(name, parentid)
    assert s["errcode"] == 0
