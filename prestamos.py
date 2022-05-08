import eventos
import var
import conexion
from datetime import datetime
from dateutil.relativedelta import relativedelta

import ventanaAviso
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton


class Prestamos:

    def gestionMultas(prestamo):

        multa=False
        fmulta=None

        # pestamo=[numSocio,codLibro,desde,hasta,devuelto,fdevolucion]
        hasta = datetime.strptime(prestamo[3], "%d/%m/%Y")
        devuelto = prestamo[4]
        hoy = datetime.now()
        delta = relativedelta(days=+15)

        if prestamo[5] != '':
            fdevolucion = datetime.strptime(prestamo[5], "%d/%m/%Y")
            if devuelto =='True' and fdevolucion > hasta:
                multa=True
                fmulta = fdevolucion + delta
                fmulta = fmulta.strftime('%d/%m/%Y')
            print('Fecha devolucion: ', fdevolucion)

        if devuelto =='False' and hoy > hasta:
            multa = True
            fmulta = hoy + delta
            fmulta = fmulta.strftime('%d/%m/%Y')

        print('Multa: ',multa)
        print('Fecha multa: ',fmulta)

        conexion.Socios.gestionMulta(prestamo[0],str(multa),fmulta)




    def modificarPrestamo(self):
        devolucion=[str(var.ui.datoCodigoLibroDevolucion.text()),str(var.ui.lineEditFechaDevolucion.text())]
        if devolucion[0] !='' and devolucion[1]!='':
            if not conexion.Libros.libroDisponible(devolucion[0]):
                #pestamo=[numSocio,codLibro,desde,hasta,devuelto,fdevolucion]
                prestamo = conexion.Prestamos.obtenerPrestamoDevolucion(devolucion[0])
                conexion.Prestamos.modificarPrestamo(devolucion[0],devolucion[1])
                prestamo[4] = 'True'
                prestamo[5]=devolucion[1]
                print(prestamo)
                Prestamos.gestionMultas(prestamo)
                conexion.Socios.modificarNumeroLibrosSocio(prestamo[0], prestamo[4])
                conexion.Libros.modificarDisponibilidadLibro(prestamo[1],prestamo[4])
                conexion.Prestamos.mostrarPrestamos(self)
                conexion.Libros.mostrarLibros(self)
                conexion.Socios.mostrarSocios(self)
            else:
                print('EL LIBRO NO ESTÁ PRESTADO')
                eventos.Aviso.mensajeVentanaAviso('EL LIBRO NO ESTÁ PRESTADO')
                eventos.Aviso.abrirVentanaAviso(self)
        else:
            print('DEBE INTRODUCIR:\n-CÓSDIGO DEL LIBRO\n-\FECHA DE DEVOLUCIÓN')
            eventos.Aviso.mensajeVentanaAviso('DEBE INTRODUCIR:\n-CÓDIGO DEL LIBRO\n-FECHA DE DEVOLUCIÓN')
            eventos.Aviso.abrirVentanaAviso(self)




    def guardarPrestamo(self):
        if str(var.ui.datoNumeroSocioPrestamo.text())!='' and str(var.ui.datoCodigoLibroPrestamo.text())!='' and str(var.ui.lineEditFechaDesde.text())!='':
            var.ui.lineEditFechaDevolucion.setText('')
            prestamo = [var.ui.datoNumeroSocioPrestamo.text(), var.ui.datoCodigoLibroPrestamo.text(), var.ui.lineEditFechaDesde.text(), var.ui.textBrowserFechaHasta.toPlainText(), 'False',var.ui.lineEditFechaDevolucion.text()]

            if conexion.Libros.libroDisponible(prestamo[1]):
                if conexion.Socios.socioAptoPrestamo(prestamo[0]):
                    conexion.Prestamos.guardarPrestamo(prestamo)
                    Prestamos.gestionMultas(prestamo)
                    conexion.Socios.modificarNumeroLibrosSocio(prestamo[0],prestamo[4])
                    conexion.Libros.modificarDisponibilidadLibro(prestamo[1],prestamo[4])
                    conexion.Prestamos.mostrarPrestamos(self)
                    conexion.Libros.mostrarLibros(self)
                    conexion.Socios.mostrarSocios(self)
                else:
                    print('EL SOCIO TIENE MULTA O NO PUEDE PEDIR MÁS LIBROS PRESTADOS O EL NÚMERO DE SOCIO NO EXISTE')
                    eventos.Aviso.mensajeVentanaAviso("NO ES POSIBLE REGISTRAR EL PRÉSTAMO DEBIDO A:\n- EL SOCIO TIENE MULTA\n- EL SOCIO NO PUEDE PEDIR MÁS LIBROS PRESTADOS\n- EL NÚMERO DE SOCIO NO EXISTE")
                    eventos.Aviso.abrirVentanaAviso(self)
            else:
                print('EL LIBRO NO ESTÁ DISPONIBLE')
                eventos.Aviso.mensajeVentanaAviso('EL LIBRO NO ESTÁ DISPONIBLE')
                eventos.Aviso.abrirVentanaAviso(self)
        else:
            print('DEBE INTRODUCIR:\n-NÚMERO DE SOCIO\n-CÓDIGO DEL LIBRO\n-FECHA DE PRÉSTAMO')
            eventos.Aviso.mensajeVentanaAviso('DEBE INTRODUCIR:\n- NÚMERO DE SOCIO\n- CÓDIGO DEL LIBRO\n- FECHA DE PRÉSTAMO')
            eventos.Aviso.abrirVentanaAviso(self)


