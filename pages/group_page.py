# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from objects.group import Group
from pages import BasePage


class GroupPage(BasePage):
    # locators
    _name_input = (By.NAME, 'group_name')
    _header_textarea = (By.NAME, 'group_header')
    _footer_textarea = (By.NAME, 'group_footer')
    _submit_btn = (By.NAME, 'submit')

    def fill_fields_and_submit(self, name: str, header: str, footer: str):
        name_input = self.find_element(self._name_input)
        name_input.clear()
        name_input.send_keys(name)
        header_input = self.find_element(self._header_textarea)
        header_input.clear()
        header_input.send_keys(header)
        footer_input = self.find_element(self._footer_textarea)
        footer_input.clear()
        footer_input.send_keys(footer)

    def press_submit_btn(self):
        self.find_element(self._submit_btn).click()

    def create_new_group(self, group: Group):
        self.fill_fields_and_submit(
            name=group.name, header=group.header, footer=group.footer)
        self.press_submit_btn()
