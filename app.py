# -*- coding: utf-8 -*-



import os
import tornado.ioloop
import tornado.web
from main import shiftgenerator
from tornado.web import url
import calendar
import datetime

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        print("getが通りました")
        now = datetime.datetime.now()
        thismonth = now.month
        nextmonth = thismonth + 1
        thisyear = now.year
        pycalendar = calendar.LocaleHTMLCalendar(0).formatmonth(thisyear, nextmonth, withyear=True)
        self.render('index.html',pycalendar = pycalendar )

    def post(self):

        print("indexhandlerのpostで通ってる")
        workernamelist = []
        workertypelist = []
        workerdayofflist = []
        workerlist = {}
        inputs = dict(self.request.arguments)
        names = self.get_body_arguments("worker-name")
        for i in names:
            workernamelist.append(i)

        types = self.get_body_arguments("worker-type")
        for i in types:
            workertypelist.append(i)

        for i in inputs["worker-dayoff"]:
            i = str(i)
            j = i[2:-1]
            workerdayofflist.append(j)


        for i in range(len(workernamelist)):
            workersinfo = {}
            workersinfo["属性"] = workertypelist[i]
            workersinfo["休み希望"] = workerdayofflist[i]
            workerlist[workernamelist[i]] = workersinfo
        print(workerlist)
        shiftgenerator(workerlist)
        self.render('result.html')

class EndHandler(tornado.web.RequestHandler):
    def get(self):
        ifilename = "Shift.xlsx"
        print('i download file handler : ',ifilename)

        self.set_header ('Content-Type', 'application/vnd.ms-excel')
        self.set_header ('Content-Disposition', 'attachment; filename=shift.xlsx')
        with open(ifilename, 'rb') as fp:
            self.write(fp.read())

BASE_DIR = os.path.dirname(__file__)

application = tornado.web.Application([
    url(r'/', IndexHandler, name="index"),
    url(r'/Shift.xlsx', EndHandler, name="shift"),
    (r'/(.*)',tornado.web.StaticFileHandler,{"path":"/Shift.xlsx"})
    ],
    template_path=os.path.join(BASE_DIR, 'templates'),
    static_path=os.path.join(BASE_DIR, 'static')
)

if __name__ == '__main__':
    application.listen(8888)
    print("Server listening...")
    tornado.ioloop.IOLoop.instance().start()
