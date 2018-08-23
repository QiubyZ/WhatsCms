import requests
def open_files(f):
    url_list = []
    with open(f) as file_Manager:
        for i in file_Manager.readlines():
            i = i.split("\n")[0].replace("www.", "").replace("http://", "").replace("https://", "")
            url_list.append(i)
    return url_list

def go_url(domain):
    msg = {0:"Server Failure",
           100: "API Key Not Set",
           101:"Invalid API Key",
           102:"Request not authenticated",
           110:"Url Parameter Not Set",
           111:"Invalid Url",112:"Missing required parameter",
           113:"Invalid value for required parameter",
           120:"Too Many Requests",121:"You have exceeded your monthly request quota",
           123:"Account disabled per violation of Terms and Conditions",
           200:"Success",
           201:"Failed: CMS or Host Not Found",
           202:"Requested Url Was Unavailable"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    data = {"key":"967ae76359fb65f3a4c9f1f32ca5527f604a1327a38ea1d1c829fa01d32913011e6b05", "url":"http://www."+domain}
    webdriver = requests
    webdriver.headers = headers
    try:
        web = webdriver.post("https://whatcms.org/APIEndpoint",data=data)
        print "======== [ DETAILS ] ========"
        print msg[web.json()["result"]["code"]]
        print "Cms Name: ", web.json()["result"]["name"]
        print "Confidence: ", web.json()["result"]["confidence"]
        print "Develop: ",web.json()["result"]["cms_url"]
        print "Version: ", web.json()["result"]["version"]
        print "========== [ END ] ========="
    except requests.exceptions.ConnectTimeout:
        print "Connection Time Out"
    except requests.exceptions.ConnectionError:
        print "COnnection Error"
    except:
        print "Unknown Error"
def menus():
    while True:
        print "1. Single Scan\r\n2. List Scan"
        try:
            ops = int(raw_input("Pilihan: "))
            if ops == 1:
                www = raw_input("Domain: http://")
                sigle(www)
            elif ops == 2:
                pritn "Example: E:\TOOLS PYTHON\webs.txt"
                fil = raw_input("Insert FUll Path: ")
                start_list(fil)
            else:
                print "tidak ada nomor: ", ops
        except ValueError, e:
            print "Input Salah"
            continue
def start_list(f):
    for urls in open_files(f):
        go_url(urls)
def sigle(domain):
    go_url(domain)

if __name__ == '__main__':
    menus()
