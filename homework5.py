immutable_var = tuple([1, 2, True, 'Илюжн идет гулять'])
print(immutable_var)
#immutable_var[1] = 2 # изменить кортеж не представляется возможным, так как он является вводимой неизменяемой константой
mutable_list = [23, 15, False, 'Илюжн хороший мальчик']
mutable_list[3] = 'Илюжн плохой мальчик'
print(mutable_list)