
try:
    from Qt import QtWidgets, QtGui, QtCore, QtCompat
except ImportError as ie:
    from .vendor.Qt import __version__ as qtpy_ver
    from .vendor.Qt import QtWidgets, QtGui, QtCore, QtCompat
    print('Cannot import "Qt.py" module falling back on '
        '"NodeGraphQt.vendor.Qt ({})"'.format(qtpy_ver))