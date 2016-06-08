# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestModelName(TransactionCase):

    def setUp(self):
        super(SomethingCase, self).setUp()

    def tearDown(self):
        super(SomethingCase, self).tearDown()

    def test_something(self):
        """First line of docstring appears in test logs.
        Other lines do not.
        Any method starting with ``test_`` will be tested.
        """
        pass
