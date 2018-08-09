import logging
import requests
import BeautifulSoup


BASE_URL = 'https://1337x.to'
SEARCH_URL = BASE_URL + '/search/{}/1/'


class BadResponse(Exception):
    pass


class NothingFound(Exception):
    pass


class Leetx_parser(object):
    def __init__(self, headers=None):
        self.headers = headers
        self.logger = logging.getLogger(__name__)
        self.logger.info('Package initialized')

    def _do_request(self, url):
        headers = self.headers if self.headers else {'User-Agent': "Magic Browser"}
        resp = requests.get(url, verify=False, headers=headers)
        if 200 != resp.status_code:
            raise BadResponse('url: {} status_code: {}'.format(url, resp.status_code))
        return resp.text

    def search(self, search_str):
        raw_html = self._do_request(SEARCH_URL.format(search_str))
        html = BeautifulSoup.BeautifulSoup(raw_html)
        table = html.find('table', {'class': 'table-list table table-responsive table-striped'})
        if not table:
            raise NothingFound(search_str)
        trs = table.findAll('tr')[1:]
        tors = []
        for tr in trs[:10]:
            tor = {}
            tds = tr.findAll('td')
            a = tds[0].findAll('a')[-1]
            tor['title'] = a.text
            tor['seeders'] = int(tds[1].text)
            raw_html = self._do_request(BASE_URL + a['href'])
            html = BeautifulSoup.BeautifulSoup(raw_html)
            ul = html.find('ul', {'class': 'download-links-dontblock btn-wrap-list'})
            lis = ul.findAll('li')
            a = lis[0].find('a')
            tor['magnet'] = a['href']
            tors.append(tor)
        return tors