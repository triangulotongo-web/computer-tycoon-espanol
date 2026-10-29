# Computer Tycoon en español

Traducción no oficial y completa al **español** de [Computer Tycoon](https://store.steampowered.com/app/686680/Computer_Tycoon/) (Progorion), hecha por fans.

| | |
|---|---|
| **Idioma** | Español (neutro, válido para España y Latinoamérica) |
| **Versión del juego** | **v0.9.9.16** (Open Beta, Steam build 19369470, Unity 6000.0.38f1 IL2CPP) |
| **Versión de la traducción** | 1.0.0 |
| **Funciona con** | BepInEx 6.0.0-be.791 (IL2CPP) + XUnity.AutoTranslator 5.6.3.1 |

> El juego trae un selector de idioma con español, pero solo traduce unos 300 textos del menú. El resto (ayudas, tutorial, mensajes de los rivales, componentes, eventos, mercados…) está solo en inglés. Esta traducción cubre todo eso.

## Qué se traduce

- Menús, ventanas, pestañas, columnas y botones
- Tutorial y textos de ayuda
- Mensajes y amenazas de los dueños de las empresas rivales
- Componentes, tecnologías, investigaciones, eventos y noticias
- Notas de la versión v0.9.9.16 en «Información y noticias»

En total son **4.995 frases fijas** y **60 patrones** para frases que el juego monta con datos variables (nombres de empresas, países, cantidades). Se dejan como en el original los nombres propios, los países del mapa, las marcas y las siglas técnicas (CPU, GPU, RAM, USB…) y las de puntos del juego (RP, PP, LP, SPP).

## Instalación

1. Descarga **BepInEx 6 para Unity IL2CPP x64** ([BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.791](https://builds.bepinex.dev/projects/bepinex_be)) y descomprímelo en la carpeta del juego:
   `C:\Program Files (x86)\Steam\steamapps\common\Computer Tycoon\`
2. Descarga **XUnity.AutoTranslator-BepInEx-IL2CPP-5.6.3.1.zip** desde [sus versiones en GitHub](https://github.com/bbepis/XUnity.AutoTranslator/releases) y descomprímelo también en la carpeta del juego.
3. Copia el contenido de este repositorio:
   - `config/AutoTranslatorConfig.ini` → `Computer Tycoon\BepInEx\config\`
   - la carpeta `Translation` → `Computer Tycoon\BepInEx\` (debe quedar `BepInEx\Translation\es\Text\ComputerTycoon_es.txt`)
4. Abre el juego desde Steam. **La primera vez tarda varios minutos** en arrancar porque BepInEx prepara sus archivos; después arranca normal.
5. Deja el idioma del juego en **English**: la traducción parte del texto en inglés.

La configuración deja la traducción automática por internet **desactivada**: solo se usan los textos de este repositorio y el mod no envía nada a ningún servicio.

### Desinstalar

Borra de la carpeta del juego `BepInEx`, `dotnet`, `winhttp.dll`, `doorstop_config.ini` y `changelog.txt`.

## Atajos del mod

- **Alt + T**: alterna entre español e inglés (útil para comparar).
- **Alt + R**: recarga los archivos de traducción sin cerrar el juego.

## Cómo se hizo

Los textos se sacaron de los archivos del propio juego con los scripts de [`tools/`](tools):

- `extract.py`: lee los MonoBehaviour de `data.unity3d` con UnityPy, la tabla de idiomas de I2 Localization y los literales de `global-metadata.dat`.
- `filter.py` y `filter2.py`: descartan identificadores y mensajes técnicos de .NET, Unity y las librerías (en este juego palabras como *server* o *memory* son contenido, así que el filtro es suave).
- `extra_es.py`: traduce a mano los tutoriales y notas que el filtro técnico había descartado.
- `merge.py`: une los lotes, comprueba que cada original existe tal cual en el juego (incluidos saltos de línea y espacios duros) y que los patrones sean expresiones regulares válidas.

Este repositorio **no incluye ningún archivo del juego**, solo las traducciones y la configuración del mod.

## Corregir o añadir textos

Los archivos de `Translation/es/Text/` tienen una línea por texto:

```
Texto original=Texto traducido
r:"^(.+) has become capitalist!$"=¡$1 se ha vuelto capitalista!
```

Dentro de cada lado, `=` se escribe `\=` y un salto de línea `\n`. Si ves algo mal traducido o en inglés, abre un *issue* con una captura o manda un *pull request*.

## Aviso legal

Proyecto de fans sin relación con Progorion ni con los autores de Computer Tycoon. El juego y su contenido pertenecen a sus dueños. Necesitas tener el juego original comprado en Steam.
