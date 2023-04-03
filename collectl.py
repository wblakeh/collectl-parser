#!/usr/bin/env python3
#import modules
import shlex, subprocess, sys

#Define dictionary with subsystem options
subsys = {'c': 'CPU Summary', 'm': 'Memory', 'Z': 'Processes', 'D': 'Disk', 'F': 'NFS Data', 'N': 'Networking', 'J': 'Interrupts'}

#Variables to parse
collectl = input('Please input file to parse: ')
start = input('Please enter start time in 24hr format with a colon: ')
end = input('Please enter end time in 24hr format with a colon: ')

#Print the dictionary
print("Subsystems:\n")
for k, v in subsys.items():
    print(' ', k, '-', v)

#While loop to choose subsystem input
while True:
    #Pick a subsystem from the list
    choice = input('\nChoose a subsystem: ')

    #If you choose the CPU summary
    if choice == 'c':
        cpu = shlex.split(str("collectl -oD -sC --verbose -p {} --from {}-{} -oTm".format(collectl, start, end)))
        subprocess.Popen(cpu, stdout=open("cpu.out", "w+"))
        print("\nYour file has been created as cpu.out")
        break
    
    #If you choose the memory usage
    elif choice == 'm':
        mem = shlex.split(str("collectl -oD -sm --verbose -p {} --from {}-{} -oTm".format(collectl, start,end)))
        subprocess.Popen(mem, stdout=open("mem.out", "w+"))
        print("\nYour file has been created as mem.out")
        break
    
    #If you choose the process information
    elif choice == 'Z':
        proc = shlex.split(str("collectl -oD -sm --verbose -p {} --from {}-{} -oTm".format(collectl, start,end)))
        subprocess.Popen(proc, stdout=open("proc.out", "w+"))
        print("\nYour file has been created as proc.out")
        break

    #If you choose the disk usage
    elif choice == 'D':
        disk = shlex.split(str("collectl -oD -sD --verbose -p {} --from {}-{} -oTm".format(collectl, start, end))) 
        subprocess.Popen(disk, stdout=open("disk.out", "w+"))
        print("\nYour file has been created as disk.out")
        break
    
0 == 1