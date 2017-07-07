#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from random import randint


def test_scheduler(scheduler):
    scheduler.clear_all()
    scheduler.log_on()
    n = 20

    input_data_list = [{"value": randint(1, n)} for _ in range(int(0.25 * n))]
    scheduler.do(
        input_data_list,
        quick_remove_duplicate=False,
        multiprocess=False,
    )

    input_data_list = [{"value": i} for i in range(1, n + 1)]
    scheduler.do(
        input_data_list,
        quick_remove_duplicate=True,
        multiprocess=False,
    )
    
    assert len(scheduler) == n
    for key, output_data in scheduler.items():
        print(key, output_data)