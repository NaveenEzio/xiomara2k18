def decryptnum(priv, c):
    (d, n) = priv
    if c < 0 or c >= n:
        print("\nOops! Something's out of range!\n")
    return pow(c, d, n)

def parityOracle(c):
    p = decryptnum(priv, c)
    return p % 2

if __name__ == '__main__':
    priv = (320799094578192692162355285134013499936955976035014791849513625061850228095856468194322285052313609463068487602895688342560302379590570739995444425224126048715492708470865002289665571993815595568533069049179767236468362331963399378891940149760768579649792296686615195432866372294733382099619145842114597451227, 481198641867289038243532927701020249905433964052522187774270437592775342143784702291483427578470414194602731404343532513840453569385856109993166637836189117235549985093499643724363002153995995953731212190003813128852867940536928597102669895224512199695772684398151784349020282852823384810308548307944122748283)
    print("\nLook...I am a very strange and \"odd\" guy, and I'll only like you, if you are alike me...\nSend me messages and I'll let you know if I like you or not...\nI hope you know my public key!\n")
    while(True):
        try:
            c = int(input())
            if(parityOracle(c)):
                print("Hey buddy! I like you <3\n")
            else:
                print("Aye fool! I don't like you _|_\n")
        except:
            exit()
