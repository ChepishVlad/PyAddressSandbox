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
    # _group_by_id = (By.CSS_SELECTOR, 'span.group input[value="%s"]')

    def open_groups_page(self) -> None:
        self.driver.get(self.URL)

    def press_create_new_btn(self) -> None:
        self.find_element(self._new_group).click()

    def get_groups_list(self) -> list:
        return self.find_elements(self._group_line)

    def get_groups_name_dict(self) -> dict:
        return {elem.find_element(By.XPATH, './input').get_attribute('value'):
                    elem.text for elem in self.get_groups_list()}

    def select_group_by_id(self, _id: str) -> None:
        self.find_element((By.CSS_SELECTOR,
                          f'span.group input[value="{_id}"]')).click()

    def press_edit_group_btn(self):
        self.find_element(self._edit_group).click()

    def press_delete_group_btn(self):
        self.find_element(self._delete_group).click()
