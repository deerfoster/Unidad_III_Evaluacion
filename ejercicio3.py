ingreso_base = 60000

edad = 70

dependientes = 2

ingreso_gravable = ingreso_base - (1000 * dependientes)

impuesto_1 = (ingreso_gravable * 0.1)

impuesto_2 = (ingreso_gravable * 0.2) + 4000

descuento_1 = (impuesto_1 * 0.05)

descuento_2 = (impuesto_2 * 0.05)

if (ingreso_base < 10000):
    print("No aplica a pagar el impuesto")
elif (10001 > ingreso_base < 50000):
    if (edad < 65):
        impuesto_final = impuesto_1
        print(f"Su impuesto es: {impuesto_final}")
    elif (edad >= 65):
        impuesto_final = descuento_1
        print(f"Su impuesto es: {descuento_1}")
elif (ingreso_base >= 50000):
    if (edad < 65):
        impuesto_final = impuesto_2
        print(f"Su impuesto es: {impuesto_final}")
    elif (edad >= 65):
        impuesto_final = descuento_2
        print(f"Su impuesto es: {descuento_2}")