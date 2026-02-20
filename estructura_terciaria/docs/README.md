# Modelado estructural de proteínas y complejos proteína–ADN

## Actividades 7.7.1 y 7.7.2

**Curso:** Modelado y análisis estructural
**Herramientas empleadas:** AlphaFold2, AlphaFold3, SwissModel Assess

---

# 1. Introducción

El modelado estructural computacional permite inferir la conformación tridimensional de proteínas y complejos biomoleculares a partir de su secuencia primaria. En este trabajo se evaluaron dos aproximaciones:

* **AlphaFold2 (AF2)** para modelado de estructura terciaria de una proteína individual.
* **AlphaFold3 (AF3)** para modelado de un complejo proteína–ADN.

En ambos casos, la calidad estructural fue evaluada mediante métricas internas de los modelos y validación externa con SwissModel Assess.

---

# 2. Organización del repositorio

```text
estructura_terciaria/
│
├── data/                  # Secuencias utilizadas en el modelado
│   ├── CD4.fa
│   ├── CD4.pdb
│   ├── EGR1_DBD.fa
│   └── EGR1_TFBS_23bp.fa
│
├── docs/                  # Interpretación biológica y análisis estructural
│   ├── Interpretacion_modeloAF2_metricas.md
│   └── Interpretacion_modeloAF3_metricas.md
│
├── results/
│   ├── AF2/               # Modelos generados con AlphaFold2
│   ├── AF3/               # Modelos generados con AlphaFold3
│   └── SWISS-MODEL/       # Validación geométrica
│       ├── CD4_evaluacion_geometria_interna/
│       ├── CD4_validacion_estructura_referencia/
│       └── complejo_EGR1_ADN_validacion/
│
└── README.md
```

---

# 3. Actividad 7.7.1 – Modelado de estructura terciaria con AlphaFold2

## 3.1 Objetivo

Modelar la estructura tridimensional de una proteína individual y evaluar la calidad del modelo mediante métricas de confianza internas y validación geométrica independiente.

---

## 3.2 Sistema estudiado

**Proteína:** CD4 humano (UniProt: P01730)
**Tipo:** Glicoproteína de superficie de linfocitos T
**Longitud:** ~458 aminoácidos

Secuencia utilizada:
`data/CD4.fa`

---

## 3.3 Metodología

1. Modelado estructural mediante AlphaFold2.
2. Evaluación de métricas internas:

   * pLDDT (confianza local por residuo)
   * pTM (confianza en la topología global)
3. Validación estructural en SwissModel Assess:

   * MolProbity
   * QMEAN / QMEANDisCo
   * Análisis de Ramachandran
4. Comparación opcional contra estructura experimental de referencia.

---

## 3.4 Resultados e interpretación general

El modelo mostró:

* Alta confianza en los dominios estructurados.
* Regiones terminales con menor confianza, consistentes con flexibilidad intrínseca.
* Valores de MolProbity y Ramachandran compatibles con geometría estereoquímica adecuada.
* Arquitectura global consistente con la organización experimental conocida de CD4.

El análisis detallado se encuentra en:

`docs/Interpretacion_modeloAF2_metricas.md`

---

# 4. Actividad 7.7.2 – Modelado de complejo proteína–ADN con AlphaFold3

## 4.1 Objetivo

Modelar un complejo proteína–ADN e interpretar tanto la confianza en la interfaz molecular como la calidad geométrica del modelo resultante.

---

## 4.2 Sistema estudiado

### 4.2.1 Proteína

**Factor de transcripción:** EGR1
**Dominio modelado:** Dominio de unión a ADN (DBD)
**Tipo estructural:** Dominio C2H2 zinc finger

Secuencia empleada:
`data/EGR1_DBD.fa`

Se utilizó exclusivamente el dominio estructural responsable del reconocimiento de ADN para reducir ambigüedad estructural en regiones intrínsecamente desordenadas.

---

### 4.2.2 ADN

Fragmento de 23 pb conteniendo el motivo consenso de unión:

Motivo central: 5’-GCGTGGGCG-3’

Secuencia empleada:
`data/EGR1_TFBS_23bp.fa`

Se incluyeron iones Zn²⁺ necesarios para la estabilidad estructural de los dedos de zinc.

---

## 4.3 Metodología

1. Modelado del complejo con AlphaFold3.
2. Evaluación de métricas internas:

   * pLDDT
   * pTM
   * ipTM (confianza específica en la interfaz proteína–ADN)
   * PAE (error alineado esperado)
3. Validación geométrica mediante SwissModel Assess:

   * MolProbity
   * QMEANDisCo
   * Diagrama de Ramachandran
4. Inspección estructural visual del modo de unión al ADN.

---

## 4.4 Resultados e interpretación general

El modelo presentó:

* **ipTM elevado (~0.81)**, indicando alta confianza en la interfaz proteína–ADN.
* **pTM elevado (~0.83)**, indicando plegamiento estable del dominio.
* MolProbity bajo (~1.6), consistente con buena estereoquímica.
* QMEANDisCo ~0.7, compatible con calidad estructural global adecuada.

Desde el punto de vista estructural:

* Las hélices α de reconocimiento se insertan en el surco mayor del ADN.
* La orientación sigue el patrón canónico de dominios C2H2.
* No se observan distorsiones estructurales evidentes.

El análisis detallado se encuentra en:

`docs/Interpretacion_modeloAF3_metricas.md`

---

# 5. Discusión general

Los resultados muestran que:

* AlphaFold2 reproduce con alta fidelidad la estructura terciaria de proteínas individuales.
* AlphaFold3 permite modelar complejos proteína–ADN con estimación explícita de confianza en la interfaz.
* La combinación de métricas internas (pTM, ipTM) y validación externa (SwissModel) proporciona una evaluación integral del modelo.
* La coherencia estructural observada es consistente con el conocimiento experimental disponible sobre dominios C2H2.

---

# 6. Conclusión

Las actividades 7.7.1 y 7.7.2 demuestran la aplicabilidad de modelos de aprendizaje profundo para:

* Inferir estructura terciaria proteica.
* Predecir interacciones proteína–ADN.
* Evaluar calidad estructural mediante métricas cuantitativas.
* Interpretar resultados desde una perspectiva estructural y funcional.

El conjunto de modelos generados es geométricamente consistente y biológicamente plausible.

---

Este proyecto fue desarrollado siguiendo los principios de "Algoritmos en Bioinformática Estructural" de Bruno Contreras-Moreira.
