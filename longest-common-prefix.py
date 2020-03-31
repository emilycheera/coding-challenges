def longest_common_prefix(strs):
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            count = 0
            for l1, l2 in zip(prefix, strs[i]):
                if l1 != l2:
                    break
                count += 1
            prefix = prefix[:count]
            
        return prefix