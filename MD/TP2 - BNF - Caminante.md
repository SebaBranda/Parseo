# Parseo

# Lenguaje a crear: **Caminante**

## Objetivo
El objetivo de *Caminante* es ofrecer un lenguaje narrativo y simbólico para programar la exploración de los Backrooms.  
Permite describir de manera sencilla acciones, decisiones y repeticiones que ejecuta un "caminante" (agente) en un entorno extraño y hostil, brindando al programador una forma expresiva y temática de representar:

- **Detección de atributos**  
- **Interacción con entidades**  
- **Control de flujo**  

---

## Alcance
- **Usuarios**: Estudiantes, desarrolladores de lenguajes, investigadores de lenguajes narrativos/esotéricos y entusiastas de los Backrooms.  
- **Dominio**: Programación de agentes autónomos que interactúan con un entorno simulado.  
- **Paradigma**: Imperativo, con soporte para control de flujo secuencial, condicional e iterativo.  

**Limitaciones**:
- No soporta funciones definidas por el usuario.  
- No permite recursividad ni modularización explícita.  
- El alcance de variables es global/anidado estático.  

---

## Especificaciones léxicas
1. **Palabras reservadas**:  

`establece`, `detecta`, `a`, `en`, `y`, `guarda`,
`si`, `entonces`, `sino`, `repite`, `veces`, `mientras`,
`mover`, `interactuar_con`, `manifestar`, `transicionar_a`,
`mas`, `menos`, `multiplicado_por`, `dividido_por`,
`es`, `es_mayor_que`, `esta_presente_en`


2. **Identificadores**:  
- Secuencia de letras y dígitos, comenzando con letra.  
-- Puede incluir `_`.  
- Ejemplo: `luz_actual`, `nivel10`, `contador_ruido`.  

Nota: en el scanner estos se emiten como el token `IDENT`.

3. **Números**:  
- Enteros (`0`, `42`, `999`) y decimales (`3.14`).  

Nota: en el scanner estos se emiten como el token `NUM`.

4. **Cadenas de texto**:  
- Encerradas entre comillas dobles `"..."`.  
- Ejemplo: `"Sonriente"`, `"Nivel_Infinito"`.  

Nota: en el scanner estas se emiten como el token `CADENA`.

5. **Símbolos especiales**:  
- `:` → inicio de bloque en ciclos  
- `,` → separador en condicionales  

Nota: los símbolos `:` y `,` son emitidos como tokens `COLON` y `COMMA` respectivamente.

6. **Comentarios** *(opcional)*:  
- `// comentario` o `# comentario`  

---

## Especificaciones sintácticas
Resumen de la gramática en BNF:

- **Programa**: Secuencia de instrucciones.  
- **Instrucción**:  
-- Declaración de atributo  
-- Condicional  
-- Ciclo  
-- Acción básica  
- **Condicional**:  
--si `<condicion>`, entonces `<bloque>` [sino `<bloque>`]
- **Ciclo**:  
--repite `<numero>` veces: `<bloque>`
--mientras `<condicion>`: `<bloque>`
- **Acciones**:  
--mover `<direccion>`
--interactuar_con `<entidad>`
--manifestar `<valor>`
--transicionar_a `<lugar>`
- **Expresiones numéricas**:  
-- `mas`, `menos`, `multiplicado_por`, `dividido_por`  

---

## Especificaciones semánticas
- **Tipado**:  
-- Débil y dinámico.  
- Los identificadores adquieren tipo (numérico o cadena) en tiempo de ejecución.  
-- `mas` → suma (números) o concatenación (texto).  

- **Alcance**:  
-- Global con anidación estática.  
-- Las variables definidas en un bloque son visibles en sub-bloques.  

- **Condicionales**:  
-- Evalúan expresiones lógicas.  
-- Ejecutan bloque `entonces` o `sino`.  

- **Bucles**:  
-- `repite` ejecuta N veces.  
-- `mientras` evalúa condición antes de cada iteración.  

- **Acciones básicas**:  
-- `mover`: cambia posición.  
-- `interactuar_con`: evento con entidad.  
-- `manifestar`: imprime o muestra valor.  
-- `transicionar_a`: cambia de nivel.  

- **Errores semánticos comunes**:  
-- Identificadores no definidos.  
-- Operaciones inválidas entre tipos.  
-- Referencias a entidades/lugares inexistentes.  

---

## AP

Imagen del Autómata de Pila generado para "Caminante".

<img width="750" height="349" alt="image" src="https://github.com/user-attachments/assets/82144063-a7af-44fc-811c-f068bccbfc8b" />



---
