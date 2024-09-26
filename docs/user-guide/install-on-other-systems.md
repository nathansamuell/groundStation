# Installing on alternate Platforms

GroundStation is a Python app that runs on PyQt5 as well as Pyserial. Interestingly, the install process on machines of other architectures and hardware is actually *simpler* than the [default install process](installation.md). 

::: info
As of Fall 2024, the PyQt5 library, when installed by pip, fails to build correctly on ARM Linux machines. This is why on the RPi, the package is installed directly to the machine -- the only working bindings for PyQt5 must be installed through the apt package manager directly to disk. 
:::