import pickle


def login(UserName, Password):

    UserPass = pickle.load(open('UserPass','rb'))

    if UserName not in list(UserPass.keys()):
        return 'Username does not exits!'

    elif UserName in list(UserPass.keys()) and Password != UserPass[UserName]['Password']:
        return 'Password is Wrong!'

    else:
        return True



def SignUp(UserName, Password, ID):

    UserPass = pickle.load(open('UserPass','rb'))
    UserPass[UserName] = {"Password" : Password, "ID" : ID}

    pickle.dump(UserPass, open('UserPass','wb'))




def reset_pass(UserName, ID):
    UserPass = pickle.load(open('UserPass','rb'))

    if  UserPass[UserName]["ID"] == ID:
        return  UserPass[UserName]["Password"]



