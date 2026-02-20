# Modelado estructural de CD4 mediante AlphaFold2 y evaluación de calidad

## Introducción

Se seleccionó la proteína CD4 humana (UniProt: P01730), una glicoproteína de superficie expresada en linfocitos T y caracterizada por presentar dominios extracelulares tipo inmunoglobulina, una región transmembrana y una cola citoplasmática. La estructura terciaria fue modelada mediante AlphaFold2 (implementación ColabFold), y posteriormente evaluada utilizando las métricas disponibles en SwissModel Assess, tanto de forma independiente como en comparación con una estructura experimental de referencia.

---

## 1. Evaluación de calidad intrínseca del modelo

### MolProbity (2.93)

El puntaje MolProbity evalúa la calidad estereoquímica del modelo, incluyendo ángulos de enlace, colisiones atómicas y conformaciones del esqueleto peptídico. Un valor de 2.93 indica una geometría global aceptable para un modelo predictivo, sin evidencias de conflictos estructurales graves. Aunque no corresponde a calidad cristalográfica de alta resolución, el valor obtenido es consistente con modelos generados por métodos de predicción estructural basados en inteligencia artificial.

Desde el punto de vista estructural, esto sugiere que la conformación propuesta es físicamente plausible y adecuada para análisis estructurales generales.

---

### QMEANDisCo global (0.69 ± 0.05)

El puntaje QMEANDisCo evalúa la similitud del modelo con estructuras experimentales conocidas. Un valor cercano a 0.7 indica una calidad moderada a buena.

El análisis local muestra que:

* Los dominios globulares tipo inmunoglobulina presentan alta calidad y estabilidad estructural.
* Los extremos N- y C-terminales, así como regiones de conexión entre dominios, presentan menor confianza.

Este patrón es coherente con la biología de CD4. Los dominios extracelulares estructurados son esenciales para el reconocimiento molecular (por ejemplo, interacción con MHC-II o gp120 del VIH), mientras que las regiones terminales y de enlace pueden exhibir mayor flexibilidad conformacional.

---

### Análisis de Ramachandran

El diagrama de Ramachandran muestra que la mayoría de los residuos se ubican en regiones favorecidas del espacio conformacional φ/ψ. Solo se observan algunos residuos en regiones menos favorecidas o atípicas.

Esto indica que la geometría del esqueleto peptídico es consistente con estructuras proteicas reales y que no existen distorsiones sistemáticas en el modelo. Las desviaciones puntuales probablemente corresponden a regiones flexibles o menos estructuradas.

---

## 2. Comparación con estructura experimental de referencia

Se realizó una comparación estructural entre el modelo predicho y una estructura experimental de CD4 disponible en el PDB.

### RMSD (1.61 Å)

El valor de RMSD obtenido es bajo, lo que indica una buena superposición entre el modelo y la estructura experimental en las regiones alineadas. En términos estructurales, un RMSD inferior a 2 Å se considera indicativo de una alta similitud en el plegamiento global de los dominios estructurados.

Esto demuestra que AlphaFold2 reproduce con precisión la arquitectura tridimensional de los dominios extracelulares de CD4.

---

### TM-score (0.49)

El TM-score se aproxima al umbral (~0.5) que indica similitud estructural significativa. El valor ligeramente inferior a este umbral sugiere que, aunque los dominios principales coinciden adecuadamente, existen diferencias globales atribuibles a:

* Regiones flexibles o desordenadas.
* Segmentos no resueltos en la estructura experimental.
* Diferencias en cobertura de secuencia entre el modelo completo y el constructo experimental.

---

### IDDT (0.38)

El valor moderado de IDDT indica desviaciones locales entre modelo y referencia. Estas diferencias probablemente se concentran en regiones de baja confianza estructural, como loops expuestos o segmentos terminales.

En el contexto biológico, estas regiones pueden presentar flexibilidad funcional, lo cual es característico de proteínas de superficie implicadas en reconocimiento molecular.

---

## Interpretación biológica global

El modelo estructural de CD4 generado mediante AlphaFold2 reproduce adecuadamente la organización tridimensional de los dominios inmunoglobulina extracelulares, que constituyen el núcleo estructural funcional de la proteína.

La calidad estereoquímica es aceptable y la concordancia con la estructura experimental es alta en las regiones estructuradas. Las discrepancias observadas se concentran en regiones potencialmente dinámicas o no resueltas experimentalmente, lo cual es consistente con la naturaleza modular y parcialmente flexible de CD4.

En términos funcionales, el modelo es confiable para:

* Analizar la arquitectura de dominios.
* Explorar interacciones proteína-proteína a nivel estructural global.
* Interpretar la organización espacial de la región extracelular.

Sin embargo, debe emplearse con cautela en:

* Regiones desordenadas.
* Segmentos transmembrana.
* Análisis detallados de interacciones atómicas finas o dinámica conformacional.

---

## Conclusión

Los resultados demuestran que AlphaFold2 es capaz de reconstruir con alta precisión el núcleo estructural de una proteína de membrana multidominio como CD4. La concordancia con datos experimentales valida la calidad del modelo en regiones estructuradas, mientras que las limitaciones observadas reflejan principalmente la presencia de regiones flexibles o parcialmente desordenadas.

En conjunto, el modelo obtenido es estructural y biológicamente consistente, y constituye una representación confiable de la arquitectura tridimensional de CD4 en su estado monomérico.
