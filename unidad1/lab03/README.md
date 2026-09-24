# Informe de Cableado Estructurado

## Integrantes

- Gian Piero Morales Tisnado
- Geraldine Ramos Zegarra
- Jherson Martin Diaz Junco
- Marco Gabriel Macedo Torres
- Brayan Gabriel Chipana Benavente
- Favio Andre Solorzano Vilca

---

## 1. Introducción

En esta práctica trabajamos con **cableado estructurado**, que es el conjunto de cables, conectores y accesorios que permite conectar equipos de una red (computadoras, switches, impresoras, etc.) de forma ordenada y estandarizada.

Durante la sesión fabricamos nosotros mismos varios cables de red usando **cable UTP** (par trenzado sin blindaje) y **conectores RJ-45**, aplicando los estándares **T568A** y **T568B**. También terminamos un cable en un **keystone** y armamos un cable con una falla intencional para practicar el diagnóstico con el tester.

Entendimos la importancia del orden de los colores, cómo se comporta cada tipo de cable y cómo detectar y corregir errores. Como se verá en el informe, **cometimos varios errores durante el proceso**, y justamente de ahí sacamos buena parte del aprendizaje.

## 2. Herramientas y materiales que usamos

| Herramienta | Cantidad | Nivel | Para qué la usamos |
|---|---|---|---|
| Crimpadora RJ-45 | 1 | Obligatorio | Fijar el conector RJ-45 al cable |
| Ponchadora tipo 110 | 1 | Recomendable | Insertar los hilos en el keystone |
| Pelacables | 1 | Opcional | Retirar la cubierta exterior del cable |
| Alicate de corte | 1 | Opcional | Cortar el cable y emparejar los hilos |
| Regla o cinta métrica | 1 | Opcional | Medir la longitud de los cables |
| Tester de cable de red | 1 | Profesor | Verificar la continuidad de cada hilo |

**Materiales:** cable UTP, conectores RJ-45, keystone RJ-45 y faceplate.

---

## 3. Desarrollo de los entregables

### 3.1 Cable directo

**¿Qué es?** Un cable con el mismo estándar en ambos extremos. Nosotros usamos **T568B en los dos lados**, de modo que cada pin de un extremo queda conectado con el pin del mismo número en el otro.

```
RJ-45 (T568B) ───────── Cable UTP ───────── RJ-45 (T568B)
```

**¿Cómo lo hicimos?** Cortamos un tramo de 1 metro, pelamos ambos extremos y ordenamos los hilos en T568B (blanco/naranja, naranja, blanco/verde, azul, blanco/azul, verde, blanco/marrón, marrón). Los emparejamos con el alicate, los insertamos en el conector y crimpamos. Después repetimos el proceso en el otro extremo con el mismo orden.

**Errores que tuvimos.** En el primer intento, al probar con el tester, **el LED del pin 8 no se encendió** en uno de los extremos. Al revisar el conector vimos que el hilo marrón **no había llegado hasta el fondo**, por lo que no hacía contacto con el pin metálico. Esto pasó porque las puntas no estaban del todo parejas cuando las insertamos: el hilo marrón era ligeramente más corto que el resto. Tuvimos que **cortar el conector, recortar unos milímetros de cable, volver a emparejar los hilos y crimpar otro conector**. Ese segundo intento sí funcionó, y es una de las razones por las que el cable terminó más corto de lo previsto.

**Verificación con el tester:** tras corregir el error, los ocho indicadores se encendieron en el orden 1→1, 2→2, 3→3, 4→4, 5→5, 6→6, 7→7 y 8→8 . Esto confirma que cada hilo tiene continuidad y llega al pin correcto en ambos extremos.

**Fotos**

<img width="400" alt="60334648-2ded-4364-8991-74c210b0bced" src="https://github.com/user-attachments/assets/9d7a728a-f3e0-4de3-a9e8-2440fcd68f9b" />
<img width="400"  alt="70ff8c10-4bb6-43ca-9a25-0114ee236bb9" src="https://github.com/user-attachments/assets/6a30ecf3-024f-4b50-bf08-7f1e9bfcf90e" />

---

### 3.2 Cable cruzado

**¿Qué es?** Un cable con **T568A en un extremo y T568B en el otro**. Al hacerlo entendimos físicamente la diferencia con el directo: en el cruzado, los pares de transmisión y recepción (pines 1-2 y 3-6) quedan intercambiados entre un lado y otro, y por eso el tester no muestra una secuencia recta.

```
RJ-45 (T568A) ───────── Cable UTP ───────── RJ-45 (T568B)
```

**¿Cómo lo hicimos?** Armamos el primer extremo en T568A (blanco/verde, verde, blanco/naranja, azul, blanco/azul, naranja, blanco/marrón, marrón) y el segundo en T568B, siguiendo el procedimiento general. Para no mezclar los estándares dejamos la tabla de colores a la vista durante todo el proceso.

**Errores que tuvimos.** Nuestra dificultad principal fue **confundirnos con el orden de los pares verde y naranja**: al principio armamos el segundo extremo en T568A por costumbre, ya que veníamos de hacer cables en T568B, y el tester mostró una secuencia recta 1→1, 2→2, 3→3… es decir, habíamos hecho un cable directo A-A sin querer. Al darnos cuenta, tuvimos que rehacer ese extremo. Fue una buena forma de comprobar físicamente cómo el tester diferencia un cable directo de uno cruzado.

