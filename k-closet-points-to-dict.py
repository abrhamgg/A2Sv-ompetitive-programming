import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points_dict = {}
        points_list = []
        j = 0
        for p in points:
            distance = math.sqrt((p[0] ** 2) + (p[1] ** 2))
            points_dict[j] = distance
            j += 1
        points_dict = sorted(points_dict.items(), key= lambda item: item[1])
        for i in range(k):
            if len(points_dict) > i:
                points_list.append(points[points_dict[i][0]])
        return points_list
