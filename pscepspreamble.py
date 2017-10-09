#!/usr/bin/env python
import codecs
import sys

if len(sys.argv) < 2:
    sys.stderr.write("input filename not specified.\n")
    sys.exit(0)

finname = sys.argv[1]
nameend = finname.rfind('.')
if nameend < 0:
    nameend = len(finname)
foutname = finname[0 : nameend] + '.sty'

fin = codecs.open(finname, 'r', 'utf_8')
fout = codecs.open(foutname, 'w', 'utf_8')
writable = False
for str in fin:
    if writable:
        str = str.strip(' \t\n')
        if len(str) > 0 and str[0] != '%':
            idx = str.find('%')
            idx = None if  idx == -1 else idx
            str = str[0 : idx]
            str = str.replace('{', '\\@charlb ')
            str = str.replace('}', '\\@charrb ')
            fout.write('\\immediate\\write\\psc@epsfile{' + str + '}%\n')
        elif str == '% endinput':
            fout.write('}\n')
            break
    elif str == '% begininput\n':
        fout.write('\\def\\@' + finname[0 : nameend] + '{%\n')
        writable = True
fin.close()
fout.close()

