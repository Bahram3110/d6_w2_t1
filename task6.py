names = ['Isa', 'Murat', 'Azim', 'Aikerim']
print('Дорогой гость, ' + names[0] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[1] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[2] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[3] + ' приглaшаю Вас на обед!')
ne_pridet = names.pop(3)
print(ne_pridet + ' прийти не сможет')
names.insert(3, 'Uluk')
print('Дорогой гость, ' + names[3] + ' приглaшаю Вас на обед!')
print('Дорогие гости нас будет больше!')
names.insert(4, 'Ilyas')
names.insert(5, 'Asan')
names.insert(6, 'Nursultan')
# print(names)
print('Дорогой гость, ' + names[4] + ' приглaшаю Вас на обед!') #dop gosti
print('Дорогой гость, ' + names[5] + ' приглaшаю Вас на обед!') #dop gosti
print('Дорогой гость, ' + names[6] + ' приглaшаю Вас на обед!') #dop gosti

print('Hа обед приглашаются всего два гостя')
ne_pridet1 = names.pop(6)
print('Сожалею ' + ne_pridet1 + ', ' + 'но вы прийти не сможете')
ne_pridet2 = names.pop(5)
print('Сожалею ' + ne_pridet2 + ', ' + 'но вы прийти не сможете')
ne_pridet3 = names.pop(4)
print('Сожалею ' + ne_pridet3 + ', ' + 'но вы прийти не сможете')
ne_pridet4 = names.pop(3)
print('Сожалею ' + ne_pridet4 + ', ' + 'но вы прийти не сможете')
ne_pridet5 = names.pop(2)
print('Сожалею ' + ne_pridet5 + ', ' + 'но вы прийти не сможете')

print('Дорогой гость, ' + names[0] + ' приглашение на обед все еще в силе!') #v sile
print('Дорогой гость, ' + names[1] + ' пприглашение на обед все еще в силе!') #v sile
names.clear()
print(names)





