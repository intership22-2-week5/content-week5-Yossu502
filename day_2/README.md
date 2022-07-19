## Ejercicio DE POO aplicando Django Rest Framework

Hacer un diagrama de clases para modelar un portafolio de obras de arte. Cada obra tiene un tipo (escultura, pintura, video,…), uno o más autores, una fecha de creación, un valor estimado. Adicionalmente cada obra tiene asociado un conjunto de fotografías y/o videos para exhibirla en el portafolio. A partir del portafolio se crean exposiciones de las obras en galerías. Cada exposición tiene unas fechas, un lugar y una descripción. Para una exposición se selecciona un conjunto de obras el portafolio que se van a presentar.

**Solucion**

Para esta parte se utilizaron 4 Clases:

1. Clase Autores

![Codigo Autores](./assets/autorescode.png)

2. Clase Obra de Arte

![Codigo Autores](./assets/obradeartecode.png)

3. Clase Exposicion

![Codigo Autores](./assets/exposicioncode.png)

4. Clase Portafolio

![Codigo Autores](./assets/portafoliocode.png)

### Peticion desde Swagger, Postman y Django

1. Autores

Django

* Obtener todos los autores
![Get](./assets/autoresgetall.png)

* Obtener un autor
![Get](./assets/djangogetone.png)

* Publica un autor
![Get](./assets/djangoauthorpost.png)

* Actualizar un autor
![Get](./assets/djangoauthorupdate.png)

* Eliminar un autor
![Get](./assets/djangoauthordelete.png)

Swagger 

* Todas las funcionalidades
![Get](./assets/swaggerautor.png)

Postman

* Obtener todos los autores
![Get](./assets/postamgetautor.png)

* Obtener un autor
![Get](./assets/postgetoneautor.png)

* Publica un Autor
![Get](./assets/postampostautor.png)

* Actualizar un Autor
![Get](./assets/postmanupdateautor.png)

* Eliminar un Autor
![Get](./assets/postamndeleteautor.png)

2. Obras de Arte

Django

* Obtener todos las obras
![Get](./assets/getobras.png)

* Obtener una obra
![Get](./assets/getoneobra.png)

* Publica una obra
![Get](./assets/postobra.png)

* Actualizar una obra
![Get](./assets/updateobra.png)

* Eliminar una obra
![Get](./assets/deleteobra.png)

Swagger 

* Todas las funcionalidades
![Get](./assets/swaggerobras.png)

3. Exposiciones

Django

* Obtener todos las exposiciones
![Get](./assets/getallexpo.png)

* Obtener una exposicion
![Get](./assets/getoneexpo.png)

* Publica una exposicion
![Get](./assets/postexpo.png)

* Actualizar una Exposicion
![Get](./assets/updateexpo.png)

* Eliminar una Exposicion
![Get](./assets/deleteexpo.png)

Swagger 

* Todas las funcionalidades
![Get](./assets/swaggerexpo.png)


4. Portafolio 

Django

* Obtener todos los Portafolios
![Get](./assets/getporta.png)

* Obtener un Portafolios
![Get](./assets/getoneporta.png)

* Publica un Portafolios
![Get](./assets/postporta.png)

* Actualizar un Portafolios
![Get](./assets/updateporta.png)

* Eliminar un Portafolios
![Get](./assets/deleteporta.png)

Swagger 

* Todas las funcionalidades
![Get](./assets/swaggerporta.png)