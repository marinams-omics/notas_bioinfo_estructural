### **1. Fundamentos y el Paradigma de la Biología Estructural**

*   **Relación Secuencia-Estructura-Función:** Las proteínas y los ácidos nucleicos son los canales principales de información genómica. El principio fundamental es que la **función biológica está íntimamente ligada a la estructura tridimensional**. 
*   **Conformación Nativa:** Es la forma 3D estable que adopta una molécula para funcionar, sostenida por interacciones no covalentes.
*   **Proteínas intrínsecamente desordenadas:** Se ha descubierto que existen proteínas que no tienen una estructura plegada fija pero que cumplen funciones celulares importantes, a menudo plegándose solo al unirse a sus ligandos.
*   **Componentes Químicos:** 
    *   **Proteínas:** Polímeros de aminoácidos unidos por **enlaces peptídicos**. Su geometría se define por los ángulos diedros **$\phi$ (fi) y $\psi$ (psi)** del esqueleto.
    *   **Ácidos Nucleicos:** Polímeros de nucleótidos unidos por **enlaces fosfodiéster**.

### **2. Interacciones No Covalentes**
Son fuerzas débiles pero cruciales para la estabilidad estructural:
*   **Interacciones hidrofóbicas:** Repulsión de sustancias por el agua en soluciones acuosas.
*   **Fuerzas de van der Waals:** Atracciones entre átomos no cargados.
*   **Interacciones electrostáticas:** Incluyen los **puentes salinos** en proteínas.
*   **Puentes de Hidrógeno:** Cruciales tanto para las hélices y láminas en proteínas como para el emparejamiento de bases en el ADN.

### **3. Niveles de Organización Estructural**

*   **Estructura Primaria:** La secuencia lineal de monómeros. En genes, las mutaciones pueden ser **sinónimas** (no cambian el aminoácido), **missense** (cambian el aminoácido) o **nonsense** (introducen un stop prematuro).
*   **Estructura Secundaria:** Patrones locales de plegamiento.
    *   **Proteínas:** Principalmente **hélices-$\alpha$** y **láminas-$\beta$**. El algoritmo **DSSP** se usa para clasificar estos estados (H para hélice, E para lámina, C para azar/coil).
    *   **Ácidos Nucleicos:** Basada en el emparejamiento (A-T/U y G-C). El ARN forma estructuras complejas como tallos (*stems*) y bucles (*loops*).
*   **Estructura Terciaria:** Plegamiento global en **dominios** compactos con núcleos hidrofóbicos. Se puede representar mediante **matrices de contactos** (*contact maps*).
*   **Estructura Cuaternaria:** Asociación de múltiples cadenas para formar una unidad funcional (ej. hemoglobina).
*   **Conservación:** Durante la evolución, **la estructura se conserva mucho más que la secuencia** primaria. La divergencia estructural se mide habitualmente mediante el **RMSD** (desviación media cuadrática).

### **4. Métodos Experimentales y Datos**

*   **Determinación de Estructuras:** Los métodos clave incluyen la **cristalografía de rayos X** (estática, alta calidad), **NMR** (útil para dinámica y flexibilidad) y la **microscopía crio-electrónica** (para grandes complejos moleculares).
*   **Protein Data Bank (PDB):** Es el repositorio mundial de coordenadas 3D. Actualmente, el formato estándar es **mmCIF**, que reemplazó al antiguo formato .pdb para manejar mejor estructuras grandes y complejas.

### **5. El Proceso de Plegamiento (Folding)**

*   **Experimento de Anfinsen:** Demostró que el plegamiento depende exclusivamente de la secuencia (al menos en proteínas pequeñas).
*   **Fuerzas Impulsoras:** El plegamiento está guiado principalmente por la **hidrofobicidad** y la formación de **puentes de hidrógeno**.
*   **Paradoja de Levinthal:** Si una proteína buscara su conformación nativa de forma aleatoria, tardaría más que la edad del universo; por tanto, el plegamiento debe ser un **proceso por etapas, no aleatorio**, dirigido por un "embudo de energía" (*folding funnel*).
*   **Velocidad de Plegamiento:** Se puede estimar mediante el **orden de contactos (CO)** (distancia promedio en la secuencia entre residuos en contacto) o el contenido de estructura secundaria.

### **6. Modelado y Dinámica**

*   **Modelos de Red (HP):** Simplifican los aminoácidos en solo dos tipos, **Hidrofóbicos (H) y Polares (P)**, para estudiar los principios del plegamiento en mallas 2D o 3D.
*   **Dinámica Molecular (MD):** Simulaciones que utilizan **campos de fuerza** para calcular el movimiento y la energía de cada átomo en intervalos de picosegundos.
*   **Modelos Aproximados:** Métodos heurísticos que predicen estructura secundaria o desorden basándose en información evolutiva (alineamientos múltiples).
*   **Foldit:** Una herramienta de **gamificación** que permite a usuarios humanos manipular manualmente estructuras de proteínas para resolver problemas de plegamiento.

