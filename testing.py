# import requests
# url = 'https://repo.clalbit.co.il/MediaServer/About/Gemel Devision/512244146_p170_0216.xls'
# resp = requests.get(url, verify=False)
# path_to_save_file = '/Applications/MAMP/htdocs/open-pension-crawler/files/clalbit/ffoo.xls'
#
# with open(path_to_save_file, 'wb') as f:
#     resp = requests.get(url)
#     f.write(resp.content)
#     f.close()
import re
url = "http://www.yl-invest.co.il/_Uploads/dbsAttachedFiles/513611509_g1162_0117.xlsx"
matches = re.findall(r'(.*)_(.+?).(xlsx|xls)', url)
print(matches[0][1][0] + "" + matches[0][1][1])
print(matches[0][1][2] + "" + matches[0][1][3])
