import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("test", pattern="test_*.py")

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
