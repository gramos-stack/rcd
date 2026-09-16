# LABORATORIO: CABLEADO ESTRUCTURADO

## 1. Datos generales

| Campo           | Información                                                |
| --------------- | ---------------------------------------------------------- |
| **Curso**       | Redes de Computadoras / Redes y Comunicaciones de Datos    |
| **Laboratorio** | Cableado Estructurado                                      |
| **Duración**    | 2 a 3 horas                                                |
| **Modalidad**   | Presencial – Práctica                                      |
| **Trabajo**     | Individual o por parejas                                   |
| **Nivel**       | Pregrado – Ingeniería de Sistemas / Ingeniería de Software |

---

# 2. Descripción

En este laboratorio el estudiante implementará físicamente un enlace básico de red utilizando cableado de par trenzado, aplicando criterios de cableado estructurado y las normas de distribución de pares para conectores RJ-45.

El estudiante realizará el reconocimiento de los componentes, preparación del cable UTP, conectorización, elaboración de un cable de red, pruebas de continuidad y diagnóstico de errores.

Finalmente, se realizará la conexión de dispositivos de red mediante el cable elaborado y se verificará su funcionamiento.

---

# 3. Competencia

Implementa y verifica infraestructura básica de redes de comunicaciones aplicando principios técnicos, normas de cableado estructurado, procedimientos de conectorización y métodos de comprobación de conectividad.

---

# 4. Resultados de aprendizaje

Al finalizar el laboratorio, el estudiante será capaz de:

* Identificar los principales componentes de un sistema de cableado estructurado.
* Reconocer las categorías y características de los cables de par trenzado.
* Diferenciar los estándares T568A y T568B.
* Preparar correctamente un cable UTP.
* Instalar conectores RJ-45.
* Elaborar cables de red de acuerdo con un estándar determinado.
* Utilizar un tester de cableado.
* Identificar errores de conectorización.
* Corregir fallas en un cable de red.
* Verificar la conectividad entre dispositivos.

---

# 5. Objetivos

## 5.1 Objetivo general

Implementar y comprobar un enlace básico de red mediante cableado de par trenzado, aplicando procedimientos de cableado estructurado y estándares de terminación RJ-45.

## 5.2 Objetivos específicos

1. Reconocer los componentes utilizados en una instalación de cableado estructurado.
2. Identificar los pares y conductores de un cable UTP.
3. Aplicar correctamente la distribución de colores T568A y T568B.
4. Elaborar un cable de red con conectores RJ-45.
5. Comprobar la continuidad de los conductores.
6. Detectar errores de conexión mediante un tester.
7. Corregir errores de cableado.
8. Comprobar la conectividad entre equipos.

---

# 6. Fundamento teórico

## 6.1 ¿Qué es el cableado estructurado?

El cableado estructurado es un sistema organizado de cables, conectores, dispositivos y elementos de distribución que permite transportar información dentro de una infraestructura de comunicaciones.

Una instalación estructurada busca que el cableado sea:

* Ordenado.
* Escalable.
* Fácil de administrar.
* Fácil de mantener.
* Independiente de los equipos específicos utilizados.
* Adecuado para diferentes servicios de red.

---

# 7. Componentes del cableado estructurado

Entre los principales componentes se encuentran:

| Componente     | Descripción                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| Cable UTP      | Medio físico compuesto por pares de conductores trenzados.                               |
| Conector RJ-45 | Conector utilizado para terminar cables de par trenzado.                                 |
| Patch cord     | Cable flexible utilizado para realizar conexiones entre dispositivos.                    |
| Patch panel    | Panel donde se terminan y organizan los cables provenientes de diferentes puntos de red. |
| Keystone       | Módulo utilizado para terminar un punto de red.                                          |
| Faceplate      | Placa que permite instalar uno o varios keystone.                                        |
| Rack           | Estructura utilizada para instalar y organizar equipos de comunicaciones.                |
| Tester         | Instrumento utilizado para comprobar continuidad y correspondencia de los conductores.   |
| Switch         | Dispositivo utilizado para interconectar equipos dentro de una red LAN.                  |

---

# 8. Cable UTP

UTP significa:

**Unshielded Twisted Pair**

En español:

**Par Trenzado No Blindado**

Un cable UTP convencional contiene cuatro pares de conductores:

1. Blanco/Naranja – Naranja
2. Blanco/Verde – Verde
3. Blanco/Azul – Azul
4. Blanco/Marrón – Marrón

