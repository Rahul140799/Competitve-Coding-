def isHappy(self, n: int) -> bool:
        memory = set()
        while n!=1:
            n = sum([int(i)**2 for i in str(n)])
            print(n)
            if n in memory:
                return False
            else:
                memory.add(n)
            
        return True
