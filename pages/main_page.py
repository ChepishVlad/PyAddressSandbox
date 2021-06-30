# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pages import BasePage


class MainPage(BasePage):
    _nav_bar = (By.CSS_SELECTOR, 'div#nav')
    _logout_btn = (By.XPATH, '//a[text()="Logout"]')

    def is_logout_btn_displayed(self) -> bool:
        return self.is_element_present(self._logout_btn)
