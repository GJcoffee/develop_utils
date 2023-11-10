import requests

data = {"question_name": "预置安装脚本集成", "knowledge_areas": "[4, 3]"}
headers={
    'Content-Type': 'application/json',
    'Content-Length': '26'
}
# Cookie = {'request_session_id_199607_doc_no_struct_scene': "dgs-hz#1699267679322217#55qE#JiZfc2NvcmUmaW52ZXJ0ZWRfb3JkZXI="}
Cookie = {}
res = requests.post(url='http://172.26.24.103:23325/search_pangu/faq/qa/feature/allsearchanswer',
              json=data, headers=headers)

if res.status_code == 200:
    print(res.json())
