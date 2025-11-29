# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.python -m venv .venv
# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit  
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Blog PC4</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("540733587_18520782685018254_5044516034138545855_n.jpg", caption='Irrrrick', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?
    texto = """
        Debajo de cada gran película hay unas letras que explican aquello que sucede y estos son los subtítulos de una parte de mi vida  .
        
        **Soy un estudiante de Publicidad del quinto ciclo de la carrera, amante del café y de la fotografía. Sin olvidar, un futuro Planner.**
        
        **Soy de Independencia City y si no conoces el distrito, probablemente hayas escuchado de Plaza Norte. Sí, vivo por ahí.**
        
        **Publicidad**
        
        **Lo que amo de mi carrera es que me permite explorar nuevos universos, aquellos universos que llamamos personas.**
        
        **Me gustaría ser un Planner Estratégico que se encuentre en búsqueda de Insights creativos.**
        
        **Me encanta ver series, veo series mientras almuerzo, estudio, ordeno, cocino y me movilizo. Así que se podría decir que es algo que hago casi 24/7.**
        """        
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

elif  pagina_seleccionada == 'Experiencia':
    
    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Al inicio todo fue sencillo. He estado encerrado ligado a una pantalla desde que tengo memoria, así que los temas de informática como hardware y software son algo de lo que estoy familiarizado.
    Me sentí emocionado. Si bien ya había explorado el HTML, todavía no me había adentrado en Python.
    Es como aprender otro idioma como el ingles o el frances, con significados y forma de utilizar cada formulación de significados para comunicar. 
    Me gusta resolver problemas. La satisfacción de poder resolver un problema complicado es gratificante.
    Lo primero es agregar la habilidad al CV, pero luego estar preparado a utilizarlo en algún ambiente laboral.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    st.video("https://drive.google.com/file/d/1M62_kcuZYnq1aoL52qkswTscN9M52xSz/view?usp=sharing")
    
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1M62_kcuZYnq1aoL52qkswTscN9M52xSz/view?usp=sharing' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 


else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico de barras verticales de lenguas aisladas', 'Gráfico de barras de familias lingüísticas', 'Gráfico de barras horizontales de familias lingüísticas', 'mapa cusco']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de barras de familias lingüísticas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("lengua_familia_GB.png", caption='Gráfico de familias lingüísticas', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de barras horizontales de familias lingüísticas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("lengua_familia_GB.png", caption='Gráfico de familias lingüísticas', width=500)
        pass
    elif grafico_seleccionado == 'Mapa de Mis Películas Favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu mapa</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas_favoritas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)