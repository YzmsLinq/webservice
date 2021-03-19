from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import platform

#新建一个用户
authorizer = DummyAuthorizer()
#将用户名，密码，指定目录，权限 添加到里面
if(platform.system() == 'Windows'):
    dirstr = "D:/"
    anondir = "D:/"
else:
    dirstr = "/home"
    anondir = "/home/linq"

authorizer.add_user("fan", "root", dirstr, perm="elr")#adfmw
#这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
authorizer.add_anonymous(anondir)

handler = FTPHandler
handler.authorizer = authorizer
#开启服务器
server = FTPServer(("127.0.0.1",2121),handler)
server.serve_forever()
