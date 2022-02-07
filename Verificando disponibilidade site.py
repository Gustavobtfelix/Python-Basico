import urllib 
import urllib.request
try:
 site = urllib.request.urlopen('file:///C:/Users/gustavo.felix/Documents/git-e-github/Gustavo/Python-Basico/index1.html')
except urllib.error.URLError:
  print('Não consegui conectar')
else:
  print('Consegui conectar')
  
pagina = urllib.request.urlopen('file:///C:/Users/gustavo.felix/Documents/git-e-github/Gustavo/Python-Basico/index1.html')
texto = pagina.read().decode("utf8")

print(texto)