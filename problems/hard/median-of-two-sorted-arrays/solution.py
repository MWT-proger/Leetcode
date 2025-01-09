from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = []
        i = 0
        generate_nums1 = self._generete_number(nums1)
        generate_nums2 = self._generete_number(nums2)

        num_from_nums1 = None
        num_from_nums2 = None

        num1_is_none = False
        num2_is_none = False
        while True:

            if not num1_is_none and num_from_nums1 is None:
                num_from_nums1 = next(generate_nums1)
                if num_from_nums1 is None:
                    num1_is_none = True

            if not num2_is_none and num_from_nums2 is None:
                num_from_nums2 = next(generate_nums2)
                if num_from_nums2 is None:
                    num2_is_none = True

            if num2_is_none and num1_is_none:
                break

            if (
                not num1_is_none
                and not num2_is_none
                and num_from_nums1 <= num_from_nums2
            ):
                all_nums.append(num_from_nums1)
                i += 1
                num_from_nums1 = None
            elif (
                not num1_is_none
                and not num2_is_none
                and num_from_nums2 <= num_from_nums1
            ):
                all_nums.append(num_from_nums2)
                i += 1
                num_from_nums2 = None
            elif num1_is_none:
                all_nums.append(num_from_nums2)
                i += 1
                num_from_nums2 = None
            elif num2_is_none:

                all_nums.append(num_from_nums1)
                i += 1
                num_from_nums1 = None

        if i % 2 == 0:
            result = (all_nums[int(i / 2 - 1)] + all_nums[int(i / 2)]) / 2
        else:

            result = all_nums[int((i - 1) / 2)]

        return result

    def _generete_number(elf, nums: List[int]):
        for num in nums:
            yield num
        yield None
