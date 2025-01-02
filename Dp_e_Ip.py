#Se sabe que L es DP al cuadrado de P y con el cubo de V e IP a la raíz cuadrada de Z.
#Completar el cuadro y hallar el valor de “a” y "b"
# L	/   a   /	108   /	324
# P	/   5	/    2	  /  4
# V	/   2	/    3	  /  b
# Z	/  25	/    9	  /  16

def calcular_valor_L(valor_x, valor_p, raiz_z, cubo_v):
    valor_L = (valor_x * raiz_z)/ (valor_p * cubo_v) 
    return valor_L
def calcular_valor_a(valor_L, Nvalor_p, Ncubo_v, Nraiz_z ):
    valor_a = (valor_L * Nvalor_p * Ncubo_v) / Nraiz_z
    return valor_a 

def calcular_valor_b(valor_L, valorx2, Nvalor_p2, Nraiz_z2 ):
    valor_b = (valorx2 * Nraiz_z2) / (valor_L* Nvalor_p2)
    return valor_b

def respuesta():
    # Datos conocidos
    valor_x = 108  
    valor_p = 2**2  
    raiz_z = pow(9,1/2)  
    cubo_v = 3**3
    # Datos conocidos para encontrar el valor de a
    Nvalor_p = 5**2
    Ncubo_v = 2**3
    Nraiz_z = pow(25,1/2)
    # Datos conocidos para encontrar el valor de b
    valorx2 = 324
    Nvalor_p2 = 4**2
    Nraiz_z2 = pow(16,1/2)

    # Calcular el costo de la casa
    resultado_L = calcular_valor_L(valor_x, valor_p, raiz_z, cubo_v)
    resultado_a = calcular_valor_a(resultado_L, Nvalor_p, Ncubo_v, Nraiz_z)
    resultado_b = calcular_valor_b(resultado_L, valorx2, Nvalor_p2, Nraiz_z2)**(1/3)

    # Mostrar resultados
    
    print(f"el valor de x es: {resultado_L:.2f}")
    print(f"el valor de a es: {resultado_a:.2f}")
    print(f"el valor de b es: {resultado_b:.2f}")
    print(f"el valor de b con otra raiz cúbica es: {resultado_b ** (1/3):.2f}")
    
        
# Llamar a la función principal
respuesta()