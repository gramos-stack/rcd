import ipaddress
import tkinter as tk
from tkinter import ttk, messagebox


# ------------------------------------------------------------
# FUNCIONES DE CALCULO
# ------------------------------------------------------------

def ip_binaria(ip):
    """Convierte una direccion IPv4 a cuatro octetos binarios."""
    return ".".join(format(int(octeto), "08b")
                    for octeto in str(ip).split("."))


def obtener_wildcard(mascara):
    """Calcula la wildcard a partir de una mascara IPv4."""
    return ipaddress.IPv4Address(int(mascara) ^ 0xFFFFFFFF)


def obtener_clase(ip):
    """Devuelve la clase IPv4 tradicional segun el primer octeto."""
    primero = int(str(ip).split(".")[0])

    if 1 <= primero <= 126:
        return "A"
    elif 128 <= primero <= 191:
        return "B"
    elif 192 <= primero <= 223:
        return "C"
    elif 224 <= primero <= 239:
        return "D (multicast)"
    else:
        return "E (reservada/experimental)"


def tipo_direccion(ip):
    """Identifica rangos privados RFC 1918."""
    rangos_privados = [
        ipaddress.ip_network("10.0.0.0/8"),
        ipaddress.ip_network("172.16.0.0/12"),
        ipaddress.ip_network("192.168.0.0/16"),
    ]
    if any(ip in red for red in rangos_privados):
        return "Privada"
    return "Publica / no RFC 1918"


def datos_host(red):
    """Devuelve extremos utilizables, contemplando /31 y /32."""
    if red.prefixlen == 32:
        return red.network_address, red.network_address
    if red.prefixlen == 31:
        return red.network_address, red.broadcast_address
    return red.network_address + 1, red.broadcast_address - 1


def bits_mascara(prefijo):
    """Representa los 32 bits de la mascara."""
    bits = "1" * prefijo + "0" * (32 - prefijo)
    return ".".join(bits[i:i + 8] for i in range(0, 32, 8))


def validar_y_calcular(ip_texto, cantidad_subredes, hosts_solicitados):
    """
    Calcula FLSM:
    - Se prestan los bits minimos necesarios para crear la cantidad solicitada.
    - Los bits restantes deben permitir la cantidad de hosts solicitada.
    - Si no se cumplen ambas condiciones, se informa el error.
    """
    interfaz = ipaddress.ip_interface(ip_texto.strip())
    ip = interfaz.ip
    red = interfaz.network

    if red.version != 4:
        raise ValueError("Solo se permiten direcciones IPv4.")

    if cantidad_subredes < 1:
        raise ValueError("La cantidad de subredes debe ser mayor que cero.")

    if hosts_solicitados < 1:
        raise ValueError("La cantidad de hosts debe ser mayor que cero.")

    # Bits minimos que se deben prestar para obtener las subredes solicitadas.
    bits_prestados = (cantidad_subredes - 1).bit_length()
    nuevo_prefijo = red.prefixlen + bits_prestados

    if nuevo_prefijo > 30:
        raise ValueError(
            "La red no tiene suficientes bits para crear subredes "
            "con al menos dos hosts utilizables."
        )

    bits_host = 32 - nuevo_prefijo
    hosts_disponibles = (2 ** bits_host) - 2
    subredes_posibles = 2 ** bits_prestados

    if hosts_solicitados > hosts_disponibles:
        raise ValueError(
            "No es posible cumplir ambos requisitos con FLSM.\n\n"
            f"Con {bits_prestados} bits prestados se crean "
            f"{subredes_posibles} subredes posibles, pero cada una "
            f"permite {hosts_disponibles} hosts utilizables.\n"
            f"Se solicitaron {hosts_solicitados} hosts por subred.\n\n"
            "Se necesita una red principal mas grande o reducir "
            "la cantidad de subredes/hosts."
        )

    mascara_original = red.netmask
    mascara_nueva = ipaddress.IPv4Network(
        f"0.0.0.0/{nuevo_prefijo}"
    ).netmask

    subredes = list(red.subnets(new_prefix=nuevo_prefijo))

    return {
        "ip": ip,
        "red": red,
        "cantidad": cantidad_subredes,
        "hosts_solicitados": hosts_solicitados,
        "bits_prestados": bits_prestados,
        "bits_host": bits_host,
        "nuevo_prefijo": nuevo_prefijo,
        "subredes_posibles": subredes_posibles,
        "hosts_disponibles": hosts_disponibles,
        "mascara_original": mascara_original,
        "wildcard_original": obtener_wildcard(mascara_original),
        "mascara_nueva": mascara_nueva,
        "wildcard_nueva": obtener_wildcard(mascara_nueva),
        "subredes": subredes[:cantidad_subredes],
    }


# ------------------------------------------------------------
# INTERFAZ GRAFICA
# ------------------------------------------------------------

