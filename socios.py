import eventos
import var
from dni import Dni
from PyQt5.QtGui import QFont
import conexion

class Socios:

    def visibilidadFechaSancion(self):
        if var.multaSocio==True:
            Socios.mostrarFechaSancion(self)
        if var.multaSocio==False:
            Socios.esconderFechaSancion(self)

    def esconderFechaSancion(self):
        var.ui.textBrowserSancionHasta.setText('')
        var.ui.labelSancionHasta.setHidden(True)
        var.ui.textBrowserSancionHasta.setHidden(True)
        var.ui.pushButtonSancionHasta.setHidden(True)

    def mostrarFechaSancion(self):
        var.ui.labelSancionHasta.setHidden(False)
        var.ui.textBrowserSancionHasta.setHidden(False)
        var.ui.pushButtonSancionHasta.setHidden(False)

    def seleccionarMulta(self):
        try:
            if var.ui.radioButtonMultaSi.isChecked():
                #print('marcado si')
                var.multaSocio=True
            if var.ui.radioButtonMultaNo.isChecked():
                #print('marcado no')
                var.multaSocio=False
        except Exception as error:
            print('Error en módulo seleccionar multa:',error)

    def seleccionarSexo(self):
        try:
            if var.ui.radioButtonMujer.isChecked():
                #print('marcado mujer')
                var.sexoSocio='Mujer'
            if var.ui.radioButtonHombre.isChecked():
                #print('marcado hombre')
                var.sexoSocio='Hombre'
        except Exception as error:
            print('Error en módulo seleccionar sexo:',error)

    def seleccionarNumLibros(self):
        try:
            var.numLibrosSocio = var.ui.spinBoxNumLibros.value()
        except Exception as error:
            print('Error seleccionar numero de libros prestados: %s' % str(error))

    def validarDNI():
        try:
            dni=var.ui.lineEditDni.text()
            var.ui.lineEditDni.setText(dni.upper())
            if (len(dni) == 9):
                numero = ""
                i = 0
                while (i < 8):
                    numero = numero + dni[i]
                    i += 1
                letra = dni[8]
                letra=letra.upper()
                dniCorrecto = Dni(numero)
                if (dniCorrecto.letra == letra):
                    print("DNI CORRECTO")
                    #var.ui.tbEstado.setText("DNI CORRECTO")
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('V')
                    return True
                else:
                    print("DNI INCORRECTO")
                   # var.ui.tbEstado.setText("DNI INCORRECTO")
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('X')
                    return False
            else:
                print("DNI INCORRECTO")
                #var.ui.tbEstado.setText("DNI INCORRECTO")
                var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.labelValidarDni.setFont(QFont("Forte"))
                var.ui.labelValidarDni.setText('X')
                return False
        except Exception as error:
            print("Error validar dni: %s " % str(error))

    def guardarSocio(self):
        if Socios.validarDNI():
            try:
                socio = [var.ui.lineEditDni.text(), var.ui.lineEditNombre.text(), var.ui.lineEditApellidos.text(), var.ui.lineEditDireccion.text(), var.sexoSocio, str(var.multaSocio),var.ui.textBrowserSancionHasta.toPlainText(),str(var.numLibrosSocio)]

                conexion.Socios.guardarSocio(socio)
                eventos.Aviso.mensajeVentanaAviso("SOCIO AÑADIDO")
                eventos.Aviso.abrirVentanaAviso(self)
                Socios.buscarSocioDni(self)
                conexion.Socios.mostrarSocios(self)

            except Exception as error:
                #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
                print('Error guardar socio (socios): %s ' % str(error))
        else:
            eventos.Aviso.mensajeVentanaAviso("EL DNI INTRODUCIDO NO ES VÁLIDO")
            eventos.Aviso.abrirVentanaAviso(self)

    def modificarSocio(self):
        if Socios.validarDNI():
            try:
                socio = [var.ui.labelNumSocioGenerado.text(), var.ui.lineEditDni.text(), var.ui.lineEditNombre.text(), var.ui.lineEditApellidos.text(), var.ui.lineEditDireccion.text(), var.sexoSocio, str(var.multaSocio),var.ui.textBrowserSancionHasta.toPlainText(),str(var.numLibrosSocio)]
                if (conexion.Socios.existeSocioNumero(socio[0])):
                    conexion.Socios.modificarSocio(socio)
                    eventos.Aviso.mensajeVentanaAviso('SOCIO MODIFICADO')
                    eventos.Aviso.abrirVentanaAviso(self)
                    conexion.Socios.mostrarSocios(self)
                else:
                    print('NO EXISTE EL SOCIO')
                    if var.ui.labelNumSocioGenerado.text() == '':
                        print("NO HA INTRODUCIDO NINGÚN NÚMERO DE SOCIO")
                        eventos.Aviso.mensajeVentanaAviso("NO HA INTRODUCIDO NINGÚN NÚMERO DE SOCIO\nEN LA BARRA DE BÚSQUEDA")
                        eventos.Aviso.abrirVentanaAviso(self)
                        #var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                    else:
                        eventos.Aviso.mensajeVentanaAviso("NO EXISTE EL SOCIO '" + socio[0].text()+ "' EN LA BIBLIOTECA")
                        eventos.Aviso.abrirVentanaAviso(self)
                        print("NO EXISTE EL SOCIO " + socio[0].text()+ " EN LA BD")
                        #var.ui.tbEstado.setText("LIBRO CON CÓDIGO '" + libro[0].text()+ "' NO EXISTE EN LA BD")
            except Exception as error:
                #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
                print('Error modificando socio: %s' % str(error))
        else:
            eventos.Aviso.mensajeVentanaAviso("EL DNI INTRODUCIDO NO ES VÁLIDO")
            eventos.Aviso.abrirVentanaAviso(self)

    def eliminarSocio(self):
        try:
            numSocio = var.ui.labelNumSocioGenerado.text()
            if (conexion.Socios.existeSocioNumero(numSocio)):
                conexion.Socios.bajaSocio(numSocio)
                eventos.Aviso.mensajeVentanaAviso("SOCIO ELIMINADO")
                eventos.Aviso.abrirVentanaAviso(self)
                conexion.Socios.mostrarSocios(self)
                Socios.limpiarSocio(self)
                #var.ui.tbEstado.setText("CLIENTE DNI '" + dni + "' HA SIDO DADO DE BAJA")
            else:
                print('NO EXISTE EL SOCIO')
                if var.ui.labelNumSocioGenerado.text()=='':
                    print("NO HA INTRODUCIDO NINGÚN NÚMERO DE SOCIO")
                    eventos.Aviso.mensajeVentanaAviso("NO HA INTRODUCIDO NINGÚN NÚMERO DE SOCIO\nEN LA BARRA DE BÚSQUEDA")
                    eventos.Aviso.abrirVentanaAviso(self)
                    #var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                else:
                    print("SOCIO CON NÚMERO '" + numSocio + "' NO EXISTE EN LA BD")
                    eventos.Aviso.mensajeVentanaAviso("SOCIO CON NÚMERO '" + numSocio + "' NO EXISTE EN LA BIBLIOTECA")
                    eventos.Aviso.abrirVentanaAviso(self)
                    #var.ui.tbEstado.setText("LIBRO CON CÓDIGO '" + codigo + "' NO EXISTE EN LA BD")
        except Exception as error:
            print('Error eliminar socio: %s' % str(error))

    def buscarSocioNum(self):
        id = var.ui.lineEditNumeroSocio.text()
        if conexion.Socios.existeSocioNumero(id):
            conexion.Socios.buscarSocioNumero(id)

            Socios.limpiarSocio(self)

            var.ui.lineEditDni.setText(var.dni)
            var.ui.lineEditNumeroSocio.setText(str(var.numSocio))
            var.ui.labelNumSocioGenerado.setText(str(var.numSocio))
            var.ui.lineEditNombre.setText(var.nombre)
            var.ui.lineEditApellidos.setText(var.apellidos)
            var.ui.lineEditDireccion.setText(var.direccion)
            var.ui.spinBoxNumLibros.setValue(var.numLibros)
            var.ui.textBrowserSancionHasta.setText(var.fmulta)

            if (var.sexo == 'Mujer'):
                var.ui.radioButtonMujer.click()
            elif (var.sexo == 'Hombre'):
                var.ui.radioButtonHombre.click()

            if(var.multa=='True'):
                var.ui.radioButtonMultaSi.click()
            if(var.multa=='False'):
                var.ui.radioButtonMultaNo.click()


            var.ui.pushButtonModificarSocio.setHidden(False)
            var.ui.pushButtonEliminarSocio.setHidden(False)

            # var.ui.tbEstado.setText('CLIENTE DNI %s ENCONTRADO' % id)

        else:
            Socios.limpiarSocio(self)
            var.ui.lineEditNumeroSocio.setText(id)
            conexion.Socios.mostrarSocios(self)
            eventos.Aviso.mensajeVentanaAviso("NO EXISTE EL SOCIO")
            eventos.Aviso.abrirVentanaAviso(self)
            # var.ui.tbEstado.setText('CLIENTE DNI %s NO ENCONTRADO' % id)
            # var.ui.lineEditCodigo.setText(id)

    def buscarSocioDni(self):
        if Socios.validarDNI():
            dni = var.ui.lineEditDni.text()
            if conexion.Socios.existeSocioDni(dni):
                conexion.Socios.buscarSocioDni(dni)

                Socios.limpiarSocio(self)

                var.ui.lineEditDni.setText(var.dni)
                #var.ui.lineEditNumeroSocio.setText(str(var.numSocio))
                var.ui.labelNumSocioGenerado.setText(str(var.numSocio))
                var.ui.lineEditNombre.setText(var.nombre)
                var.ui.lineEditApellidos.setText(var.apellidos)
                var.ui.lineEditDireccion.setText(var.direccion)
                var.ui.spinBoxNumLibros.setValue(var.numLibros)
                var.ui.textBrowserSancionHasta.setText(var.fmulta)

                if (var.sexo == 'Mujer'):
                    var.ui.radioButtonMujer.click()
                elif (var.sexo == 'Hombre'):
                    var.ui.radioButtonHombre.click()

                if (var.multa == 'True'):
                    var.ui.radioButtonMultaSi.click()
                if (var.multa == 'False'):
                    var.ui.radioButtonMultaNo.click()

                var.ui.pushButtonModificarSocio.setHidden(False)
                var.ui.pushButtonEliminarSocio.setHidden(False)

                #var.ui.tbEstado.setText('CLIENTE DNI %s ENCONTRADO' % id)

            else:
                Socios.limpiarSocio(self)
                var.ui.lineEditDni.setText(dni)
                conexion.Socios.mostrarSocios(self)
                #var.ui.tbEstado.setText('CLIENTE DNI %s NO ENCONTRADO' % id)
                #var.ui.lineEditCodigo.setText(id)

    def limpiarSocio(self):

        var.ui.lineEditNumeroSocio.setText("")
        var.ui.labelNumSocioGenerado.setText("")
        var.ui.lineEditDni.setText("")
        var.ui.labelValidarDni.setText("")
        var.ui.lineEditNombre.setText("")
        var.ui.lineEditApellidos.setText("")
        var.ui.lineEditDireccion.setText("")
        Socios.esconderFechaSancion(self)

        var.ui.buttonGroupMulta.setExclusive(False)
        var.ui.radioButtonMultaNo.setChecked(True)
        var.ui.radioButtonMultaSi.setChecked(False)
        var.ui.buttonGroupMulta.setExclusive(True)

        var.ui.buttonGroupSexo.setExclusive(False)
        var.ui.radioButtonHombre.setChecked(False)
        var.ui.radioButtonMujer.setChecked(False)
        var.ui.buttonGroupSexo.setExclusive(True)

        var.ui.spinBoxNumLibros.setValue(0)

        var.ui.pushButtonModificarSocio.setHidden(True)
        var.ui.pushButtonEliminarSocio.setHidden(True)
