import socket
import threading
import time
from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario compartido para guardar las coordenadas en tiempo real
DATA_STATE = {
    'ejeX': 0.0,
    'ejeY': 0.0
}

# CONFIGURACIÓN: Dirección IP de tu teléfono celular en la red Wi-Fi
PHONE_IP = "192.168.1.167"  
PORT = 12345      

def socket_client():
    """
    Cliente TCP secundario. Se conecta al celular y procesa la telemetría.
    """
    while True:
        try:
            print(f" -> [CONECTANDO] Buscando servidor del celular en {PHONE_IP}:{PORT}...")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5.0)
            client_socket.connect((PHONE_IP, PORT))
            print(f" -> [ÉXITO] ¡Conectado al celular! Leyendo flujo de datos...")
            
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                raw_payload = data.decode('utf-8', errors='ignore').strip()
                
                try:
                    if "\n" in raw_payload:
                        raw_payload = raw_payload.split("\n")[-1]
                    
                    # Quitar prefijos literales "X:" y "Y:"
                    clean_payload = raw_payload.replace("X:", "").replace("Y:", "")
                    
                    partes = clean_payload.split(',')
                    if len(partes) >= 2:
                        # SE CORRIGE EL ORDEN DE LOS EJES:
                        # Para emular un volante/yugo de avión usando el celular de lado,
                        # se invierte el mapeo de los índices del arreglo recibido.
                        DATA_STATE['ejeX'] = float(partes[1].strip())
                        DATA_STATE['ejeY'] = float(partes[0].strip())
                except (ValueError, IndexError):
                    pass
            
            client_socket.close()
        except Exception as e:
            print(f" -> [ERROR DE CONEXIÓN] Servidor del celular inaccesible: {e}")
            time.sleep(2)

@app.route('/')
def index():
    current_view = request.args.get('view', 'radar')
    return render_template(
        'index.html', 
        ejeX=DATA_STATE['ejeX'], 
        ejeY=DATA_STATE['ejeY'], 
        current_view=current_view
    )

if __name__ == '__main__':
    threading.Thread(target=socket_client, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
