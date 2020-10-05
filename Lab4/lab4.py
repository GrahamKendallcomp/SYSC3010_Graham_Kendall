import httplib
import urllib
while True:
    key = "54CDA6FJF4RCJ92C"

    params = urllib.urlencode({"field1": "grahamkendall@cmail.carleton.ca", "field2": "L2-M-14", "field3":"b"
                              , "key":key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        conn.close()
        break
    except:
        print "connection failed"