Cada par está trenzado para reducir interferencias electromagnéticas y diafonía.

---

# 9. Categorías de cable

Algunas categorías utilizadas en redes Ethernet son:

| Categoría | Uso habitual                                                                       |
| --------- | ---------------------------------------------------------------------------------- |
| Cat 5e    | Redes Ethernet de hasta 1 Gbit/s en condiciones apropiadas                         |
| Cat 6     | Redes Ethernet de alta velocidad y mejores características frente a interferencias |
| Cat 6A    | Diseñada para soportar 10 Gbit/s hasta 100 metros en condiciones especificadas     |

> **Nota:** La velocidad real depende también de la longitud del enlace, calidad de los componentes, instalación y equipos utilizados.

---

# 10. Estándares T568A y T568B

Los estándares de terminación definen el orden de los ocho conductores dentro del conector RJ-45.

## 10.1 T568A

| Pin | Color          |
| --: | -------------- |
|   1 | Blanco/Verde   |
|   2 | Verde          |
|   3 | Blanco/Naranja |
|   4 | Azul           |
|   5 | Blanco/Azul    |
|   6 | Naranja        |
|   7 | Blanco/Marrón  |
|   8 | Marrón         |

## 10.2 T568B

| Pin | Color          |
| --: | -------------- |
|   1 | Blanco/Naranja |
|   2 | Naranja        |
|   3 | Blanco/Verde   |
|   4 | Azul           |
|   5 | Blanco/Azul    |
|   6 | Verde          |
|   7 | Blanco/Marrón  |
|   8 | Marrón         |

---

# 11. Cable directo y cable cruzado

## Cable directo

Utiliza el mismo estándar en ambos extremos.

Ejemplo:

```text
T568B                         T568B

1 Blanco/Naranja  ----------  1 Blanco/Naranja
2 Naranja         ----------  2 Naranja
3 Blanco/Verde    ----------  3 Blanco/Verde
4 Azul            ----------  4 Azul
5 Blanco/Azul     ----------  5 Blanco/Azul
6 Verde           ----------  6 Verde
7 Blanco/Marrón   ----------  7 Blanco/Marrón
8 Marrón          ----------  8 Marrón
```

También puede utilizarse:

```text
T568A <----------> T568A
```

## Cable cruzado

Utiliza un estándar diferente en cada extremo:

```text
T568A <----------> T568B
```

En equipos Ethernet modernos, la función **Auto-MDI/MDI-X** permite que muchos dispositivos detecten automáticamente este tipo de conexión, por lo que los cables directos son suficientes para la mayoría de conexiones actuales.

---

# 12. Materiales

Cada grupo deberá disponer de:

* Cable UTP Cat 5e o superior.
* Conectores RJ-45.
* Capuchones para RJ-45, opcional.
* Patch cord comercial.
* Keystone RJ-45.
* Faceplate.
* Patch panel, si está disponible.
* Tester de cable de red.
* Switch.
* Computadoras o laptops.
* Alicate de corte.
* Crimpadora RJ-45.
* Ponchadora tipo 110.
* Pelacables.
* Regla o cinta métrica.
* Etiquetas.
* Organizador de cables, opcional.

---

# 13. Normas de seguridad

Antes de iniciar el laboratorio:

* Mantener limpia y ordenada el área de trabajo.
* Manipular la crimpadora con cuidado.
* No dirigir las herramientas de corte hacia otra persona.
* No dejar restos de cable en el área de trabajo.
* Mantener los conectores y herramientas organizados.
* No manipular equipos eléctricos con las manos húmedas.
* Desconectar los equipos antes de realizar modificaciones físicas.
* Utilizar correctamente las herramientas proporcionadas.
* No forzar conectores RJ-45 dentro de los puertos de red.

---

# 14. PARTE I — Reconocimiento de componentes

## Actividad

Identifique físicamente los componentes proporcionados por el docente.

Complete la siguiente tabla:

| N.º | Componente  | Función | Características |
| --: | ----------- | ------- | --------------- |
|   1 | Cable UTP   |         |                 |
|   2 | RJ-45       |         |                 |
|   3 | Keystone    |         |                 |
|   4 | Patch panel |         |                 |
|   5 | Patch cord  |         |                 |
|   6 | Tester      |         |                 |
|   7 | Crimpadora  |         |                 |
|   8 | Ponchadora  |         |                 |
|   9 | Switch      |         |                 |

