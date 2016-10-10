#!/usr/bin/env python3

import Julia

def test_julia():
    """ This function is for testing Julia"""
    f = Julia.julia( -1.037 + 0.17j )
    assert f(-1.00 - 0.2j) == 0
    assert f(-1.01 - 0.2j) == 20
    assert f(-1.02 - 0.2j) == 13
    assert f(-1.03 - 0.2j) == 10