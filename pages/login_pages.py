# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from pages import BasePage


class LoginPage(BasePage):
    # locators
    _login_input = (By.NAME, 'user')
    _password_input = (By.NAME, 'pass')
    _submit_btn = (By.CSS_SELECTOR, 'input[type="submit"]')

    def open_login_page(self) -> None:
        self.driver.get('http://addressbook.u0541324.cp.regruhosting.ru/')

    def login(self, login: str, password: str) -> None:
        login_input = self.find_element(self._login_input)
        login_input.clear()
        login_input.send_keys(login)
        pass_input = self.find_element(self._password_input)
        pass_input.clear()
        pass_input.send_keys(password)
        self.find_element(self._submit_btn).click()


