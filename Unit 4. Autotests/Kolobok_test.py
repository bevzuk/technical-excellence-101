# -*- coding: utf-8 -*-

import os
import pytest


@pytest.fixture()
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.fixture()
def text(change_test_dir):
    with open('./Kolobok.md', mode='r', encoding="utf-8") as output_file:
        return output_file.read()


def test_has_header(text):
    assert '# Сказка про Колобка' in text

def test_has_subheader_1(text):
    assert '## 1. Как Колобок появился' in text

def test_has_subheader_2(text):
    assert '## 2. Как Колобок убежал' in text

def test_has_subheader_3_1(text):
    assert '### 3.1 Заяц' in text

def test_has_subheader_3_4(text):
    assert '### 3.4 Медведь' in text

