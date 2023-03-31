"""9. A importância de R$ 780.000,00 será dividida entre três ganhadores de
um concurso. Sendo que da quantia total: - O primeiro ganhador receberá 46%; - O segundo receberá 32%; - O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores."""



valor = 780.000;
ganhador1 = (valor * 46) / 100;
print ("O primeiro ganhador ficará com: ", ganhador1);
valor = valor - ganhador1;
ganhador2 = (valor * 32) / 100;
print ("O segundo ganhador ficará com: ", ganhador2);
valor = valor - ganhador2;
print ("O terceiro ganhador ficará com: ", valor);
