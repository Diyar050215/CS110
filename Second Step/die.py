import stdio
import stdrandom

n= stdrandom.uniformInt(1,6)
if n==1:
    stdio.writeln(" " + " " + " " + " " + " ")
    stdio.writeln(" " + " " + "*" + " " + " ")
    stdio.writeln(" " + " " + " " + " " + " ") 
elif n==2:
    stdio.writeln("*" + " " + " " + " " + " ")
    stdio.writeln(" " + " " + " " + " " + " ")
    stdio.writeln(" " + " " + " " + " " + "*")
elif n==3:
    stdio.writeln("*" + " " + " " + " " + " ")
    stdio.writeln(" " + " " + "*" + " " + " ")
    stdio.writeln(" " + " " + " " + " " + "*")
elif n==4:
    stdio.writeln("*" + " " + " " + " " + "*")
    stdio.writeln(" " + " " + " " + " " + " ")
    stdio.writeln("*" + " " + " " + " " + "*")
elif n==5:
    stdio.writeln("*" + " " + " " + " " + "*")
    stdio.writeln(" " + " " + "*" + " " + " ")
    stdio.writeln("*" + " " + " " + " " + "*")
elif n==6:
    stdio.writeln("*" + " " + "*" + " " + "*")
    stdio.writeln(" " + " " + " " + " " + " ")
    stdio.writeln("*" + " " + "*" + " " + "*")