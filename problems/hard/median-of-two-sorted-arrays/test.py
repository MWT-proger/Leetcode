import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected_output = 2.00000
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1, nums2), expected_output
        )

    def test_example_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_output = 2.50000
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1, nums2), expected_output
        )

    def test_single_element_arrays(self):
        nums1 = [1]
        nums2 = [2]
        expected_output = 1.5
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1, nums2), expected_output
        )

    def test_uneven_lengths(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4]
        expected_output = 3.0
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1, nums2), expected_output
        )

    def test_large_arrays(self):
        nums1 = list(range(1, 1000001))
        nums2 = list(range(1000001, 2000001))
        expected_output = 1000000.5
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1, nums2), expected_output
        )


if __name__ == "__main__":
    unittest.main()
