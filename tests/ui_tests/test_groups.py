# -*- coding: utf-8 -*-
import random

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
    group_page.fill_fields_and_submit(group)
    groups_page.open_groups_page()
    groups_after = groups_page.get_groups_list()
    assert len(groups_after) == len(groups_before) + 1


def test_group_changing(login_page, groups_page, group_page):
    group = Group('NewGroup', 'NewHeader', 'NewFooter')
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    groups_page.open_groups_page()
    groups_before = groups_page.get_groups_name_dict()
    ch_group = random.choice(list(groups_before.items()))
    print(f'Выбранная группа: {ch_group}')
    groups_page.select_group_by_id(ch_group[0])
    groups_page.press_edit_group_btn()
    group_page.fill_fields_and_submit(group)
    groups_page.open_groups_page()
    groups_before[ch_group[0]] = group.name
    groups_after = groups_page.get_groups_name_dict()
    assert groups_after == groups_before


def test_deleting_group(login_page, groups_page, group_page):
    login_page.open_login_page()
    login_page.login('admin', 'secret')
    groups_page.open_groups_page()
    groups_before = groups_page.get_groups_name_dict()
    ch_group = random.choice(list(groups_before.items()))
    print(f'Выбранная группа: {ch_group}')
    groups_page.select_group_by_id(ch_group[0])
    groups_page.press_delete_group_btn()
    groups_page.open_groups_page()
    groups_before.pop(ch_group[0])
    groups_after = groups_page.get_groups_name_dict()
    assert groups_after == groups_before
