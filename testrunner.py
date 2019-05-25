import glob
import importlib
from unittest import *
from configure import Configure

def run():
    path = Configure.get_value('Test', 'path')
    method = Configure.get_value('Test', 'method')
    
    if method == 'All':
        suite = TestLoader().discover(path, pattern='*.py')
    elif method == 'Manual':
        cases = Configure.get_value('Test', 'manual_list').split(',')
        suite = build_suite(path, cases)

    runner = TextTestRunner(verbosity=1)
    runner.run(suite)

def build_suite(path, cases):
    suite = TestSuite()

    for case in cases:
        test_case = TestLoader().loadTestsFromName(f'{path}.{case}')
        suite.addTest(test_case)

    return suite
    

if __name__ == '__main__':
    run()