import sys 
from PyQt5 import * #создадим приложение и передадим аргументы 
a = QApplication(sys.argv) #создание виджета #Первый аргумент – текст, который мы хотим увидеть. #Воторой аргумент – родительский виджет, #т.к. Hello – единственный виджет, то у него нет родителя 
hello = QLabel("Hello world!",None) #делаем виджет главным
a.setMainWidget(hello) #показать виджет 
hello.show(hello) #запустить приложение 
#a.exec_loop()