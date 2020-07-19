names = ['Isa', 'Murat', 'Azim', 'Aikerim']
print('Дорогой гость, ' + names[0] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[1] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[2] + ' приглaшаю Вас на обед!')
print('Дорогой гость, ' + names[3] + ' приглaшаю Вас на обед!')
ne_pridet = names.pop(3)
print(ne_pridet + ' прийти не сможет')
names.insert(3, 'Uluk')
print('Дорогой гость, ' + names[3] + ' приглaшаю Вас на обед!')

