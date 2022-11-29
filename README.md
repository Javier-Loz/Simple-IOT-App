# TE2004B
Sistema contra robo de  vehículos

## Objetivo
Desarrollar un sistema con dos cámaras de video, las cuales monitorearán el  interior del vehículo,
en específico a la persona
que está conduciendo. 
El sistema iniciará cuando el usuario entre al
vehículo, las cámaras integradas al sistema capturarán la imagen del conductor cada 30
segundos y un sistema comparará la imagen con los registros de 5 personas que están autorizadas
para manejar el coche y cuyos números de celular se encuentran registrados. 

En caso que la
persona al volante no esté registrada en el sistema, este deberá de enviar una alerta a los
celulares de las personas autorizadas. En el mensaje se deberá de incluir la ubicación del
vehículo así como la foto de quien está conduciendo el coche. El sistema deberá de tener una
opción de Valet parking para desactivar el sistema cuando se deja en un estacionamiento.

## Solución Propuesta
El diseño propuesto funcionará a partir de dos componentes principales, un microcontrolador
que tome las fotografías de la persona al interior del vehículo con conexión a internet y un dispositivo que aloje la base de datos
con las personas registradas, procese la imagen generada y determine si la persona tiene permitido manejar el  vehículo. 

### Componentes
- Microcontrolador: ESP-32
- Cámara: OV2640
- Host: Raspberry Pi 4 

### Diagrama de bloques de la solución propuesta

<img src="imgs/savi_bloques.png" alt="Diagrama de Bloques">


## Funcionamiento 
Dentro de la Raspberry Pi se alojará la base de datos con las imágenes de las personas registradas, las imágenes generadas por 
el ESP-32 y el estatus de identificación de la persona. 
El ESp-32, en su versión "-cam", tomará la fotografía en formato ".png" y hará una solicitud para almacenar la imagen debtro de la base de datos, 
además hará una pétición del estatus de identificación de la imagen y controlará el actuador.


