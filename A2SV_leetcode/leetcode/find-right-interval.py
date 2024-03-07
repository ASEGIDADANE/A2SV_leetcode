class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_time = [[intervals[i][0], i] for i in range(n)]
        end_time = [intervals[i][1] for i in range(n)]
        start_time.sort()
        ans = []

        def find_with_binary_search(num):
            left, right = 0, n-1

            if num > start_time[n-1][0]: return -1
            
            while left <= right:
                mid = left+(right-left)//2

                if start_time[mid][0] >= num:
                    right = mid - 1
                else:
                    left = mid + 1

            return start_time[left][1]

        for every_end_time in end_time:
            key = find_with_binary_search(every_end_time)
            ans.append(key)

        return ans