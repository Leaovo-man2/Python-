height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（公斤）："))
# 计算BMI
 
BMI = weight / (height ** 2)
print("BMI值为：{:.2f}".format(BMI)) 
 
if BMI < 18.5:
    print("您的体重过轻")
elif BMI < 24.9:
    print("您的体重正常")
elif BMI < 29.9:
    print("您的体重过重")
else:
    print("您的体重属于肥胖")