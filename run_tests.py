import unittest


def run_coverage():
    import coverage

    cov = coverage.Coverage()
    cov.start()
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("test", pattern="test_*.py")

    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory="coverage")
    cov.erase()


if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("test", pattern="test_*.py")

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        run_coverage()
        exit(0)
    else:
        exit(1)
