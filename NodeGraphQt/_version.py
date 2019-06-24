__version__ = '0.0.7'
__status__ = 'Work in Progress'
__license__ = 'MIT'

__author__ = 'Johnny Chan'
__email__ = 'http://chantasticvfx.com/contact'

__module_name__ = 'NodeGraphQt'
__url__ = 'https://github.com/jchanvfx/NodeGraphQt'

__all__ = [
    'BackdropNode', 'BaseNode', 'Menu', 'MenuCommand', 'NodeGraph',
    'NodeObject', 'NodeTreeWidget', 'Port', 'PropertiesBinWidget',
    'constants', 'setup_context_menu'
]

try:
    from Qt import QtWidgets, QtGui, QtCore, QtCompat
except ImportError as ie:
    from .vendor.Qt import __version__ as qtpy_ver
    from .vendor.Qt import QtWidgets, QtGui, QtCore, QtCompat
    print('Cannot import "Qt.py" module falling back on '
        '"NodeGraphQt.vendor.Qt ({})"'.format(qtpy_ver))

from .base.graph import NodeGraph
from .base.node import NodeObject, BaseNode, BackdropNode
from .base.port import Port
from .base.menu import Menu, MenuCommand

# functions
from .base.actions import setup_context_menu

# widgets
from .widgets.node_tree import NodeTreeWidget
from .widgets.properties_bin import PropertiesBinWidget