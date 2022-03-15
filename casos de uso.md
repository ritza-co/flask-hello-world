**Casos de uso:**


|<p>**CU01:**</p><p>**Registro del usuario al sistema.**</p>|
| :-: |
|**Descripción:**|El usuario, ya sea votante o administrador, deberá de ingresar su matrícula para ser identificado por el sistema.|
|**Actores:**|Usuarios votantes y administradores.|
|**Precondiciones:**|<p>-El usuario debe poseer su matrícula.</p><p>-El usuario debe de estar dado de alta en el sistema.</p>|
|**Secuencia normal:**|**Paso**|**Acción**|
||1|El usuario accederá a la página web.|
||2|Al acceder a la página web, aparecerá un mensaje dándole la bienvenida al usuario y pidiéndole que ingrese su matrícula para identificarlo, seguido de esto habrá un espacio de texto donde el usuario podrá ingresar su matrícula.|
||3|Una vez ingresado su matrícula, el usuario será identificado y redirigido a la pantalla principal que le corresponde según si es un administrador o un votante.|
||4|El usuario podrá salir de sesión simplemente cerrando la ventana o dándole clic al botón para salir sesión en la esquina superior izquierda, donde será redirigido a la página de inicio de sesión.|
|**Postcondiciones:**|El usuario al iniciar sesión será capaz de realizar funciones de votante o administrador, según sea su cuenta.|
|**Excepciones:**|**Paso**|**Acción.**|
||2|*Al acceder a la página web, aparecerá un mensaje dándole la bienvenida al usuario y pidiéndole que ingrese su matrícula para identificarlo, seguido de esto habrá un espacio de texto donde el usuario podrá ingresar su matrícula.*|
|||E.1|En caso de ingresar credenciales invalidas, el sistema enviara un mensaje en el que indique que la información es incorrecta, lo corrija e intente de nuevo.|
|**Comentarios:**|En el caso de la cuenta administrador, por el momento solo será una, tendrá acceso a ella solamente el equipo de desarrollo y para acceder a ella será a través de una cadena de caracteres que el equipo de desarrollo decida.|



|<p>**CU02:**</p><p>**Visualizar los candidatos al momento de votar y solo poder efectuar un voto.**</p>|
| :-: |
|**Descripción:**|El usuario podrá ver a los candidatos con su respectiva imagen y podrá emitir un único voto.|
|**Actores:**|Votantes.|
|**Precondiciones:**|El usuario ya autentificado debe encontrarse en la plataforma.|
|**Secuencia normal:**|**Paso**|**Acción**|
||1|El votante ingresa a la opción de votar.|
||2|El votante visualizará la imagen y el nombre de cada candidato. El nombre está dentro de un recuadro.|
||3|El votante selecciona el nombre del candidato por el cual desea votar.|
||4|El votante selecciona el recuadro que dice confirmar.|
||5|El sistema genera una ventana emergente que le advierte al usuario que solo puede votar una vez y le pide al usuario confirmar nuevamente su voto.|
||6|El votante confirma su voto.|
||7|El sistema redirige al usuario a la página principal.|
||8|El votante al intentar darle a la opción de votar este no podrá acceder.|
|**Postcondiciones:**|<p>1.- El voto se registró </p><p>2.- El usuario no está en la posibilidad de realizar otro voto.</p>|
|**Comentarios:**|Será una única imagen la que tendrá cada candidato.|



