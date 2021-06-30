# -*- coding: utf-8 -*-
import pytest

from objects.group import Group

GROUPS = [
    Group(name='name', header='header', footer='footer'),
    Group(name='', header='', footer=''),
    Group(name='Название', header='Шапка', footer='Подвал')
    ]


@pytest.mark.parametrize('group', GROUPS)
def test_group_creation(login_page, groups_page, group_page, group):
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    groups_page.open_groups_page()
    groups_before = groups_page.get_groups_list()
    groups_page.press_create_new_btn()
    group_page.create_new_group(group)
    groups_page.open_groups_page()
    groups_after = groups_page.get_groups_list()
    assert len(groups_after) == len(groups_before) + 1
