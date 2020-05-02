def defineusername():
    try:
        username
    except:
        username = input('Qual o nome de usuário do GitHub? ')
    
      
    return username

def definepassword():
    try:
        pw
    except:
        pw = input('Qual a senha do GitHub? ')
    
    return pw

def definerepository():
    
    try:
        repo
    except:
        repo = input('Qual o nome do repositório? ')
    
    return repo