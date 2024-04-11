metro = float(input('Digite uma medida em metros: '))
cent = 100 * metro
mili = 1000 * metro
dam = metro / 10
hm = metro / 100
km = metro / 1000
print('O valor {} em metros corresponde a {} centímetros e a {}milímetros'.format(metro, cent, mili))
print('O valor {} em metros corresponde a {} decâmetros, a {} hectômetros e a {} quilômetros'.format(metro, dam, hm, km))
