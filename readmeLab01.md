Editor.md
Open source online Markdown editor.

TABLA DE CONTENIDO
1.-Objetivo del proyecto.
​
2.-Esquema preliminar del trabajo a realizar.
​
3.-Lista de Herramientas a utilizar.
​
4.-Plan de Acción.
​
5.-Conclusiones y recomendaciones al cliente.
​
6.- Anexos.
​
Notebook de Python- EDA.
Backup de la base de datos.
Notebook del API.
​

1,-OBJETIVO
​
El proyecto individual tiene como finalidad realizar las tareas de un perfil de Data Engineer.
​
Las fuentes entregadas para el inicio de esta tarea son archivos CSV y Json, que contienen información de las películas y series que ofrecen las plataformas de Streaming.
​
El reto es realizar el análisis exploratorio de datos (EDA), las tareas de ETL y disponibilizar las consultas en una API, para realizar comparaciones entre plataformas, donde se detallan 4 consultas principales:
​
Films con máxima duración por plataforma y por Año.
Cantidad de películas y series por plataforma.
Cantidad de películas por género y plataforma.
El actor que tiene más películas registradas en el servicio de streaming por plataforma y año.

.

2.-ESQUEMA PRELIMINAR DE TRABAJO A REALIZAR
​
​
​
​
*se anexa imagen.

LISTA DE HERRAMIENTAS A UTILIZAR
Python, Pandas, Sqlalchemy.
Mysql.
Docker desktop para Windows.
FastAPI.
​

IMPLEMENTACIONES DENTRO DE DOCKER FILE PARA FUNCIONAMIENTO DEL API
anyio==3.6.2
TABLA DE CONTENIDO
1.-Objetivo del proyecto.

2.-Esquema preliminar del trabajo a realizar.

3.-Lista de Herramientas a utilizar.

4.-Plan de Acción.

5.-Conclusiones y recomendaciones al cliente.

6.- Anexos.

 Notebook de Python- EDA.
 Backup de la base de datos.
 Notebook del API.
1,-OBJETIVO
El proyecto individual tiene como finalidad realizar las tareas de un perfil de Data Engineer.

Las fuentes entregadas para el inicio de esta tarea son archivos CSV y Json, que contienen información de las películas y series que ofrecen las plataformas de Streaming.

El reto es realizar el análisis exploratorio de datos (EDA), las tareas de ETL y disponibilizar las consultas en una API, para realizar comparaciones entre plataformas, donde se detallan 4 consultas principales:

Films con máxima duración por plataforma y por Año.
Cantidad de películas y series por plataforma.
Cantidad de películas por género y plataforma.
El actor que tiene más películas registradas en el servicio de streaming por plataforma y año.
.

2.-ESQUEMA PRELIMINAR DE TRABAJO A REALIZAR
*se anexa imagen.

LISTA DE HERRAMIENTAS A UTILIZAR
Python, Pandas, Sqlalchemy.
Mysql.
Docker desktop para Windows.
FastAPI.
IMPLEMENTACIONES DENTRO DE DOCKER FILE PARA FUNCIONAMIENTO DEL API
anyio==3.6.2
charset-normalizer==2.1.1
click==8.1.3
colorama==0.4.6
docopt==0.6.2
fastapi==0.88.0
greenlet==2.0.1
h11==0.14.0
idna==3.4
mysql==0.0.3
mysqlclient==2.1.1
pipreqs==0.4.11
pydantic==1.10.2
PyMySQL==1.0.2
requests==2.28.1
sniffio==1.3.0
SQLAlchemy==1.4.44
starlette==0.22.0
typing_extensions==4.4.0
urllib3==1.26.13
uvicorn==0.20.0
wincertstore==0.2
yarg==0.1.9
4.- PLAN DE ACCION
4.1.- Trabajo de EDA a través de Python.

Utilización de Pandas para Carga de datos y limpieza, se analiza tabla por tabla con las siguientes premisas:
Eliminación de columnas no significativas para las consultas.
Llenado de datos por ‘No dato’ en nulo para columnas relevantes, que serán informadas al cliente.
Separación de datos relevantes para las consultas y normalización
Creación de índices y columnas de clasificación de plataforma
Concatenación de tablas y extracción de maestros de actores y géneros.
Utilización de Sqlalchemy para la carga a Mysql.
*Nota. - detalle y documentación anexo 6.1

4.2.- Carga de tablas a Mysql, preparación de consultas. Revisión de la información, preparación y verificación de las consultas(modelado).
4.3.-Instalacion de Docker desktop para Windows.
4.4. Instalación de FastAPI donde se organiza:
App que contiene las librerías :

Config,
Models,
Router
En router se detallan la lógica de las consultas para que son visualizadas a través del localhost

5.- CONCLUSIONES Y RECOMENDACIONES
En la base de Hulu en la columna Rating se encontró información duraciones de películas/serie. No se procedió a realizar la modificación, ya que se validó los resultados pruebas sin modificaciones.
Analizar y completar el llenado de otros campos, como por ejemplo Rating, que es una buena medida para análisis de plataformas.
6.- REVISAR DOCUMENTACION ANEXA

Example
<link rel="stylesheet" href="editormd/css/editormd.css" />
<div id="test-editor">
    <textarea style="display:none;">### Editor.md

**Editor.md**: The open source embeddable online markdown editor, based on CodeMirror & jQuery & Marked.
    </textarea>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="editormd/editormd.min.js"></script>
<script type="text/javascript">
    $(function() {
        var editor = editormd("test-editor", {
            // width  : "100%",
            // height : "100%",
            path   : "editormd/lib/"
        });
    });
</script>Copy
More Examples >>

Features
Support Standard Markdown / CommonMark and GFM(GitHub Flavored Markdown);
Full-featured: Real-time Preview, Image (cross-domain) upload, Preformatted text/Code blocks/Tables insert, Code fold, Search replace, Read only, Themes, Multi-languages, L18n, HTML entities, Code syntax highlighting...;
Markdown Extras : Support ToC (Table of Contents), Emoji, Task lists, @Links...;
Support TeX (LaTeX expressions, Based on KaTeX), Flowchart and Sequence Diagram of Markdown extended syntax;
Support identification, interpretation, fliter of the HTML tags;
Support AMD/CMD (Require.js & Sea.js) Module Loader, and Custom/define editor plugins;
Compatible with all major browsers (IE8+), compatible Zepto.js and iPad;
Support Custom theme styles;
Download & install
Latest version: v1.5.0，Update: 2015-06-09



 


Or NPM install:

npm install editor.md



Or Bower install:

bower install editor.md




Change logs:

CHANGES

Dependents
Projects :

CodeMirror
marked
jQuery
FontAwesome
github-markdown.css
KaTeX
Rephael.js
prettify.js
flowchart.js
sequence-diagram.js
Prefixes.scss

Development tools :

Visual Studio Code
Sass/Scss
Gulp.js
License
Editor.md follows the MIT License, Anyone can freely use.





Fork me on Github :







Users

 Contact Us: editor.md@ipandao.com


Editor.md
Copyright © 2015-2019 Editor.md, MIT license.

Design & Develop By: Pandao     