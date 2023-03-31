str1 = input ("Digite a primeira String: ");
str2 = input ("Digite a segunda String: ");

print ("O conteúdo da String um: ", str1, "/ O comprimento: ", len(str1));
print ("O conteúdo da String dois: ", str2, "/ O comprimento: ", len(str2));

if (len(str1) == len(str2)):
    print ("O comprimento é o mesmo.");
else:
    print ("As strings não tem o mesmo cumprimento");
if (str1 == str2):
    print ("As Strings são iguais");
else:
    print ("As strings são diferentes")