### Evidencia

Tomar fotografías de los componentes identificados.

---

# 15. PARTE II — Identificación del cable UTP

Seleccione un segmento de cable UTP.

### Procedimiento

1. Retire aproximadamente 3 cm de la cubierta exterior.
2. Identifique los cuatro pares.
3. Separe cuidadosamente los conductores.
4. Identifique los colores.
5. Evite desenrollar innecesariamente los pares.

Complete:

| Par   | Conductor 1 | Conductor 2 |
| ----- | ----------- | ----------- |
| Par 1 |             |             |
| Par 2 |             |             |
| Par 3 |             |             |
| Par 4 |             |             |

### Pregunta

¿Por qué los conductores se encuentran trenzados?

**Respuesta:**

..............................................................................

..............................................................................

---

# 16. PARTE III — Elaboración de un cable de red

## Material

* Cable UTP.
* 2 conectores RJ-45.
* Crimpadora.
* Pelacables.
* Alicate de corte.
* Tester.

## Procedimiento

### Paso 1 — Cortar el cable

Corte un segmento de aproximadamente:

```text
1 metro
```

El docente puede establecer otra longitud.

### Paso 2 — Retirar la cubierta

Retire aproximadamente 2 a 3 cm de la cubierta exterior.

No retire una longitud excesiva.

### Paso 3 — Separar los pares

Desenrolle cuidadosamente los conductores necesarios para organizarlos.

### Paso 4 — Ordenar los conductores

Para este laboratorio se utilizará **T568B**.

Ordene los conductores:

```text
1. Blanco/Naranja
2. Naranja
3. Blanco/Verde
4. Azul
5. Blanco/Azul
6. Verde
7. Blanco/Marrón
8. Marrón
```

### Paso 5 — Alinear los conductores

Alinee los ocho conductores de izquierda a derecha.

Verifique nuevamente el orden antes de introducirlos en el conector.

### Paso 6 — Cortar los conductores

Realice un corte uniforme para que todos tengan aproximadamente la misma longitud.

### Paso 7 — Introducir los conductores

Introduzca los ocho conductores en el conector RJ-45.

Verifique que:

* Los ocho conductores lleguen hasta el extremo del conector.
* El orden sea correcto.
* La cubierta exterior quede dentro de la zona de sujeción del conector.

### Paso 8 — Crimpar

Introduzca el conector en la crimpadora y realice la presión necesaria para fijar los conductores.

### Paso 9 — Repetir

Repita el procedimiento en el segundo extremo.

Utilice:

```text
T568B
```

en ambos extremos.

Por tanto:

```text
T568B <----------------> T568B
```

---

# 17. PARTE IV — Verificación visual

Antes de utilizar el tester, realice una inspección visual.

Compruebe:

* [ ] Los ocho conductores están presentes.
* [ ] El orden de colores es correcto.
* [ ] Los conductores llegan hasta el extremo del RJ-45.
* [ ] La cubierta exterior está sujeta.
* [ ] El conector no presenta daños.
* [ ] No existen conductores fuera de posición.
* [ ] Ambos extremos utilizan T568B.

---

# 18. PARTE V — Prueba con tester

Conecte cada extremo del cable al tester.

Encienda el dispositivo y observe la secuencia de los indicadores.

Un cable correctamente conectado debe mostrar correspondencia:

```text
1 → 1
2 → 2
3 → 3
4 → 4
5 → 5
6 → 6
7 → 7
8 → 8
```

Registre el resultado:

| Pin | Resultado |
| --: | --------- |
|   1 |           |
|   2 |           |
|   3 |           |
|   4 |           |
|   5 |           |
|   6 |           |
|   7 |           |
|   8 |           |

### Resultado general

```text
Cable aprobado:   [   ]
Cable rechazado:  [   ]
```

---

# 19. PARTE VI — Diagnóstico de errores

El docente proporcionará o solicitará elaborar un cable con una falla intencional.

Algunos errores posibles:

* Conductor abierto.
* Conductor en posición incorrecta.
* Cortocircuito.
* Par invertido.
* Orden incorrecto.
* Conector mal crimpado.
* Conductor que no llega correctamente al conector.

## Actividad

Utilice el tester para identificar la falla.

Complete:

