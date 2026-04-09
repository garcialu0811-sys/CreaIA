# Manejo de archivos en python

## Metodos de apertura de un archivo
"open()"

Es el puente de nuestro programa al sistema operativo para acceder a nuestros datos

Esta funcion requiere dos argumentos obligatorios: el nombre del archivo y el "Modo" en el que queremos abrirlo

### Modos de apertura
1. **Modo `w`** (write/escribir)
    * Crea un archivo nuevo
    * Si el archivo no existe, lo crea
    * **Advertencia**: Si el archivo ya existía, el modo "w" lo destruye por completo y lo sobrescribe desde cero

2. **Modo `a`** (append/ añadir)
    * Abre un archivo existente y coloca el cursos al final.
    * Todo lo que escribimos se agregara sin borrar lo anterior

3. **Modo `r`** (read/leer)
    * Solo nos permite ver el contenido
    * NO podemos modificar o agregar al archivo
    * Si el archivo no existe, el programa se detendra con un error.

SIEMPRE que abro un archivo, hay que cerrar el archivo
`close()`

Para escribir en mi archivo usamos la  funcion `write()`


```py
archivo_prueba = open("archivo.txt", "a")
archivo_prueba.write("Hoy aprendí a escribir en un archivo")

archivo_prueba.close()
```

# administrador de contexto `with open`

```py
with open("archivo.txt", "a") as archivo_prueba:
    archivo_prueba.write("Hoy aprendí a escribir en un archivo\n")
    archivo_prueba.write("ahora puedo escribir varias líneas\n")
```

## Leer nuestro archivo
```py
with open("archivo.txt", "a") as archivo_prueba:

```

## El metodo `read()` 
Python tomara todo el contenido del archivo y lo guardara en una sola variable de tipo cadena de texto (string)
```py
with open("cuento.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido completo:")
    print(contenido)
```

## Metodo `readline()`
```python
with open("lista_alumnos.txt", "r") as archivo:
    
```