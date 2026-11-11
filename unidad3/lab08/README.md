# Informe de Laboratorio: Subnetting IPv4 de Clase A, B y C utilizando Cisco Packet Tracer

## 25.1 Datos del estudiante
- **Curso:** Redes y Comunicación de Datos
- **Apellidos y nombres:** Ramos Zegarra, Geraldine
- **Apellidos y nombres:** Morales Tisnado, Gian Piero Nau
- **Fecha:** 11 de Noviembre de 2026

---

## 25.2 Desarrollo teórico

### Concepto de subnetting
El subnetting (creación de subredes) es un proceso lógico y matemático que permite dividir una red IP principal (de gran tamaño) en múltiples subredes más pequeñas e independientes. Técnicamente, esto se logra tomando "prestados" bits de la porción de host para asignarlos a la porción de red. Esto minimiza el tamaño de los dominios de broadcast, mejora la seguridad al permitir listas de control de acceso (ACLs) entre segmentos y optimiza drásticamente el espacio de direcciones IP.

### Diferencias entre clases A, B y C
En el direccionamiento IPv4 tradicional (classful), las redes se categorizan según los bits más significativos del primer octeto:
- **Clase A:** Rango del 1 al 126. Su máscara por defecto es `255.0.0.0` (`/8`). Están diseñadas para redes masivas, soportando más de 16 millones de hosts por red.
- **Clase B:** Rango del 128 al 191. Su máscara por defecto es `255.255.0.0` (`/16`). Orientadas a redes empresariales medianas (hasta 65,534 hosts).
- **Clase C:** Rango del 192 al 223. Su máscara por defecto es `255.255.255.0` (`/24`). Son las más comunes para redes LAN pequeñas, soportando un máximo de 254 hosts utilizables.

### Fórmulas utilizadas
Para este laboratorio se utilizó la técnica de Máscara de Subred de Longitud Fija (FLSM), aplicando las siguientes fórmulas matemáticas:
1. **Subredes obtenidas:** S = 2^n (donde n = bits prestados de la porción de host).
2. **Hosts utilizables por subred:** H = 2^h - 2 (donde h = bits de host restantes. Se restan 2 porque la primera IP es la dirección de red y la última es el broadcast).
3. **Nuevo prefijo CIDR:** Prefijo_Original + n.
4. **Incremento (Salto de red):** 256 - Valor del octeto modificado en la máscara.

### Cálculos de subnetting

**Actividad 1: Subnetting Clase A**
- **Red:** `10.0.0.0/8` | **Requerimiento:** 16 subredes.
- **Cálculo de bits:** 2^n \ge 16 \implies n=4 bits prestados.
- **Nueva máscara y prefijo:** `255.240.0.0` (`/12`).
- **Hosts por subred:** 2^{20} - 2 = 1,048,574 hosts.
- **Direcciones (Red / Broadcast):**
  1. `10.0.0.0/12` / `10.15.255.255`
  2. `10.32.0.0/12` / `10.47.255.255`
  3. `10.64.0.0/12` / `10.79.255.255`
  4. `10.96.0.0/12` / `10.111.255.255`

**Actividad 2: Subnetting Clase B**
- **Red:** `172.20.0.0/16` | **Requerimiento:** 32 subredes.
- **Cálculo de bits:** 2^n \ge 32 \implies n=5 bits prestados.
- **Nueva máscara y prefijo:** `255.255.248.0` (`/21`).
- **Hosts por subred:** 2^{11} - 2 = 2,046 hosts.
- **Direcciones (Red / Broadcast):**
  1. `172.20.0.0/21` / `172.20.7.255`
  2. `172.20.8.0/21` / `172.20.15.255`
  3. `172.20.16.0/21` / `172.20.23.255`
  4. `172.20.24.0/21` / `172.20.31.255`

