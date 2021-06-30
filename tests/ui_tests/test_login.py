# -*- coding: utf-8 -*-


def test_successful_login(login_page, main_page):
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    assert main_page.is_logout_btn_displayed(), (
        'Авторизвания не была выполнена')


def test_unsuccessful_login(login_page, main_page):
    login_page.open_login_page()
    login_page.login('admin', 'not_secret')
    assert not main_page.is_logout_btn_displayed(), (
        'Авторизвания была выполнена')

