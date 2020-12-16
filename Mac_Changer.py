#!/usr/bin/python3
import subprocess

def banner():
    B_Text = '''
    ███╗   ███╗██████╗    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗ █████╗ ████████╗
    ████╗ ████║██╔══██╗   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║  ██║██╔══██╗╚══██╔══╝
    ██╔████╔██║██████╔╝   ██████╔╝██║     ███████║██║     █████╔╝ ███████║███████║   ██║
    ██║╚██╔╝██║██╔══██╗   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔══██║██╔══██║   ██║
    ██║ ╚═╝ ██║██║  ██║██╗██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██║██║  ██║   ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
                        Mac_Changer V2.0
                        Coded by Abinash Raju

    '''
    print(B_Text)
print(banner())

Interface = input("Enter Your Interface: \n")
NewMac = input("Enter New Mac: \n")
print("......................................")
print("Changing Your Mac Address " + Interface + "To" + NewMac)

subprocess.call(["sudo ifconfig", Interface, "down"])
subprocess.call(["sudo ifconfig", Interface, "hw", "ether", NewMac])
subprocess.call(["sudo ifconfig", Interface, "up"])
