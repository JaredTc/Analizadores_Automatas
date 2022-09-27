import re
from cgitb import text

texto = "int _Numero_1=3"


if re.match("\Aint [_a-z][\w\d]+=+\d", texto):    
    print(texto);
