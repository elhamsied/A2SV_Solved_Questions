class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapp = {}
        for string in paths:
            parts = string.split()
            path = parts[0] 

            for i in range(1, len(parts)):
                fname, content = parts[i].split("(")
                content = content[:-1]
                full_path = path + "/" + fname

                if content not in mapp:
                    mapp[content] = []
                mapp[content].append(full_path)


        return [v for k,v in mapp.items() if len(v) > 1]