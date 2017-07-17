import requests
url = 'https://repo.clalbit.co.il/MediaServer/About/Gemel Devision/512244146_p170_0216.xls'
resp = requests.get(url, verify=False)
path_to_save_file = '/Applications/MAMP/htdocs/open-pension-crawler/files/clalbit/ffoo.xls'

with open(path_to_save_file, 'wb') as f:
    resp = requests.get(url)
    f.write(resp.content)
    f.close()
