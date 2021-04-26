from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_index = 0
        task_heap  = []
        result     = []
        cpu_ready  = 0
        tasks      = sorted([(t, i) for i, t in enumerate(tasks)], key=lambda t: t[0])
        print(tasks)
        while True:
            if task_index < len(tasks):
                if cpu_ready < tasks[task_index][0][0] and len(task_heap):
                    pass
                else:
                    next_time = max(cpu_ready, tasks[task_index][0][0])
                    while tasks[task_index][0][0] <= next_time:
                        heapq.heappush(task_heap, (tasks[task_index][0][1],
                                                   tasks[task_index][1],
                                                   tasks[task_index][0][0]))
                        task_index += 1
                        if task_index >= len(tasks):
                            break
            if not len(task_heap):
                return result
            current_task = heapq.heappop(task_heap)
            result.append(current_task[1])
            cpu_ready = max(cpu_ready, current_task[2])
            cpu_ready += current_task[0]
        

S = Solution()
print(S.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(S.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))
print(S.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(S.getOrder([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]])) # [15,14,13,1,6,3,5,12,8,11,9,4,10,7,0,2]
