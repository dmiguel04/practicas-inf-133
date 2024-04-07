from http.server import HTTPServer, BaseHTTPRequestHandler
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Definir las operaciones
def sumar(m, p):
    return m + p

def restar(m, p):
    return m - p

def multiplicar(m, p):
    return m * p

def dividir(m, p):
    if p == 0:
        raise ValueError("No se puede dividir por cero")
    return m / p

dispatcher = SoapDispatcher(
    "ejercicio-uno",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns="http://localhost:8000"
)

dispatcher.register_function(
    "sumar",
    sumar,
    returns={"result": int},
    args={"m": int, "p": int}
)

dispatcher.register_function(
    "restar",
    restar,
    returns={"result": int},
    args={"m": int, "p": int}
)

dispatcher.register_function(
    "multiplicar",
    multiplicar,
    returns={"result": int},
    args={"m": int, "p": int}
)

dispatcher.register_function(
    "dividir",
    dividir,
    returns={"result": float},
    args={"m": int, "p": int}
)

# Iniciar el servidor
try:
    server = HTTPServer(("localhost", 8000), SOAPHandler)
    server.dispatcher = dispatcher
    print("Server started")
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
    print("Server stopped")