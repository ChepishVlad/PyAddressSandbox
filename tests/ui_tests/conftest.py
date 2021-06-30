# -*- coding: utf-8 -*-
import pytest

from pages.group_page import GroupPage
from pages.groups_page import GroupsPage
from pages.login_pages import LoginPage
from pages.main_page import MainPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def groups_page(driver):
    return GroupsPage(driver)


@pytest.fixture()
def group_page(driver):
    return GroupPage(driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)
