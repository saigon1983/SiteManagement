import urllib.request

def getRequest(url):
    rawData = urllib.request.urlopen(url).readlines()
    bitrixData = []
    for line in rawData:
        bitrixData.append(tuple(str(line, encoding='utf-8').split("<br/>")))
    for line in bitrixData:
        print(line)

getRequest("https://techno-lux.ru/bitrix/admin/trinet_tools_csvreports.php")