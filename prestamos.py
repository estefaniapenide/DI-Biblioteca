import var
import conexion
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Prestamos:

    def visibilidadFechaDevolucion(self):
        if var.devuelto==True:
            Prestamos.mostrarFechaDevolucion(self)
        if var.devuelto==False:
            Prestamos.esconderFechaDevolucion(self)

    def esconderFechaDevolucion(self):
        var.ui.lineEditFechaDevolucion.setText('')
        var.ui.labelFechaDevolucion.setHidden(True)
        var.ui.lineEditFechaDevolucion.setHidden(True)
        var.ui.pushButtonCalendarioDevolucion.setHidden(True)

    def mostrarFechaDevolucion(self):
        var.ui.labelFechaDevolucion.setHidden(False)
        var.ui.lineEditFechaDevolucion.setHidden(False)
        var.ui.pushButtonCalendarioDevolucion.setHidden(False)

    def seleccionarDevuelto(self):
        try:
            if var.ui.radioButtonDevueltoSi.isChecked():
                #print('marcado si')
                var.devuelto=True
            if var.ui.radioButtonDevueltoNo.isChecked():
                #print('marcado no')
                var.devuelto=False
        except Exception as error:
            print('Error en módulo seleccionar devuelto:',error)

    def gestionMultas(prestamo):
        try:
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
                print('Fecha devolucion: ', fdevolucion)

            if devuelto =='False' and hoy > hasta:
                multa = True
                fmulta = hoy + delta

            print('Multa: ',multa)
            print('Fecha multa: ',fmulta)

            # Actualizar las multas y la fecha de sanción ene el socio!!


            #actualizar los datos del socio y del libro(ver como hacer lo del libro)#Creo que ya lo controlé en guardar prestamo

        except Exception as error:
            print('Excepcion gestion multa: ',str(error))

    #cuando haga el meétdo para modificar un préstamo, hacerlo de manera que solo se va pedir el codlibro, devuelto (como false)
    #y que solo modificará el devuelto y la fecha de devolucion


    def guardarPrestamo(self):
        try:
            prestamo = [var.ui.datoNumeroSocioPrestamo.text(), var.ui.datoCodigoLibroPrestamo.text(), var.ui.lineEditFechaDesde.text(), var.ui.textBrowserFechaHasta.toPlainText(), str(var.devuelto), var.ui.lineEditFechaDevolucion.text()]

            if conexion.Libros.libroDisponible(prestamo[1]):
                if conexion.Socios.socioAptoPrestamo(prestamo[0]):
                    conexion.Prestamos.guardarPrestamo(prestamo)
                    Prestamos.gestionMultas(prestamo)
                    conexion.Socios.modificarNumeroLibrosSocio(prestamo[0],prestamo[4])  # Pendiente revisar que funciona bien
                    conexion.Libros.modificarDisponibilidadLibro(prestamo[1],prestamo[4])  # Pendiente revisar que funciona bien
                    conexion.Prestamos.mostrarPrestamos(self)
                    conexion.Libros.mostrarLibros(self)
                    conexion.Socios.mostrarSocios(self)
                else:
                    print('EL SOCIO TIENE MULTA O EL NÚMERO DE SOCIO NO EXISTE O NO PUEDE PEDIR MÁS LIBROS PRESTADOS')
            else:
                print('EL LIBRO NO ESTÁ DISPONIBLE')

        except Exception as error:
            #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
            print('Error guardar prestamo (prestamos): %s ' % str(error))

