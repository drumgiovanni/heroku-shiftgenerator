# -*- coding: utf-8 -*-



import os
import tornado.ioloop
import tornado.web
from main import shiftgenerator
from tornado.web import url
import calendar
import datetime
from tornado.options import define, options


define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        pubholys = {4:[30] ,5:[3, 4, 5], 7:[16], 8:[11], 9:[17, 24], 10:[8], 11:[3, 23], 12:[24]}
        noWorkingDays = {4:8,5:6,6:10,7:8,8:12,9:9,10:8,11:11,12:9} # 休刊日のディクショナリ
        now = datetime.datetime.now()
        thismonth = now.month
        nextmonth = thismonth + 1
        thisyear = now.year
        pycalendar = calendar.HTMLCalendar(0).formatmonth(thisyear, nextmonth, withyear=True)
        message1 = f"{nextmonth}月の祝日は{pubholys[nextmonth]}、休刊日は{noWorkingDays[nextmonth]}です"
        self.render('index.html',pycalendar = pycalendar, message1=message1 )

    def post(self):

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
        shiftgenerator(workerlist)
        self.render('result.html')

class EndHandler(tornado.web.RequestHandler):
    def get(self):
        ifilename = "Shift.xlsx"

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
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
