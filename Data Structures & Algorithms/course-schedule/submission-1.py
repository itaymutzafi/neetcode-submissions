from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [0 for _ in range(numCourses)]
        G = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            G[b].append(a)
            pre[a] +=1
        
        q = deque()
        cnt = 0

        for i in range(numCourses):
            if pre[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            cnt +=1
            for neigh in G[curr]:
                pre[neigh] -= 1
                if pre[neigh] == 0:
                    q.append(neigh)
                
        return cnt == numCourses
                
            