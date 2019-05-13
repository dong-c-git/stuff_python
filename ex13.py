class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = input()
        #取出列表中数值组成数字
        l = ""
        for i in digits:
            l += str(i)
        print (l)
        l2 = int(l)+1
        list_return = []
        for t in str(l2):
            list_return.append(t)
        return list_return
#test_list = [4,3,2,1]
test = Solution()
tt2 = test.plusOne(digits)
print(tt2)
            
