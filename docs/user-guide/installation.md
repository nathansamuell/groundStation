# Installation: 

<div class="tip custom-block" style="padding-top: 8px">

This software is meant to be run on a Raspberry Pi -- To install on other operating systems, click [here.](install-on-other-systems.md)

</div>

For those that have done this before, [skip to the install instructions.](#install-source-code)

## Overview

This installation process is the *fastest, least-configurable* method - **other configuration will likely be necessary.** More info [here.](env.md)


FlightControl is a python app, and will be installed using pip. Once you install the dependencies, you can install the the latest stable release through ```pip``` or grab the binaries manually from [GitHub/PyPI](#pypigithub-binaries).

## Install Latest Release

### Install Project Dependencies:

::: warning
you will also need a DE/WM!!
:::  
```sudo apt-get update && sudo apt-get upgrade -y```  
```sudo apt-get install python3-pyqt5 -y```  

### Using ```pip```:

```pip install flightctl```

### PyPi/Github Binaries:

Sources:
- [PyPi](https://pypi.org/project/flightctl/#files) 
- [GitHub](https://github.com/nathansamuell/FlightControl/releases)

Once the .whl file is downloaded, you can use pip to install. If you prefer zipped source code, enter the directory and run ```pip install . --break-system-packages```. This will install the software directly to your system. The ```--break-system-packages``` flag is **NEEDED** to directly install the package to disk. More information on this decision was made can be found [here.](install-on-other-systems.md) The good news is, FlightControl won't actaully break any of your system packages, despite the name of the flag.

### Finishing up
For now, head to the [.env instructions](#setup-env-file)

## Install Latest Dev Release

If you so desire, you are free to install the latest dev release. This is distributed solely through the GitHub repo and will need to be periodically updated manually if you want to stay on the bleeding edge.

### Install source code:
```git clone https://github.com/nathansamuell/FlightControl/```

### Install the package:
```cd FlightControl```  
```pip3 install . --break-system-packages```


## Setup .env file:

::: danger
This should be set up as specified in the [.env file page](env.md) as a default .env file has not been packaged or configured yet. Eventually it will to speed and smooth out the install. The below information will give you a bare minimum install that will run but not function properly.
:::


::: info
Replace your-pass with a numeric code in the following snippet:
:::

```echo 'USER_PIN="*your_pass*"' > .env```  
```cp .env ~/.local/lib/python3.11/site-packages/flightctl/.env```  

The ```--break-system-packages``` flag is **NEEDED** to directly install the package to disk. More information on this decision was made can be found [here.](install-on-other-systems.md) The good news is, FlightControl won't actaully break any of your system packages, despite the name of the flag.

::: tip
Don't forget to look at FlightControl's [configuration options!](env.md)
:::