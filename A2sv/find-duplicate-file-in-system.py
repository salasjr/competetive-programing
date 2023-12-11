class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = defaultdict(list)
        for path in paths:
            values = path.split(" ")
            for i in range(1, len(values)):
                dirr = values[i].split("(")
                dirr[1] = dirr[1].replace(")", "")
                file_path = values[0] + "/" + dirr[0]
                file_dict[dirr[1]].append(file_path)

        result = [files for files in file_dict.values() if len(files) > 1]
        return result
       
        
        