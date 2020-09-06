# -*- coding: utf-8 -*-


def test_login(login_page, groups_page):
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    groups_page.open_groups_page()
    groups_page.create_new_group(
        name='name', header='header', footer='footer')
