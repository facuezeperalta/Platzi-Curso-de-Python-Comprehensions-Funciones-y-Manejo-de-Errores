try:
    print(0/0)
    assert 1 != 1, 'uno es igual a uno'
    age = 10
    if age < 18:
        raise Exception('Debes ser mayor de edad')
except ZeroDivisionError as error:
    print('Division por 0 NO ESTA PERMITIDA')

except AssertionError as error:
    print(error)
    
except Exception as error:
    print(error)

print('Hola!')
