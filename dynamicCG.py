import sys
import pytest
import py_call_graph


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tc_file = sys.argv[1]
        with open(tc_file) as f:
            for line in f:
                pytest.main(['-x', str(line.replace("\n", ""))], plugins=[py_call_graph])
    else:
        pytest.main(['-x', './tests/'], plugins=[py_call_graph])
