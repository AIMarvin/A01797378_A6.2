# A01797378_A6.2 — Sistema de Reservaciones

## Descripción

Sistema de reservaciones de hotel desarrollado en Python como parte de la **Actividad 6.2 — Ejercicio de Programación 3** del Tecnológico de Monterrey.

El programa implementa tres clases principales (`Hotel`, `Customer`, `Reservation`) con persistencia en archivos JSON, manejo de errores y pruebas unitarias con cobertura superior al 85%.

---

## Estructura del Proyecto

```
A01797378_A6.2/
├── hotel.py                 # Clase Hotel (CRUD + reserva de habitaciones)
├── customer.py              # Clase Customer (CRUD de clientes)
├── reservation.py           # Clase Reservation (crear/cancelar reservaciones)
├── data_utils.py            # Utilería para persistencia JSON
├── test_hotel.py            # Pruebas unitarias - Hotel
├── test_customer.py         # Pruebas unitarias - Customer
├── test_reservation.py      # Pruebas unitarias - Reservation
├── pylint_evidence.txt      # Evidencia de análisis Pylint
├── flake8_evidence.txt      # Evidencia de análisis Flake8
├── coverage_evidence.txt    # Evidencia de cobertura de código
└── README.md
```

---

## Clases Implementadas

### Hotel
| Método | Descripción |
|---|---|
| `create_hotel()` | Crea un hotel y lo guarda en `hotels.json` |
| `delete_hotel()` | Elimina un hotel por su ID |
| `display_hotel()` | Muestra la información de un hotel |
| `modify_hotel()` | Modifica nombre, ubicación o habitaciones |

### Customer
| Método | Descripción |
|---|---|
| `create_customer()` | Crea un cliente y lo guarda en `customers.json` |
| `delete_customer()` | Elimina un cliente por su ID |
| `display_customer()` | Muestra la información de un cliente |
| `modify_customer()` | Modifica nombre o email |

### Reservation
| Método | Descripción |
|---|---|
| `create_reservation()` | Crea una reservación validando cliente, hotel y disponibilidad |
| `cancel_reservation()` | Cancela una reservación y libera la habitación |

---

## Ejecución de Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest test_hotel.py test_customer.py test_reservation.py -v

# Ejecutar con cobertura
python -m coverage run -m pytest test_hotel.py test_customer.py test_reservation.py
python -m coverage report
```

---

## Análisis de Código

```bash
# Pylint
python -m pylint hotel.py customer.py reservation.py data_utils.py

# Flake8
python -m flake8 hotel.py customer.py reservation.py data_utils.py
```

---

## Resultados

| Métrica | Resultado |
|---|---|
| Pylint | 10.00 / 10 en todos los módulos |
| Flake8 | 0 errores |
| Pruebas unitarias | 21 tests (11 casos negativos) |
| Cobertura total | 94% |

### Cobertura por Archivo

| Archivo | Cobertura |
|---|---|
| `customer.py` | 98% |
| `reservation.py` | 96% |
| `hotel.py` | 90% |
| `data_utils.py` | 86% |

---

## Requisitos

- Python 3.10+
- `pytest`
- `coverage`
- `pylint`
- `flake8`

```bash
pip install pytest coverage pylint flake8
```

---

## Autor

**Marvin H. Arias** — A01797378  
Tecnológico de Monterrey