**Actividad 3: Subnetting Clase C (Para implementación)**
- **Red:** `192.168.50.0/24` | **Requerimiento:** 8 subredes.
- **Cálculo de bits:** 2^n \ge 8 \implies n=3 bits prestados.
- **Nueva máscara y prefijo:** `255.255.255.224` (`/27`).
- **Hosts por subred:** 2^5 - 2 = 30 hosts.

### Tabla de direccionamiento IP (Red 192.168.50.0/24)

| Subred | Dirección de red | Rango utilizable (Primer - Último) | Broadcast |
| :--- | :--- | :--- | :--- |
| 1 | `192.168.50.0/27` | `192.168.50.1` - `192.168.50.30` | `192.168.50.31` |
| 2 | `192.168.50.32/27` | `192.168.50.33` - `192.168.50.62` | `192.168.50.63` |
| 3 | `192.168.50.64/27` | `192.168.50.65` - `192.168.50.94` | `192.168.50.95` |
| 4 | `192.168.50.96/27` | `192.168.50.97` - `192.168.50.126` | `192.168.50.127` |
| 5 | `192.168.50.128/27` | `192.168.50.129` - `192.168.50.158` | `192.168.50.159` |
| 6 | `192.168.50.160/27` | `192.168.50.161` - `192.168.50.190` | `192.168.50.191` |
| 7 | `192.168.50.192/27` | `192.168.50.193` - `192.168.50.222` | `192.168.50.223` |
| 8 | `192.168.50.224/27` | `192.168.50.225` - `192.168.50.254` | `192.168.50.255` |

---

## 25.3 Diseño de red

### Descripción de dispositivos y subredes
Para la simulación en Cisco Packet Tracer, se diseñó una topología en estrella extendida utilizando las **primeras 4 subredes** calculadas de la Clase C. 
- **1 Router (Cisco 2911):** Nombrado `R1`. Ya que el modelo 2911 posee solo 3 interfaces GigabitEthernet nativas, fue necesario apagar el equipo virtual e instalarle físicamente el módulo de expansión `HWIC-4ESW` para dotarlo de puertos FastEthernet adicionales y poder conectar la cuarta subred.
- **4 Switches (Cisco 2960):** Encargados de la distribución de Capa 2 en cada subred lógica.
- **8 Computadoras (PCs):** Ubicadas en pares (2 por cada switch/subred). Todo el cableado se realizó utilizando cables de cobre de conexión directa (Copper Straight-Through).

### Diagrama de topología
<img width="967" height="491" alt="TOPOLOGIA (1)" src="https://github.com/user-attachments/assets/a1fa12c8-3287-4253-8cec-e48f94ec4571" />
<img width="993" height="525" alt="TOPOLOGIA1 2" src="https://github.com/user-attachments/assets/db0ad4d2-df7a-4533-b909-26a15a836753" />
---

## 25.4 Configuración

### Configuración de las PCs (Máscaras y puertas de enlace)
Se ingresó a la pestaña **Desktop -> IP Configuration** de cada equipo de usuario final para realizar la asignación estática de parámetros de red. A todas las PCs se les configuró la nueva máscara adaptada `/27` (`255.255.255.224`). Como Puerta de Enlace Predeterminada (Default Gateway), se asignó la primera IP utilizable de cada subred, la cual corresponde a la interfaz del router `R1`.

- **Subred 1 (Gateway 192.168.50.1):** PC1 (`.10`), PC2 (`.20`)
- **Subred 2 (Gateway 192.168.50.33):** PC3 (`.40`), PC4 (`.50`)
- **Subred 3 (Gateway 192.168.50.65):** PC5 (`.70`), PC6 (`.80`)
- **Subred 4 (Gateway 192.168.50.97):** PC7 (`.100`), PC8 (`.110`)

<img width="697" height="573" alt="CONFIGURACION_PC" src="https://github.com/user-attachments/assets/e9b569da-a573-431c-80aa-7c597ed8e49e" />

