class Solution:
    def interpret(self, command: str) -> str:
        
        x = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                x+=command[i]
                i+=1
            elif command[i] == "(":
                
                if command[i+1] == ")":
                    x+="o"
                    i+=2
                else:
                    x+="al"
                    i+=4
        return x


                           