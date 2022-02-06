Para utilizar este programa se recomienda un virtualenv de python, aunque no es necesario para su correcto funcionamiento.

El único requerimiento para este programa es numpy en su versión 1.22.1

Al iniciar el programar se pedirán una serie de parametros para configurar el sistema que se desea representar.
Una vez culminada esta etapa se llega al menu principal en donde se pueden realizar las siguientes acciones:

(1)Convertir un número real del dominio en bits

	Pide como entrada un individuo (conjunto de valores) del sistema y devuelve como salida el string de bits que representan al individuo dentro del sistema

(2)Convertir un conjunto de bits en un número real del dominio

	Pide como entrada un conjunto de bits (representación del individuo) y devuelve los valores reales de dicha representación 

(3)Mostrar Variables

	Muestra la configuración de las variables insertadas dentro del sistema

(4)Reprogramar variables

	Permite reconfigurar las variables insertadas dentro del sistema (vuelve a correr el inicio del programa)

(5)Salir

	Permite salir del programa

Cabe aclarar que no se utilizó ningún tipo de almacenamiento para el sistema, por lo cual una mejora a futuro podría ser la implementación de un crud y una db para 
almacenar las variables insertadas dentro del sistema.