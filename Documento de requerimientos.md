Resumen: Prototipo de un sistema de votación basado en la tecnología blockchain para la elección de un representante del aula.

Método de priorización: MosCow

**Requerimientos funcionales.**



|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RF1|Visualizar los candidatos al momento de votar y solo poder efectuar un voto.|Must|
|RF2|El administrador podrá crear y configurar una elección.|Must|
|RF3|El administrador podrá finalizar una elección.|Must|
|RF4|Mostrar en pantalla al candidato ganador cuando haya finalizado la elección.|Must|
|RF5|Eliminar candidatos de la elección en el transcurso de la misma.|Should|
|RF6|Visualizar al final de la elección la cantidad de votos total o en porcentaje por candidato|Should|
|RF7|Permitir ingresar tanto información como imágenes del candidato.|Should|
|RF8|Visualizar la cantidad de votos por candidato en el transcurso de la elección.|Could|
|RF9|En caso de empate, repetir la votación únicamente con los candidatos más votados. |Could|


**Requerimientos no funcionales.**

|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RNF1|El voto se podrá efectuar desde cualquier computadora.|Must|
|RNF2|Validación de la Blockchain|Must|
|RNF3|Registrar la cantidad de votos por candidato en cada elección. |Must|
|RNF3|Mantener la votación anónima.|Must|
|RNF4|La interfaz para votar será estética y amigable para el usuario.|Should|






**Casos de uso:**

**CU01:** El usuario se registrará para acceder al sistema**.**

**Descripción:** El usuario, ya sea votante o administrador, deberá de ingresar su matrícula para ser identificado por el sistema.

**Precondiciones:**

-El usuario debe poseer su matrícula.

-El usuario debe de estar dado de alta en el sistema.

**Secuencia normal:**

**P1**  El usuario accederá a la página web.

**P2** Al acceder a la página web, aparecerá un mensaje dándole la bienvenida al usuario y pidiéndole que ingrese su matrícula para identificarlo, seguido de esto habrá un espacio de texto donde el usuario podrá ingresar su matrícula.

**P3** Una vez ingresado su matrícula, el usuario será identificado y redirigido a la pantalla principal que le corresponde según si es un administrador o un votante.

**P4** El usuario podrá salir de sesión simplemente cerrando la ventana o dándole clic al botón para salir sesión en la esquina superior izquierda, donde será redirigido a la página de inicio de sesión.

**Postcondiciones:**

-El usuario al iniciar sesión será capaz de realizar funciones de votante o administrador, según sea su cuenta.

**Excepciones.**

**P2** En caso de ingresar credenciales invalidas, el sistema enviara un mensaje en el que indique que la información es incorrecta, lo corrija e intente de nuevo.

**Comentarios.**

En el caso de la cuenta administrador, por el momento solo será una, tendrá acceso a ella solamente el equipo de desarrollo y para acceder a ella será a través de una cadena de caracteres que el equipo de desarrollo decida.

**CU02**: Visualizar los candidatos al momento de votar y solo poder efectuar un voto.

**Descripción:**  El usuario podrá ver a los candidatos con su respectiva imagen y podrá emitir un único voto.

**Actores:** El usuario 

**Precondiciones:** El usuario ya autentificado debe encontrarse en la plataforma. 

**Secuencia normal:**

**P1:** El votante ingresa a la opción de votar.

**P2:** El votante visualizará la imagen y el nombre de cada candidato. El nombre está dentro de un recuadro.

**P3:** El votante selecciona el nombre del candidato por el cual desea votar.

**P4**: El votante selecciona el recuadro que dice confirmar.

**P5:** El sistema genera una ventana emergente que le advierte al usuario que solo puede votar una vez y le pide al usuario confirmar nuevamente su voto.

**P6:** El votante confirma su voto.

**P7:** El sistema redirige al usuario a la página principal.

**P8:** El votante al intentar darle a la opción de votar este no podrá acceder.

**Postcondiciones:** 

1.- El voto se registró 

2.- El usuario no está en la posibilidad de realizar otro voto.

**Comentarios:**

Será una única imagen la que tendrá cada candidato.

**CU03:**  Iniciar y configurar una elección.

**Descripción:** El administrador podrá crear una elección y configurar la misma al momento de crearla.

**Precondiciones:** 

El usuario ya debió de haberse autentificado como administrador.

**Secuencia normal:**

**P1** En la pantalla habrá un solo botón, el cual permitirá al administrador a ir a otra página.

