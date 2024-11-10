# Setup

This document details what FlightControl currently expects from your rocket, as well as how you can configure it for your needs on your machine

## Setting Up Your Running machine

If you remember from the [installation instructions](installation.md), we executed a series of copy commands:

```echo 'USER_PIN="*your_pass*"' > .env```  
```cp .env ~/.local/lib/python3.11/site-packages/flightctl/.env```  

These commands copy your password to a .env file that only lives on your machine -- if you reinstall, you will need to re-execute these commands, or login to the app will become impossible. 

::: tip
At a future date, much of FlightControl's behavior will be configurable with variables in the .env file! For now, just the password lives there.
:::

FlightControl can also be started automatically on machine boot by taking advantage of the Linux [systemd](https://systemd.io/) boot system -- more on that in the [Advanced Config](#advanced-config).

### Setting your serial port

UNDER CONSTRUCTION

## Setting Up Your Rocket

This part is the fun part! FlightControl only has a few design restrictions that define the way it receives data from your rocket.

### FlightControl's expectations

1. Data is read through [SPI](https://www.geeksforgeeks.org/what-is-serial-peripheral-interface-spi/#) 
    ::: details
    For AIAA-UH, the team's rocket computer send data down using an [XBEE](https://www.digi.com/products/embedded-systems/digi-xbee/rf-modules/sub-1-ghz-rf-modules/xbee-pro-900hp) module system. This was connected to an Adafruit chip that plugged into the Raspberry Pi USB just like an Arduino plugs into a PC/Laptop! Serial communication is not limited to USB ports on Raspberry Pi if this setup is not for your team.
    :::

2.  Data Headers are defined either before launch or during the first transmission of data
   
3. Data format is a string of [CSV](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/)
    ::: details
    FlightControl parses data until it reaches a comma in the string -- the headers define which value is assigned where! CSVs can also be loaded into Excel or [LibreOffice Calc](https://www.libreoffice.org/discover/calc/) for analysis! 
    :::

If your rocket sends data in this way, FlightControl will monitor it effectively out of the box! If modifying the flight computer is out of the question, tweaking data processing should be fairly straightforward. Take a look at the [Developer Docs](../developer-reference/dev-landing.md).


## Advanced Config

### Linux OS Autostart

FlightControl can be initialized as a systemd service -- the intricacies of this process have not been worked out, but some starter systemd units are included in the os-files directory of the repo. More information on including them in your build structure is [here](https://linuxhandbook.com/create-systemd-services/).