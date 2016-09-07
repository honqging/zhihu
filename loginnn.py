# encoding:utf8
import requests
from bs4 import BeautifulSoup


# cookies are attrived from my logged in data
new_cookies = {}
raw_cookies = '''_za=f0575d17-54c8-48b8-b072-074154a42a1c; udid="AIBA9MQ-lQmPTp42Xf-DGP6x-HbWNNpgh_U=|1457548986"; d_c0="AFAAAPsxogmPTiCUqZT5JH284-0VV9t50os=|1458283560"; _ga=GA1.2.1721338737.1459267911; _zap=88b82f3d-9cc3-4924-9f3b-3c5b7e040a96; _xsrf=eeddb794b20f4600ec8ebac62125696e; q_c1=40400848340b4301843b5e4639a7e479|1472144073000|1472144073000; l_cap_id="YTQwOTZlNjQwNWQxNGNhZmIzMjkyZGE5ZTNhZjllOWM=|1472144073|ec29ba8c64c4c3984709544884667f618a73193b"; cap_id="OWYyYzdhYWZlMWQyNDY5ZjkwZGM0ZWQ1MTNlN2RiZDY=|1472144073|061b734c2b034771ead177e9b751fbd1cec84d9c"; __utmt=1; __utma=51854390.1721338737.1459267911.1472056462.1472143357.4; __utmb=51854390.42.9.1472143620120; __utmc=51854390; __utmz=51854390.1472056462.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|2=registration_date=20140412=1^3=entry_date=20160826=1; login="ZjkwN2RmNWM4ZGFlNDBjNmEzZjg4ZmZkMmMzYTNiNTk=|1472144080|85dad794cd53014119588558520eacf6d8f18d29"; n_c=1; a_t="2.0AACAWecrAAAXAAAA0K_mVwAAgFnnKwAAAFAAAPsxogkXAAAAYQJVTdCv5lcAkTxjDYmW_suWiSn_sZQtfZ3yVWSs7ex7mCp1I4BEAUfvwWzzyjvBbQ=="; z_c0=Mi4wQUFDQVdlY3JBQUFBVUFBQS16R2lDUmNBQUFCaEFsVk4wS19tVndDUlBHTU5pWmIteTVhSktmLXhsQzE5bmZKVlpB|1472144080|4db3c4fb5bbb5bfc00faeae0ddc4416302130f10'''
for line in raw_cookies.split(';'):
    key,value=line.split('=',1)
    new_cookies[key] = value

# print raw_cookies, new_cookies

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Connection':'keep-alive',
    'Cookie':'''_za=f0575d17-54c8-48b8-b072-074154a42a1c; udid="AIBA9MQ-lQmPTp42Xf-DGP6x-HbWNNpgh_U=|1457548986"; d_c0="AFAAAPsxogmPTiCUqZT5JH284-0VV9t50os=|1458283560"; _ga=GA1.2.1721338737.1459267911; _zap=88b82f3d-9cc3-4924-9f3b-3c5b7e040a96; _xsrf=eeddb794b20f4600ec8ebac62125696e; q_c1=40400848340b4301843b5e4639a7e479|1472144073000|1472144073000; l_cap_id="YTQwOTZlNjQwNWQxNGNhZmIzMjkyZGE5ZTNhZjllOWM=|1472144073|ec29ba8c64c4c3984709544884667f618a73193b"; cap_id="OWYyYzdhYWZlMWQyNDY5ZjkwZGM0ZWQ1MTNlN2RiZDY=|1472144073|061b734c2b034771ead177e9b751fbd1cec84d9c"; __utmt=1; __utma=51854390.1721338737.1459267911.1472056462.1472143357.4; __utmb=51854390.42.9.1472143620120; __utmc=51854390; __utmz=51854390.1472056462.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|2=registration_date=20140412=1^3=entry_date=20160826=1; login="ZjkwN2RmNWM4ZGFlNDBjNmEzZjg4ZmZkMmMzYTNiNTk=|1472144080|85dad794cd53014119588558520eacf6d8f18d29"; n_c=1; a_t="2.0AACAWecrAAAXAAAA0K_mVwAAgFnnKwAAAFAAAPsxogkXAAAAYQJVTdCv5lcAkTxjDYmW_suWiSn_sZQtfZ3yVWSs7ex7mCp1I4BEAUfvwWzzyjvBbQ=="; z_c0=Mi4wQUFDQVdlY3JBQUFBVUFBQS16R2lDUmNBQUFCaEFsVk4wS19tVndDUlBHTU5pWmIteTVhSktmLXhsQzE5bmZKVlpB|1472144080|4db3c4fb5bbb5bfc00faeae0ddc4416302130f10''',
    'Host':'www.zhihu.com',
    'Referer':'http://www.zhihu.com/?next=%2Fpeople%2Fyijun-li-3%2Fabout',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
testurl='https://www.zhihu.com/people/sen-sen-63-92/followers'
s=requests.get(testurl,cookies=new_cookies,headers=headers,verify=False)
print s.status_code
# print s.text

html_doc = s.text
soup = BeautifulSoup(html_doc, 'html.parser',from_encoding = 'utf-8')
print html_doc
print "获取关注他的人"
movies = soup.find('div', class_="zh-general-list clearfix")
movies2 = movies.find_all('div', class_='zm-profile-card zm-profile-section-item zg-clear no-hovercard')
for movie in movies2:
    print movie.find('a', class_="zg-link author-link").get_text()
