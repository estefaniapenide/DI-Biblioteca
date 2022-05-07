import eventos
import var
import conexion
from datetime import datetime
from dateutil.relativedelta import relativedelta

import ventanaAviso


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




    def guardarPrestamo(self):
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
                eventos.Aviso.abrirVentanaAviso(self)
                #ventanaAviso.Ui_DialogAviso.labelInfo.setText(2)
                #var.uiAviso.labelInfo.setText('EL SOCIO TIENE MULTA NO PUEDE PEDIR MÁS LIBROS PRESTADOS EL NÚMERO DE SOCIO NO EXISTE')
                #var.uiAviso.pushButtonOK.clicked.connect(eventos.Aviso.cerrarVentanaAviso)
        else:
            print('EL LIBRO NO ESTÁ DISPONIBLE')


