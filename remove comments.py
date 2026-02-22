class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res=[]
        flags= False
        a=""
        for i in range(len(source)):
            w = source[i]
            j = 0
            if not flags :
                    a=""
            while j < len(w):
                if not flags and j+1 < len(w) and  w[j:j+2] == "/*":
                    flags = True
                    j+=2
                elif flags and j+1 < len(w) and w[j:j+2]=="*/":
                    flags = False
                    j+=2
                elif not flags and j+1 < len(w) and w[j:j+2]=="//":
                    break
                elif not flags:
                    a+=w[j]
                    j+=1
                else:
                    j+=1
                print(a)
            

            if not flags and a:
                res.append(a)
               

        return res
