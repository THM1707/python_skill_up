from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        tmp = newInterval

        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[len(intervals) - 1][1]:
            intervals.append(newInterval)
            return intervals

        start = end = -1
        for index, interval in enumerate(intervals):
            if self.merge_able(newInterval, interval):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                if start == -1:
                    start = index
                end = index
            else:
                if start == -1 and interval[0] > newInterval[1]:
                    intervals.insert(index, tmp)
                    return intervals

        if start != -1:
            for i in range(start, end + 1):
                intervals.pop(start)

            intervals.insert(start, newInterval)
        # else:
        #     insert_idx = 0
        #     for index, interval in enumerate(intervals):
        #         if interval[0] > tmp[1]:
        #             insert_idx = index
        #             break
        #     intervals.insert(insert_idx, tmp)
        return intervals

    @staticmethod
    def merge_able(new_interval: List[int], target_interval: List[int]) -> bool:
        if new_interval[0] > target_interval[1] or new_interval[1] < target_interval[0]:
            return False

        return True


def main():
    solution = Solution()
    # assert solution.insert([[1, 5], [9, 12]], [0, 4]) == [[0,5], [9, 12]]
    # print(solution.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])
    print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))



if __name__ == '__main__':
    main()
