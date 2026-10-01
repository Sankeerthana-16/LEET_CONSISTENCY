class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum=0
        for rows in accounts:
            for values in accounts:
                wealth1=sum(rows)
               

                if wealth1>maximum:
                    maximum=wealth1
                
        return maximum
        