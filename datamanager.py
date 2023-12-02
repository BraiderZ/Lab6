import time
import random
import threading
from eventmanager import EventManager

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()
        self.running = True  # Bandera para controlar la ejecución del hilo
        self.stop_event = threading.Event()  # Evento para señalar la detención del hilo

    def start_real_time_updates(self):
        while self.running and not self.stop_event.is_set():
            time.sleep(3)
            self.generate_real_time_data()

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        self.event_manager.notify("Datos actualizados", self.data) #Se notifica cada cambio con ayuda de EventManager

    def stop_updates(self):
        self.running = False  # Establecer la bandera para detener el hilo
        self.stop_event.set()  # Establecer el evento para detener el hilo

#Imprime los cambios cada vez que se den
def datos_actualizados(data):
    print("Se actualizaron los datos:",data)


#Todo dentro de except para evitar errores
try:
    if __name__ == "__main__": 
        tiempo_real = RealTimeDataManager()
        tiempo_real.event_manager.subscribe("Datos actualizados",datos_actualizados)  #Callback de la función
        
        #Actualizaciones en tiempo real
        update_thread = threading.Thread(target=tiempo_real.start_real_time_updates)
        update_thread.start()
        while True:
            time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")
    tiempo_real.stop_updates()  # Detener el hilo cuando se interrumpe el programa
    update_thread.join()  # Esperar a que el hilo termine antes de salir
