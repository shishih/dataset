# -*- coding: utf-8 -*-

import re
import sys,os, urllib, urllib2, time, random
import threading

maxTryNum=5

class KThread(threading.Thread):

    """A subclass of threading.Thread, with a kill()

    method.

    

    Come from:

    Kill a thread in Python: 

    http://mail.python.org/pipermail/python-list/2004-May/260937.html

    """

    def __init__(self, *args, **kwargs):

        threading.Thread.__init__(self, *args, **kwargs)

        self.killed = False



    def start(self):

        """Start the thread."""

        self.__run_backup = self.run

        self.run = self.__run      # Force the Thread to install our trace.

        threading.Thread.start(self)



    def __run(self):

        """Hacked run function, which installs the

        trace."""

        sys.settrace(self.globaltrace)

        self.__run_backup()

        self.run = self.__run_backup



    def globaltrace(self, frame, why, arg):

        if why == 'call':

          return self.localtrace

        else:

          return None



    def localtrace(self, frame, why, arg):

        if self.killed:

          if why == 'line':

            raise SystemExit()

        return self.localtrace



    def kill(self):

        self.killed = True
def timeout(seconds):

    """超时装饰器，指定超时时间

    若被装饰的方法在指定的时间内未返回，则抛出Timeout异常"""

    def timeout_decorator(func):

        """真正的装饰器"""

        

        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):

            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        

        def _(*args, **kwargs):

            result = []

            new_kwargs = { # create new args for _new_func, because we want to get the func return val to result list

                'oldfunc': func,

                'result': result,

                'oldfunc_args': args,

                'oldfunc_kwargs': kwargs

            }

            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)

            thd.start()

            thd.join(seconds)

            alive = thd.isAlive()

            thd.kill() # kill the child thread

            if alive:

                raise Timeout(u'function run too long, timeout %d seconds.' % seconds)

            else:

                return result[0]

        _.__name__ = func.__name__

        _.__doc__ = func.__doc__

        return _

    return timeout_decorator


videolink=link+‘videos’
for tryNum in range(maxTryNum):
    try:
        req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml, */*',
        'Accept-Language': 'zh-CN',
        'Connection':'Keep-Alive',
        'Referer':'http://weibo.cn/search/?gsid=' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        #ckjar=cookielib.MozillaCookieJar(os.path.join('C:\Users\Agnes\AppData\Local\Google\Chrome\User Data\Default','Cookies'))
        jr=cookielib.CookieJar()
        cookie_support=urllib2.HTTPCookieProcessor(jr)
        opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        #req=urllib2.Request(source_url,None,req_header)
        #request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
        #html = urllib2.urlopen(source_url, timeout=12)
        req=urllib2.Request(source_url,headers=req_header)
        #req.add_header(req_header)
        
        html = urllib2.urlopen(req,timeout=12)
        
        
        data = html.read()
        data = gzip.GzipFile(fileobj = StringIO.StringIO(data)).read()
        fdata=open('F:\temp.html','w+')
        fdata.write(data)
        fdata.close()
        
        break
    except:
        if tryNum < (maxTryNum-1):
            print 'Connect again'
            time.sleep(10)
        else:
            print 'Internet Connect Error!'
            self.logger.error('Internet Connect Error!')
            self.logger.info('filePath: ' + savedir)
            self.logger.info('url: ' + source_url)
            self.logger.info('fileNum: ' + str(fileNum))
            self.logger.info('page: ' + str(i))
            self.flag = False
            goon = False
            break

pattern=re.compile(r'/watch?v=.{11}')

match=pattern.match(data)
file.write(str(len(match.group()))+'\n')
for video in match.group():
    file.write(str(video)+'\n')