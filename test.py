# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<p>法晚深度即时 今日，少林寺方丈释永信被举报违反戒律问题调查结果公布。
<div class="test">
    <span><font size="4">testtesttest中文</font></span>中文
</div>
这是少林寺方丈释永信自今年7月25日被多家网络论坛发布举报涉嫌经济问题、男女关系等诸多问题的贴文后，
官方历经数月调查后，首次公布调查结果。调查结果显示：释永信当年“被迁单”的说法不实、也并未存在私生女等问题。</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
test = soup.find(class_='test').findChild()
test = unicode(test)

print type(test),test
