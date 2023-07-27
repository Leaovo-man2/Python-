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
# 添加嘉宾，因为找到了更大的桌子
names.insert(0,'bob')
names.insert(2,'jhon')
names.append('mickey')
# 再次发出邀请
message = f'Please {names[0].title()} join me for dinner.'
print(message)
message = f'Please {names[1].title()} join me for dinner.'
print(message)
message = f'Please {names[2].title()} join me for dinner.'
print(message)
message = f'Please {names[3].title()} join me for dinner.'
print(message)
message = f'Please {names[4].title()} join me for dinner.'
print(message)
message = f'Please {names[5].title()} join me for dinner.'
print(message)
# 表明原因
print('I found a bigger dining table')
# 有多少人参加
print(f'I invited {len(names)} guests to dinner')