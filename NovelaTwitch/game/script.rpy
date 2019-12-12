# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define diane = "???"
define d = Character(_("[diane]"), color="#a76df7")
define you = Character("[yourName]", color="#0075b0")
define younv = Character("[yourName]", color="#0075b0", kind=nvl)
define dad = Character("Papá", color="#de841d")
define gui.choice_button_text_idle_color="#222222"
define s = "o"
define ab = "el"
# El juego comienza aquí.

label start:
    "Hola, bienvenido a este mundo, pero antes de entrar y ponerte en tu nueva vida debo hacerte unas preguntas, ¿de acuerdo?"


    menu:

        "Primero, porque no me cuentas sobre ti"
        "¿Que eres?, ¿Hombre o mujer?"

        "Hombre":

            python:
                s = "o"
                ab = "el"

        "Mujer":

            python:
                s = "a"
                ab = "la"


    python:
        yourName = renpy.input("Ahora, cuentame, ¿Cual es tu nombre?",default="Nombre")
        yourName = yourName.strip()

        if not yourName:
            yourName = "MC"


    scene bg sky with fade

    nvl show

    younv "Hola, mi nombre es [yourName] tengo 19 años de edad, estoy a punto de empezar una nueva vida universitaria, Estoy tan emocionad[s]
    por esto que simplemente no se cómo sentirme al respecto."

    younv"Se podría decir que todos los niveles de educación en mi vida fueron un poco, \"decepcionantes\",
    siempre fui muy buen[s] en los estudios"

    younv "me encanta aprender pero esto usualmente me causa problemas con mis compañeros de clase,
    nunca pude encajar en nungún grupo."

    younv "pero espero que esta vez sea diferente, tal vez pueda hacer nuevos amigos, o por lo menos no ser un
    bicho raro con el que nadie quiera estar."

    nvl clear

    younv "Supongo que me cuesta relacionarme gracias a que soy un poco diferente a los demás,
    mis padres fallecieron cuando era niñ[s] y mi hermana mayor se encargó de mí."

    younv "por eso quiero ser [ab] mejor en la escuela."

    younv "Siento que se los debo, quiero convertirme en alguien de quien pudieran estar orgullosos."

    younv "lo lograre cueste lo que cueste.
    Pero eso no importa ahora."

    younv "he dejado todo atras y estoy list[s] para empezar con esta nueva fase de mi vida con el pie derecho,
    o al menos, eso esperaba..."

    nvl clear

    younv "El dia anterior a mi ingreso fue un día bastante normal, pase el día entero en el pc
    ocupándome de mis asuntos hasta que fue el momento de ir a la cama."

    younv "Prepare mis cosas como lo había planeado y me precipite hacia mi cama, ahi fue cuando las cosas extrañas empezaron..."

    nvl clear
    scene bg galaxy

    younv "¿Alguna vez han sentido como que en verdad no conocen su entorno?, como si la familia con la que viven, los amigos que tienen,
    incluso su casa o todo es diferente."

    younv "Como si el lugar en el que crecieron fuera diferente, como si nada tuviera sentido y estuvieran en un lugar que no conocen,
    y aun asi, todo les parece tan familiar..."

    nvl clear
    scene bg city

    younv "El día comenzó como lo usual, fue mi primer noche en mi nuevo apartamento, una nueva ciudad y una escuela nueva,
    no me entusiasma mucho la escuela para ser sincero."

    younv "Mis padres siempre quisieron que fuera una persona productiva y estudiosa, pero no soy de ese tipo, me gusta mas
    centrarme en mis hobbies que en mis estudios, al fin y al cabo, ¿Quien necesita la escuela?."

    younv "En fin, aun así no quiero romperle el corazón a mi madre, y mi padre hizo un esfuerzo enorme en conseguirme este departamento,
    en el sector de la ciudad cercano a mi nueva escuela."

    younv " no quiero decepcionarlos..."

    younv "Espera un momento, ¿padres?, recuerdo vivir con mi hermana pero, soy hij[s] unic[s], o al menos eso recuerdo, bueno, no importa,
    debo estar divagando, sera mejor que me apresure."

    younv "No quiero llegar tarde el primer día de universidad, eso no dejaria una muy buena impresion"

    younv "Apenas salir de casa recibí una llamada de mi padre..."

    nvl hide

    you "Hola Papá, sí, estoy llegando a la escuela, no te preocupes, todo bien"

    dad "Está bien, confiare en ti esta vez, simplemente no salgas de clases como es tu usual ¿entendido?"

    dad "No queremos tener problemas contigo otra vez"

    you "¿Escapar?, yo nunca haria eso, de hecho estoy bastante emocionad[s]"

    dad "Si, si, como si no te conociera de toda la vida, simplemente no lo hagas de nuevo"

    you "Te digo que no pasara, confía en mi, nos vemos luego"

    "Vaya, eso fue raro, ¿escapar de clase?, nunca haria algo asi, ¿que clase de persona se cree que soy?,
    bueno, me apresurare, que ya casi es hora de la ceremonia de ingreso."

    scene bg lecturehall
    nvl clear
    nvl show

    younv "Pase toda la ceremonia de ingreso divagando mi mente de un lado a otro, ¿que fue esa extraña sensacion que tuve?,
    parecía como si estuviera olvidándome de algo, algo importante"

    younv "El sonido de los aplausos me saco de mis fantasias, debo estar dandole demasiadas vueltas, mejor me relajo un poco."

    younv "Tal vez este es el estres universitario del que tanto hablan"

    nvl hide

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg club

    "Al salir del auditorio una chica alta y con un aura elegante interrumpio mi paso, su cabello es morado y tiene una
    expresión que me causa intriga"

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show diane normal at left with dissolve

    d "¿Supongo que tu debes de ser [yourName] verdad?"

    you "¿Eh?, si, soy yo, ¿pasa algo?"

    d "¿No estabas prestando atención?, yo seré tu nueva mentora, me asignaron a ti porque fuiste uno de los promedios mas bajos
    en el examen de ingreso."

    d "Mi nombre es Diane, Diane Greson, gusto en conocerte"

    python:
        diane = "Diane Greson"

    you "Mucho gust... Espera un momento, ¿promedio mas bajo?, no puede ser cierto, recuerdo haber estado entre los más altos de la
    selección, ¿como puede ser eso si quiera posible?."

    d "Je, es gracioso, no te preocupes, no debes apenarte por tus calificaciónes, para eso estoy yo aqui, ayudare a tu nivelación en
    cuestiones académicas, así que no debes preocuparte por no estar a la altura, todo mejorara a partir de ahora."

    nvl clear
    nvl show

    younv "Ahí está de nuevo, esa sensación, como si algo faltara, finalmente asiento y Diane termina por resumirme las reglas de la academia
    y explicarme unas cuantas dudas acerca de mi situación actual"

    nvl hide

    d "Bueno, ya deberías saber todo lo esencial para que tu vida académica sea lo más productiva posible. Así que comencemos con el
    recorrido por la escuela si no te molesta."

    you "Oh claro, no hay problema, te sigo."

    # Presenta las líneas del diálogo.

    # Finaliza el juego:

    return