**P2** En esa nueva página, tendrá las opciones de crear los candidatos, poner un tiempo límite de la elección, cancelar la elección y confirmar la creación de la misma, para cada opción hay un botón especifico.

**P2.1** El administrador al interactuar con el botón de crear candidatos aparecerá una 	ventana emergente con una lista de los candidatos ya creados, un botón para confirmar 	cambios, un botón para cerrar la ventana y dos espacios para poner el nombre y la 	imagen del candidato.

a) El espacio de texto será de máximo 50 caracteres para el nombre.

b) El espacio para subir la imagen solo permitirá archivos de imagen .jpg y .png y 		con un tamaño menor a 5MB.

c) Al presionar el botón para cerrar la ventana, el administrador vuele a **P2.**

d) Al presionar el botón de confirmar, el nombre de candidato se guardará en la 		lista de candidatos.** 

e) En la lista de candidatos habrá un boto al lado de cada nombre para eliminar 		candidatos, cuando el candidato sea borrado se eliminará de la lista.

**P2.2** Al presionar el botón de tiempo límite de la elección saldrá una ventana emergente 	con 3 campos de texto y un botón para confirmar cambios.

a) Los 3 campos de texto servirán para establecer los minutos, horas y días que 		durará específicamente la elección.

b) Al presionar el botón para confirmar los cambios el administrador vuelve a P2.

**P2.3** Al presionar el botón de cancelar elección, el administrador será devuelto a P1.

**P3** Una vez ya ingresado los candidatos y el tiempo que durará la elección, el administrador pulsará el botón crear elección.

**P4** Al presionar el botón, aparecerá una ventana emergente que avisará al administrador que, una vez iniciada la elección, no se puede configurar.

**P5** El administrador presionara el botón de aceptar, esto ocasionara que sea devuelto a la pantalla principal y la elección empiece a estar en curso.

**P6** El botón para crear elección es sustituido por uno que dice “finalizar elección”.

**Postcondiciones:**

` `La elección ya está creada y ya no se puede configurar.

**Excepciones:**

-Durante el proceso de creación de la elección, si el usuario pierde la conexión con la página web entonces el administrador tendrá que iniciar sesión de nuevo y empezar todo el proceso de nuevo

**P2.1 d)** En caso de no haber un nombre en el espacio de texto, no se agregará nada a la lista.

**P2.2 b)** En caso de que en los espacios de texto haya caracteres que no sean números, saldrá un aviso al administrador indicando que solo debe ingresar números en ese espacio.

**P3** En caso de haber menos de dos candidatos, saldrá un mensaje indicando que la cantidad de candidatos es insuficiente para crear una elección.

**Comentarios:**

Solo se mantendrá una elección a la vez y solo habrá una cuenta administradora por el momento.

**CU04:** Finalizar la elección

**Descripción:** El administrador podrá ingresar a la página web para finalizar manualmente una elección.

**Precondiciones:**

**1.-**El administrador ya debió de haberse autentificado.

**2.-**Debe de estar en curso una elección.

**Secuencia normal:**

**P1** En la pantalla principal del administrador habrá un botón para finalizar una elección.

**P2** El administrador al presionar ese botón recibirá una ventana emergente advirtiendo que, una vez finalizada la elección, se mostrarán los resultados y no podrán alterarse los mismos.

**P3** Al aceptar, la elección será finalizada y el administrador será llevado de vuelta a una pantalla principal con un botón para crear una elección. 

**Postcondiciones:**

-La elección ha finalizado y se mostraran los resultados

-Se podrá crear una nueva elección pasadas las 24 horas de haber finalizado la anterior.

**CU05:** Mostrar resultados de la elección.

**Descripción:** Al finalizar la elección, el votante podrá visualizar la cantidad de votos de cada candidato de la elección y el ganador de la misma.

**Precondiciones:**

-La elección ha finalizado.

\- No han transcurrido las 24 horas desde que finalizo la elección

**Secuencia normal:**

**P1** Posterior a registrarse, en la pantalla del votante aparecerá un botón para visualizar los resultados.

**P2** Al presionar el botón, el votante irá a una página donde se podrá ver una lista con los candidatos y la cantidad de votos que recibieron. La lista estará ordenada de mayor a menor cantidad de votos.

**P3** Cuando el votante este dentro de esta página, aparecerá una advertencia en la que se dirá que en un lapso de 24 horas ya no será posible ver los resultados. 

**Postcondiciones:**

-Una vez pasadas las 24 horas, ya no será posible ver los resultados de la elección.
