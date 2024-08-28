curents_users = ['noob11','luanzito123','jorginho bala fora','ricardão','player1']
new_users = ['noob11', 'luanzito123','aninha','juca','mario']

for user in new_users:
    if user in curents_users:
        print (f'O nome {user} já foi utilazado, por favor insira um novo nome de usuário')
    else:
        print (f'O nome {user} está disponivel!')