import random
count = 7
sampleList = ['a', 'b', 'c', 'd', 'e']

final= [random.choice(sampleList) for i in range(count)]
print(final)

final_no_du= random.sample(sampleList, count)
print(final_no_du)






import random
count = 7
sampleList = ['a', 'b', 'c', 'd', 'e']
final= [random.choice(sampleList) for i in range(count)]
print(final)
final_no_du= random.sample(sampleList, count)
print(final_no_du)







'''
Team 8 finish
'''
import random
COUNT = 7
sampleList = ['a', 'b', 'c', 'd', 'e']
final= [random.choice(sampleList) for i in range(COUNT)]
print(final)
final_no_du= random.sample(sampleList, COUNT)
print(final_no_du)

