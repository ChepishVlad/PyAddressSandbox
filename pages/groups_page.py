# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pages import BasePage


class GroupsPage(BasePage):
    # locators
    new_group = (By.NAME, 'new')
    _delete_group = (By.NAME, 'delete')
    _edit_group = (By.NAME, 'edit')

    def open_groups_page(self):
        self.driver.get('http://addressbook.u0541324.cp.regruhosting.ru/group.php')

    def press_create_new_btn(self):
        self.find_element(self.new_group).click()

    def fill_fields_and_submit(self,
                               name: str,
                               header: str,
                               footer: str):
        pass

    def create_new_group(self,
                         name: str,
                         header: str = '',
                         footer: str = ''):
        self.press_create_new_btn()
        self.fill_fields_and_submit(
            name=name, header=header, footer=footer)
