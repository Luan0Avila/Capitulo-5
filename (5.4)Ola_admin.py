users = ['luan','lucas','joão','admin','mateus']

for user in users:
    if user == 'admin':
        print (f'Olá {user}, gostaria de ver um relatório de status?')
    else:
        print (f"Olá, {user} bem vindo!!!")