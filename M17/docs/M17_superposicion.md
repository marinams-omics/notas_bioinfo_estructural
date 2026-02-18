# M17 — Alineamiento y superposición estructural

**Superfamilia CATH 2.60.40.10 (Immunoglobulin domain)**

## Objetivo

Aprender a realizar alineamientos estructurales múltiples, visualizar superposiciones tridimensionales y calcular métricas cuantitativas de similitud estructural (RMSD) e identidad de secuencia para pares seleccionados de dominios pertenecientes a una misma superfamilia estructural.

---

## Metodología

### 1. Selección de dominios (CATH)

Se seleccionaron dominios pertenecientes a la superfamilia:

> **CATH 2.60.40.10 — Immunoglobulin domain**

Se eligieron entre 5 y 10 dominios relacionados estructuralmente para su análisis comparativo.

---

### 2. Alineamiento estructural múltiple

El alineamiento estructural se realizó utilizando:

**Foldmason (FoldSeek Webserver)**
[https://search.foldseek.com/foldmason](https://search.foldseek.com/foldmason)

Se descargaron los siguientes archivos:

* `foldmason.pdb` → superposición estructural
* `foldmason_aa.fa` → alineamiento múltiple de secuencias
* `foldmason.png` → imagen de superposición
* `foldmason_MSA.png` → captura del alineamiento múltiple
* `foldmason.json` → metadatos

---

### 3. Envío a FoldSeek

Las estructuras resultantes fueron enviadas a FoldSeek para análisis estructural comparativo.

Se guardaron los reportes en formato `.m8` como evidencia del análisis.

---

### 4. Modificación del script para cálculo de RMSD

Se utilizó como base el código `prog3.1.py`, el cual implementa:

* Extracción de coordenadas Cα desde archivos PDB
* Superposición óptima mediante descomposición en valores singulares (SVD)
* Cálculo del RMSD

Se realizaron modificaciones para:

* Manejar residuos faltantes en los PDB
* Evitar errores por desalineación entre alineamiento y coordenadas reales
* Calcular el RMSD únicamente sobre posiciones alineadas y mapeables

---

## Pares analizados

Se seleccionaron tres pares representativos para evaluar la relación entre identidad de secuencia y similitud estructural.

---

## Resultados

| Par de dominios        | Posiciones comparadas | % Identidad | RMSD (Å) | Interpretación                                                                 |
| ---------------------- | --------------------- | ----------- | -------- | ------------------------------------------------------------------------------ |
| 3BT1cif_U vs 3BT2cif_U | 258                   | 99.22%      | **0.92** | Estructuras prácticamente idénticas.                                           |
| 3BRBcif_A vs 3BPRcif_C | 254                   | 97.64%      | **1.84** | Misma arquitectura global con variaciones locales.                             |
| 3BO8cif_A vs 3BEWcif_A | 248                   | 37.50%      | **2.94** | Conservan el pliegue β tipo inmunoglobulina con mayor divergencia estructural. |

---

## Análisis e interpretación

Se observa una relación directa entre identidad de secuencia y similitud estructural:

* Cuando la identidad es cercana al 100%, el RMSD es menor a 1 Å.
* Con identidades aún altas (~97%), el RMSD aumenta ligeramente (~1.8 Å).
* Cuando la identidad disminuye (~37%), el RMSD aumenta (~3 Å), aunque el núcleo estructural del dominio inmunoglobulina permanece conservado.

Esto confirma que dentro de una misma superfamilia estructural puede existir divergencia significativa en secuencia, mientras se mantiene el mismo pliegue tridimensional general (β-sándwich característico del dominio inmunoglobulina).

---

## Conclusión

El ejercicio demuestra que:

1. El alineamiento estructural es una herramienta más robusta que el alineamiento de secuencia para identificar relaciones evolutivas distantes.
2. El RMSD es una métrica sensible a la divergencia estructural.
3. Existe una correlación clara entre identidad de secuencia y similitud estructural, aunque dominios con identidad moderada aún pueden conservar el mismo pliegue global.

La superfamilia inmunoglobulina ejemplifica cómo la estructura tridimensional puede conservarse incluso cuando la secuencia evoluciona considerablemente.
