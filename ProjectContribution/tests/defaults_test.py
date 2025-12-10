# Wrapper Testing 

import os
import unittest

import dataclasses
import io
import contextlib
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Testing functionality of API Wrapper
class TestOptionsModule(unittest.TestCase):
    def test_options_module_importable(self):
        # ensure submodule is importable
        try:
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
            from src.options.defaultFilters import BaseOptions, StandardOption, LooseOption, StrictOption
        except Exception as e:
            self.fail(f"Failed to import src.options.defaultFilters: {e}")

    def test_classes_exist_and_are_dataclasses(self):
        for name in ("BaseOptions", "StandardOption", "LooseOption", "StrictOption"):
            self.assertTrue(hasattr(options, name), f"{name} not found in options module")
            cls = getattr(options, name)
            # dataclass classes (and instances) should be recognized by dataclasses.is_dataclass
            self.assertTrue(dataclasses.is_dataclass(cls), f"{name} should be a dataclass")

    def test_default_attribute_types_and_values(self):
        import src.options.defaultFilters as options

        base = options.BaseOptions()
        # basic types and defaults
        self.assertIsInstance(base.rarity, float)
        self.assertIsInstance(base.reverse, bool)
        self.assertIsInstance(base.format, str)
        self.assertEqual(base.format, "json")
        self.assertIsInstance(base.include_filenames, bool)
        # boundaryless may be None or a Filter instance if available
        if hasattr(options, "Filter"):
            self.assertTrue(base.boundaryless is None or isinstance(base.boundaryless, options.Filter))
        # key should be an Enum member
        self.assertTrue(hasattr(base, "key"))
        self.assertIsInstance(base.key, options.Enum)

    def test_subclass_rarity_overrides(self):
        import src.options.defaultFilters as options

        self.assertAlmostEqual(options.StandardOption().rarity, 0.15)
        self.assertAlmostEqual(options.LooseOption().rarity, 0.05)
        self.assertAlmostEqual(options.StrictOption().rarity, 0.4)

    def test_dataclass_mutability(self):
        import src.options.defaultFilters as options

        inst = options.BaseOptions()
        # BaseOptions declared frozen=False so attributes should be mutable
        orig = inst.rarity
        inst.rarity = 0.99
        self.assertNotEqual(orig, inst.rarity)
        self.assertEqual(inst.rarity, 0.99)

    def test_main_runs_and_prints(self):
        import src.options.defaultFilters as options

        buf = io.StringIO()
        # main should run without raising and produce output (string representation of instances)
        with contextlib.redirect_stdout(buf):
            options.main()
        out = buf.getvalue()
        self.assertTrue(len(out) > 0, "options.main() produced no output")
        # basic check that the names of the dataclasses appear in the printed output
        self.assertIn("StandardOption", out)
        self.assertIn("LooseOption", out)
        self.assertIn("StrictOption", out)


if __name__ == "__main__":
    unittest.main()
