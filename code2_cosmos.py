def cliente(informacion:dict):

    ingreso= 1 if informacion['primer_ingreso'] else 0

    if informacion ['edad'] > 18:
        atraccion='X-Treme'
        apto = True
        preciobol = 20000 * ( 1 -0.05 * ingreso)
    
    elif informacion ['edad'] >= 15 and informacion ['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True
        preciobol = 5000 - 350*ingreso
        
    elif informacion ['edad'] >= 7 and informacion ['edad'] < 15:
        atraccion = 'Sillas voladorassss'
        apto = True
        preciobol = 10000 - 500*ingreso
        
    else:
        atraccion = 'N/A'
        apto = False
        preciobol = 'N/A'
        
    if not informacion['primer_ingreso']:
        preciobol=int(preciobol)
    
        
        
    dicc2 = {'nombre': informacion ['nombre'], 'edad': informacion ['edad'], 'atraccion': atraccion, 'apto': apto, 'primer_ingreso': informacion ['primer_ingreso'],
         'total_boleta':preciobol}
    return dicc2

informacion = {'nombre': 'Johana Fernandez', 'edad': 8, 'primer_ingreso':True}
print (cliente (informacion))