import json
import urllib.request
urlData = "http://localhost:8080/converter/api?currancy=usd&amount=544"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
print(json.loads(data.decode(encoding)))