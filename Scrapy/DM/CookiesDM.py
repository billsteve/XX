#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2019/2/22 16:17
import XX.HTML.HtmlHelper as UH


class DataSheetCookie(object):

    def process_request(self, request, spider):
        # cookie = "IPLOC=CN1200; SUID=3060247D2013940A000000005C2EBD27; SUV=1546566951191080; pgv_pvi=2621366272; pgv_si=s5189274624; ABTEST=8|1546566953|v1; SNUID={0}; weixinIndexVisited=1"
        cookie = "CFID=Z4iqyj5ekgtiqnnaafjwnjfv918npvjndfx6r17xcvr0lrdc1ny-238338775; CFTOKEN=Z4iqyj5ekgtiqnnaafjwnjfv918npvjndfx6r17xcvr0lrdc1ny-65854503; visid_incap_1764171=xbqVUiZjTFKxsabma8pwe4ZcalwAAAAAQUIPAAAAAABVRMI0i5CoEGeGfS/SYej4; s_fid=4EEE4CEEAC95F2ED-26088EDF3300658E; __gads=ID=11e416ab98d3cf23:T=1550474464:S=ALNI_MbQJ38X36gKJd6r3xoKDTIn2VSWqg; s_nr=1550478519334; incap_ses_560_1764171=Pp2RNCOt7hTsx/YpKYbFB/itb1wAAAAAZGUo2eH38qr6e/X0HSdRwg==; OptanonConsent=landingPath=NotLandingPage&datestamp=Fri+Feb+22+2019+16%3A08%3A27+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=4.1.0&groups=1%3A1%2C2%3A0%2C3%3A0%2C4%3A0%2C0_20504%3A0%2C0_20505%3A0&AwaitingReconsent=false; s_cc=true; s_vnum=1553066448448%26vn%3D5; s_invisit=true; s_lv=1550822907500; s_lv_s=Less%20than%201%20day; s_sq=%5B%5BB%5D%5D; __atuvc=58%7C8; __atuvs=5c6fadfb49f4aa32000; __utma=1.736096348.1550474452.1550807780.1550822909.6; __utmc=1; __utmz=1.1550822909.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=1.1.10.1550822909"
        cookie = UH.getCookieFromStr(cookie)
        request.cookies = cookie
        request.headers.setdefault('Referer', "https://www.datasheets360.com/part/detail/5962-8870101xx/2044037045222141529/")
        print("Add Cookie---")
