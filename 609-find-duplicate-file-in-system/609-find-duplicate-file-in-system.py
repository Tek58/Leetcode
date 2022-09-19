class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            files = path.split(' ')
            directory = files.pop(0)
            for file in files:
                name, content = file.split('(')
                content = content[:-1]
                if content in d:
                    d[content].append(directory + '/' + name)
                else:
                    d[content] = [directory + '/' + name]
                    
        output = []
        for key in d:
            if len(d[key]) > 1:
                output.append(d[key])
        return output