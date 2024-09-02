import pandas as pd

# En terminos muy simplistas, una serie es un arreglo que tiene emparentado unos indices que tu mismo puedes definir.
# Las series son mucho mas optimas que los arreglos cuando se tratan de conjuntos grandes de datos

if __name__ == "__main__":

    notas = pd.Series([5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9],
            index=["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"])

    print("-----------------")
    print(notas)
    print("-----------------")
    print("Min:",notas.min()) #Valor minimo
    print("Max:",notas.max()) #Valor maximo
    print("Prom:",notas.mean()) #Valor promedio
    print("Suma:",notas.sum()) #Suma de los valores
    print("-----------------")

    liga_espanola = pd.Series(['Real Sociedad','Real Madrid','Sevilla','Atlético de Madrid','Osasuna'],index=['1°','2°','3°','4°','5°'])

    print(liga_espanola['1°']) #Acceder a indice individual
    print(liga_espanola[['2°','3°']]) #Acceder a multiples indices
    print(liga_espanola[liga_espanola == 'Atlético de Madrid']) #Acceder al valor sin conocer su indice

    print("-----------------")

    # Crear pd.Series individuales
    serie_1 = pd.Series( [1, 2, 3], index=['A', 'B', 'C'] )
    serie_2 = pd.Series([4, 5, 6], index=['D', 'E', 'F'])
    serie_3 = pd.Series([7, 8, 9], index=['G', 'H', 'I'])

    # Crear una Serie de pd.Series
    serie_de_series = pd.Series([serie_1, serie_2, serie_3], index=['Serie 1', 'Serie 2', 'Serie 3'])

    # Mostrar la Serie de pd.Series
    print(serie_de_series)

    # Acceder a la Serie 1
    print("\nAcceder a Serie 1:")
    print(serie_de_series['Serie 1'])

    # Acceder a un valor específico dentro de una Serie
    print("\nAcceder a un valor dentro de Serie 2:")
    print(serie_de_series['Serie 2']['E'])

    print("-----------------")

inflacion= pd.Series(range(100,400,25),index=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])

print(inflacion)

