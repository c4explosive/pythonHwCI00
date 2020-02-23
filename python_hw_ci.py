import os
import pytest

def hw_fx():
    print("Hello, World")
    return 0

def test_hw():
    assert hw_fx() == 0
