import threading
import datetime
import time

print(datetime.datetime.now())

def funcion():
    print(f"Hilo en marca identificador{threading.current_thread().name}")
    for i in range(1,5):
        time.sleep(1)
    print(f"hora Intermedio {(datetime.datetime.now())}")

hilo1 = threading.Thread(target = funcion)
hilo2 = threading.Thread(target = funcion)
hilo3 = threading.Thread(target = funcion)


hilo1.start()
hilo1.join()

hilo2.start()
hilo2.join()

hilo3.start()
hilo3.join()


print(f"hora final {(datetime.datetime.now())}")
