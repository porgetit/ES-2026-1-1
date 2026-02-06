# Taller de Repaso: Estadística Descriptiva
---
### Autor: Kevin Esguerra Cardona
---
## Uso del Script de Estadísticas

Para calcular los valores de este taller, puedes usar el script `statistics_calc.py`.

### Ejecución básica (un conjunto):

```bash
python3 statistics_calc.py 8 10 6 12 9 11 7 10
```

### Ejecución multi-conjunto (separados por coma):

```bash
python3 statistics_calc.py 70 72 71 69 68 70 , 60 80 75 65 85 55
```

---

## Ejercicio 1. Cálculo e interpretación básica

**Datos:** 8, 10, 6, 12, 9, 11, 7, 10

1. **Media aritmética:**

   > 9.1250

2. **Varianza muestral:**

   > 4.1250

3. **Desviación estándar:**

   > 2.0310

4. **Interpretación:**
   > Media: un estudiante en promedio estudia 9.1250 horas semanales.
   > Varianza muestral: los estudiantes toman en promedio entre 5 y 13 horas semanales de estudio.
   > Desv. Estandar: con una desviación estándar de un 22.25%, algo grande, podríamos decir que faltan datos para tener una mejor representación de la población real.

---

## Ejercicio 2. Comparación de dispersión

**Grupo A:** 70, 72, 71, 69, 68, 70

**Grupo B:** 60, 80, 75, 65, 85, 55

1. **Media de cada grupo:**
   - **Grupo A:** 70.0000
   - **Grupo B:** 70.0000

2. **Desviación estándar de cada grupo:**
   - **Grupo A:** 1.2910
   - **Grupo B:** 10.8012

3. **¿Cuál grupo presenta mayor homogeneidad? Justifique:**
   > Grupo A, la dispersión es menor, así se deduce que los datos son más homogéneos, están más agrupados.

---

## Ejercicio 3. Efecto de valores extremos

**Datos:** 900, 950, 1000, 980, 970, 5000

1. **Media aritmética:**

   > 960.0000 sin el valor extremo, 1633.3333 con el valor extremo.

2. **Efecto del valor extremo sobre la media:**

   > El valor extremo (5000) tiene un gran impacto en la media, ya que es un valor muy alto en comparación con los demás datos, elevando la media al rededor de un 70% en comparación con la muestra sin el valor extremo.

3. **¿Qué ocurre con la varianza y la desviación estándar?**
   > En ambos casos, los valores se disparan, mas resulta interesante analizar la relación entre la media y la desviación estándar, en el caso de la muestra sin el valor extremo vemos que la Desv. Est. es apenas de un 3% del valor de la media, mientras que en la muestra completa, la dispersión es de un 92.22% del valor de la media, invalidando completamente la representación poblacional.

---

## Ejercicio 4. Análisis conceptual: medidas descriptivas

1. **¿Por qué la media aritmética puede no ser representativa?**

   > Porque puede ser computada conteniendo valores extremos, los cuales generan que el valor de esta se dispare en comparación con la media poblacional real.\_

2. **¿Qué información aporta la varianza que no se observa con la media?**

   > La varianza nos permite observar cuán alejados están los extremos del conjunto muestral de datos.

3. **¿Por qué la desviación estándar suele ser más interpretable?**
   > Porque nos permite observar de manera intuitiva cuán alejados están los datos del valor central, o media del conjunto muestral de datos.

---

## Ejercicio 5. Comparación conceptual de conjuntos de datos

1. **¿Qué puede decirse sobre la distribución de los datos con misma media pero diferente desviación?**

   > Este caso nos habla de la disperción o heterogeneídad del conjunto muestral de datos. Al tener una misma media aritmética podemos decir que los datos podrían corresponder a caracterísicas similares de una población, sin embargo, la desviación estándar es quién nos dirá si existe una relación real entre el conjunto y la población a estudiar.

2. **¿Cuál conjunto presenta mayor dispersión? Justifique:**

   > El conjunto con mayor desviación estándar es el que presenta mayor dispersión. Desde la interpretación de que la desviación estándar es la medida de cuán alejados están los datos entre sí, podemos concluir que el conjunto con mayor desviación estándar es el que presenta mayor dispersión.

3. **¿Por qué es importante analizar la dispersión junto con la media?**
   > Porque porque nos permite identificar la calidad del conjunto muestral.

---

## Ejercicio 6. Desarrollo matemático integrador

**Datos:** 15, 18, 20, 22, 25, 30

1. **Media aritmética:**

   > 21.6667

2. **Varianza muestral:**

   > 28.2667

3. **Desviación estándar:**

   > 5.3166

4. **Comportamiento general de los datos:**
   > La desviacion estándar es alrededor del 24.5% de la media, lo que nos indica que existe una dispersión considerable entre los datos.

---

## Ejercicio 7. Reflexión descriptiva

1. **¿Por qué no es suficiente reportar solo la media?**

   > Porque es un dato insuficiente para describir el comportamiento general de los datos. Además de ser altamente susceptible a la influencia de valores extremos.

2. **¿Qué tipo de conclusiones pueden obtenerse de la desviación estándar?**

   > La desviación estándar nos permite obtener conclusiones sobre la dispersión o heterogeneidad/homogeneidad de los datos.

3. **¿Cómo contribuyen estas medidas a la comprensión del fenómeno?**

   > Estas medidas nos permiten generar conclusiones sobre la calidad de los datos, sin embargo para conjuntos de datos muy grandes o complejos, podrían resultar insuficientes para dar un veredicto válido y resultaría necesaria la aplicación de técnicas estadísticas más avanzadas.
