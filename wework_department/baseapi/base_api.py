import requests


class BaseApi:
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "wwe4f2e4b113af2b30"
    corpsecret = "ENyEkc1Y1QQcLLUABVGr0eRvRArJOoIS06cPYi72E8A"

    @classmethod
    def setup(cls):
        r = requests.get(cls.base_url, params={"corpid":cls.corpid,"corpsecret":cls.corpsecret})
        return r.json()["access_token"]
