import sys
import os
import subprocess
import time
import signal

def signal_handler(signal, frame):
    print('\nInterrupt!')
    process.terminate()
    code_process.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

n = len(sys.argv)
if (n < 2) or (n > 4):
    print("Usage: python3 run.py <executable> <num_procs(default=32)> <ppn(default=4)>")
    exit(0)

executable = sys.argv[1]
num_procs = 32
ppn = 4
if (n>2):
    num_procs = eval(sys.argv[2])
if (n>3):
    ppn = eval(sys.argv[3])

os.chdir(executable[0:executable.rfind('/')])

# Try to start server
while (True):
    process = subprocess.Popen(["/users/misc/sagnikd/Libraries/mpiPV3.5/rundir/server", "3600", "15"]) # Might wanna take that as input later
    time.sleep(2)
    if (process.poll() != None):
        print ("Server busy. Retrying...")
    else:
        print ("Server running!")
        break

# Server running

exec_command = "mpirun -np " + str(num_procs) + " -ppn " + str(ppn) + " -f /users/misc/sagnikd/hostfile " + executable
print(exec_command)
code_process = subprocess.Popen(exec_command.split())

process.wait()
