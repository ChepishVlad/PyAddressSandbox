# -*- coding: utf-8 -*-
import pytest

from pages.login_pages import LoginPage, GroupsPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def groups_page(driver):
    return GroupsPage(driver)