### Configuración del router y comandos utilizados
La configuración de `R1` se ejecutó mediante la Interfaz de Línea de Comandos (CLI). Durante este proceso se resolvió un desafío técnico crucial: al utilizar el módulo de expansión `HWIC-4ESW`, el puerto `FastEthernet 0/3/0` opera estrictamente en Capa 2 (Switching). Por lo tanto, el sistema operativo Cisco IOS rechazaba la asignación directa de una IP arrojando el error `% Invalid input detected`. 

**Solución aplicada:** Se configuró el puerto físico como modo de acceso a la VLAN 1 y se levantó una interfaz virtual (SVI) `interface vlan 1`, a la cual se le asignó exitosamente la dirección IP de la cuarta puerta de enlace.

**Secuencia de comandos ejecutada:**
```text
enable
configure terminal

interface gigabitEthernet 0/0
 ip address 192.168.50.1 255.255.255.224
 no shutdown
 exit

interface gigabitEthernet 0/1
 ip address 192.168.50.33 255.255.255.224
 no shutdown
 exit

interface gigabitEthernet 0/2
 ip address 192.168.50.65 255.255.255.224
 no shutdown
 exit

interface fastEthernet 0/3/0
 switchport access vlan 1
 exit

interface vlan 1
 ip address 192.168.50.97 255.255.255.224
 no shutdown
 exit

end
write memory

```


Para comprobar la correcta inicialización lógica y física, se empleó el comando `show ip interface brief`.
<img width="659" height="461" alt="CONFIGURACION_ROUTER" src="https://github.com/user-attachments/assets/e231b4bd-a13f-4bbe-8686-7a689de231ae" />



---

## 25.5 Pruebas y Resultados

Para comprobar que toda la red funciona, entré al **Command Prompt** de la **PC1** (`192.168.50.10`) y hice tres pruebas con `ping`:

1. **Ping hacia el router (Default Gateway):**
   Se ejecutó el comando `ping 192.168.50.1`. La respuesta fue inmediata, recibiendo los 4 paquetes (0% de pérdida). Esto confirmó que el enlace físico, la configuración de la subred local y el puerto del router operan correctamente.
2. **Ping entre PCs de una misma subred:**
   Se ejecutó el comando `ping 192.168.50.20` (dirigido a la PC2). La comunicación se realizó exitosamente a través de la red local, mediante la conmutación de tramas MAC efectuada por el Switch 1, sin necesidad de que los paquetes alcanzaran al router.
3. **Ping entre PCs de diferentes subredes:**
   Se ejecutó el comando `ping 192.168.50.40` (dirigido a la PC3 ubicada en la Subred 2). El primer paquete enviado generó un evento de `Request timed out`. Este fenómeno técnico es completamente esperado en el primer intento, y representa el tiempo milimétrico que toma el protocolo ARP (Address Resolution Protocol) en realizar la resolución de direcciones físicas para construir y conocer la ruta hacia un destino remoto desconocido. Los tres paquetes subsiguientes respondieron con éxito (`Reply from 192.168.50.40: bytes=32...`), lo que confirma categóricamente que el router está enrutando paquetes a nivel de Capa 3 de forma correcta.
<img width="682" height="359" alt="PRUEBAS_PING" src="https://github.com/user-attachments/assets/5b692bae-7003-4912-90bc-12024b5ed11d" />

### Pruebas desde las 8 PCs
<img width="544" height="703" alt="prueba_pc1" src="https://github.com/user-attachments/assets/3212d7ff-b298-41e6-b669-494017f47d2d" />

<img width="499" height="725" alt="prueba_pc2" src="https://github.com/user-attachments/assets/98bb8023-e3d3-41f6-920f-4cc548409fd0" />

<img width="503" height="736" alt="prueba_pc3" src="https://github.com/user-attachments/assets/823b64af-f46a-464a-846e-66f79467b8d7" />

<img width="457" height="722" alt="prueba_pc4" src="https://github.com/user-attachments/assets/e3148bca-353d-41ea-94bd-c6856e262cbc" />

