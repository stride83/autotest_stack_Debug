# -*- coding=utf-8 -*-


from selenium import webdriver

__author__='stride83-yp'
__doc__='此文件用于验证码的识别，识别将基于以下几点workflow：' \
        '1：尝试多次下载，保存图片' \
        '2：进行图片的分割，分割之后进行保存基础元素' \
        '3：进行基础元素的旋转变形等' \
        '4：进行分类对比，找出最相近的' \
        '...'

class Baseworkflow():
    def __init__(self):
        pass

class download():
    '''
    进行下载指定的验证码图片
    '''
    def __init__(self,url,**kwargs):
        '''

        :param url:
        :param kwargs:不同的网页获取验证码的方式不同，需要区别对待
        '''
        self.driver=webdriver.Firefox()
        self.driver.get(url)

        pass