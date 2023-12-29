class Solution:
    def smallestNumber(self, num: int) -> int:
        flag=False
        if num<0:
            flag=True
            num=-1*num
        num=str(num)
        lst=[i for i in num]
        for i in range(len(lst)):
            for j in range(len(lst)-1-i):
                if int(lst[j]) > int(lst[j+1]):
                    lst[j],lst[j+1]=lst[j+1],lst[j]
        if flag:
            lst=lst[::-1]
            z="".join(lst)
            a=int(z)
            return -1*a
        else:
            b=0
            for i in range(len(lst)):
                if lst[i] !="0":
                    b=i
                    break
            if lst[0]=="0":
                lst[0],lst[b]=lst[b],lst[0]
                z="".join(lst) 
                return int(z)
            z="".join(lst)   
            return int(z)
                
                
        