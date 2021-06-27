# -*- coding: utf-8 -*-
from objects.group import Group


def test_login(login_page, groups_page, group_page):
    group = Group(name='name', header='header', footer='footer')
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    groups_page.open_groups_page()
    groups_before = groups_page.get_groups_list()
    groups_page.press_create_new_btn()
    group_page.create_new_group(group)
    groups_page.open_groups_page()
    groups_after = groups_page.get_groups_list()
    assert len(groups_after) == len(groups_before) + 1


def test_unsuccessful_login(login_page):
    login_page.open_login_page()
    login_page.login('admin', 'not_secret')
    assert login_page.find_element(login_page._submit_btn).is_displayed(), (
        'Кнопка логина не отображается')
