# GRUPO 1 — Cableado estructurado y componentes
Tema: "Introducción al cableado estructurado y componentes de una red LAN"

## 1. ¿Qué es cableado estructurado?

Es un sistema organizado de:

- cables;
- conectores;
- puntos de red;
- patch panels;
- patch cords;
- racks;
- dispositivos de red.

## Su objetivo es conseguir una infraestructura:

- ordenada;
- escalable;
- administrable;
- mantenible.

## 2. Componentes

Deben explicar físicamente:

- Cable UTP
  - Medio físico formado por pares de conductores trenzados.
- RJ-45
  - Conector utilizado para terminar el cable.
- Patch cord
  - Cable utilizado para conectar dispositivos.
- Keystone
  - Módulo donde se termina un cable de red.
- Faceplate
  - Placa donde se instala el Keystone.
- Patch panel
  - Elemento donde se organizan las terminaciones provenientes del cableado.
- Switch
  - Interconecta dispositivos dentro de una LAN.
- Tester
  - Permite comprobar continuidad y correspondencia de los conductores.

# GRUPO 2 — Cable UTP, pares trenzados y categorías
Tema: "Cable UTP y transmisión de datos"

UTP significa: Unshielded Twisted Pair

o: Par Trenzado No Blindado.

Un cable convencional contiene cuatro pares:

| Par | Colores                  |
| --- | ------------------------ |
| 1   | Blanco/Naranja – Naranja |
| 2   | Blanco/Verde – Verde     |
| 3   | Blanco/Azul – Azul       |
| 4   | Blanco/Marrón – Marrón   |


## ¿Por qué están trenzados?

El trenzado ayuda a reducir:

- interferencias electromagnéticas;
- diafonía;
- ruido.
- Categorías

Explicar al menos:

| Categoría | Característica general                                         |
| --------- | -------------------------------------------------------------- |
| Cat 5e    | Ethernet hasta 1 Gb/s en condiciones apropiadas                |
| Cat 6     | Mejores características frente a interferencias                |
| Cat 6A    | Diseñada para 10 Gb/s hasta 100 m en condiciones especificadas |


La velocidad real también depende de longitud, componentes, instalación y equipos.


# GRUPO 3 — T568A, T568B y cables Ethernet
Tema: "Normas de terminación y elaboración de cables de red"

Este debería ser uno de los grupos más importantes.

T568A
1  Blanco/Verde
2  Verde
3  Blanco/Naranja
4  Azul
5  Blanco/Azul
6  Naranja
7  Blanco/Marrón
8  Marrón

T568B
1  Blanco/Naranja
2  Naranja
3  Blanco/Verde
4  Azul
5  Blanco/Azul
6  Verde
7  Blanco/Marrón
8  Marrón

Truco para memorizar T568B
BN
N
BV
A
BA
V
BM
M

Es decir:

Blanco Naranja
Naranja
Blanco Verde
Azul
Blanco Azul
Verde
Blanco Marrón
Marrón

Cable directo
T568B ───────── T568B

o:

T568A ───────── T568A
Cable cruzado
T568A ───────── T568B

Ordenar físicamente ocho hilos delante de sus compañeros.
Después deberá introducirlos en un RJ-45.

# GRUPO 4 — Crimpación, ponchado y tester
Tema: "Conectorización y comprobación de cables de red"

Este grupo debe enseñar cómo fabricar físicamente el cable.

Procedimiento
Paso 1

Cortar aproximadamente:

1 metro
Paso 2

Retirar:

2–3 cm

de cubierta.

Paso 3

Separar los pares.

Paso 4

Ordenar según T568B:

BN
N
BV
A
BA
V
BM
M
Paso 5

Alinear.

Paso 6

Cortar uniformemente.

Paso 7

Introducir en RJ-45.

Los ocho conductores deben llegar hasta el extremo.

Paso 8

Comprobar que la cubierta entre en la zona de sujeción.

Paso 9

Crimpar.

Paso 10

Repetir en el otro extremo.

El procedimiento está descrito paso a paso en el laboratorio.

Tester

Mostrar:

MASTER                  REMOTE

  1 ───────────────────── 1
  2 ───────────────────── 2
  3 ───────────────────── 3
  4 ───────────────────── 4
  5 ───────────────────── 5
  6 ───────────────────── 6
  7 ───────────────────── 7
  8 ───────────────────── 8

  
¿Qué significa un error?

Por ejemplo:

1 → 1
2 → 2
3 → 6
4 → 4
5 → 5
6 → 3
7 → 7
8 → 8

Esto indica que existe una alteración en el orden de los conductores.

# GRUPO 5 — Keystone, punto de red y conectividad
Tema: 
"Implementación y prueba de un punto de red"

Este grupo debe explicar cómo pasar de un simple cable a una instalación estructurada.

Keystone

Explicar:

Cable UTP
     │
     ▼
┌─────────┐
│ KEYSTONE│
└─────────┘
     │
     ▼
FACEPLATE

La terminación se realiza utilizando una ponchadora tipo 110.

Punto de red

Explicar:

PC
 │
 │ Patch Cord
 ▼
Keystone
 │
 │ UTP
 ▼
Patch Panel
 │
 │ Patch Cord
 ▼
Switch

Prueba de conectividad

En Linux:

ip addr

para consultar las interfaces.

También:

ip link

para revisar el estado del enlace.

Y:

ping 192.168.1.20

para comprobar conectividad con otro equipo.
