# Abbreviated function
def shell(command) : 
    import subprocess
    subprocess.run(command, shell = True)

def eprint(error) : 
    import sys
    print(error)
    sys.exit(0)