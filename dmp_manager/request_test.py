# paste into QGIS python console....

from json import dumps, loads
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkRequest 
from qgis.core import QgsBlockingNetworkRequest

#************** New handlerequest function using QgsNetworkAccessManager, only "get" is tested **************

def handleRequest(urlstr, ispost=False, headers=None, package=None, authconf = ''):
    """TBD"""

    bnr = QgsBlockingNetworkRequest()
    req = QNetworkRequest()
    
    req.setUrl(QUrl(urlstr))

    if authconf and authconf != '':
        bnr.setAuthCfg(authconf)
        print('Authentification id is: {}'.format(bnr.authCfg()))

    if headers:
        for key, value in headers.items():
            req.setRawHeader(bytes(key, "utf-8"), bytes(value, "utf-8"))

    if ispost:
        jpack = bytes(dumps(package), "utf-8") if package else None
        err = bnr.post(req, jpack, True)
    else:
        err = bnr.get(req, True)

    print('Error message is: {}'.format(bnr.errorMessage()))
    
    resp = bnr.reply() 
    scode = resp.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    dictr = loads(str(resp.content(), "utf-8" )) if scode == 200 else None

    return scode, dictr

# Common constants
myUrlstr = 'https://arealeditering-api.demo.miljoeportal.dk/temakoder'
myIsPost = False
myPackage= None

