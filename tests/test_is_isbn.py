#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `is_isbn` package."""


import unittest

from is_isbn import is_isbn


class TestIs_isbn(unittest.TestCase):
    """Tests for `is_isbn` package."""

    def test_isbn_true(self):
        self.assertTrue(is_isbn.is_isbn('978.9941.445.26.2'))
        self.assertTrue(is_isbn.is_isbn('978-9941-445-51-4'))
        self.assertTrue(is_isbn.is_isbn('978-9941-445-51-4'))
        self.assertTrue(is_isbn.is_isbn('97w8-994e1-44r5-51r-4e'))
        self.assertTrue(is_isbn.is_isbn('9789941478437'))
        self.assertTrue(is_isbn.is_isbn('9994055429'))

    def test_isbn_false(self):
        self.assertFalse(is_isbn.is_isbn('ინფორმაცია არ არის'))
        self.assertFalse(is_isbn.is_isbn('Some string set up to fail'))
        self.assertFalse(is_isbn.is_isbn('1512-1518'))
        self.assertFalse(is_isbn.is_isbn(''))
        self.assertFalse(is_isbn.is_isbn('1242$%...'))
        self.assertFalse(is_isbn.is_isbn('@#()||><.'))
