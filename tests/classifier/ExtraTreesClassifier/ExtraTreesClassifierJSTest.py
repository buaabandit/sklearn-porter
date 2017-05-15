# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.ensemble import ExtraTreesClassifier

from ..Classifier import Classifier
from ...language.JavaScript import JavaScript as JS


class ExtraTreesClassifierJSTest(JS, Classifier, TestCase):

    def setUp(self):
        super(ExtraTreesClassifierJSTest, self).setUp()
        mdl = ExtraTreesClassifier(random_state=0)
        self._port_model(mdl)

    def tearDown(self):
        super(ExtraTreesClassifierJSTest, self).tearDown()
