from main import check_valid_func_names
import pytest

def test_for_check_valid_func_names:
    assert check_valid_func_names('tests/test_student_work_1.py')   == 1, "wrong function names, test ok"
