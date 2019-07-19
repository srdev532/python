def modifylist(listname):
    a = ''
    for i in listname:
        a = a + str(i)
        if listname.index(i) == (len(listname)-2):
            a = a + ', and '
        elif listname.index(i) == (len(listname)-1):
            a = a
        else:
            a = a + ', '
    return str(a)
        
spam = ['apples','ban','demon']

listname = spam
print(modifylist(listname))


########################################