**Verificación con el tester:** una vez corregido, el orden de encendido fue 1→3, 2→6, 3→1, 4→4, 5→5, 6→2, 7→7 y 8→8 . Que los pines 1-3 y 2-6 aparezcan cruzados es exactamente lo esperado para un cable A-B, y confirma que el cable está bien hecho.

**Fotos**

<img width="400" alt="cruzado1" src="https://github.com/user-attachments/assets/155a970a-6db8-482b-8a44-8ae6cafdc244" />
<img width="400"  alt="cruzado2" src="https://github.com/user-attachments/assets/a1165680-c8ae-4b45-bbca-167b8cce8e65" />



---

### 3.3 Cable Patch Cord (latiguillo)

**¿Qué es?** Un latiguillo (patch cord) es un cable corto y flexible que se usa para conectar un equipo a la toma de red o para hacer conexiones dentro de un rack. El nuestro mide aproximadamente 1 metro y tiene terminación **T568B en ambos extremos**, por lo que funciona como un cable directo.

```
RJ-45 (T568B) ───────── Cable UTP ───────── RJ-45 (T568B)
```

**¿Cómo lo hicimos?** Aplicamos lo que aprendimos con el cable directo. Antes de insertar los hilos en el conector revisamos que las puntas estuvieran exactamente al mismo nivel y que el orden de colores fuera el correcto. También cuidamos que la cubierta del cable quedara bien sujeta por la pestaña de crimpado, porque en un latiguillo el cable se mueve y se jala con frecuencia, y si la cubierta no queda firme los hilos terminan soltándose.

**Errores que tuvimos.** Esta vez el cable funcionó al primer intento, gracias a lo aprendido antes. Aun así, en el primer conector **la cubierta no quedó completamente dentro del conector**, por lo que el cable quedaba flojo al jalarlo. Lo corregimos pelando un poco menos de cubierta en el otro extremo para que el crimpado atrapara bien la cubierta.

**Fotos**

<img width="500"  alt="paaaachh" src="https://github.com/user-attachments/assets/8ac57839-40bd-48d9-ae10-9996b30856e9" />

<img width="400"  alt="2223" src="https://github.com/user-attachments/assets/1ee8394c-01d5-4a03-8cf5-d4a57bb88567" />



---

### 3.4 Cable Keystone

**¿Qué es?** Es la terminación del cable UTP en un **keystone RJ-45**, la pieza que se instala en la pared o en un patch panel para crear una toma de red. A diferencia de los cables anteriores, aquí no se usa la crimpadora, sino la **ponchadora tipo 110**.

```
Cable UTP ──► KEYSTONE RJ-45 ──► FACEPLATE
```

**¿Cómo lo hicimos?**
1. Retiramos la cubierta del cable y destrenzamos los pares solo lo necesario, para no perder calidad de transmisión.
2. Revisamos el esquema de colores impreso en el keystone (A o B según el fabricante) y lo seguimos al pie de la letra.
3. Colocamos cada hilo en su ranura correspondiente, sin cruzarlos.
4. Usamos la ponchadora 110, que inserta cada hilo a presión y corta el sobrante.
5. Cerramos el keystone y lo montamos en el faceplate.
6. Probamos la toma conectando un patch cord y usando el tester.

**Fotos**

<img width="400"  alt="key" src="https://github.com/user-attachments/assets/59bfff1c-1928-4b2c-9619-faa6a9f1c17f" />
<img width="400"  alt="keyston" src="https://github.com/user-attachments/assets/adef22f9-a3d5-43c4-a950-e3582f9ab586" />

---

### 3.5 Cableado con error

**¿Qué es?** Un cable fabricado **a propósito con una falla**, para que otro grupo use el tester y descubra qué está mal. Sirve para evaluar si realmente entendemos cómo funciona el cable, no solo cómo armarlo.

```
T568B ───────────────── T568B
             ↑
      pin incorrecto
```

**¿Cómo lo hicimos?** Armamos el cable como un directo T568B, pero en uno de los extremos **intercambiamos intencionalmente los hilos de los pines 3 y 6** (el blanco/verde y el verde), es decir, un extremo quedó en T568B y en el otro lado esos dos hilos quedaron invertidos.

**Lo que mostró el tester.** Al conectar el cable, el tester mostró la secuencia **1→1, 2→2, 3→6, 4→4, 5→5, 6→3, 7→7, 8→8**. Es decir, los pines 1, 2, 4, 5, 7 y 8 encendieron normalmente y en el mismo orden, pero **el LED 3 de un lado encendió el 6 del otro, y el 6 encendió el 3**. Con esto se puede saber que no es un cable cortado (todos los hilos conducen) sino un cable con **dos hilos intercambiados**.

**Por qué es importante.** Este tipo de error es muy común y confuso: el cable "tiene continuidad", pero los hilos están en posiciones incorrectas. En una red real, esto puede impedir la conexión o hacer que funcione de forma inestable, porque los pines 3 y 6 pertenecen al par de recepción y quedan mal asignados.

   
**Fotos**

<img width="400"  alt="path1" src="https://github.com/user-attachments/assets/99770d35-1b2b-4d2a-a0d3-d02251cd759b" />



---