<img width="473" height="749" alt="prueba_pc5" src="https://github.com/user-attachments/assets/3fa5d822-4fa0-427e-a7ae-9e047da6329d" />

<img width="493" height="890" alt="prueba_pc6" src="https://github.com/user-attachments/assets/06f8edf6-7043-4e16-a3bb-9472763e8472" />

<img width="502" height="727" alt="prueba_pc7" src="https://github.com/user-attachments/assets/145349db-7b66-4400-bb67-9a679508ec9a" />

<img width="538" height="774" alt="prueba_pc8" src="https://github.com/user-attachments/assets/fac64acd-1a3c-47d2-9e53-1b4c33b3729f" />



**Resultado de `show ip route`:**
Ejecuté `show ip route` en el router (`R1#`). En la tabla aparecen las 4 subredes. Cada una sale con la letra "C" (conectada) y la IP del router en esa subred sale con la letra "L" (local). Esto confirma que R1 conoce las 4 subredes y puede enrutar entre ellas.
<img width="641" height="408" alt="route" src="https://github.com/user-attachments/assets/51b5fda5-ce09-45c8-a511-c301becc991f" />


---

## 25.6 Conclusiones

1. **La importancia del subnetting:** El desarrollo técnico y analítico de este laboratorio demuestra fehacientemente que el subnetting es una estrategia fundamental para la correcta arquitectura de las redes de datos. Al segmentar la red principal `/24` en subredes `/27`, se logró aislar de manera efectiva los dominios de broadcast. Esta contención evita las denominadas tormentas de difusión, reduce drásticamente la congestión de la red y establece fronteras lógicas indispensables para posteriormente aplicar políticas de seguridad interdepartamentales.
2. **La optimización del direccionamiento IP:** La aplicación rigurosa de la técnica FLSM permitió ajustar el esquema matemático de direccionamiento a las necesidades reales y precisas del escenario planteado. En lugar de desperdiciar una red entera con 254 direcciones para un segmento que solo posee un par de equipos conectados, se optimizó el espacio IPv4, entregando bloques exactos de 30 hosts útiles. Esta acción evita el agotamiento innecesario del limitado protocolo IPv4, reservando un amplio margen para futuras expansiones.
3. **La configuración y verificación en Packet Tracer:** La herramienta de simulación permitió comprobar empíricamente que los cálculos teóricos operan con total precisión en entornos de hardware simulados. Adicionalmente, el desarrollo práctico fomentó sólidas habilidades de resolución de problemas (troubleshooting) en el sistema operativo Cisco IOS. Se abordaron y superaron situaciones como el bloqueo de consola por búsquedas DNS erróneas (interrumpidas con `Ctrl+Shift+6`) y el desafío de configurar interfaces virtuales (SVI / VLANs) para sortear las limitaciones físicas al implementar módulos de conmutación de Capa 2 (HWIC-4ESW) en un dispositivo de enrutamiento.

---

## Respuestas a las Preguntas de Evaluación

1. **¿Qué diferencia existe entre una dirección IP y una máscara de subred?**
   La dirección IP es un identificador lógico asignado de forma unívoca a un nodo en la red. La máscara de subred es el parámetro fundamental que el sistema operativo utiliza (mediante la operación matemática booleana AND) para separar la IP y determinar con exactitud qué porción binaria de dicha IP corresponde al identificador de la red, y qué porción identifica al host específico.
2. **¿Por qué se utilizan bits prestados para crear subredes?**
   Porque los bits originales definidos por la clase de red son inflexibles y fijos. Se toman bits prestados estrictamente de la porción de host para "extender" la longitud de la porción de red. Esta conversión matemática es la que permite subdividir de manera lógica un bloque grande en múltiples segmentos más pequeños y manejables.
