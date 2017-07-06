from __future__ import absolute_import, print_function

import os

import pytest
from selenium import webdriver as wd

from .utils import write

@pytest.fixture(scope='session')
def webdriver(request, log_file):
    web_driver = wd.PhantomJS(service_log_path=os.path.devnull)
    # Add in the clean-up code
    def stop_phantomjs_webdriver():
        write("Shutting down PhantomJS Webdriver ...")
        web_driver.quit()
    request.addfinalizer(stop_phantomjs_webdriver)
    return web_driver