class AplicacionSubneteo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Subneteo IPv4 - FLSM")
        self.ventana.geometry("1120x780")
        self.ventana.minsize(850, 600)
        self.ventana.configure(bg="#eef2f7")

        self.crear_interfaz()

    def crear_interfaz(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=9
        )
        estilo.configure(
            "TLabel",
            background="#ffffff",
            font=("Segoe UI", 10)
        )

        encabezado = tk.Frame(self.ventana, bg="#17365d", pady=17)
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="SISTEMA DE SUBNETEO IPv4",
            bg="#17365d",
            fg="white",
            font=("Segoe UI", 20, "bold")
        ).pack()

        tk.Label(
            encabezado,
            text="Calculo de bits prestados, mascaras y distribucion FLSM",
            bg="#17365d",
            fg="#dce6f1",
            font=("Segoe UI", 10)
        ).pack(pady=(4, 0))

        panel = tk.Frame(
            self.ventana, bg="white",
            padx=18, pady=15,
            highlightbackground="#d5dce5",
            highlightthickness=1
        )
        panel.pack(fill="x", padx=18, pady=15)

        tk.Label(
            panel, text="DATOS DE ENTRADA",
            bg="white", fg="#17365d",
            font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=0, columnspan=6, sticky="w", pady=(0, 12))

        self.entrada_ip = self.crear_campo(
            panel, "IP principal / prefijo",
            "192.168.1.1/24", 0, 0
        )
        self.entrada_subredes = self.crear_campo(
            panel, "Cantidad de subredes",
            "4", 0, 2
        )
        self.entrada_hosts = self.crear_campo(
            panel, "Hosts por subred",
            "62", 0, 4
        )

        botones = tk.Frame(panel, bg="white")
        botones.grid(row=2, column=0, columnspan=6, sticky="w", pady=(14, 0))

        ttk.Button(
            botones, text="CALCULAR SUBNETEO",
            command=self.calcular
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            botones, text="LIMPIAR",
            command=self.limpiar
        ).pack(side="left")

        tk.Label(
            panel,
            text="Ejemplo: 192.168.1.1/24  |  Subredes: 4  |  Hosts: 62",
            bg="white", fg="#64748b",
            font=("Segoe UI", 9)
        ).grid(row=3, column=0, columnspan=6, sticky="w", pady=(10, 0))

        marco_resultado = tk.Frame(self.ventana, bg="#eef2f7")
        marco_resultado.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        tk.Label(
            marco_resultado,
            text="RESULTADOS DEL SUBNETEO",
            bg="#eef2f7", fg="#17365d",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 8))

        contenedor = tk.Frame(marco_resultado, bg="white")
        contenedor.pack(fill="both", expand=True)

        barra_y = ttk.Scrollbar(contenedor, orient="vertical")
        barra_y.pack(side="right", fill="y")

        barra_x = ttk.Scrollbar(contenedor, orient="horizontal")
        barra_x.pack(side="bottom", fill="x")

        self.resultado = tk.Text(
            contenedor,
            wrap="none",
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#1e293b",
            padx=14,
            pady=12,
            yscrollcommand=barra_y.set,
            xscrollcommand=barra_x.set,
            relief="flat",
            state="disabled"
        )
        self.resultado.pack(fill="both", expand=True)

        barra_y.config(command=self.resultado.yview)
        barra_x.config(command=self.resultado.xview)

        self.resultado.tag_configure(
            "titulo", foreground="#17365d",
            font=("Consolas", 12, "bold")
        )
        self.resultado.tag_configure(
            "subtitulo", foreground="#087e8b",
            font=("Consolas", 10, "bold")
        )
        self.resultado.tag_configure(
            "red", foreground="#2563eb",
            font=("Consolas", 10, "bold")
        )
        self.resultado.tag_configure(
            "prestado", foreground="#16a34a",
            font=("Consolas", 10, "bold")
        )
        self.resultado.tag_configure(
            "host", foreground="#d97706",
            font=("Consolas", 10, "bold")
        )
        self.resultado.tag_configure(
            "normal", foreground="#1e293b"
        )

        self.mostrar_mensaje_inicial()

    def crear_campo(self, padre, etiqueta, valor, fila, columna):
        grupo = tk.Frame(padre, bg="white")
        grupo.grid(
            row=fila + 1, column=columna,
            sticky="ew", padx=(0, 14), pady=3
        )

        tk.Label(
            grupo, text=etiqueta,
            bg="white", fg="#334155",
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")

        entrada = ttk.Entry(grupo, width=23, font=("Segoe UI", 10))
        entrada.pack(fill="x", pady=(5, 0))
        entrada.insert(0, valor)

        padre.grid_columnconfigure(columna, weight=1)
        return entrada

    def escribir(self, texto="", etiqueta="normal"):
        self.resultado.insert("end", texto + "\n", etiqueta)

    def mostrar_mensaje_inicial(self):
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")
        self.escribir(
            "Ingrese los tres datos y presione CALCULAR SUBNETEO.",
            "subtitulo"
        )
        self.escribir()
        self.escribir(
            "El programa calcula los bits prestados para la cantidad "
            "de subredes y verifica los hosts solicitados.",
            "normal"
        )
        self.resultado.configure(state="disabled")

    def calcular(self):
        try:
            ip_texto = self.entrada_ip.get().strip()
            cantidad = int(self.entrada_subredes.get())
            hosts = int(self.entrada_hosts.get())

            datos = validar_y_calcular(ip_texto, cantidad, hosts)
            self.mostrar_resultados(datos)

        except ValueError as error:
            messagebox.showerror("No se puede realizar el subneteo", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"Ocurrio un error: {error}")

    def mostrar_resultados(self, d):
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")

        self.escribir("=" * 112, "titulo")
        self.escribir("INFORMACION DE LA RED PRINCIPAL", "titulo")
        self.escribir("=" * 112, "titulo")

        mostrar_datos = [
            ("Address:", d["ip"], d["ip"]),
            ("Netmask:", f'{d["mascara_original"]} = /{d["red"].prefixlen}',
             d["mascara_original"]),
            ("Wildcard:", d["wildcard_original"], d["wildcard_original"]),
            ("Network:", d["red"], d["red"].network_address),
        ]

        for nombre, valor, ip_bin in mostrar_datos:
            self.escribir(
                f"{nombre:<16} {str(valor):<22} {ip_binaria(ip_bin)}",
                "normal"
            )

        host_min, host_max = datos_host(d["red"])
        self.escribir(
            f'{"HostMin:":<16} {str(host_min):<22} {ip_binaria(host_min)}'
        )
        self.escribir(
            f'{"HostMax:":<16} {str(host_max):<22} {ip_binaria(host_max)}'
        )
        self.escribir(
            f'{"Broadcast:":<16} {str(d["red"].broadcast_address):<22} '
            f'{ip_binaria(d["red"].broadcast_address)}'
        )
        self.escribir(f'{"Hosts/Net:":<16} {d["red"].num_addresses - 2}')
        self.escribir(f'{"Clase:":<16} {obtener_clase(d["ip"])}')
        self.escribir(f'{"Tipo:":<16} {tipo_direccion(d["ip"])}')

        self.escribir()
        self.escribir("=" * 112, "titulo")
        self.escribir("CALCULO DE BITS PRESTADOS", "titulo")
        self.escribir("=" * 112, "titulo")

        self.escribir(
            f'Subredes solicitadas: {d["cantidad"]}',
            "normal"
        )
        self.escribir(
            f'Bits prestados:       {d["bits_prestados"]} '
            f'(2^{d["bits_prestados"]} = {d["subredes_posibles"]} subredes posibles)',
            "prestado"
        )
        self.escribir(
            f'Bits para hosts:      {d["bits_host"]}',
            "host"
        )
        self.escribir(
            f'Transicion:           /{d["red"].prefixlen} a /{d["nuevo_prefijo"]}'
        )
        self.escribir(
            f'Hosts solicitados:    {d["hosts_solicitados"]}'
        )
        self.escribir(
            f'Hosts disponibles:    {d["hosts_disponibles"]}'
        )

        self.escribir()
        self.escribir("MASCARA NUEVA Y WILDCARD", "subtitulo")
        self.escribir(
            f'Netmask:   {d["mascara_nueva"]} = /{d["nuevo_prefijo"]}'
        )
        self.escribir(
            f'Wildcard:  {d["wildcard_nueva"]}'
        )
        self.escribir(
            f'Mascara binaria: {bits_mascara(d["nuevo_prefijo"])}'
        )
        self.escribir(
            "Leyenda: 1 = bit de red (incluye bits prestados); "
            "0 = bit de host.",
            "normal"
        )

        self.escribir()
        self.escribir("=" * 112, "titulo")
        self.escribir("DISTRIBUCION DE SUBREDES", "titulo")
        self.escribir("=" * 112, "titulo")

        for numero, subred in enumerate(d["subredes"], start=1):
            minimo, maximo = datos_host(subred)
            self.escribir()
            self.escribir(f"SUBRED {numero:02d}", "subtitulo")
            self.escribir("-" * 112, "normal")

            filas = [
                ("Network:", subred.network_address),
                ("HostMin:", minimo),
                ("HostMax:", maximo),
                ("Broadcast:", subred.broadcast_address),
            ]

            for etiqueta, direccion in filas:
                self.escribir(
                    f"{etiqueta:<16} {str(direccion):<22} "
                    f"{ip_binaria(direccion)}",
                    "normal"
                )

            self.escribir(
                f'{"Hosts/Net:":<16} {subred.num_addresses - 2}'
            )
            self.escribir(
                f'{"Prefijo:":<16} /{d["nuevo_prefijo"]}'
            )

        self.escribir()
        self.escribir("=" * 112, "titulo")
        self.escribir(
            f'SUBNETEO FINALIZADO: {d["cantidad"]} subred(es) distribuidas.',
            "prestado"
        )
        self.escribir("=" * 112, "titulo")

        self.resultado.configure(state="disabled")
        self.resultado.see("1.0")

    def limpiar(self):
        self.entrada_ip.delete(0, "end")
        self.entrada_subredes.delete(0, "end")
        self.entrada_hosts.delete(0, "end")
        self.mostrar_mensaje_inicial()


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = AplicacionSubneteo(ventana)
    ventana.mainloop()
