import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
respuesta = requests.get(url)
#print(respuesta)

if respuesta.status_code == 200:
    datos = respuesta.json()

    # Obtener la lista de empleados
    empleados = datos.get('data', [])
    # Calcular la cantidad de empleados
    cantidad_empleados = len(empleados)
    print(f"Cantidad de empleados: {cantidad_empleados}")

    # Calcular el promedio de salario
    salarios = [empleado.get('employee_salary', 0) for empleado in empleados]
    salario_promedio = sum(salarios) / cantidad_empleados
    print(f"Promedio de salario: {salario_promedio}")

    # Calcular el promedio de edad
    edades = [empleado.get('employee_age', 0) for empleado in empleados]
    edad_promedio = sum(edades) / cantidad_empleados
    print(f"Promedio de edad: {edad_promedio}")

    # Encontrar el salario mínimo y máximo
    salario_minimo = min(salarios)
    salario_maximo = max(salarios)
    print(f"Salario mínimo: {salario_minimo}")
    print(f"Salario máximo: {salario_maximo}")

    # Encontrar la edad menor y mayor
    edad_menor = min(edades)
    edad_mayor = max(edades)
    print(f"Edad menor: {edad_menor}")
    print(f"Edad mayor: {edad_mayor}")



else:
    # Mostrar un mensaje de error si la solicitud no fue exitosa
    print(f"Error en la solicitud. Código de estado: {respuesta.status_code}")