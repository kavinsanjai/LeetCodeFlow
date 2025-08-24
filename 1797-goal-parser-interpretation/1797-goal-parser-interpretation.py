class Solution(object):
    def interpret(self, command):
        result_string=""
        i=0
        while(i<len(command)):
            if command[i]=="G":
                result_string+="G"
                i+=1
            elif command[i:i+2]=='()':
                result_string+='o'
                i+=2
            else:
                result_string+='al'
                i+=4

        return result_string


        