|<p>**CU03:**</p><p>**Iniciar y configurar una elección.**</p>|
| :-: |
|**Descripción:**|El administrador podrá crear una elección y configurar la misma al momento de crearla.|
|**Actores:**|Administradores.|
|**Precondiciones:**|El usuario ya debió de haberse autentificado como administrador.|
|**Secuencia normal:**|**Paso**|**Acción**|
||1|En la pantalla habrá un solo botón, el cual permitirá al administrador a ir a otra página.|
||2|En esa nueva página, tendrá las opciones de crear los candidatos, poner un tiempo límite de la elección, cancelar la elección y confirmar la creación de la misma, para cada opción hay un botón especifico.|
|||2.1|El administrador al interactuar con el botón de crear candidatos aparecerá una ventana emergente con una lista de los candidatos ya creados, un botón para confirmar cambios, un botón para cerrar la ventana y dos espacios para poner el nombre y la imagen del candidato.|
||||a)|El espacio de texto será de máximo 50 caracteres para el nombre.|
||||b)|El espacio para subir la imagen solo permitirá archivos de imagen .jpg y .png y con un tamaño menor a 5MB.|
||||c)|Al presionar el botón para cerrar la ventana, el administrador vuele al paso 2.|
||||d)|Al presionar el botón de confirmar, el nombre de candidato se guardará en la lista de candidatos.|
||||e)|En la lista de candidatos habrá un voto al lado de cada nombre para eliminar candidatos, cuando el candidato sea borrado se eliminará de la lista.|
|||2.2|Al presionar el botón de tiempo límite de la elección saldrá una ventana emergente con 3 campos de texto y un botón para confirmar cambios.|
||||a)|Los 3 campos de texto servirán para establecer los minutos, horas y días que durará específicamente la elección.|
||||b)|Al presionar el botón para confirmar los cambios el administrador vuelve al paso 2.|
|||2.3|Al presionar el botón de cancelar elección, el administrador será devuelto al paso 1.|
||3|Una vez ya ingresado los candidatos y el tiempo que durará la elección, el administrador pulsará el botón crear elección.|
||4|Al presionar el botón, aparecerá una ventana emergente que avisará al administrador que, una vez iniciada la elección, no se puede configurar.|
||5|El administrador presionara el botón de aceptar, esto ocasionara que sea devuelto a la pantalla principal y la elección empiece a estar en curso.|
||6|El botón para crear elección es sustituido por uno que dice “finalizar elección”.|
|**Postcondiciones:**|La elección ya está creada, en curso y ya no se puede configurar.|
|**Excepciones:**|Durante el proceso de creación de la elección, si el usuario pierde la conexión con la página web entonces el administrador tendrá que iniciar sesión de nuevo y empezar todo el proceso de nuevo|
||**Paso**|**Acción**|
||2.1 - d)|*Al presionar el botón de confirmar, el nombre de candidato se guardará en la lista de candidatos.*|
|||E.1|En caso de no haber un nombre en el espacio de texto, no se agregará nada a la lista.|
||2.2 - b)|*Al presionar el botón para confirmar los cambios el administrador vuelve al paso 2.*|
|||E.1|En caso de que en los espacios de texto haya caracteres que no sean números, saldrá un aviso al administrador indicando que solo debe ingresar números en ese espacio.|
||3|*Una vez ya ingresado los candidatos y el tiempo que durará la elección, el administrador pulsará el botón crear elección.*|
|||E.1|En caso de haber menos de dos candidatos, saldrá un mensaje indicando que la cantidad de candidatos es insuficiente para crear una elección.|
|**Comentarios:**|Solo se mantendrá una elección a la vez y solo habrá una cuenta administradora durante el desarrollo de este proyecto.|



|<p>**CU04:**</p><p>**Finalizar la elección.**</p>|
| :-: |
|**Descripción:**|El administrador podrá ingresar a la página web para finalizar manualmente una elección.|
|**Precondiciones:**|<p>1.-El administrador ya debió de haberse autentificado.</p><p>2.-Debe de estar en curso una elección.</p>|
|**Secuencia normal:**|**Paso**|**Acción**|
||**1**|En la pantalla principal del administrador habrá un botón para finalizar una elección.|
||**2**|El administrador al presionar ese botón recibirá una ventana emergente advirtiendo que, una vez finalizada la elección, se mostrarán los resultados y no podrán alterarse los mismos.|
||**3**|Al aceptar, la elección será finalizada y el administrador será llevado de vuelta a una pantalla principal con un botón para crear una elección.|
|**Excepciones:**|N/A|
|**Postcondiciones:**|<p>-La elección ha finalizado y se mostraran los resultados</p><p>-Se podrá crear una nueva elección pasadas las 24 horas de haber finalizado la anterior.</p>|
|**Comentarios:**|N/A|



|<p>**CU05:**</p><p>**Mostrar resultados de la elección.**</p>|
| :-: |
|**Descripción:**|Al finalizar la elección, el votante podrá visualizar la cantidad de votos de cada candidato de la elección y el ganador de la misma.|
|**Actores:**|Votantes.|
|**Precondiciones:**|<p>- La elección ha finalizado.</p><p>- No han transcurrido las 24 horas desde que finalizo la elección.</p>|
|**Secuencia normal:**|**Paso**|**Acción**|
||1|Posterior a registrarse, en la pantalla del votante aparecerá un botón para visualizar los resultados.|
||2|Al presionar el botón, el votante irá a una página donde se podrá ver una lista con los candidatos y la cantidad de votos que recibieron. La lista estará ordenada de mayor a menor cantidad de votos.|
||3|Cuando el votante este dentro de esta página, aparecerá una advertencia en la que se dirá que en un lapso de 24 horas ya no será posible ver los resultados.|
|**Postcondiciones:**|Una vez pasadas las 24 horas, ya no será posible ver los resultados de la elección.|
|**Excepciones:**|N/A|
|**Comentarios:**|N/A|
