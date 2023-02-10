# -*- coding: utf-8 -*-

import os
import pytest


@pytest.fixture()
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.fixture()
def html(change_test_dir):
    with open('build/Kolobok.html', mode='r') as output_file:
        return output_file.read()


def test_has_header(html):
    assert '<h1>Сказка про колобка</h1>' in html

def test_has_subheader1(html):
    assert '<h2>1. Как колобок появился</h2>' in html
