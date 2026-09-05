import unittest

from check_hw1 import check_case, dataset_paths


class HW1Tests(unittest.TestCase):
    def test_main_dataset_through_cli(self):
        paths = dataset_paths("main")
        self.assertTrue(paths, "tests/hw1 dataset is missing")
        for path in paths:
            with self.subTest(case=path.stem):
                result = check_case(path)
                self.assertTrue(result["passed"], result)


if __name__ == "__main__":
    unittest.main()
