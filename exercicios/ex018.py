import math
a = int(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo {:.2f}° tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, sen, cos, tan))
