# Productos finales que debe elaborar cada grupo

Cada grupo entrega productos físicos verificables.

## Producto 1 — Latiguillo / patch cord artesanal

Cada grupo debe fabricar:

1 latiguillo de aproximadamente 1 metro

RJ-45                         RJ-45
T568B                         T568B
   │                             │
   └──────── Cable UTP ──────────┘

La elaboración de aproximadamente 1 metro y la terminación T568B en ambos extremos.

Debe quedar:

T568B ───────────────── T568B

y el tester debe mostrar:

1 → 1
2 → 2
3 → 3
4 → 4
5 → 5
6 → 6
7 → 7
8 → 8

## Producto 2 — Cable cruzado

Para reforzar la comprensión de los estándares, cada grupo puede fabricar un segundo cable:

T568A ───────────────── T568B

Es decir:

EXTREMO A          EXTREMO B

T568A               T568B

Esto permitirá que los estudiantes comprendan físicamente la diferencia entre:

cable directo
cable cruzado.

El cable directo como A-A o B-B y el cruzado como A-B. También aclara que muchos equipos modernos soportan Auto-MDI/MDI-X.

## Producto 3 — Terminación en Keystone

Cada grupo debe realizar:

Cable UTP
    │
    ▼
┌───────────────┐
│    KEYSTONE   │
│    RJ-45      │
└───────────────┘
        │
        ▼
    FACEPLATE

La actividad requiere seleccionar el esquema indicado por el fabricante, colocar los conductores y utilizar la ponchadora tipo 110.

## Producto 4 — Punto de red

Finalmente, recomiendo que cada grupo arme un pequeño punto de red demostrativo:

             CABLEADO HORIZONTAL

 PC
 │
 │ Patch Cord
 ▼
KEYSTONE
 │
 │ Cable UTP
 ▼
PATCH PANEL
 │
 │ Patch Cord
 ▼
SWITCH

Este es justamente el esquema planteado en el laboratorio.

## Producto 5 — Cable con falla intencional

Este producto puede ser muy bueno para evaluar comprensión.

Un grupo fabrica deliberadamente un cable defectuoso, por ejemplo:

T568B ─────────────── T568B
           ↑
      pin incorrecto

Otro grupo deberá utilizar el tester para descubrir:

qué pin está mal;
cuál es la falla;
cuál podría ser la causa;
cómo solucionarla.

El README contempla fallas como conductor abierto, posición incorrecta, cortocircuito, par invertido, orden incorrecto y mala crimpación.
