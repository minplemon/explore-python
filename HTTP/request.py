#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 18:12
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : request.py
# @Software: PyCharm

import json
import requests
import unittest
from requests_oauthlib import OAuth2Session

payload = {'page': 1, 'per_page': 10}
url_post = 'http://httpbin.org/post'
url_cookies = 'http://httpbin.org/cookies'
cookies = dict(key1='value1')


class Test(unittest.TestCase):
    @unittest.skip('测试http_get')
    def test_http_get(self):
        """
        get请求不带参数
        :return:
        """
        get_res = requests.get("http://httpbin.org/get")
        print(get_res.text)

    @unittest.skip('测试http_get_arg带参数')
    def test_http_get_arg(self):
        """
        get请求带参数
        需要注意的是字典里值为 None 的键不会被添加到 URL 的查询字符串中
        :return:
        """
        payloadNode = {'page': 1, 'per_page': 10, 'type': None}
        get_res = requests.get('http://httpbin.org/get', params=payloadNode)
        print(get_res.text)

    @unittest.skip('测试http_post')
    def test_http_post(self):
        """
        post请求
        :return:
        """
        post_r1 = requests.post("http://httpbin.org/post", data=payload)
        print(post_r1.text)

    @unittest.skip('测试post_json')
    def test_post_json(self):
        """
        json传递数据
        :return:
        """
        post_json1 = requests.post(
            "http://httpbin.org/post",
            data=json.dumps(payload))
        print(post_json1.text)

    @unittest.skip('测试post_json2')
    def test_post_json2(self):
        """
        json传递数据2
        :return:
        """
        post_json2 = requests.post("http://httpbin.org/post", json=payload)
        print(post_json2.text)

    @unittest.skip('测试post_setHeaders')
    def test_post_setHeaders(self):
        """
        设置请求头文件
        :return:
        """
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        post_headers = requests.post(
            "http://httpbin.org/post",
            json=payload,
            headers=headers)
        print(post_headers.text)

    @unittest.skip('普通响应')
    def test_fun_common(self):
        """
        普通响应，使用 r.text 获取    来读取 unicode 形式的响应
        :param self:
        :return:
        """
        r = requests.get("https://github.com/timeline.json")
        print(r.text)
        print(r.encoding)

    @unittest.skip('JSON 响应')
    def test_fun_json(self):
        """
        JSON 响应，使用 r.json() 获取          JSON 响应的内容
        :param self:
        :return:
        """
        r = requests.get("https://github.com/timeline.json")
        if r.status_code == 200:
            print(r.headers.get('content-type'))
            print(r.json())

    @unittest.skip('二进制响应')
    def test_fun_content(self):
        """
        二进制响应，使用 r.content 获取      通常针对图片
        :param self:
        :return:
        """
        url = 'https://github.com/reactjs/redux/blob/master/logo/logo.png?raw=true'
        r = requests.get(url)
        image_data = r.content  # 获取二进制数据
        with open('/Users/minp/Downloads/redux.png', 'wb') as fout:
            fout.write(image_data)

    @unittest.skip('原始响应')
    def test_fun_raw(self):
        """
        原始响应，使用 r.raw 获取  获取来自服务器的原始套接字响应  同时请求的时候设置stream=True
        :param self:
        :return:
        """
        url = 'https://github.com/reactjs/redux/blob/master/logo/logo.png?raw=true'
        r = requests.get(url, stream=True)
        print(r.raw)
        r.raw.read(10)

    @unittest.skip('原始响应')
    def test_fun_cookies(self):
        """
        发送 cookies 到服务器，可以使用 cookies 参数
        :param self:
        :return:
        """
        get_cookies = requests.get(url_cookies, cookies=cookies)
        print(get_cookies.text)

    @unittest.skip('通过cookies保存session')
    def test_fun_session(self):
        """
        发送 cookies 到服务器，可以使用 cookies 参数
        :param self:
        :return:
        """
        s = requests.Session()
        s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
        r = s.get('http://httpbin.org/cookies')
        print(r.text)

    @unittest.skip('请求方法提供缺省数据')
    def test_fun_auth(self):
        """
        请求方法提供缺省数据
        :param self:
        :return:
        """
        s = requests.Session()
        s.auth('user', 'pass')
        s.headers.update({'x-test': 'true'})
        # x-test 和 x-test2 都会被发送
        s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

    # @unittest.skip('SOCKS 代理')
    def test_fun_http(self):
        proxies = {
            "http": "socks5://user:pass@host:port",
            "https": "socks5://user:pass@host:port",
        }
        requests.get("http://example.org", proxies=proxies)

    # @unittest.skip('基本身份认证')
    def test_fun_auth(self):
        requests.get('https://api.github.com/user', auth=('user', 'pass'))

    # @unittest.skip('OAuth 2 认证')
    def test_fun_auth(self):
        # This information is obtained upon registration of a new GitHub
        client_id = "<your client key>"
        client_secret = "<your client secret>"
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        github = OAuth2Session(client_id)
        authorization_url, state = github.authorization_url(
            authorization_base_url)


if __name__ == "__main__":
    unittest.main(verbosity=2)