| Elemento            | Resultado |
| ------------------- | --------- |
| Falla detectada     |           |
| Pin afectado        |           |
| Posible causa       |           |
| Solución aplicada   |           |
| Resultado posterior |           |

---

# 20. PARTE VII — Terminación en Keystone

Ahora se realizará la terminación de un punto de red.

## Procedimiento

1. Corte el cable a la longitud requerida.
2. Retire cuidadosamente la cubierta.
3. Identifique los pares.
4. Seleccione el esquema indicado por el fabricante del keystone.
5. Organice los conductores.
6. Coloque cada conductor en su posición.
7. Utilice la ponchadora.
8. Corte los excedentes.
9. Coloque el keystone en el faceplate.

> **Importante:** En una instalación permanente se debe mantener el mismo esquema de terminación en ambos extremos del enlace, siguiendo el diseño y las especificaciones de la instalación.

---

# 21. PARTE VIII — Implementación de un punto de red

Construya el siguiente esquema:

```text
                 CABLEADO HORIZONTAL

┌─────────────┐                       ┌─────────────┐
│   SWITCH    │                       │  FACEPLATE  │
│             │                       │  KEYSTONE   │
└──────┬──────┘                       └──────┬──────┘
       │                                     │
       │ Patch Cord                          │
       │                                     │
       └─────── Patch Panel ─────────────────┘
                    |
                    |
              Cable UTP
                    |
                    |
              Punto de red
```

El estudiante deberá identificar cada componente y explicar su función.

---

# 22. PARTE IX — Prueba de conectividad

Conecte una computadora al punto de red.

Esquema:

```text
PC
 |
 | Patch Cord
 |
Keystone
 |
 | Cableado UTP
 |
Patch Panel
 |
 | Patch Cord
 |
Switch
```

Verifique:

1. Estado físico del enlace.
2. Indicadores LED del puerto.
3. Configuración de red del equipo.
4. Dirección IP.
5. Conectividad con otro equipo.

En Linux puede utilizar:

```bash
ip addr
```

Para consultar las interfaces de red:

```bash
ip link
```

Para comprobar conectividad:

```bash
ping <IP_DEL_OTRO_EQUIPO>
```

Ejemplo:

```bash
ping 192.168.1.20
```

---

# 23. Registro de resultados

Complete la siguiente tabla:

| Parámetro           | Resultado |
| ------------------- | --------- |
| Equipo 1            |           |
| Equipo 2            |           |
| Interfaz de red     |           |
| Dirección IP        |           |
| Máscara             |           |
| Gateway             |           |
| Estado del enlace   |           |
| Resultado del ping  |           |
| Pérdida de paquetes |           |

---

# 24. Actividad de análisis

Responda las siguientes preguntas.

### 1. ¿Cuál es la función del cableado estructurado?

..............................................................................

..............................................................................

### 2. ¿Cuál es la diferencia entre T568A y T568B?

..............................................................................

..............................................................................

### 3. ¿Qué diferencia existe entre un cable directo y uno cruzado?

..............................................................................

..............................................................................

### 4. ¿Por qué es importante mantener el orden de los conductores?

..............................................................................

..............................................................................

### 5. ¿Qué ocurre si un conductor está abierto?

..............................................................................

..............................................................................

### 6. ¿Qué información proporciona un tester de cableado?

..............................................................................

..............................................................................

### 7. ¿Cuál es la función de un patch panel?

..............................................................................

..............................................................................

### 8. ¿Cuál es la diferencia entre un patch cord y un cable de instalación?

..............................................................................

..............................................................................

### 9. ¿Por qué no se debe retirar excesivamente el trenzado de los pares?

..............................................................................

..............................................................................

### 10. ¿Qué factores pueden provocar problemas de conectividad en un cable UTP?

..............................................................................

..............................................................................

---

# 25. Reto de laboratorio

El docente entregará un cable que presenta una falla desconocida.

El estudiante deberá:

1. Probar el cable.
2. Registrar el resultado.
3. Identificar el pin o par afectado.
4. Formular una hipótesis sobre la causa.
5. Revisar físicamente el conector.
6. Corregir el problema.
7. Volver a realizar la prueba.
8. Documentar el procedimiento.

## Registro

```text
Falla encontrada:

________________________________________________

Diagnóstico:

________________________________________________

Corrección realizada:

________________________________________________

Resultado final:

________________________________________________
```

---

# 26. Evidencias

