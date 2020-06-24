import requests


class BaseApi:
    corpid = "wwe4f2e4b113af2b30"

    # corpsecret = "ENyEkc1Y1QQcLLUABVGr0eRvRArJOoIS06cPYi72E8A"
    @classmethod
    def get_token(cls, corpsecret):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(base_url, params={"corpid": cls.corpid, "corpsecret": corpsecret})
        return r.json()["access_token"]
