from solution import Solution


def test_one():
    solution = Solution()
    testdata = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("dvdf", 3), (" ", 1)]
    for td in testdata:
        result = solution.lengthOfLongestSubstring(td[0])
        assert (
            result == td[1]
        ), f"Неверный результат. Ожидается: {td[1]}. По факту: {result}"


print(test_one())
