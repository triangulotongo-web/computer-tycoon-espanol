"""Traducciones a mano de los textos de juego que el filtro técnico descartó (tutoriales, ayudas, notas de versión)."""
import json

X = json.load(open("work/extra.json", encoding="utf-8"))
T = {
    7: "Un tipo pequeño con botones que mueve un puntero en la pantalla del ordenador. Mantenlo limpio, ¡o su bola (la que da velocidad y orientación al puntero) no se moverá!",
    9: "Y... un proceso es una instancia de un programa informático que se está ejecutando. Contiene el código del programa y su actividad actual. Según el sistema operativo (SO), un proceso puede estar formado por varios hilos de ejecución que ejecutan instrucciones a la vez. ¡Espero que lo vayas pillando!",
    10: "¡La capacidad de este hardware no puede ser 0!",
    11: "¡Haz clic para unirte a mi lista de correo, por favor! <3",
    12: "¡Haz clic para unirte! <3",
    14: "Los crímenes deben castigarse. Esto es lo que hemos hecho hoy.",
    22: "Semi Crystal Drives empieza a usar cristales en lugar de tecnología flash. Aun así, es caro, así que tardaremos en usarlo como material principal de almacenamiento.",
    23: "¡Así que más sigue siendo mejor! Pero... la capacidad de los procesadores multinúcleo para mejorar el rendimiento del software o del SO depende de que usen varios hilos. Estaría bien saber qué es un hilo, ¿verdad?",
    24: "Pues... en informática, un hilo de ejecución es la secuencia más pequeña de instrucciones programadas que un planificador puede gestionar por separado, y ese planificador suele formar parte del sistema operativo. ¡En los próximos niveles tecnológicos lo entenderás!",
    25: "Pues... en la mayoría de los casos, un hilo es una parte de un proceso. Dentro de un proceso pueden existir varios hilos que se ejecutan a la vez y comparten recursos como la memoria, mientras que los procesos distintos no comparten esos recursos. ¡Así es como estas cosas pueden funcionar juntas! Continuará...",
    28: "La pequeña matriz de la parte inferior de la pantalla de precios también te ayudará a saber lo buenos que son tus ordenadores. Elige los rivales que quieres incluir en la comparación y compruébalo tú mismo. Ten en cuenta que, aunque los atributos de tus ordenadores vienen de distintas piezas de hardware y se resumen en un solo valor, ¡los distintos grupos de usuarios también miran tus piezas por separado! Por ejemplo, a los jugadores les importa más la tarjeta gráfica que el almacenamiento, aunque ambos suman a la \"Capacidad\".",
    29: "El mundo material es muy aburrido... quédate el dinero. ¡Yo ya hago negocios en el plano astral!",
    33: "Este enorme árbol de investigación te ayudará a planificar. Si haces doble clic en un nodo, se añadirá automáticamente a tu cola de investigación (junto con los nodos que llevan a él). Busca el segundo nodo de la categoría \"Data Projection\", llamado \"Glass Teletype\", ¡y haz doble clic en él!",
    34: "¡Este es el lugar de los usuarios que ayudaron al desarrollo del juego enviando informes de errores e ideas o escribiendo reseñas! Al ser un juego en acceso anticipado, recibir opiniones es muy importante, ¡así que quiero mostrarles mi RESPETO de esta forma! <3",
    35: "Este es el mapa del mundo. Algunos mercados están abiertos para ti y otros cerrados. Cada mercado prefiere atributos de ordenador distintos y tiene sus propios impuestos y márgenes de distribuidor.",
    36: "Para descargar contenido del que ya tienes licencia. ¡Apoya a los desarrolladores y artistas independientes, por favor! <3",
    37: "¡Bien hecho! Como ves, tu ordenador tiene atributos. Cuanto más altos son, mejor es el ordenador. Sin embargo, cuantas más cosas le añades, más PP, o \"Puntos de producción\", hacen falta para fabricarlo. El coste inicial también sube, ¡pero solo lo pagas una vez al terminar este diseño, no por cada ordenador fabricado!",
    38: "¡Con un material mejor podemos aumentar la eficiencia de nuestros viejos disipadores!",
    39: "Puedes comprar licencias no exclusivas de utilidades para añadirlas a tu sistema operativo. La licencia es tuya para siempre, aunque con el tiempo seguramente encontrarás versiones nuevas y mejores. Solo el precio de la licencia depende de la habilidad de tu directivo.",
    45: "Tu mercado debería ser más grande. Más gente -> más ventas -> ¡más dinero! ¡Expándete!",
    # notas de la versión v0.9.9.16, en "Información y noticias"
    2: "- He corregido un error grave en la simulación de clientes en las ventas de hardware: provocaba ventas anormalmente altas sin tener en cuenta los parámetros ni la antigüedad del producto, y permitía acumular hardware para inflar los beneficios, entre otros problemas. Corregido\n"
       "- Había un posible exploit en el sistema de negociación que permitía conseguir tecnología de los rivales sin que pudieran demandar, jugando con regalos y abandonos de contrato, etc. Corregido\n"
       "- En la versión anterior había problemas al seleccionar y colorear el mapa. Corregido\n"
       "- Había un error grave que impedía a los jugadores de la IA actualizar sus CPU y algunas otras piezas en las fases finales de la partida por intentos incorrectos de reducir el calor. Corregido\n"
       "- Había un error raro que, en ciertas circunstancias, hacía que los jugadores de la IA vendieran sus piezas de hardware por cifras aleatorias, lo que les impedía sacar beneficio de ellas. Corregido\n"
       "- Al final de la partida podía pasar que los directores generales pidieran cantidades negativas de dinero... Corregido\n"
       "- He mejorado el algoritmo de la IA para elegir qué tecnologías está dispuesta a comprar o intercambiar.\n"
       "- He corregido un error en el algoritmo de investigación de la IA que a veces le permitía investigar más rápido de lo debido.\n"
       "- He cambiado el botón de subir de nivel de +-10 puntos a +-5 puntos.\n"
       "- El evento de marketing viral afectaba negativamente a las ventas de hardware. Corregido\n"
       "- A veces los niveles de la oficina se quedaban atascados y los gráficos no se actualizaban. Corregido\n"
       "- He corregido varios fallos gráficos, como partículas de flechas que se veían en otras ventanas o barras de desplazamiento que se descolocaban al cargar\n"
       "- He corregido muchos errores gramaticales y erratas en el tutorial, en los consejos de la ventana principal y en otros textos de la interfaz\n\n"
       "Y más... Para ver la lista completa, consulta la última noticia, por favor.",
}
REGEX = [
    r'r:"^(.+) failed to steal your technology\. You could sue them\.$"=$1 no ha conseguido robar tu tecnología. Podrías demandarle.',
    r'r:"^You can support a developer and get an exclusive video game for 10 years to add to your Operating System\. After the 5 years the deal is over, so you can.t add it to your OS anymore\. Only the price of the development is dependent on your Manager.s skill\.\s*$"=Puedes apoyar a un desarrollador y conseguir un videojuego exclusivo durante 10 años para añadirlo a tu sistema operativo. Pasados los 5 años el trato termina y ya no podrás añadirlo a tu SO. Solo el precio del desarrollo depende de la habilidad de tu directivo.',
]


def esc(s):
    return s.replace("\\", "\\\\").replace("=", "\\=").replace("\r", "\\r").replace("\n", "\\n").replace("\t", "\\t")


out = [esc(X[i].strip()) + "=" + esc(v.strip()) for i, v in T.items()]
out.append("Localization Information=Información de traducción")
out += REGEX
open("work/out/c10.txt", "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
json.dump(X + ["Localization Information"], open("work/chunks/c10.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(out))
