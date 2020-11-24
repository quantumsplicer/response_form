import mechanize
from bs4 import BeautifulSoup
# import urllib2 
# import cookielib

user = input("Enter your username: ")
passwd = input("Enter your password: ")
c = input("Enter the number of courses that you have excluding the NPTEL courses: ")

# cj = cookielib.CookieJar()
br = mechanize.Browser()
# br.set_cookiejar(cj)
br.open("http://acad.iitr.ac.in/login.aspx?ReturnUrl=%2fStudent%2fResponseForm.aspx%3fid%3d100085%26sid%3d12302&id=100085&sid=12302&AspxAutoDetectCookieSupport=1")

br.select_form(nr=0)

br.form['txtusername'] = user
br.form['password'] = passwd
br.submit()

response = br.response().geturl()
# print response
c= int(c)
br.open(response)

for i in range (18,(18+c)):

    br.select_form(nr=0)
    br.follow_link(nr=8)
    br.select_form(nr=0)
    br.follow_link(nr=i)
    br.select_form(nr=0)
    # print br.response().read()

    br.form["ctl00$maincontent$sc1"] = ['4']
    br.form["ctl00$maincontent$sc2"] = ['4']
    br.form.find_control("ctl00$maincontent$sc3$0").items[0].selected=True
    br.form.find_control("ctl00$maincontent$sc3$1").items[0].selected=True
    br.form.find_control("ctl00$maincontent$sc3$2").items[0].selected=True
    br.form["ctl00$maincontent$sc5"] = ['4']
    br.form["ctl00$maincontent$sc6"] = ['4']
    br.form["ctl00$maincontent$sc7"] = ['4']
    br.form["ctl00$maincontent$sc8"] = ['4']
    br.form["ctl00$maincontent$sc9"] = ['4']
    br.form.find_control("ctl00$maincontent$sc10$0").items[0].selected=True
    br.form.find_control("ctl00$maincontent$sc10$1").items[0].selected=True
    br.form.find_control("ctl00$maincontent$sc10$2").items[0].selected=True
    br.form.find_control("ctl00$maincontent$sc10$3").items[0].selected=True
    br.form["ctl00$maincontent$sc11"] = ['More than 90%']

    br.submit()
# # print br.links()


