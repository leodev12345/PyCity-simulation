# PyCity-simulation
![PyCity](images/pycity2.png)

## Instalation

  To play PyCity you first have to install pygame to install pygame open cmd or terminal and type:

  In linux:
```
$ sudo apt update
```
```
$ pip3 install pygame
```
  In Windows:

```
pip install pygame
```
  For more info visit:
[https://www.pygame.org/wiki/GettingStarted](https://www.pygame.org/wiki/GettingStarted)

>   When you have pygame installed cilck green "Clone or download" and click download .zip or clone it with git

  When files are downloaded go into src folder and run pycity.py
  In windows double click it
  In linux you can run it with python in terminal

```
$ python3 pycity.py
```
## How to play


## Building
  Enter map size,diffculty,city name and press ENTER the game window should appear
  To build hover with your mouse cursor over a square where you want to build and press one od the following keys:
+ R - build rezidential zone
+ C - build comercial zone
+ O - build road
+ L - build police station
+ F - build fire station
+ H - build hospital
+ S - build prison
+ P - build park
+ I - build industrial zone
+ E - erase a building
## Indicators
  If you see square in right in one of following colors
+ Light blue - Police station needed
+ Blue - Comercial zone needed
+ Red - Fire station needed
+ Brown - Industrial zone needed
+ Grey - Prison needed
+ White - Hospital needed
## Land value
  Building parks increased land value,more parks,better rezidential zones
