class Solution:
    def interpret(self, command: str) -> str:
        
        ret = []
        length = len(command)
    
        i = 0
        while (i < length):
            if command[i] == 'G':
                ret.append('G')
            elif command[i] == '(':
                if command[i+1] == ')':
                    ret.append('o')
                    i +=1
                else: 
                    ret.append('al')
                    i+=3
            i+=1
        return "".join(ret)