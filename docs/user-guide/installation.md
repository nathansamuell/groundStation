# Installation: 

<div class="tip custom-block" style="padding-top: 8px">

This software is meant to be run on a Raspberry Pi -- To install on other operating systems, click [here.](install-on-other-systems.md)

</div>

### Overview

For those that don't like reading, [skip to the install instructions.](#install-source-code)

GroundStation is a python app, and will be installed using pip. The app is currently in alpha release, and as such is not uploaded to PyPi or any similar package index. Instead, we will clone the project from github, and install from the source code file. Don't worry -- installing from source code still gives you stable code and is fairly straightforward.


### Install source code:
```git clone https://github.com/nathansamuell/groundStation/```

### Install Project Dependencies:

::: warning
you will also need a DE/WM!!
:::  
```sudo apt-get update && sudo apt-get upgrade -y```  
```sudo apt-get install python3-pyqt5 -y```  

### Setup .env file:

::: info
Replace your-pass with a numeric code in the following snippet:
:::

```echo 'USER_PIN="*your_pass*"' > .env```  
```cp .env ~/.local/lib/python3.11/site-packages/groundStation/.env```  

### Install the package:
```cd groundStation```  
```pip3 install . --break-system-packages```

The ```--break-system-packages``` flag is **NEEDED** to directly install the package to disk. More information on this decision was made can be found [here.](install-on-other-systems.md) The good news is, GroundStation won't actaully break any of your system packages, despite the name of the flag :)