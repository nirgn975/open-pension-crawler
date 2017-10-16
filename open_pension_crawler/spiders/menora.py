from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class MenoraDashSpider(OpenPensionCrawlSpiderBase):
    name = 'menora'
    allowed_domains = ['https://www.menoramivt.co.il']
    start_urls = ['https://www.menoramivt.co.il/wps/portal/about-menora/menora-mivtachim-pension-gemel/assets/' +
                  'new-mivtachim-plus-assets/!ut/p/a1/lZPdcoIwEIWfxQdwErBAvERFKBZ_' +
                  'ikjhpoMgBA34Q1X06QtOxxnJmNhwxcx39mw2Z4' +
                  'EPvoCfB6c0CX7SbR6Q-t-Xv0cz1DdMKJgTeSFDdfKObGSocDqVK8B7AGaqBlVds6yx04NQF5h6QfnTwydHhQ29aQyhihaapdh' +
                  'InAm0PwUw9IYmARd4Q-AbsNxrCfCBvwvTCHhJWVzOWdJO1tF1fUpIugoJycNsc8ThISM5OWF8o4tzjfvK0ysaArvFuoeHFmF' +
                  'P7lR6e-DM53pHQVJTTwOsEVkSZ0SWxHqiLoKUngJeemIGwImYW0-aU4E3AzagvlEAneMbwAoq08KhAH1hDC'
                  'pgMBZm2rQDBZFdoQ6K9xi1RhImIrDpCJN9tF5m0boIonKLz5cCZ2Vw3acxiVbA5GXP7d-Xw2PlvFuxNm9_' +
                  '9ngTYnzAxWoZk2PTnM6Vq71mPpUg37yxvJyC4r8LmtwY6_' +
                  'fb7DLHcTbLazyqzof8qVUfgh0pv87jLB6P28ESXdRW6xet7HhZ/dl5/d5/L2dBISEvZ0FBIS9nQSEh/']
    regex = r'[0-9]*_[0-9]*_[0-9]*_[0-9]*_(Q1|Q2|Q3|Q4)[0-9]*.(xlsx|xls)'
