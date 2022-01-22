# -*- coding: utf-8 -*-

import pytest


@pytest.fixture()
def html():
    with open('./build/Kolobok.html', mode='r') as output_file:
        return output_file.read()


def test_has_header(html):
    assert '<h1>Сказка про колобка</h1>' in html
