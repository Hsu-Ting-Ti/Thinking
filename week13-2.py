#數字1到10之和
## 1+2+3+4+5+6+7+8+9+10 = ?
sum = 0 # 起始條件
for i in range(1, 11, 1): #數字串列[,1,2,3,4,5,6,7,8,9,10]
      sum = sum + i # 加總運算,變更條件
      print("Total is", sum)
      
      
# 2. 數字1到10奇數之和
## 1+3+5+7+9 = ?
sum = 0 #起始值
for i in range(1, 11, 2): # 數字串列[1,3,5,7,9]
      sum = sum + i #加總運算,變更條件
print("Total is", sum)


# 2+4+6+8+10 = ?
sum = 0
for i in range(2,11,2):
    sum = sum + i
print("Total is", sum)