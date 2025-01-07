class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_id = 0
        last_id = 0
        cache = {}
        max_count = 0

        for value in list(s):
            if element_id := cache.get(value):

                count = last_id - start_id

                if count > max_count:
                    max_count = count

                items = cache.items() | []
                for k, v in items:
                    if v <= element_id:
                        cache.pop(k)
                start_id = element_id
            last_id += 1
            cache[value] = last_id

        count = last_id - start_id

        if count > max_count:

            max_count = count

        return max_count
