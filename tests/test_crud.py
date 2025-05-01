# tests/test_crud.py
import pytest
from unittest.mock import MagicMock
from catalogo.crud import crear_producto, listar_productos, buscar_producto, modificar_producto, eliminar_producto
from catalogo.models import Producto


@pytest.fixture
def mock_session(mocker):
    mock = mocker.patch("catalogo.crud.Session", autospec=True)
    return mock()


def test_crear_producto(mock_session):
    # Simulamos que la base de datos devuelve un objeto Producto con el id 1
    mock_producto = MagicMock(spec=Producto)
    mock_session.add.return_value = None
    mock_session.commit.return_value = None

    crear_producto("Té verde", "Caja de 20 bolsitas", 3.5, 15)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.close.assert_called_once()


def test_listar_productos(mock_session):
    # Simulamos la lista de productos
    mock_productos = [MagicMock(spec=Producto), MagicMock(spec=Producto)]
    mock_session.query.return_value.all.return_value = mock_productos

    productos = listar_productos()

    assert len(productos) == 2
    mock_session.query.assert_called_once()


def test_buscar_producto(mock_session):
    mock_producto = MagicMock(spec=Producto)
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_producto

    producto = buscar_producto(1)

    assert producto is mock_producto
    mock_session.query.assert_called_once()


def test_modificar_producto(mock_session):
    mock_producto = MagicMock(spec=Producto)
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_producto

    modificar_producto(1, nuevo_nombre="Nuevo nombre")

    assert mock_producto.nombre == "Nuevo nombre"
    mock_session.commit.assert_called_once()



def test_eliminar_producto(mock_session):
    mock_producto = MagicMock(spec=Producto)
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_producto

    eliminar_producto(1)

    mock_session.delete.assert_called_once()
    mock_session.commit.assert_called_once()
