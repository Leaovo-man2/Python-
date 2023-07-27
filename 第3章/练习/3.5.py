# 定义列表
names = ['albert Einstein','charlotte Sherlock Holmes','michael jackson']
# 定义message并打印出邀请信息
message = f'Please {names[0].title()} join me for dinner.'
print(message)
message = f'Please {names[1].title()} join me for dinner.'
print(message)
message = f'Please {names[2].title()} join me for dinner.'
print(message)
# 一嘉宾无法赴约
print("Michael jackson couldn't make it to the appointment")
# 从列表中删除，并追加（append）新嘉宾
names.remove('michael jackson')
names.append('super man')
# 再次发出邀请
message = f'Please {names[0].title()} join me for dinner.'
print(message)
message = f'Please {names[1].title()} join me for dinner.'
print(message)
message = f'Please {names[2].title()} join me for dinner.'
print(message)
