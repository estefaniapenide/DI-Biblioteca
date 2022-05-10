import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import zipfile
import shutil
import os.path
import var

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDialogButtonBox


import var

class Calendario:

    def abrirCalendarioPrestamo(self):
        try:
            var.uiCalendarioPrestamo.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def abrirCalendarioDevolucion(self):
        try:
            var.uiCalendarioDevolucion.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def abrirCalendarioSancion(self):
        try:
            var.uiCalendarioSancion.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def cargarFechaDesde(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.textBrowserFechaDesde.setText(str(data))
            var.uiCalendarioPrestamo.hide()
        except Exception as error:
            print('Error cargar fecha prestamo: %' % str(error))

    def cargarFechaHasta(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.addDays(15).day(), qDate.addDays(15).month(), qDate.addDays(15).year()))
            var.ui.textBrowserFechaHasta.setText(str(data))
        except Exception as error:
            print('Error cargar fecha devolución: %s' % str(error))

    def cargarFechaDevolucion(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.textBrowserFechaDevolucion.setText(str(data))
            var.uiCalendarioDevolucion.hide()
        except Exception as error:
            print('Error cargar fecha devolución: %' % str(error))

    def cargarFechaSancion(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.textBrowserSancionHasta.setText(str(data))
            var.uiCalendarioSancion.hide()
        except Exception as error:
            print('Error cargar fecha sancion: %' % str(error))

class Aviso:

    def abrirVentanaAviso(self):
        try:
            var.uiAviso.show()
        except Exception as error:
            print('Error abrir aviso: %s' % str(error))

    def cerrarVentanaAviso(self):
        try:
            var.uiAviso.hide()
        except Exception as error:
            print('Error cerrar aviso: %s' % str(error))

    def mensajeVentanaAviso(mensaje):
        var.uiAviso.setText(mensaje)
        '''var.uiAviso.layout = QVBoxLayout()
        var.mensajeAviso = QLabel(mensaje)
        var.uiAviso.setLayout(var.uiAviso.layout)
        var.uiAviso.layout.addWidget(var.mensajeAviso)'''


class Salir:
    def salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error salir : %s " % str(error))

    def preguntaSalir(self):
        try:
            var.uiSalir.show()
            if var.uiSalir.exec():
                sys.exit()
            else:
                var.uiSalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))

class Comprimir:

    def BackupBaseDatos(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + 'BibliotecaDB.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.uiAbrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip',
                                                                    options=option)
            if var.uiAbrir.Accepted and filename != '':
                ficheroZip = zipfile.ZipFile(var.copia, 'w')
                ficheroZip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                ficheroZip.close()
                Aviso.mensajeVentanaAviso("BASE DE DATOS BIBLIOTECA COPIADA A ARCHIVO ZIP")
                Aviso.abrirVentanaAviso(self)
                shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print('Error al comprimir: %s' % str(error))

class Abrir:

    def abrirExplorador(self):
        try:
            var.uiAbrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))