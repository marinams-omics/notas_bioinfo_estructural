# Interpretación biológica de las métricas del complejo EGR1–ADN modelado con AF3

## Evaluación de confianza del modelo (AlphaFold3)

El modelo del complejo entre el dominio de unión a ADN de EGR1 (residuos 335–420) y un fragmento de ADN de 23 pb que contiene el motivo consenso 5’-GCGTGGGCG-3’ fue evaluado mediante las métricas internas de AlphaFold3.

El valor de **pTM = 0.83** indica alta confianza en la topología global del dominio proteico y en la disposición general del complejo. Este valor sugiere que el plegamiento del dominio C2H2 es estructuralmente consistente y estable.

Más relevante para un complejo multimolecular es el valor de **ipTM = 0.81**, que evalúa específicamente la confianza en la interfaz entre entidades distintas. Un ipTM superior a 0.7 se considera indicativo de una orientación relativa confiable entre proteína y ADN. Por tanto, el valor obtenido respalda una predicción robusta de la interacción proteína–ADN.

La matriz de error alineado (PAE) muestra valores bajos en la región correspondiente a la interfaz, lo que indica que la posición relativa entre el dominio proteico y el ADN está bien determinada por el modelo. No se observan bloques de alta incertidumbre que sugieran ambigüedad en el acoplamiento.

En conjunto, las métricas internas de AF3 indican una predicción estructural consistente tanto en el plegamiento del dominio como en su interacción con el ADN.

---

## Validación estereoquímica (SwissModel Assess)

La calidad geométrica del modelo fue evaluada mediante SwissModel Assess.

### MolProbity (1.63)

El valor de MolProbity obtenido (1.63) corresponde a una calidad estereoquímica alta, comparable a estructuras experimentales de resolución moderada a buena. Este resultado indica:

* Ausencia significativa de colisiones atómicas.
* Geometría adecuada de enlaces y ángulos.
* Conformaciones laterales plausibles.

Esto sugiere que el dominio proteico está modelado con una geometría interna físicamente realista.

---

### QMEANDisCo Global (0.71 ± 0.11)

El valor global de QMEANDisCo (0.71) indica buena similitud estadística con estructuras proteicas experimentales del PDB. El perfil local muestra que:

* Las regiones estructuradas correspondientes a los dedos de zinc presentan alta calidad.
* Las regiones terminales exhiben una ligera disminución en la puntuación, lo cual es esperable dada su mayor flexibilidad intrínseca.

Estos resultados son consistentes con la naturaleza modular de los dominios C2H2, que contienen núcleos estructurales compactos estabilizados por coordinación metálica.

---

### Análisis de Ramachandran

El diagrama de Ramachandran muestra que la mayoría de los residuos se ubican en regiones favorecidas del espacio conformacional φ/ψ. No se observan acumulaciones significativas en regiones prohibidas.

Esto confirma que el esqueleto peptídico presenta una conformación compatible con estructuras proteicas reales, reforzando la validez geométrica del modelo.

---

## Interpretación estructural y funcional

La inspección visual del complejo revela que:

* Las hélices α de reconocimiento de los dedos de zinc se insertan en el surco mayor del ADN.
* El dominio proteico sigue la curvatura del ADN de manera coherente.
* La arquitectura global es consistente con el modo canónico de unión de factores de transcripción C2H2.

Este patrón estructural coincide con lo descrito experimentalmente para EGR1 y otros factores C2H2, donde cada dedo reconoce aproximadamente tres pares de bases mediante interacciones específicas en el surco mayor.

La alta confianza en la interfaz (ipTM) y la estabilidad geométrica del dominio respaldan que la secuencia consenso utilizada corresponde a una configuración estructuralmente favorable y biológicamente plausible.

---

## Conclusión

Las métricas obtenidas indican que el modelo del complejo EGR1–ADN presenta:

* Alta confianza en la interacción proteína–ADN.
* Geometría estereoquímica adecuada.
* Arquitectura consistente con el mecanismo canónico de reconocimiento de ADN por dominios C2H2.

En conjunto, el modelo generado por AlphaFold3 constituye una representación estructural coherente y biológicamente consistente del complejo entre el dominio de unión a ADN de EGR1 y su sitio consenso.
