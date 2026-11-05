# Programa - Laboratorio 05
Este repositorio contiene el desarrollo de nuestro proyecto para el *Laboratorio 05* del curso de Redes. Diseñamos y desarrollamos una aplicación interactiva en *Python* con interfaz gráfica (GUI) utilizando *Tkinter* para realizar cálculos de subneteo IPv4 mediante la técnica *FLSM (Fixed Length Subnet Mask)*.

---

##  Integrantes 

* Geraldine Ramos Zegarra
* Gian Piero Morales Tisnado 

---

##  ¿De qué trata nuestro proyecto?

Nuestra aplicación recibe como entrada una dirección IP base con su prefijo, la cantidad de subredes requeridas y el número de hosts deseados por subred. A partir de estos datos, el programa calcula automáticamente:

* Los *bits prestados* necesarios para cumplir con el número de subredes solicitadas.
* La *nueva máscara de red* (en notación CIDR, decimal y binaria) y su respectiva *wildcard*.
* La verificación matemática para garantizar que los hosts solicitados quepan en cada subred.
* La tabla detallada con cada subred creada (Dirección de Red, Host Inicial, Host Final y Broadcast).

---

##  ¿Cómo ejecutar nuestro programa?

### Requisitos
Solo se necesita tener *Python 3* instalado en la computadora. No requiere la instalación de librerías externas con pip, ya que utilizamos únicamente módulos nativos de Python (ipaddress y tkinter).

### Pasos para ejecutar:
1. Descargar o clonar este repositorio en el equipo.
2. Abrir una terminal o consola de comandos en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

   ```bash
   python sistema_subneteo_ipv4.py
