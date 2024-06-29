#You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
#You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
#Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
#A node u is an ancestor of another node v if u can reach v via a set of edges.


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: [] for i in range(n)}
        reversed_graph = {i: [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            reversed_graph[v].append(u)
        
        # Step 2: Function to perform DFS on the reversed graph
        def dfs(node: int, visited: Set[int], ancestors: Set[int]):
            for neighbor in reversed_graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ancestors.add(neighbor)
                    dfs(neighbor, visited, ancestors)
        
        # Step 3: Find all ancestors for each node
        result = []
        for node in range(n):
            ancestors = set()
            dfs(node, set(), ancestors)
            result.append(sorted(ancestors))
        
        return result
