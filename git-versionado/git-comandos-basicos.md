
## Comandos para usar la terminal de Bash

Para acceder a un directorio/carpeta se utiliza
```
cd MisDocumentos

cd Escritorio/repositorios
```
Para retroceder en la jerarquía de directorios un nivel hacia arriba, se utiliza
```
cd ..
```
Para mostrar el directorio en el que uno se encuentra parado
```
ls
```

## Comandos de Git
Comandos para configurar nombre de usuario e email que figuran en los commits que se hagan
```
git config --local user.name "FIRST_NAME LAST_NAME"
git config --local user.email "MY_NAME@example.com"
```
Comando para clonar el repositorio
```
git clone url_repositorio

git clone https://github.com/FedericoNery/poo-en-python.git
```
Comando para agregar un archivo al stage de git
``` 
git add uri_archivo
```
Comando para agregar todos los archivos al stage de git
``` 
git add .. 
```
Comando para realizar un commit
```
git commit -m "Mensaje"
```
Comando para enviar los commits que se hicieron locales a la rama del servidor remoto
donde se hostea el repositorio
```
git push 

"Y si no existe la rama que se está pusheando debemos ejecutar el siguiente comando"
git push --set-upstream origin nombre_rama 
```

Comando para crear una nueva rama a partir de la que estamos parados
```
git checkout -b nombre_rama
```

Comando para traernos todos los commits que están en la rama del repositorio remoto al local
```
git pull
```
