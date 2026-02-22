class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {} 
        
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split(" ")
            count = int(count_str)
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdo = ".".join(parts[i:])
                if subdo not in counts:
                    counts[subdo] = 0
                counts[subdo] += count
        
        res = [f"{cnt} {sub}" for sub, cnt in counts.items()]
        return res