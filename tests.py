from main import check_valid_func_names
import pytest

def test_run():
    assert check_valid_func_names('students_works/test_student_work_1.py') == 1
    # assert check_valid_func_names('students_works\test_student_work_2.py') == 1
    # assert check_valid_func_names('students_works\test_student_work_3.py') == 1
    # assert check_valid_func_names('students_works\test_student_work_ok.py') == 0