## Componentes del AFD
El autómata se define por sus estados, su alfabeto y sus transiciones.

### Estados (Q):

- S0: Estado inicial.

- S ID/KW: Para leer identificadores o palabras clave.

- S NUM ENT: Para leer la parte entera de un número.

- S NUM DEC: Para leer la parte decimal de un número.

- S CADENA: Para leer cadenas de texto.

- S COMENT LINEA: Para ignorar comentarios de línea.

- S FIN: Estado de aceptación final para todos los tokens.

- S ERROR: Estado de error para caracteres no válidos.

### Alfabeto de Entrada (Σ):

- Letras (a-z, A-Z).

- Dígitos (0-9).

- Guion bajo (_).

- Comillas dobles (").

- Barra inclinada (/).

- Almohadilla (#).

- Dos puntos (:).

- Coma (,).

- Espacios en blanco, tabuladores, saltos de línea.

- Otros caracteres.

### Transiciones (δ): 
Las transiciones se basan en el carácter actual y el estado en el que se encuentra el autómata. El proceso es determinista; para cada estado y carácter, solo hay una transición posible.

### Estados y Transiciones del Autómata
- Estado Inicial (S 0)

    - Enfoque: Aquí comienza el análisis. El autómata determina qué tipo de token se está formando.

    - Transiciones:

        - Si lee una letra o _ → va a S D/KW.
        - Si lee un dígito → va a S NUM ENT.

        - Si lee " → va a S CADENA.

        - Si lee : → va al estado final, emite el token COLON y regresa a S 0.

        - Si lee , → va al estado final, emite el token COMMA y regresa a S 0.

        - Si lee // o # → va a S COMENT LINEA.

        - Si lee un espacio en blanco (o tabulador, salto de línea) → se queda en S 0 (ignora los espacios).

        - Cualquier otro carácter → va a S ERROR.

### Estado de Identificadores y Palabras Clave (S ID/KW)

- Enfoque: Se ha iniciado la lectura de un identificador. Este estado continúa leyendo hasta que el patrón se rompe.

- Transiciones:

    - Si lee una letra, dígito o _ → se queda en S ID/KW (continúa leyendo el identificador).

    - Si lee cualquier otro carácter → el identificador o palabra clave ha terminado. Se detiene, compara la cadena leída con la lista de palabras reservadas, emite el token apropiado (IDENTIFIER o KEYWORD_...), y regresa a S 0.

### Estado de Número Entero (S NUM ENT)

- Enfoque: Se ha iniciado la lectura de un número. Se encarga de los dígitos y el punto decimal.

- Transiciones:

    - Si lee un dígito → se queda en S NUM ENT.

    - Si lee . → va a S NUM DEC.

    - Si lee cualquier otro carácter → el número ha terminado. Se detiene, emite el token NUMBER, y regresa a S 0.

### Estado de Número Decimal (S NUM DEC)

- Enfoque: Se está leyendo la parte decimal del número.

- Transiciones:

    - Si lee un dígito → se queda en S NUM DEC.

    - Si lee cualquier otro carácter → el número decimal ha terminado. Se detiene, emite el token NUMBER, y regresa a S 0.

### Estado de Cadena de Texto (S CADENA)

- Enfoque: Se está leyendo una cadena de texto.

- Transiciones:

    - Si lee cualquier carácter excepto " → se queda en S CADENA.

    - Si lee " → la cadena ha terminado. Se detiene, emite el token STRING, y regresa a S 0.

    - Si llega al final del archivo sin leer la comilla de cierre → va a S ERROR.

### Estado de Comentario (S COMENT LINEA)

- Enfoque: El autómata ignora todos los caracteres hasta que encuentra un salto de línea.

- Transiciones:

    - Si lee cualquier carácter excepto un salto de línea (\n) → se queda en S COMENT LINEA.

    - Si lee un salto de línea → se detiene (el comentario ha terminado) y regresa a S 0.

### Estados Finales (Implícitos)

- Para cada tipo de token (IDENTIFIER, NUMBER, STRING, KEYWORD_..., COLON, COMMA), existe un estado final (o de aceptación). La transición a este estado indica que se ha reconocido un token válido.

### Funcionamiento del Proceso
El escáner, al usar este autómata, simula el recorrido de los estados. Comienza en S 0 ​y avanza un carácter a la vez. 

Cada transición de estado "consume" un carácter. 

Cuando una secuencia de caracteres lleva al autómata a un estado donde el siguiente carácter lo hace regresar a S 0​, el autómata ha identificado un token completo. 

En ese momento, el escáner "emite" el token y el proceso se repite desde S 0 para el siguiente.

---

### **Tabla de Transición de Estados para Caminante**

| **Estado (Q)** | **Letra** | **Dígito (0-9)** | **"** | **_** | **:** | **,** | **/** | **#** | **Espacio/Salto de línea** | **Otros** | **Token** | **Retorno** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **0 (Inicial)** | 1 | 2 | 3 | 1 | 4 | 5 | 6 | 6 | 0 | **Error** | - | - |
| **1 (ID/KW)** | 1 | 1 | **Error** | 1 | **Error** | **Error** | **Error** | **Error** | 0 | **Error** | **ID/KW** | 1 |
| **2 (Número)** | **Error** | 2 | **Error** | **Error** | **Error** | **Error** | **Error** | **Error** | 0 | **Error** | **NÚMERO** | 1 |
| **3 (Cadena)** | 3 | 3 | **0** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | **CADENA** | 1 |
| **4** | - | - | - | - | - | - | - | - | - | - | **COLON** | 0 |
| **5** | - | - | - | - | - | - | - | - | - | - | **COMMA** | 0 |

| **6 (Comentario)** | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | **0** | 6 | - | - |

---

Implementación del scanner

El código de implementación del scanner se mantiene como archivo separado y canonico: `caminante_lex.py`.
Para evitar inconsistencias, no mantengas una copia completa del código dentro de esta documentación. Si necesitas ver o modificar el lexer, edita `caminante_lex.py` directamente.

Ejecuta el scanner de prueba con:

```powershell
python .\caminante_lex.py
```

---

## Mapeo canónico de tokens (recomendado)

Para evitar discrepancias entre el scanner y el parser, sugerimos el siguiente mapeo canonical entre lexemas y nombres de tokens (mayúsculas usadas por el parser):

| Lexema / patrón | Token (nombre) | Notas |
|---|---:|---|
| `inicio` | `INICIO` | marca inicio del programa |
| `fin` | `FIN` | marca fin del programa |
| `mover` | `MOVER` | instrucción de movimiento |
| `norte`, `sur`, `este`, `oeste` | `NORTE`, `SUR`, `ESTE`, `OESTE` | literales de dirección |
| `manifestar` | `MANIFESTAR` | acción de salida |
| `si`, `entonces`, `sino` | `SI`, `ENTONCES`, `SINO` | control condicional |
| `mientras`, `hacer`, `finmientras` | `MIENTRAS`, `HACER`, `FINMIENTRAS` | control iterativo (forma larga) |
| `repite`, `veces` | `REPETIR`, `VECES` | alternativa: `repite N veces:` |
| `es_mayor_que`, `es_menor_que`, `igual`, `distinto`, `es` | `ES_MAYOR_QUE`, `ES_MENOR_QUE`, `IGUAL`, `DISTINTO`, `ES` | comparadores |
| identificadores (regex) | `IDENT` | p.ej. `ruido_ambiente` |
| números (entero/decimal) | `NUM` | p.ej. `50`, `3.14` |
| cadenas entre comillas | `CADENA` | p.ej. `"Hola"` |
| `:` | `COLON` | separador / inicio de bloque en la sintaxis `repite` |
| `,` | `COMMA` | separador en condicionales |

Notas:
- Usar tokens en mayúsculas hace que el parser escrito con PLY (yacc) coincida con las producciones GRAMATICALES (p. ej. `program : INICIO bloque FIN`).
- Normalizar los nombres (por ejemplo `NUM` vs `NUMBER` o `CADENA` vs `STRING`) evita confusiones; el scanner de referencia usa `NUM` y `CADENA`.
