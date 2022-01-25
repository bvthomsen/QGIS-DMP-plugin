import win32file, win32pipe, subprocess, time, json
from PyQt5.QtCore import (QDateTime, Qt)



class NamedPipe:

    def __init__(self, 
                 progName=r'D:\GitHub\DMPLogin_udv\bin\Debug\netcoreapp3.1\DMPLogin.exe',
                 clientId = "qgisplugin-integration-daiedittest",
                 host = r'http://localhost',
                 port = 5001,
                 redirectUri = "http://localhost:5001/login",
                 postLogoutRedirectUri = "http://localhost:5001/login",
                 authority = "https://log-in.test.miljoeportal.dk/runtime/oauth2",
                 scope = "openid http://www.miljoeportal.dk/roles",
                 api = "https://arealeditering-api.udv.miljoeportal.dk/",
                 pipeName="qgisplugin-integration-daiedittest",
                 showConsole=True):

        self.progName = progName
        self.clientId = clientId
        self.host = host
        self.port = port
        self.redirectUri = redirectUri
        self.postLogoutRedirectUri = postLogoutRedirectUri
        self.authority = authority
        self.scope = scope
        self.api = api
        pipeName="qgisplugin-integration-daiedittest"
        self.pipeName=pipeName
        self.showConsole = showConsole
        self.pid = None
#        print(self.progName)
#        print(self.clientId)
#        print(self.host)
#        print(self.port)
#        print(self.redirectUri)
#        print(self.postLogoutRedirectUri)
#        print(self.authority)
#        print(self.scope)
#        print(self.api)
#        print(self.pipeName)
#        print(self.showConsole)
        
        self.accessToken = None
        self.expirationTime = None

        startArgs = [self.progName,
                     self.pipeName,
                     self.clientId,
                     self.host,
                     str(self.port),
                     self.redirectUri,
                     self.postLogoutRedirectUri,
                     self.authority,
                     self.scope,
                     self.api]

        if self.pid: 
            self.pid.kill()
            self.pid = None

        if self.showConsole == True:                     
            subprocess.Popen(startArgs, creationflags = subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            subprocess.Popen(startArgs, creationflags = subprocess.CREATE_NO_WINDOW + subprocess.CREATE_NEW_PROCESS_GROUP)

        time.sleep (1.0)
        
        self.handle = win32file.CreateFile(
                    r'\\.\pipe\{}'.format(self.pipeName),
                    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                    0,
                    None,
                    win32file.OPEN_EXISTING,
                    0,
                    None
                )
        win32pipe.SetNamedPipeHandleState(self.handle, win32pipe.PIPE_READMODE_BYTE, None, None)



    def doExec (self, command):

        if self.handle:
            b =  str.encode(command)
            win32file.WriteFile(self.handle, b)
    
            win32file.SetFilePointer(self.handle, 0, win32file.FILE_BEGIN)
            result, data = win32file.ReadFile(self.handle, 4096, None) 
    
            res = data.decode("utf-8").rstrip('\x00')
            return json.loads(res)
        
        return {'error':'HandleNotSet'}

    def login (self):

        res = self.doExec('login')
        if res['error'] == '':
            self.accessToken = res['token']
            self.expirationTime = QDateTime().fromString(res['time'], Qt.ISODate)
        return res['error']

    def refresh (self):

        if self.expirationTime and self.accessToken: # Login er kørt mindst een gang
            if QDateTime.currentDateTime() >= self.expirationTime: # Tid udløbet for eks. token 
                res = self.doExec('refresh')
                if res['error'] == '':
                    self.accessToken = res['token']
                    self.expirationTime = QDateTime().fromString(res['time'], Qt.ISODate)
                return res['error']
            return 'NotExecuted' 
        else:
            return self.login() # login udføres i stedet for refresh
    

    def logout (self):
        
        res = self.doExec('logout')
        return res['error']

    def stop (self):

        res = self.doExec ('stop')
        win32file.CloseHandle(self.handle)
        return res['error']

   
