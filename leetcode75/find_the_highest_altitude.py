class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0
        for i in gain:
            current_altitude += i
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude