# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    driver = None
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install())
    driver.maximize_window()

    def tear_down():
        driver.quit()

    request.addfinalizer(tear_down)
    yield driver
