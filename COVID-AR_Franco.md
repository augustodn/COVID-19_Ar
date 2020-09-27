- Contagios por rango etario
- Diferencias entre datasets: Min de Salud vs. COVID Stats AR

## Contagios por rango etario

### Limpieza de datos para análisis de contagiados

Para realizar esta sección se tomaron [datos del Ministerio de salud](http://datos.salud.gob.ar/dataset/covid-19-casos-registrados-en-la-republica-argentina), los datos que vamos a tomar son para analizar la cantidad de contagiados por rango etario y se añadirá un pequeño analisis comparando los contagiados por el sexo. Del datasets original podemos ver que tenemos:

| Tipo | Cantidad  |
|--|--|
| Descartado | 1003458 |
| Confirmado | 691230 |
| Sospechoso | 146139 |
| Sin Clasificar | 372 |

Tomaremos los datos confirmados. El dataset en bruto tiene 25 columnas. Las de interés nuestro son el sexo, edad, fecha de diagnóstico, la columna que indica si se encuentra fallecido o no y en que fecha fallecio.

Luego de limpiar los datos lo que haremos será obtener subdatasets de este y normalizarlos para realizar el estudio.

### Normalización

¿Pero porque decidimos normalizar?

La poblacion de Argentina que ocupa la franja de entre 20-40 años es mucho mayor que la de 60-80, esto generará en los histogramas de contagios y muertes un sesgo, sólo por el factor poblacional.

En el siguiente enlace, [link censo poblacional](https://redatam.indec.gob.ar/argbin/RpWebEngine.exe/PortalAction?&MODE=MAIN&BASE=CPV2010B&MAIN=WebServerMain.inl&_ga=2.177965477.1629507683.1526925251-993948438.1526925251), tenemos a la poblacion total de Argentina del último censo oficial, por el INDEC. Los datos con los que se trabajaron contienen a la población dividada en varón y mujer, en rangos quinquenales cada uno.

Los que haremos es dividir la población de contagiados (y fallecida) por la población total, por cada rango quinquenal. Con esto tendremos a nuestros datos en un rango de 0 a 1. Si a esto lo multiplicamos por 100 tendremos una porcentaje. Obtendremos diferentes datasets para el estudio de contagiados y fallecidos.

```py
    # Contagiados
    (df_poblacion_contagiados['total'] / df_poblacion['total']) * 100

    # Fallecidos
    (df_poblacion_fallecidos['total'] / df_poblacion['total']) * 100
```

### Distribución de contagiados por rango etario

![distribución-contagiados](https://imgur.com/sNNaVoa.png)

Expliquemos el gráfico. En el eje **x** tenemos el rango de edades de la población de contagiados en categorias que van de 5 en 5. En el eje **y** tenemos al porcentaje de contagiados por rango etario, respecto a la población total de Argentina.

Podemos ver como el COVID-19 tiene un mayor impacto sobre los adultos mayores, esto se debe a que hay menos población en esos rangos.

Veamos un ejemplo tomando un rango cualquiera. Puede ser el de (30,35].

Si nos posicionamos sobre este, nos esta diciendo que el porcentaje o la población contagiada total que tiene entre 30 y 35 años es del 2.67% aproximadamente de esa misma categoria de la poblacion Argentina. Con numeros sería, la categoria 30-35 de la población total tiene 3.098.713 personas, si a esto lo multiplicamos por 2.67% (0.0267) tendremos a la población contagiada de ese rango. Los datos de la población total de Argentina la podemos ver en la siguiente tabla.

![poblacion-argentina](https://imgur.com/RTHNH4M.png)

### Distribución de fallecidos por rango etario

![distribución-fallecidos](https://imgur.com/pXXSp5a.png)

En este histograma vemos que la población más afectada por el COVID-19 en Argentina, y en todo el mundo, fue y es la adulta mayor a 60 años. Esto nos dice que en esta población deberiamos haber hecho hincapíe, ayudarla mas. A su vemos podemos ver los porcentajes de fallecidos respecto a la población total de Argentina.

El procedimiento para analizar estos es el mismo que el explicado en la gráfica anterior. Tomamos un rango de interés, obtenemos el porcentaje y lo multiplicamos por la población total de ese rango de la tabla de población total.

### Impacto de fallecidos sobre contagiados

Ahora veamos la distribución de fallecidos sobre la distribución de contagiados. Con esto veremos el impacto de los fallecidos que tiene el COVID-19 sobre la población infectada.

![fallecidos-contagiados](https://imgur.com/SI1FZIn.png)

En este histograma podemos apreciar el impacto real que tiene el COVID-19 sobre la población. Expliquemos detalladamente que significa para elemento de nuestro gráfico. Las barras azules son los contagiados y las barras anaranjadas son los fallecidos. En el eje **x** tenemos el rango etario y en el eje **y** tenemos el porcentaje de contagiados y fallecidos respecto a la población total de Argentina.

La población mas afectada por este virus como dijimos antes es la adulta mayor a 60 años. Los grupos por encima de esta edad son los que corren y corrierón mayor riesgo de sufrir complicaciones graves o morir por esta condición. **Caso cerrado**.

### Analisis por rango etario y sexo

Para finalizar esta sección del estudio veamos quienes son mas afectados por el COVID-19, ¿los hombres o las mujeres?. Este ultimo apartado podría parecer una especie de competencia de quien aguanta mas este virus. Es interesante observar que parte de la población es mas afectada por el mismo.

Para llegar a diferentes conclusiones primero se obtuvo dos dataset de interés. Se extrayeron los datos del dataset en bruto, transformamos al mismo, lo normalizamos y graficamos.

![contagiados-edad-sexo](https://imgur.com/Jf7gduF.png)

Podemos ver a simple vista en la curva de contagiados del COVID-19 que en general afecta mas a la población masculina. En porcentaje tenemos que el **50.82%** de la poblacion afectada por el COVID-19 es masculina y el **49.18%** es femenina. Veamos ahora la curva de fallecidos.

![fallecidos-edad-sexo](https://imgur.com/l02GsBk.png)

Como veniamos viendo en el histograma anterior, a simple vista en la siguiente curva de fallecidos por COVID-19 afecta mas a la población masculina que a la femenina. En porcentaje tenemos que el **56.96%** de la poblacion afectada por el COVID-19 es masculina y el **43.04%** es femenina.