import requests
def login():

    cookie=''
    return cookie


def post_form(cookie):
    cookies = dict(cookies_are='ASP.NET_SessionId=dczjxp3o2iwez5mi1j4blur1; .ncov2019selfreport_shnu=8926E7B9FF568934F7BD21687A5C264224C191804EF880B7F505E50FC16F04DC9E4F42CA1839317AA0D45623E0CCD8E9B43FEF597826E621F81107A5D23927B328988ED8B1B53813FC55B76F85F0212D88B0307477DF630F191CC95C0151D03C3C80D54EFBC18FE9D9328B7DACE266C135F80E675A4292BE67BA770AA17B2D3C')
    url = 'https://yqfk.shnu.edu.cn/DayReport.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    files = {'file': open('report.xls', 'rb')}
    r = requests.get(url, headers=headers,  files=files,cookies=cookies)
    print(r.text)

def result():
    ''