
# str = 'abcdeagregreehwtsagergreawedsf'
#
# # for i in str:
# #     str = i + str
# # print(str)
#
# str = str[::-1]
# print(str)

# height = 5
#
# for i in range(5):
#     print('*' * i)
# while (height > 0):
#     print('*' * height)
#     height-=1

array = [ [0, 1],
          [0, 1]]

def turnRight():
     for elem in range(2):
        for index in range(2):
            if(array[index] + 1 == 2):
                index = 0



turnRight()
print(array)
