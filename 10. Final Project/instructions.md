
![Título Imagen](https://raw.githubusercontent.com/codedex-io/projects/main/projects/generate-a-blog-with-openai/header.png)

**Requisitos previos:** Fundamentos de python  
**Versiones:** Python 3.10, python-dotenv 0.21.0, openai 1.0.0  
**Tiempo de Lectura:** 60 Minutos

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#introduction) Introducción

[Inteligencia Artificial (IA)](https://en.wikipedia.org/wiki/Artificial_intelligence) se está convirtiendo en la próxima gran tecnología para aprovechar. Desde refrigeradores inteligentes hasta autos sin conductor, la IA se implementa en casi todo lo que se te ocurra. Así que adelantémonos y aprendamos cómo podemos aprovechar el poder de la IA con Python y OpenAI.

En este tutorial, aprenderemos cómo crear un generador de blogs con [GPT-3](https://openai.com/api/), un modelo de IA proporcionado por [OpenAI](https://www.openai.com/). El generador leerá un tema para hablar como la entrada, y GPT-3 nos devolverá un párrafo sobre ese tema como la salida.

Entonces AI estará "escribiendo" cosas para nosotros. ¡Diga adiós al bloque del escritor!

¡Pero espera, espera! ¡Inteligencia artificial?! ¡Modelos de IA?! Esto debe ser complicado de codificar. 😵

![meme](https://raw.githubusercontent.com/codedex-io/projects/main/projects/generate-a-blog-with-openai/calculation-math.gif)

No, es más fácil de lo que piensas. ¡Se necesitan alrededor de 25 líneas de código Python!

El resultado final se verá así:

![demo del generador](https://raw.githubusercontent.com/codedex-io/projects/main/projects/generate-a-blog-with-openai/generator-demo.gif)

_Quién sabe, tal vez todo este proyecto fue escrito por el generador que estamos a punto de crear. 👀_

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#what-is-gpt-3) ¿Qué es GPT-3?

[GPT-3](https://en.wikipedia.org/wiki/GPT-3) es un modelo de IA lanzado por OpenAI en 2020. Un modelo de IA es un programa entrenado en un montón de datos para realizar una tarea específica. En este caso, GPT-3 fue entrenado para hablar como un ser humano y predecir lo que viene después dado el contexto de una oración, con su conjunto de datos de entrenamiento de 45 terabytes de texto (!) de internet.

> Como referencia, si tuviera que seguir escribiendo hasta que su papel alcance los 45 terabytes de tamaño, tendría que escribir [22.500.000.000](https://www.techtarget.com/searchstorage/definition/How-many-bytes-for) páginas de texto sin formato.

Dado que GPT-3 fue entrenado en datos de Internet, sabe lo que Internet sabe (no todo, por supuesto). Esto significa que si tuviéramos que dar GPT-3 una oración, sería capaz de predecir lo que viene después en esa oración con alta precisión, en base a todo el texto que se utilizó para entrenarla.

Ahora sabemos con qué trabajaremos, ¡construyamos el programa!

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#setting-up) Configuración

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#openai-account) Cuenta OpenAI

Antes de hacer algo, necesitamos un [OpenAI](https://openai.com/api) cuenta. Necesitaremos esto para acceder a una clave API para usar GPT-3. Tenga en cuenta que OpenAI ya no ofrece créditos gratuitos, por lo que deberá comprar al menos 5 dólares en créditos para comenzar a usar la API.

> [API (Interfaz de Programación de Aplicaciones)](https://en.wikipedia.org/wiki/API) es una forma para que dos computadoras se comuniquen entre sí. Piense en ello como dos amigos enviando mensajes de texto de un lado a otro. Una clave API es un código que recibimos para acceder a la API. Piense en ello como una contraseña importante, ¡así que no la comparta con otros!

Ir a [www.en.com](http://www.openai.com/) y regístrese para obtener una cuenta OpenAI.

Después de crear una cuenta, haga clic en la imagen de su perfil en la parte superior derecha, luego haga clic en "Ver claves API" para acceder a su clave API. Deberías ver [esta página](https://beta.openai.com/account/api-keys) y debería verse como:

![Clave API](https://raw.githubusercontent.com/codedex-io/projects/main/projects/generate-a-blog-with-openai/api-key.png)

Ahora que sabemos dónde se encuentra la clave API, tengamos en cuenta para más adelante.

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#python-setup) Configuración de Python

Para este proyecto, necesitaremos [Python 3](https://www.python.org/downloads/) y [pip](https://pip.pypa.io/en/stable/) (instalador de paquetes) instalado.

Suponiendo que tenemos esos dos instalados, abramos el editor de código de nuestra elección (recomendamos [código VS](https://code.visualstudio.com/)) y crear un nuevo archivo llamado **blog\_generador.py**.

**Nota**: Puede nombrar este archivo cualquier cosa excepto **openai.p**, ya que el nombre chocará con un paquete que instalaremos.

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#beginning-the-project) Comenzando el Proyecto

En el centro de este proyecto, todo lo que haremos es enviar datos con instrucciones a un servidor propiedad de OpenAI, luego recibir una respuesta de ese servidor y mostrarla.

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#install-openai) Instalar openai

Interactuaremos con el modelo GPT-3 usando un paquete python llamado `openai`. Este paquete consta de métodos que pueden conectarse a Internet y otorgarnos acceso al modelo GPT-3 alojado por OpenAI, la empresa.

Para instalar `openai`, todo lo que tenemos que hacer es ejecutar el siguiente comando en nuestro terminal:

    pip install openai
    

Ahora podemos usar este paquete importándolo a nuestro **blog\_generador.py** archivo como así:

    import openai
    

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#authorize-api-key) Autorizar API Key

Antes de que podamos trabajar con GPT-3, debemos establecer nuestra clave API en el `openai` módulo. Recuerde, la clave API es lo que nos da acceso a GPT-3; nos autoriza y dice que se nos permite usar esta API.

Podemos establecer nuestra clave API extendiendo un método en el `openai` módulo llamado `api_key`:

    openai.api_key = 'Your_API_Key'
    

El método tomará la clave API como una cadena. Recuerde, su clave API se encuentra en su [Cuenta openAI](https://beta.openai.com/account/api-keys).

Hasta ahora, el código debería verse así:

    import openai
    
    openai.api_key = 'sk-jAjqdWoqZLGsh7nXf5i8T3BlbkFJ9CYRk' # Fill in your own key
    

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#the-core-function) La Función Central

Ahora que tenemos acceso a GPT-3, podemos llegar a la carne de la aplicación, que está creando una función que toma un mensaje como entrada del usuario y devuelve un párrafo sobre ese mensaje.

Esa función se verá así:

    def generate_blog(paragraph_topic):
      response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
      )
    
      retrieve_blog = response.choices[0].text
    
      return retrieve_blog
    

Desglosemos esta función y veamos qué está pasando aquí.

Primero, definimos una función llamada `generate_blog()`. Hay un solo parámetro llamado `paragraph_topic`, que será el tema utilizado para generar el párrafo:

    def generate_blog(paragraph_topic):
      # The code inside
    

Y entremos en la función. Aquí está la primera parte:

    def generate_blog(paragraph_topic):
      response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
      )
    

Esta es la mayor parte de nuestra función y donde usamos GPT-3. Creamos una variable llamada `response` para almacenar la respuesta generada por la salida de la `completions.create()` llamada de método en nuestro `openai` módulo.

GPT-3 tiene diferentes puntos finales para propósitos específicos, pero para nuestro objetivo, usaremos el [finalización](https://beta.openai.com/docs/api-reference/completions) punto final. El punto final de finalización generará texto dependiendo del mensaje proporcionado. Puede leer sobre los diferentes puntos finales en el [documentación](https://beta.openai.com/docs/introduction).

Ahora que tenemos acceso al punto final de finalización, debemos especificar algunas cosas, la primera es:

`model`: El parámetro del modelo tomará en el modelo que queremos utilizar. OpenAI ofrece varios modelos con diferentes capacidades. Para este tutorial, estamos usando `gpt-3.5-turbo-instruct` para proporcionar ejemplos claros y confiables.

La sintaxis y las capacidades varían entre los modelos. Puede leer más sobre los modelos disponibles en el [documentación](https://platform.openai.com/docs/models).

    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    

`prompt`: Aquí es donde diseñamos las instrucciones principales para GPT-3. Este parámetro tomará en nuestro `paragraph_topic` argumento, pero antes de eso, podemos decirle a GPT-3 qué hacer con ese argumento. Actualmente, estamos instruyendo a GPT-3 a `Write a paragraph about the following topic`. GPT-3 hará todo lo posible para seguir esta instrucción y devolvernos un párrafo.

GPT-3 es muy flexible; si la cadena inicial se cambia a `Write a blog outline about the following topic`éste nos dará un esquema en lugar de un párrafo normal. Más tarde puede jugar con esto diciéndole al modelo exactamente lo que debería generar y viendo qué respuestas interesantes obtiene.

    max_tokens = 400
    

`tokens`: El número de token decide cuánto tiempo será la respuesta. Un número de token más grande producirá una respuesta más larga. Al establecer un número específico, estamos diciendo que la respuesta no puede superar este tamaño de token. La forma en que se cuentan los tokens para una respuesta es un poco compleja, pero puede leer esto [artículo](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) por OpenAI que explica cómo se calcula el tamaño del token.

Aproximadamente 75 palabras son aproximadamente 100 fichas. Un párrafo tiene 300 palabras en promedio. Entonces, 400 tokens tienen aproximadamente la longitud de un párrafo normal. El modelo `gpt-3.5-turbo-instruct` tiene un límite de token de 4.096.

    temperature = 0.3
    

`temperature`: La temperatura determina la aleatoriedad de una respuesta. Una temperatura más alta producirá una respuesta más creativa, mientras que una temperatura más baja producirá una respuesta mejor definida.

-   `0`: La misma respuesta cada vez.
-   `1`: Una respuesta diferente cada vez, incluso si es el mismo mensaje.

Hay muchos otros campos que podemos especificar para ajustar aún más el modelo, que puede leer en el [documentación](https://beta.openai.com/docs/api-reference/completions/create), pero por ahora, estos son los cuatro campos con los que debemos preocuparnos.

Ahora que tenemos nuestra configuración de modelo, podemos ejecutar nuestra función y sucederán las siguientes cosas:

1.  Primero, el `openai` el módulo tomará nuestra clave API, junto con los campos que especificamos en el `response` variable, y hacer una solicitud al punto final de finalización.
2.  OpenAI verificará que se nos permite usar GPT-3 verificando nuestra clave API.
3.  Después de la verificación, GPT-3 utilizará los campos especificados para producir una respuesta.
4.  La respuesta producida se devolverá en forma de un objeto y se almacenará en el `response` variable.

Ese objeto devuelto se verá así:

    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "logprobs": null,
          "text": "\n\nPython is a programming language with many features, such as an intuitive syntax and powerful data structures. It was created in the late 1980s by Guido van Rossum, with the goal of providing a simple yet powerful scripting language. Python has since become one of the most popular programming languages, with a wide range of applications in fields such as web development, scientific computing, and artificial intelligence."
        }
      ],
      "created": 1664302504,
      "id": "cmpl-5v9OiMOjRyoyypRQWAdpyAtjtgVev",
      "model": "gpt-3.5-turbo-instruct",
      "object": "text_completion",
      "usage": {
        "completion_tokens": 80,
        "prompt_tokens": 19,
        "total_tokens": 99
      }
    }
    

Weirre proporcionó toneladas de información sobre la respuesta, pero lo único que nos importa es la `text` campo que contiene texto generado.

Podemos acceder al valor en el `text` campo como así:

    retrieve_blog = response.choices[0].text
    

Finalmente, devolvemos el `retrieve_blog` variable que contiene el párrafo que acabamos de sacar del diccionario.

    return retrieve_blog
    

¡Whoah! Tomemos un momento y respiremos. Eso fue mucho lo que acabamos de cubrir. Vamos a darnos una palmadita en la espalda, ya que hemos terminado en un 90% con la aplicación.

Podemos probar para ver si nuestro código funciona hasta ahora imprimiendo el `generate_blog()` función que acabamos de crear, dándole un tema sobre el que escribir y viendo la respuesta que recibimos.

    print(generate_blog('Why NYC is better than your city.'))
    

Aquí está el código completo hasta ahora:

    import openai
    
    openai.api_key = 'sk-jAjqdWoqZLGsh7nXf5i8T3BlbkFJ9CYRk' # Fill in your own key
    
    def generate_blog(paragraph_topic):
      response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
      )
    
      retrieve_blog = response.choices[0].text
    
      return retrieve_blog
    
    print(generate_blog('Why NYC is better than your city.'))
    

Y boom, después de 2-3 segundos, debería escupir un párrafo como este:

![Salida: NYC](https://raw.githubusercontent.com/codedex-io/projects/main/projects/generate-a-blog-with-openai/output-nyc.png)

Intenta ejecutar el código un par de veces más; ¡la salida debe ser diferente cada vez! 🤯

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#multiple-paragraphs) Párrafos Múltiples

En este momento, si ejecutamos nuestro código, solo podremos generar un párrafo de texto. Recuerde, estamos tratando de crear un generador de blogs, y un blog tiene múltiples secciones, con cada párrafo teniendo un tema diferente.

Agreguemos algún código adicional para generar tantos párrafos como queramos, con cada párrafo discutiendo un tema diferente:

    keep_writing = True
    
    while keep_writing:
      answer = input('Write a paragraph? Y for yes, anything else for no. ')
      if (answer == 'Y'):
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
      else:
        keep_writing = False
    

Primero, definimos una variable llamada `keep_writing`, para usar como un valor booleano para lo siguiente `while` bucle.

En el `while` loop, creamos un `answer` variable que tomará una entrada del usuario utilizando el incorporado `input()` función.

Luego creamos un `if` declaración que continuará el bucle o detendrá el bucle.

-   Si la entrada del usuario es `Y`, luego le preguntaremos al usuario sobre qué tema desea generar texto, almacenando ese valor en una variable llamada `paragraph_topic`. Luego ejecutaremos e imprimiremos el `generate_blog()` función usando el `parapgraph_topic` variable como argumento.
-   De lo contrario, detendremos el bucle asignando el `keep_writing` variable a `False`.

¡Con eso completo, ahora podemos escribir tantos párrafos como queramos ejecutando el programa una vez!

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#rate-limit) Límite de Tasa

Ya que estamos usando un `while` loop, tenemos el potencial de ser limitado en la tasa.

> [Límite de tasa](https://en.wikipedia.org/wiki/Rate_limiting) es el número de llamadas API que una aplicación o usuario puede hacer dentro de un período de tiempo determinado.

Esto normalmente se hace para proteger la API del abuso o [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) ataques.

Para GPT-3, el límite de tasa es de 20 solicitudes por minuto. Mientras no ejecutemos la función tan rápido, estaremos bien. Pero en un raro caso de que ocurra, GPT-3 dejará de producir respuestas y nos hará esperar un minuto para producir otra respuesta.

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#credit-limit) Límite de Crédito

En este punto, si ha estado jugando con la API sin parar, existe la posibilidad de que haya excedido su límite de crédito comprado. El siguiente error se lanza cuando eso sucede:

    openai.error.RateLimitError:  
    You exceeded your current quota, please check your plan and billing details.
    

Si ese es el caso, ve a OpenAI's [Resumen de facturación](https://platform.openai.com/settings/organization/billing/overview) página y compra créditos adicionales.

Tomemos otro respiro. ¡Ya casi terminamos!

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#securing-our-app) Asegurando Nuestra App

Pensemos en esto por un minuto. Creamos esta increíble aplicación y queremos compartirla con el mundo, ¿verdad? Bueno, cuando lo implementamos en la web o lo compartimos con nuestros amigos, podrán ver cada pieza de código en el programa. ¡Ahí es donde radica el problema!

Al comienzo de este artículo, creamos una cuenta con OpenAI y se nos asignó una clave API. Recuerde, esta clave API es lo que nos da acceso a GPT-3. Dado que GPT-3 es un servicio de pago, la clave API también se utiliza para rastrear el uso y cobrarnos en consecuencia. Entonces, ¿qué sucede cuando alguien conoce nuestra clave API? Podrán usar el servicio con nuestra llave, y seremos los que cobramos, ¡potencialmente miles de dólares!

Para protegernos, necesitamos ocultar la clave API en nuestro código pero aún así poder usarla. Veamos cómo podemos hacer eso.

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#install-python-dotenv) Instalar `python-dotenv`

[`python-dotenv`](https://pypi.org/project/python-dotenv)es un paquete que nos permite crear y utilizar variables de entorno sin tener que configurarlas manualmente en el sistema operativo.

> Las variables de entorno son variables cuyos valores se establecen fuera del programa, generalmente en el sistema operativo.

Podemos instalar `python-dotenv` ejecutando el siguiente comando en el terminal:

    pip install python-dotenv
    

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#env-file) Archivo .env

Luego, en el directorio raíz de nuestro proyecto, cree un archivo llamado **.env**. Este archivo mantendrá nuestra variable de entorno.

Abre el **.env** archiva y crea una variable como así:

    API_KEY=<Your_API_Key>
    

La variable incluirá nuestra clave API sin comillas ni espacios. Recuerde nombrar esta variable como `API_KEY` sólo.

### [##](https://www.codedex.io/projects/generate-a-blog-with-openai#python-file) Archivo Python

Ahora que tenemos nuestro conjunto de variables de entorno, abramos el **blog\_generador.py** archiva y pega este código debajo `import openai`.

    from dotenv import dotenv_values
    
    config = dotenv_values(".env")
    

Primero, hemos importado un método llamado `dotenv_values` del módulo.

El `dotenv_values()` tomará el camino hacia el **.env** archiva y devuélvanos un diccionario con todas las variables en el **.env** archivo. Luego creamos un `config` variable para mantener ese diccionario.

Ahora, todo lo que tenemos que hacer es reemplazar la clave API expuesta con la variable de entorno en el `config` diccionario como así:

    openai.api_key = config['API_KEY']
    

¡Eso es todo! Nuestra clave API ahora está segura y oculta del código principal.

**Nota**: Si desea enviar su código a [GitHub](https://www.github.com/), no quieres empujar el **.env** archivo también. En el directorio raíz de su proyecto, cree un archivo llamado **.gitignore**, y en el archivo Git ignore, escriba `.env`. Esto evitará que el archivo sea rastreado por Git y finalmente empujado a GitHub.

¡Con todo ese set y hecho, weizre terminado! ¡El código ahora debería verse así!

**blog\_generador.py** archivo:

    # Generate a Blog with OpenAI 📝
    
    import openai
    from dotenv import dotenv_values
    
    config = dotenv_values('.env')
    
    openai.api_key = config['API_KEY']
    
    def generate_blog(paragraph_topic):
      response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
      )
      retrieve_blog = response.choices[0].text
      return retrieve_blog
    
    keep_writing = True
    
    while keep_writing:
      answer = input('Write a paragraph? Y for yes, anything else for no. ')
      if (answer == 'Y'):
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
      else:
        keep_writing = False
    

**.env** archivo:

    API_KEY=sk-jAjqdWoqZLGsh7nXf5i8T3BlbkFJ9CYRk
    

## [#](https://www.codedex.io/projects/generate-a-blog-with-openai#finish-line) Línea de Acabado

¡Felicidades, acabas de crear un generador de blogs con OpenAI y Python! A lo largo del proyecto, aprendimos cómo usar GPT-3 para generar un párrafo, usar un `while` bucle para crear múltiples párrafos y proteger nuestra aplicación con un **.env** archivo. 🙌

La IA se está expandiendo rápidamente, y los primeros en utilizarla adecuadamente a través de servicios como GPT-3 se convertirán en los inovadores en el campo. Espero que este proyecto te ayude a entenderlo un poco más.

¡Y por último, nos encantaría ver lo que construyes con este tutorial! Etiqueta [@codedex\_io](https://twitter.com/intent/tweet?text=Generate+a+Blog+with+OpenAI&hashtags=Python&hashtags=Codedex+@codedex_io) y [@openai](https://twitter.com/openai) ¡en Twitter si haces algo genial!



