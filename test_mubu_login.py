import requests


class TestMubu:

    def test_mubu_home(self):
        url="https://mubu.com/login"
        headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0)" "Gecko/20100101 Firefox/70.0"}
        resp = requests.get(url, headers=headers, verify=False)
        print("resp-----", resp.text)
        assert resp.status_code==200