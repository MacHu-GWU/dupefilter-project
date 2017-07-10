#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from dupefilter import SqliteDictScheduler
from dupefilter.tests.test_basic import (
    BasicTestSchdueler, validate_schduler_implement,
)


def test():
    class Scheduler(BasicTestSchdueler, SqliteDictScheduler):
        user_db_path = ":memory:"

    scheduler = Scheduler()
    validate_schduler_implement(scheduler)


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