#************** Test run 1, works **************
# Variable myToken is manually set using DMP Swagger webpage; pushing a *lot* of buttons -
# starting with "Authorize" in the Swagger web page and using the username/password below
# for authentication; pushing the "get /temakoder" button on the webpage and finally copy-paste
# the token from the resulting curl commandline example as the content of variable "myToken".
#
# Swagger site address: https://arealeditering-api.demo.miljoeportal.dk/swagger/index.html
# Username: 1085aesta 
# Password: F0r44r__2o21
#
#myToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjIzTF9NdlhLWndXUW8xeGdRZkVoWk50Z2tZZyIsIng1dCI6IjIzTF9NdlhLWndXUW8xeGdRZkVoWk50Z2tZZyIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDg1YWVzdGEiLCJ1aUlkIjoiOWEwYzA1NGUtOGE3Yi00NGMwLWI4MzctNTU1NjE4OGQ1NmZmIiwidW5pcXVlX25hbWUiOiIxMDg1YWVzdGEiLCJkazpnb3Y6c2FtbDphdHRyaWJ1dGU6VW5pcXVlQWNjb3VudEtleSI6IlhyaTovL0BESy1YUkkqMjkxOTA2NTgvMjAyMDExMDUxMjI3NTAuMFova2FJdCs1TEdxMHlySFJCU1ptRk5XZz09IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kIjoiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3Bhc3N3b3JkIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9uaW5zdGFudCI6IjIwMjEtMDQtMDJUMTE6NDg6NDMuNTQzWiIsImRrOmdvdjpzYW1sOmF0dHJpYnV0ZTpBc3N1cmFuY2VMZXZlbCI6IjIiLCJkazpnb3Y6c2FtbDphdHRyaWJ1dGU6U3BlY1ZlciI6IkRLLVNBTUwtMi4wIiwiZGs6Z292OnNhbWw6YXR0cmlidXRlOkN2ck51bWJlcklkZW50aWZpZXIiOiIyOTE5MDY1OCIsInVybjpvaWQ6Mi41LjQuMyI6IjEwODVhZXN0YSIsInVybjpvaWQ6MC45LjIzNDIuMTkyMDAzMDAuMTAwLjEuMyI6ImJ2dEBhZXN0YXMuZGsiLCJodHRwOi8vd3d3Lm1pbGpvZXBvcnRhbC5kay9lbXBsb3llZUlEIjoiYWVzdGEiLCJodHRwOi8vd3d3Lm1pbGpvZXBvcnRhbC5kay9vcmdhbml6YXRpb25OdW1iZXIiOiIxMDg1IiwiaHR0cDovL3d3dy5taWxqb2Vwb3J0YWwuZGsvZ2l2ZW5OYW1lIjoiQm8iLCJodHRwOi8vd3d3Lm1pbGpvZXBvcnRhbC5kay9vYmplY3RHVUlEIjoiZmIyZGEyOTEtYzY5Mi00Y2FiLWFiMWQtMTA1MjY2NjE0ZDVhIiwidXJuOm9pZDowLjkuMjM0Mi4xOTIwMDMwMC4xMDAuMS4xIjoiMTA4NWFlc3RhIiwidXJuOm9pZDoyLjUuNC40IjoiVGhvbXNlbiIsImh0dHA6Ly93d3cubWlsam9lcG9ydGFsLmRrL3VzZXJQcmluY2lwYWxOYW1lIjoiMTA4NWFlc3RhQG1ic2RrLmRrIiwidXBuIjoiMTA4NWFlc3RhQG1ic2RrLmRrIiwiaHR0cDovL3d3dy5taWxqb2Vwb3J0YWwuZGsvd2hlbkNyZWF0ZWQiOiIyMDIwMTEwNTEyMjc1MC4wWiIsIndpbmFjY291bnRuYW1lIjoibWJzZGtpbnRcXDEwODVhZXN0YSIsInJvbGUiOlsiQnJ1Z2VyZSIsIlJlZ2lvbiIsIk9mZmVudGxpZyIsIjI5MTkwNjU4IiwibWlsam9lX2FyZWFsaW5mb19za3Jpdl9yZWciLCJEb21haW4gVXNlcnMiXSwiaHR0cDovL3d3dy5taWxqb2Vwb3J0YWwuZGsvcm9sZXMiOlsiQnJ1Z2VyZSIsIlJlZ2lvbiIsIk9mZmVudGxpZyIsIjI5MTkwNjU4IiwibWlsam9lX2FyZWFsaW5mb19za3Jpdl9yZWciLCJEb21haW4gVXNlcnMiXSwibmFtZSI6IjEwODVhZXN0YSIsInRva2VuX3VzYWdlIjoiYWNjZXNzX3Rva2VuIiwianRpIjoiZDlhMjc2M2YtYWM4Mi00OTdiLTlkNGYtZDA4NDRmNTBjYWEwIiwic2NvcGUiOiJpZGVudGlmeSplbXB0eSIsImF1ZCI6Imh0dHBzOi8vbG9nLWluLnRlc3QubWlsam9lcG9ydGFsLmRrL3Jlc291cmNlcyIsImF6cCI6ImRhaWVkaXRkZW1vLXN3YWdnZXIiLCJpYXQiOjE2MTczNjQxMjQsIm5iZiI6MTYxNzM2NDEyNCwiZXhwIjoxNjE3MzY3NzI0LCJpc3MiOiJodHRwczovL2xvZy1pbi50ZXN0Lm1pbGpvZXBvcnRhbC5kay9ydW50aW1lL29hdXRoMiJ9.V06qCFXgyJNF2lp6Sng08sSbmie5Bku2Kp9q6mMNWqc0zJ3cZXQeD6TgaiUFmlg0uaVw8trZj_Oz603HurUYb_pR0Jy-EcdL4a36NmuRd14ju9q4I3z0GNcMNHHZSBT3HOd4La4WinyMpC2bUqpMaD9kRAXRKFqgpBE2WBDixRUBQ1vpDXuFhyA5TIOdLO_r6zXlFQ_o5_YIJfdG0bHfRxpgr6pOrRkXqjHvCbor9SxbTWPp1B4DGXPwtiDM38DcbXX511pgCEAKq0OPqAla6bdx-nJ1hhSqFq-omxXqRnridPelsAF229fALgA810vX8pAyhtUy1DxuqVJ78bwlsg'
#myHeaders = {"accept": "application/vnd.api+json", "Authorization": "Bearer {}".format(myToken)}
#myAuthconf=''

#myCode, myResult = handleRequest(myUrlstr, myIsPost, myHeaders, myPackage, myAuthconf)
#print ('Test1 returns -> {} \nResult ->\n{}\n'.format(myCode, myResult))    


#************** Test run 2, doesn't work **************
# Token supposedly generated by QGIS authentication, id 'dmptest'. *Doesn't work*

# https://log-in.test.miljoeportal.dk/runtime/oauth2/authorize.idp?response_type=code&nonce=rqAu-XH8yteZNN4b9GUt5A&state=CNobOQXNZCkaazoXLZ0GJg&code_challenge=IPz7XubpYoKnTAEDgWPJZfCiyuOGA7hqKrCzX263Idc&code_challenge_method=S256&client_id=qgisplugin-integration-daiedittest&scope=openid%20http%3A%2F%2Fwww.miljoeportal.dk%2Froles&redirect_uri=http%3A%2F%2Flocalhost%3A5001%2Flogin
myHeaders = {"accept": "application/vnd.api+json"}
myAuthconf='dmptest'

myCode, myResult = handleRequest(myUrlstr, myIsPost, myHeaders, myPackage, myAuthconf)    
print ('Test2 returns -> {} \nResult ->\n{}\n'.format(myCode, myResult))    
    
    