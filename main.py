import Config as Conf
import Lib.Functions as Func


BASE = Conf.base
RESPONSEXML = Conf.RESPONSEXML
URL = "/qps/rest/2.0/deactivate/am/asset"
ACTION = "?module=AGENT_VM,AGENT_PC,AGENT_EDR,AGENT_EDR,AGENT_PM"
tag = Conf.TAG
payload = Func.getXmlTagPayload(tag)
header = Func.getXmlHeader(Conf.USERNAME,Conf.PASSWORD) 
REQUEST_URL = BASE + URL + ACTION


response = Func.postRequest(REQUEST_URL,payload,header)

if (response.ok != True):
  print("Failed to get response from API")
  exit()

with open(RESPONSEXML, "w") as f:
    f.write(response.text.encode("utf8").decode("ascii", "ignore"))
    f.close()

print("result of action can be found under the folder : " + RESPONSEXML)