3. **¿Qué diferencia existe entre una dirección de red y una dirección broadcast?**
   La dirección de red tiene todos los bits de su porción de host en estado apagado (en `0`), sirve para representar al segmento lógico en su totalidad y es la única IP que no puede asignarse a un dispositivo final. Por el contrario, la dirección de broadcast posee todos sus bits de host en estado encendido (en `1`) y funciona como un destino universal diseñado para enviar un paquete de datos de manera simultánea a todos los nodos conectados dentro de esa misma subred.
4. **¿Cuántos hosts utilizables tiene una subred /26?**
   El prefijo CIDR `/26` indica que se emplean 26 bits para la red, dejando 6 bits disponibles para la porción de host (resultado de $32 - 26 = 6$). Aplicando la fórmula de hosts utilizables, $H = 2^6 - 2$, es decir, $64 - 2$, se obtienen **62 hosts útiles** para dispositivos finales.
5. **¿Qué función cumple la puerta de enlace predeterminada (Default Gateway)?**
   Funciona como el punto de salida principal de la subred local. Es la dirección IP asignada a la interfaz del router a la cual los dispositivos finales (PCs) envían por defecto todo el tráfico de red, siempre y cuando los paquetes estén dirigidos a direcciones lógicas (IPs) que no pertenecen a su propia subred local.
6. **¿Por qué es necesario utilizar un router para comunicar diferentes subredes?**
   Porque los switches locales son dispositivos que operan a nivel de Capa 2 (Enlace de datos) y su función está limitada a conmutar y reenviar tramas basadas en direcciones MAC exclusivamente dentro del mismo dominio de broadcast. El router opera en la Capa 3 (Red) del modelo OSI, y es el único equipo capacitado para examinar encabezados IP, consultar su tabla de ruteo e interconectar dominios de difusión lógicamente separados.
7. **¿Qué información proporciona el comando `show ip route`?**
   Proporciona la lectura detallada de la tabla de enrutamiento almacenada en la memoria RAM del dispositivo. Despliega todas las redes IP lógicas que el router conoce para encaminar tráfico, detallando si dichas redes fueron configuradas de forma estática, si fueron aprendidas a través de un protocolo de enrutamiento dinámico, o si se encuentran directamente conectadas (físicamente) al dispositivo, especificando en todos los casos la interfaz de salida correspondiente.
8. **¿Qué sucede si una PC tiene una máscara incorrecta?**
   El sistema operativo del equipo calculará de forma errónea los límites lógicos, el rango de IPs y la dirección de broadcast del segmento de red en el que está insertado. A consecuencia de esto, se alterará gravemente el proceso de decisión local: el dispositivo enviará tráfico de red local hacia su Default Gateway por equivocación, o, de lo contrario, intentará buscar y resolver direcciones de destinos remotos en su red LAN, resultando en una pérdida de conectividad, parcial o total, según la desviación del cálculo.
9. **¿Por qué dos PCs de diferentes subredes necesitan un router para comunicarse?**
   Porque habitan en espacios lógicos, segmentos de direccionamiento y dominios de difusión completamente independientes. Cuando intentan establecer comunicación, la computadora de origen, al detectar que la IP objetivo no pertenece a su bloque, encapsulará el paquete de red con la dirección MAC destino del router (no de la otra PC). Esto exige obligatoriamente que el router reciba la trama, la desencapsule, tome una decisión de ruteo a nivel IP (Capa 3), y finalmente vuelva a encapsularla con la MAC correcta para enviarla hacia la red de destino pertinente.
10. **¿Qué ventajas ofrece el subnetting en la administración de redes?**
    El subnetting facilita el mantenimiento general al posibilitar la creación de una arquitectura de red jerárquica y ordenada (como asignar rangos específicos por departamentos operativos). Incrementa sustancialmente el rendimiento de los equipos aislando el tráfico de broadcast para evitar cuellos de botella masivos, conserva y administra de manera eficiente el espacio de direccionamiento IP existente, y posibilita la implementación de políticas de seguridad robustas, permitiendo configurar Listas de Control de Acceso (ACL) para delimitar de manera estricta qué subredes pueden o no comunicarse entre sí.
