""" 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um
crime."""

perg1 = input ("Telefonou para a vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg2 = input ("Esteve no local do crime? Responda com 'S' (Sim) ou 'N' (Não): ");
perg3 = input ("Mora perto da vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg4 = input ("Devia para vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg5 = input ("Já trabalhou com a vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
aux = 0
if (perg1 == "S"):
    aux = aux + 1;
if (perg2 == "S"):
    aux = aux + 1;
if (perg3 == "S"):
    aux = aux + 1;
if (perg4 == "S"):
    aux = aux + 1;
if (perg5 == "S"):
    aux = aux + 1;

if(aux == 2):
    print ("Suspeito!");
if(aux == 3 or aux == 4):
    print ("Cúmplice!");
if (aux == 5):
    print("Assassino!");

