#!/usr/bin/env python

"""Run all the tests."""

import unittest
import sys


if __name__ == "__main__":
    logfile = None
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = None
    if len(sys.argv) > 1:
        logfile = open(sys.argv[1], "w")
        testRunner = unittest.runner.TextTestRunner(logfile)
    else:
        testRunner = unittest.runner.TextTestRunner(verbosity=2, resultclass=unittest.TextTestResult)
    result = testRunner.run(tests)
    if logfile is not None:
        logfile.close()
    sys.exit(not result.wasSuccessful())
