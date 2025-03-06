# MissingDisplayHamRadio
This implements additional features for ham radios through CAT control

We are starting off with FT-3000 and similar because there are many menu items inside the deep 
menu which do not have a nice graphical representation.

This first cut provides interfaces to the RX audio filters and the volume. 
The volume was just experimental and is not needed because there is a volume knob on the FT3000.
Anyway this gives access to the menues :
048, 049, 051, 051
055, 056, 057, 058
071, 072, 073, 074
080, 081, 082, 083
089, 090, 091, 092
099, 100, 101, 102

You can just run the executable which is in the folder executable (dah). 
The default settings nevertheless are COM4, 9600, and debug mode. 
So you only see nice figures because in debug mode it is not accessing your FT3000. 
So you have to run it with the following parameters

Setting debug to false:

-dbg False

Setting another rate:

-bd 38400

Setting a different COM port:

-com COM3

Regardless of the other settings you always have to set -dbg False

So if you want to use it start it from the command line like one of the commands below 

MissingDisplayFT3000.exe -dbg False

MissingDisplayFT3000.exe -dbg False -com COM5

MissingDisplayFT3000.exe -dbg False -bd 38400

MissingDisplayFT3000.exe -dbg False -bd 19200 -com COM4

# Starting from Python
Otherwise you can go into the source and start the main.py:

python main.py -dbg False -com COM5

The executable is directly compiled from the python code. 
















