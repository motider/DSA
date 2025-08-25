class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
                z = []
                for i in str(num):
                    z.append(int(i))
                print(z)
                lst = [x for x in z if x != 0]
                print(lst)      
                new = ""
                up = min(lst)
                new+=str(up)
                print(new)
                z.remove(min(lst))
                print(z)
                sor = sorted(z)
                for yes in sor:
                    new+=str(yes)
                return int(new)
        elif num < 0:
            no = []
            for j in str(abs(num)):
                no.append(int(j))
            print(no)
            lsts = [y for y in no if y != 0]
            print(lsts)
            old = ""
            down = max(lsts)
            old+=str(down)
            print(old)
            no.remove(max(lsts))
            print(no)
            nope = sorted(no,reverse = True)
            print(nope)
            for mot in nope:
                old+=str(mot)
            p = -int(old)

            return p 
        else:
            return 0
