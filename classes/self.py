class SearchEngineEntry:
    secure_prefix = 'https://'

    def __init__(self, url):
        self.url = url

    def secure(self):
        return '{prefix}{site}'.format(prefix=self.secure_prefix, site=self.url)


codecademy = SearchEngineEntry('www.codecademy.com')
wikipedia = SearchEngineEntry('www.wikipedia.com')

print(codecademy.url)
