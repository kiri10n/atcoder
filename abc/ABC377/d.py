import math

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:  # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:  # non-overlapping interval, add the previous internval and reset
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals

# def main():
#     n, m = map(int, input().split())

#     ans_set = set()
#     for i in range(n):
#         l_i, r_i = map(int, input().split())

#         for l in range(1, l_i+1):
#             for r in range(r_i, m+1):
#                 ans_set.add((l, r))
    
#     all_combinations = math.comb(m+1, 2)
#     print(all_combinations - len(ans_set))

def main():
    n, m = map(int, input().split())

    intervals = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        intervals.append(Interval(l_i, r_i))
    
    intervals = merge(intervals)
    
    include_num = 0
    for interval in intervals:
        print(f"({interval.start}, {interval.end})")
        print(f"(interval.start) * (m - interval.end + 1) = {(interval.start) * (m - interval.end + 1)}")
        include_num += (interval.start) * (m - interval.end + 1)
    
    ans = math.comb(m+1, 2) - include_num
    print(ans)


if __name__ == '__main__':
    main()