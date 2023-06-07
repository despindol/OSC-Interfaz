import tkinter as tk
from pythonosc import dispatcher, osc_server
import threading

# Función para manejar los mensajes OSC recibidos
def handle_osc_message(address, *args):
    message = f"Mensaje recibido en '{address}': {args}"
    text.insert(tk.END, message + "\n")  # Agregar mensaje al componente de texto
    text.see(tk.END)  # Desplazarse automáticamente hacia el final del texto

# Configuración de la ventana
window = tk.Tk()
window.title("Visualizador de datos OSC")
window.geometry("400x300")

# Componente de texto para mostrar los datos
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True)

# Configuración del servidor OSC
ip = "127.0.0.1"  # IP en la que escucha el servidor OSC
port = 9000       # Puerto en el que escucha el servidor OSC

# Crea un despachador de mensajes OSC
d = dispatcher.Dispatcher()
d.set_default_handler(handle_osc_message)

# Configura el servidor OSC con el despachador
server = osc_server.ThreadingOSCUDPServer((ip, port), d)

# Función para iniciar el servidor OSC
def start_server():
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    start_button.config(state=tk.DISABLED)  # Deshabilitar botón de inicio

# Botón para iniciar el servidor OSC
start_button = tk.Button(window, text="Iniciar servidor", command=start_server)
start_button.pack(pady=10)

# Función para detener el servidor OSC
def stop_server():
    server.shutdown()
    server.server_close()
    start_button.config(state=tk.NORMAL)  # Habilitar botón de inicio

# Botón para detener el servidor OSC
stop_button = tk.Button(window, text="Detener servidor", command=stop_server)
stop_button.pack()

# Ejecutar la ventana principal
window.mainloop()

#Desarrollado por Diego Espíndola y Javier Mendez.