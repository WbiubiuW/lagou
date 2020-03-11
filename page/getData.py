from units import req


class getData(req.req):

    def get_page(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
        data = {
            'px': 'default',
            'city': '深圳',
            'needAddtionalResult': False,
            'first': True,
            'pn': 1,
            'kd': '软件测试工程师',
        }
        temp = self.req_post(url, data)
        if temp.status_code == 200:
            return temp.json()

    def get_data(self, json):
        print(json)
        if json['content']['positionResult']['totalCount'] > 0:
            for item in json['content']['positionResult']['result']:
                print(item)

    def main(self):
        json = self.get_page()
        self.get_data(json)


if __name__ == "__main__":
    temp = getData()
    temp.main()
