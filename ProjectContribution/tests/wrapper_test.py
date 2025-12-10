import unittest




class pyWhatAPIWrapperTestCase(unittest.TestCase):
    def test_wrapper_importable(self):
        # ensure wrapper module is importable
        try:
            from src.api import what_wrapper
        except Exception as e:
            self.fail(f"Failed to import src.api.what_wrapper: {e}")

    def test_wrapper_class_exists(self):
        from src.api import what_wrapper
        self.assertTrue(hasattr(what_wrapper, "pyWhatWrapper"), "pyWhatWrapper class not found in what_wrapper module")

if __name__ == '__main__':
    unittest.main()