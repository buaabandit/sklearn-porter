# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.ensemble import RandomForestClassifier

from ..Classifier import Classifier
from ...language.JavaScript import JavaScript as JS


class RandomForestClassifierJSTest(JS, Classifier, TestCase):

    def setUp(self):
        super(RandomForestClassifierJSTest, self).setUp()
        mdl = RandomForestClassifier(n_estimators=100, random_state=0)
        self._port_model(mdl)

    def tearDown(self):
        super(RandomForestClassifierJSTest, self).tearDown()
