#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import mongomock
from dupefilter import MongoDBScheduler
from dupefilter.tests.test_basic import (
    BasicTestSchdueler, validate_schduler_implement,
)


def test():
    class Scheduler(BasicTestSchdueler, MongoDBScheduler):
        pass

    scheduler = Scheduler(collection=mongomock.MongoClient().db.collection)
    validate_schduler_implement(scheduler)


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
