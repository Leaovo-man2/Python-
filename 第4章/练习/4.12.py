foods = ('fish','meet','noodles','pizza','hamburger')
for food in foods:
    print(food)
# wrong
foods[0] = 'cake'
#
foods = ('cake','meet','fish','pizza','hamburger')
for food in foods:
    print(food)