El estudiante deberá presentar:

### Evidencia 1

Fotografía de los materiales utilizados.

### Evidencia 2

Fotografía del cable UTP antes de la preparación.

### Evidencia 3

Fotografía de los conductores ordenados según T568B.

### Evidencia 4

Fotografía del conector RJ-45 terminado.

### Evidencia 5

Fotografía de la prueba con el tester.

### Evidencia 6

Fotografía del punto de red implementado.

### Evidencia 7

Captura del resultado del comando:

```bash
ip addr
```

### Evidencia 8

Captura del resultado de:

```bash
ping <IP>
```

### Evidencia 9

Fotografía o registro del diagnóstico y corrección de una falla.

---

# 27. Informe del laboratorio

El informe deberá contener:

```text
1. Portada

2. Objetivos

3. Materiales y herramientas

4. Fundamento teórico

5. Procedimiento

6. Resultados

7. Evidencias

8. Diagnóstico de fallas

9. Respuestas a las preguntas

10. Conclusiones

11. Recomendaciones
```

---

# 28. Conclusiones

El estudiante deberá elaborar como mínimo tres conclusiones relacionadas directamente con los resultados obtenidos.

Ejemplo de estructura:

```text
Conclusión 1:
________________________________________________

Conclusión 2:
________________________________________________

Conclusión 3:
________________________________________________
```

Las conclusiones deben estar relacionadas con las actividades realizadas y no limitarse a repetir la teoría.

---

# 29. Rúbrica de evaluación

| Criterio                        | Excelente                               | Bueno                         | En proceso                  | Puntaje |
| ------------------------------- | --------------------------------------- | ----------------------------- | --------------------------- | ------: |
| Identificación de componentes   | Identifica correctamente todos          | Identifica la mayoría         | Presenta dificultades       |       2 |
| Preparación del cable           | Procedimiento correcto y ordenado       | Presenta pequeños errores     | Requiere asistencia         |       2 |
| Conectorización RJ-45           | Correcta y limpia                       | Presenta pequeños defectos    | Presenta errores            |       3 |
| Uso del tester                  | Interpreta correctamente los resultados | Presenta alguna dificultad    | No interpreta correctamente |       2 |
| Diagnóstico de fallas           | Identifica y corrige la falla           | Identifica la falla           | Requiere asistencia         |       2 |
| Implementación del punto de red | Correcta                                | Presenta pequeños errores     | Incompleta                  |       3 |
| Prueba de conectividad          | Realizada correctamente                 | Presenta dificultades menores | No logra comprobarla        |       2 |
| Informe y evidencias            | Completo y ordenado                     | Presenta algunas omisiones    | Incompleto                  |       2 |
| **TOTAL**                       |                                         |                               |                             |  **18** |

---

# 30. Criterios de aprobación

Para considerar el laboratorio satisfactorio, el estudiante deberá:

* Implementar correctamente el cable solicitado.
* Aplicar correctamente el esquema de colores.
* Realizar la prueba con el tester.
* Identificar y corregir una falla.
* Implementar el punto de red.
* Comprobar conectividad.
* Presentar las evidencias solicitadas.
* Entregar el informe correspondiente.

---

# 31. Pregunta final de reflexión

> **¿Por qué una instalación de cableado estructurado debe considerarse parte fundamental de la infraestructura de una red y no simplemente un conjunto de cables conectados entre dispositivos?**

Respuesta:

..............................................................................

..............................................................................

..............................................................................

..............................................................................

---

# 32. Resultado esperado

Al finalizar el laboratorio, el estudiante deberá haber construido y verificado un enlace físico de red funcional:

```text
       CABLEADO ESTRUCTURADO

 ┌──────────┐
 │   PC 1   │
 └────┬─────┘
      │
 Patch Cord
      │
      ▼
┌─────────────┐
│   Keystone  │
└──────┬──────┘
       │
       │ UTP
       │
       ▼
┌─────────────┐
│ Patch Panel │
└──────┬──────┘
       │
  Patch Cord
       │
       ▼
┌─────────────┐
│    Switch   │
└──────┬──────┘
       │
  Patch Cord
       │
       ▼
 ┌──────────┐
 │   PC 2   │
 └──────────┘

Resultado:

PC 1  <────────── RED LAN ──────────>  PC 2
```

El enlace deberá haber sido **conectorizado, probado, documentado y verificado mediante conectividad de red**.
