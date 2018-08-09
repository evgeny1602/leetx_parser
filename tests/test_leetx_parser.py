# Sample Test passing with nose and pytest
from .context import Leetx_parser
import os


tests_dir = os.path.dirname(__file__)


def mock_func(url):
    raw_html = open(os.path.join(tests_dir, 'resp.html')).read()
    return raw_html


def test_search():
    lp = Leetx_parser()
    lp._do_request = mock_func
    tors = Leetx_parser().search('the flash s04e01')
    assert True, tors[0]['title'] == 'The.Flash.2014.S04E01.HDTV.x264-LOL[eztv]'

