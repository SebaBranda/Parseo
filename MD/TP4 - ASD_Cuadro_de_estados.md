## Análisis Sintáctico Descendente con Retroceso (ASDB)

Conceptos
Consiste en recorrer el árbol de izquierda a derecha y de arriba abajo de manera que para la sentencia a analizar, se la compara con cada nodo del árbol que va recorriendo y en el caso de que los terminales a la izquierda del primer no terminal no coincidan, se termina la búsqueda por esa rama y se vuelve hacia atrás para buscar otra rama
Problema: ineficiente

Ejemplo
 
- INICIO -> MOVER NORTE FIN

| **Pila**         | **Entrada**              | **Transición**                               |
| :--------------- | :----------------------- | :------------------------------------------- |
| λ                | INICIO MOVER NORTE FIN λ | δ(q0, λ, λ) = (q1, λ)                        |
| λ                | INICIO MOVER NORTE FIN λ | δ(q1, λ, λ) = (q2, $S)                       |
| $S               | INICIO MOVER NORTE FIN λ | δ(q2, INICIO, λ) = (q2, λ)                   |
| $S               | MOVER NORTE FIN λ        | δ(q2, λ, S) = (q2, INSTRUCCIONES)            |
| $INSTRUCCIONES   | MOVER NORTE FIN λ        | δ(q2, λ, INSTRUCCIONES) = (q2, INSTRUCCION)  |
| $INSTRUCCION     | MOVER NORTE FIN λ        | δ(q2, λ, INSTRUCCION) = (q2, MOVIMIENTO)     |
| $MOVIMIENTO      | MOVER NORTE FIN λ        | δ(q2, λ, MOVIMIENTO) = (q2, DIRECCION MOVER) |
| $DIRECCION MOVER | MOVER NORTE FIN λ        | δ(q2, MOVER, MOVER) = (q2, λ)                |
| $DIRECCION       | NORTE FIN λ              | δ(q2, NORTE, DIRECCION) = (q2, λ)            |
| $                | FIN λ                    | δ(q2, FIN, λ) = (q3, λ)                      |
| λ                | λ                        | δ(q3, λ, $) = (q3, λ)                        |
| λ                | λ                        |  **accept**                                  |

