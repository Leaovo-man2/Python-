#导入模块（计时）
import time

# 汪汪队发射程序
print('汪汪队发射程序，启动')
print('Warn! Non-combatants please evacuate!')
time.sleep(2)
# 报道
classmates = ['毛毛','小丽','灰灰']
time.sleep(1)
print(len(classmates),'名队员')
print(classmates[0],'队长')
time.sleep(1)
print(classmates[1],'队员')
time.sleep(1)                    
print(classmates[2],'队员')
time.sleep(1)
name = input("新队员的名字\
             ")
classmates.append(name)
print('你好',name)
time.sleep(1)
print(len(classmates),'名队员')
name = input("新队员的名字\
             ")
classmates.insert(1, name)
time.sleep(1)
print('你好',name)
time.sleep(1)
print(len(classmates),'名队员')
# 准备
time.sleep(1)
print(classmates[3],'准备就绪!'\
      )
time.sleep(1)
print(classmates[1],'准备就绪!'\
      )
time.sleep(1)
print(classmates[2],'准备就绪！'\
      )
time.sleep(1)
print(classmates[3],'准备就绪！'\
      )
time.sleep(1)
print(classmates[4],'准备就绪！'\
      )
# 发射
print('please wait')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print(classmates[0],'发射！'\
      )
time.sleep(1)
print(classmates[1],'发射！'\
      )
time.sleep(1)
print(classmates[2],'发射！'\
      )
time.sleep(1)
print(classmates[3],'发射！'\
      )
time.sleep(1)
print(classmates[4],'发射！'\
      )
time.sleep(1)
# 发射完毕
print('发射完毕！')