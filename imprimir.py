from reportlab.pdfgen import canvas
import os
import var
from PyQt5 import QtWidgets, QtSql
from datetime import datetime

class Imprimir():

    def pie(self):
        try:
            var.rep.line(45,45,525,45)
            fecha= datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique',size=7)
            var.rep.drawString(460,35,str(fecha))
            var.rep.drawString(275, 35, str('Página %s' % var.rep.getPageNumber()))
            #var.rep.drawString(45, 35, str(textlistado))
        except Exception as error:
            print('Error pie informe: %s' % str(error))


    def cabecera(titulo):
        try:
            var.rep.setTitle('INFORMES %s' % titulo)
            var.rep.setAuthor('IES Teis')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45,810,525,810)
            var.rep.line(45,745,525,745)
            textnom='BIBLIOTECA IES TEIS'
            textdir='Avenida Galicia, 101 - Vigo'
            texttlfo='886 12 04 04'
            var.rep.drawString(50,790, textnom)
            var.rep.drawString(50,775, textdir)
            var.rep.drawString(50,760, texttlfo)
            #var.rep.drawImage(logo,450,752)
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE %s' % titulo
            var.rep.drawString(240, 695, textlistado)
        except Exception as error:
            print('Error cabecera informe prestamos: %s' % str(error))

    def cuerpoPrestamos(self):
        try:
            itemCli=['NUM SOCIO', 'COD LIBRO', 'DESDE','HASTA']
            var.rep.setFont('Helvetica-Bold', size=9)
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(65,667,itemCli[0])
            var.rep.drawString(190, 667, itemCli[1])
            var.rep.drawString(330, 667, itemCli[2])
            var.rep.drawString(445, 667, itemCli[3])
            var.rep.line(45,660,525,660)
            query = QtSql.QSqlQuery()
            query.prepare('select numSocio, codLibro, desde, hasta from prestamos order by devuelto')
            if query.exec_():
                i=50
                j=645
                cont=0
                while query.next():
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i,j, str(query.value(0)))
                    var.rep.drawString(i+130, j, str(query.value(1)))
                    var.rep.drawString(i+280, j, str(query.value(2)))
                    var.rep.drawString(i+400, j, str(query.value(3)))
                    j=j-30
                    cont=cont+1
                    if (cont == 20):
                        Imprimir.pie(self)
                        var.rep.showPage()
                        i=50
                        j=745
                        var.rep.setFont('Helvetica-Bold', size=9)
                        var.rep.line(45, 790, 525, 790)
                        var.rep.drawString(65, 777, itemCli[0])
                        var.rep.drawString(190, 777, itemCli[1])
                        var.rep.drawString(330, 777, itemCli[2])
                        var.rep.drawString(445, 777, itemCli[3])
                        var.rep.line(45, 770, 525, 770)
                        cont = 0
                Imprimir.pie(self)
        except Exception as error:
            print('Error cuerpo informe prestamos: %s' % str(error))




    def informePrestamos(self):
        try:
            var.rep = canvas.Canvas('Listado_prestamos.pdf')
            Imprimir.cabecera('PRÉSTAMOS')
            Imprimir.cuerpoPrestamos(self)
            var.rep.save()
            rootPath=".\\"
            cont =0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error informePrestamos %s' % str(error))



    def cuerpoLibros(self):
        try:
            itemCli = ['CÓDIGO', 'ESTADO', 'TÍTULO', 'AUTOR']
            var.rep.setFont('Helvetica-Bold', size=9)
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(65, 667, itemCli[0])
            var.rep.drawString(190, 667, itemCli[1])
            var.rep.drawString(330, 667, itemCli[2])
            var.rep.drawString(445, 667, itemCli[3])
            var.rep.line(45, 660, 525, 660)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, estado, titulo, autor from libros order by codigo')
            if query.exec_():
                i = 50
                j = 645
                cont = 0
                while query.next():
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 130, j, str(query.value(1)))
                    var.rep.drawString(i + 280, j, str(query.value(2)))
                    var.rep.drawString(i + 400, j, str(query.value(3)))
                    j = j - 30
                    cont = cont + 1
                    if (cont == 20):
                        Imprimir.pie(self)
                        var.rep.showPage()
                        i = 50
                        j = 745
                        var.rep.setFont('Helvetica-Bold', size=9)
                        var.rep.line(45, 790, 525, 790)
                        var.rep.drawString(65, 777, itemCli[0])
                        var.rep.drawString(190, 777, itemCli[1])
                        var.rep.drawString(330, 777, itemCli[2])
                        var.rep.drawString(445, 777, itemCli[3])
                        var.rep.line(45, 770, 525, 770)
                        cont = 0
                Imprimir.pie(self)
        except Exception as error:
            print('Error cuerpo informe libros: %s' % str(error))

    def informeLibros(self):
        try:
            var.rep = canvas.Canvas('Listado_libros.pdf')
            Imprimir.cabecera('LIBROS')
            Imprimir.cuerpoLibros(self)
            var.rep.save()
            rootPath = ".\\"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error informeLibros %s' % str(error))


    def cuerpoSocios(self):
        try:
            itemCli = ['NUM SOCIO', 'DNI', 'MULTA', 'SANCIÓN']
            var.rep.setFont('Helvetica-Bold', size=9)
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(65, 667, itemCli[0])
            var.rep.drawString(190, 667, itemCli[1])
            var.rep.drawString(330, 667, itemCli[2])
            var.rep.drawString(445, 667, itemCli[3])
            var.rep.line(45, 660, 525, 660)
            query = QtSql.QSqlQuery()
            query.prepare('select numSocio, dni, multa, fmulta from socios order by multa desc')
            if query.exec_():
                i = 50
                j = 645
                cont = 0
                while query.next():
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 130, j, str(query.value(1)))
                    var.rep.drawString(i + 280, j, str(query.value(2)))
                    var.rep.drawString(i + 400, j, str(query.value(3)))
                    j = j - 30
                    cont = cont + 1
                    if (cont == 20):
                        Imprimir.pie(self)
                        var.rep.showPage()
                        i = 50
                        j = 745
                        var.rep.setFont('Helvetica-Bold', size=9)
                        var.rep.line(45, 790, 525, 790)
                        var.rep.drawString(65, 777, itemCli[0])
                        var.rep.drawString(190, 777, itemCli[1])
                        var.rep.drawString(330, 777, itemCli[2])
                        var.rep.drawString(445, 777, itemCli[3])
                        var.rep.line(45, 770, 525, 770)
                        cont = 0
                Imprimir.pie(self)
        except Exception as error:
            print('Error cuerpo informe libros: %s' % str(error))

    def informeSocios(self):
        try:
            var.rep = canvas.Canvas('Listado_socios.pdf')
            Imprimir.cabecera('SOCIOS')
            Imprimir.cuerpoSocios(self)
            var.rep.save()
            rootPath = ".\\"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error informeLibros %s' % str(error))