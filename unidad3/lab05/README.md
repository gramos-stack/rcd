# Programa - Laboratorio 07

Este repositorio contiene el desarrollo de nuestro proyecto para el *Laboratorio 07* del curso de Redes. Diseñamos y desarrollamos una aplicación interactiva en *Python* con interfaz gráfica (GUI) utilizando *Tkinter* para realizar cálculos de subneteo IPv4. La primera versión usó la técnica *FLSM (Fixed Length Subnet Mask)* y la versión actual implementa *VLSM (Variable Length Subnet Mask)*.

---

## Integrantes

- Geraldine Ramos Zegarra
- Gian Piero Morales Tisnado

---

## Evolución del proyecto

| Versión | Técnica | Descripción |
|---|---|---|
| Inicial | FLSM | Divide la red en subredes **del mismo tamaño** según la cantidad de subredes y hosts. |
| Actual | VLSM | Asigna a cada subred un **tamaño distinto**, según los hosts que necesita. |

El historial de commits muestra paso a paso los cambios hechos para pasar de FLSM a VLSM.

---

## ¿De qué trata nuestro proyecto?

Nuestra aplicación recibe como entrada una dirección IP base con su prefijo y la lista de hosts que necesita cada subred, separados por comas (por ejemplo `100,50,25,2,2`). A partir de estos datos, el programa calcula automáticamente:

- El bloque más pequeño (prefijo CIDR) que soporta los hosts de cada subred.
- Los *bits prestados* y los bits de host de cada subred.
- La máscara de red de cada subred (en notación CIDR, decimal y binaria) y su respectiva *wildcard*.
- La verificación matemática de que todos los bloques caben dentro de la red principal.
- La tabla detallada de cada subred creada (Dirección de Red, Host Inicial, Host Final y Broadcast).
- Las direcciones que quedan libres al final.

---

## ¿Qué es VLSM y cómo lo aplicamos?

En FLSM todas las subredes tienen el mismo tamaño, lo que desperdicia direcciones cuando las subredes necesitan cantidades distintas de hosts. VLSM resuelve esto asignando a cada subred el bloque más pequeño que le sirva.

El algoritmo que implementa el programa sigue estos pasos:

1. **Leer** la red principal y la lista de hosts por subred.
2. **Ordenar** los requisitos de mayor a menor cantidad de hosts.
3. **Calcular** para cada uno el bloque mínimo, es decir, el menor tamaño donde `2^n - 2` sea mayor o igual a los hosts pedidos (se reservan la dirección de red y la de broadcast).
4. **Verificar** que la suma de todos los bloques quepa en la red principal.
5. **Asignar** los bloques de forma consecutiva y alineada, empezando en la dirección de red.
6. **Mostrar** los resultados de cada subred y el espacio libre restante.

---

## Ejemplo

Entrada: `192.168.10.0/24` con hosts `100,50,25,2,2`

| Subred | Hosts pedidos | Red | Máscara | Rango de hosts | Broadcast |
|---|---|---|---|---|---|
| 1 | 100 | 192.168.10.0/25 | 255.255.255.128 | .1 a .126 | 192.168.10.127 |
| 2 | 50 | 192.168.10.128/26 | 255.255.255.192 | .129 a .190 | 192.168.10.191 |
| 3 | 25 | 192.168.10.192/27 | 255.255.255.224 | .193 a .222 | 192.168.10.223 |
| 4 | 2 | 192.168.10.224/30 | 255.255.255.252 | .225 a .226 | 192.168.10.227 |
| 5 | 2 | 192.168.10.228/30 | 255.255.255.252 | .229 a .230 | 192.168.10.231 |

Direcciones libres: 24 (de 192.168.10.232 a 192.168.10.255).

---

## Validaciones del programa

La aplicación muestra un mensaje de error claro cuando:

- La IP o el prefijo no tienen un formato válido.
- La lista de hosts está vacía, tiene texto en lugar de números o incluye valores menores que 1.
- Algún requisito es más grande que la red principal.
- La suma de los bloques necesarios no cabe en la red principal.

---

## ¿Cómo ejecutar nuestro programa?

### Requisitos

Solo se necesita tener *Python 3* instalado en la computadora. No requiere la instalación de librerías externas con pip, ya que utilizamos únicamente módulos nativos de Python (`ipaddress` y `tkinter`).

### Pasos para ejecutar:

1. Descargar o clonar este repositorio en el equipo.

2. Abrir una terminal o consola de comandos en la carpeta del proyecto.

3. Ejecutar el siguiente comando:

```bash
python sistema_subneteo_ipv4.py
```

4. En la ventana, escribir la **IP principal con su prefijo** (por ejemplo `192.168.10.0/24`) y los **hosts por subred separados por coma** (por ejemplo `100,50,25,2,2`).

5. Presionar **CALCULAR SUBNETEO** para ver los resultados.
## EJECUCION VLSM
![opcional](img/captura1.png)
![opcional](img/captura2.png)
![opcional](img/captura3.png)
![opcional](img/captura4.png)
