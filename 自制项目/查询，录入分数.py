k = input('您要进行什么操作？ （查询），（录入）：')
if k == '查询':
    n = 'Mickey', 'Bob', 'Jon'
    d = {'Mickey': 95, 'Bob': 100, 'Jon': 90}
    print(n)
    print(d[input('学生姓名 ')], '分')
if k == '录入':
    na = ['Mickey', 'Bob', 'Jon']
    nam = input('新学生名字？ ')
    na.append(nam)
    f = input('分数？')
    d = {'Mickey': 95, 'Bob': 100, 'Jon': 90, nam: f}
    print('添加成功！')
    print(d)
    print(d[input('学生姓名 ')], '分')
