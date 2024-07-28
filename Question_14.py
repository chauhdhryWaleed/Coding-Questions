class Solution:
    def overlappedInterval(self, Intervals):
    
        Intervals.sort(key=lambda x: x[0])

        merged = [Intervals[0]]
        
 
        for current in Intervals[1:]:
            last_interval = merged[-1]
         
            if current[0] <= last_interval[1]:
               
                last_interval[1] = max(last_interval[1], current[1])
            else:
            
                merged.append(current)
        
        return merged