# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pages import BasePage


class GroupsPage(BasePage):
    # locators
    URL = 'http://addressbook.u0541324.cp.regruhosting.ru/group.php'
    _new_group = (By.NAME, 'new')
    _delete_group = (By.NAME, 'delete')
    _edit_group = (By.NAME, 'edit')
    _group_line = (By.CSS_SELECTOR, 'span.group')

    def open_groups_page(self):
        self.driver.get(self.URL)

    def press_create_new_btn(self):
        self.find_element(self._new_group).click()

    def get_groups_list(self) -> list:
        return self.find_elements(self._group_line)
