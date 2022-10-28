class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        record = {}
        for domain in cpdomains:
            separateVal = domain.split(" ")
            num = separateVal[0]
            url = separateVal[1].split(".")
            temp = ""
            for i in range(len(url)-1, -1, -1):
                if i == len(url) - 1:
                    temp += url[i]
                else:
                    temp = url[i] + "." + temp

                if temp in record:
                    record[temp] += int(num)
                else:
                    record[temp] = int(num)
        
        result = []
        for key in record.keys():
            result.append(str(record[key]) + " " + key)
        
        return result

                            

