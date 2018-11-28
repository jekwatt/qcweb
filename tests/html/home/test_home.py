import time

from pytest import mark


@mark.smoke
@mark.ui
def test_can_navigate_to_home_page(chrome_browser):
    local_browser = chrome_browser
    local_browser.get('http://localhost:5000/home')

    time.sleep(5)

    dev_browser = chrome_browser
    dev_browser.get('http://submissions-dev.hgsc.bcm.edu/qcweb/main/home')

    time.sleep(5)

    assert True