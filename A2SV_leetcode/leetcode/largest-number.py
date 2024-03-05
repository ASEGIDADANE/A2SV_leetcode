class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = "".join(
            sorted(
                (str(n) for n in nums),
                key=cmp_to_key(lambda s1, s2: int(s2 + s1) - int(s1 + s2))
            )
        )
        return n if int(n[0]) > 0 else "0"

        