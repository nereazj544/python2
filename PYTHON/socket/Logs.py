# IMPORTAR LIBRERÍAS
import logging

# CONFIGURACIÓN DEL LOG
def setup_logging():
    logging.basicConfig(filename="PYTHON/socket/log/info_servidor_2.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def setup_cliente():
    logging.basicConfig(filename="PYTHON/socket/log/info_cliente_2.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# CONFIGURACIÓN DEL LOG
def server_log(message):
    setup_logging()
    logging.info(f"[SERVER]: {message}")

def client_log(message):
    setup_cliente()
    logging.info(f"[CLIENT]: {message}")


def server_error(message):
    setup_logging()
    logging.error(f"[SERVER]: {message}")

def client_error(message):
    setup_cliente()
    logging.error(f"[CLIENT]: {message}")

def server_warning(message):
    setup_logging()
    logging.warning(f"[SERVER]: {message}")

def client_warning(message):
    setup_cliente()
    logging.warning(f"[CLIENT]: {message}")


def server_debug(message):
    setup_logging()
    logging.debug(f"[SERVER]: {message}")

def client_debug(message):
    setup_cliente()
    logging.debug(f"[CLIENT]: {message}")

def server_critical(message):
    setup_logging()
    logging.critical(f"[SERVER]: {message}")

def client_critical(message):
    setup_cliente()
    logging.critical(f"[CLIENT]: {message}")