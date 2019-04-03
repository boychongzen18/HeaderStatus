import urllib
import requests

# Tools Priv8 Header Status Website Python 
# Lihat Header Status Website
# Tested : Windows & Termux Working
# Regard Boychongzen aka Xroot


print ('''\033[1m\033[93m[\033[91m!\033[93m] Tools Priv8 Header Status Website Python \n \033[1;37m          
  __    __                            __                     
/  |  /  |                          /  |                    
$$ |  $$ |  ______    ______    ____$$ |  ______    ______  
$$ |__$$ | /      \  /      \  /    $$ | /      \  /      \ 
$$    $$ |/$$$$$$t  | $$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
$$$$$$$$ |$$    $$ | /    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ |  $$ |$$$$$$$$/ /$$$$$$$ |$$ \__$$ |$$$$$$$$/ $$ |      
$$ |  $$ |$$       |$$    $$ |$$    $$ |$$       |$$ |      
$$/   $$/  $$$$$$$/  $$$$$$$/  $$$$$$$/  $$$$$$$/ $$/       
  ______    __                  __                          
 /      \  /  |                /  |                         
/$$$$$$  |_$$ |_     ______   _$$ |_    __    __   _______  
$$ \__$$// $$   |   /      \ / $$   |  /  |  /  | /       | 
$$      \$$$$$$/    $$$$$$  |$$$$$$/   $$ |  $$ |/$$$$$$$/  
 $$$$$$  | $$ | __  /    $$ |  $$ | __ $$ |  $$ |$$      \  
/  \__$$ | $$ |/  |/$$$$$$$ |  $$ |/  |$$ \__$$ | $$$$$$  | 
$$    $$/  $$  $$/ $$    $$ |  $$  $$/ $$    $$/ /     $$/  
 $$$$$$/    $$$$/   $$$$$$$/    $$$$/   $$$$$$/  $$$$$$$/   
 
\033[1;34mAuthor \033[91m:\033[37m Boychongzen aka Xroot  
 ''')
print"\033[1;31mEksekusi \033[1;34m: \033[1;37m[Windows]python \033[1;31m& \033[1;37m[Termux]python2 \033[1;34mheader.py"

print ('\033[1;31m--------------------------------------------\033[1;34m( \033[1;33mWELCOME My Tools Header Status Website \033[1;34m)\033[1;31m-----------------------------------------------\033[1;m\n')

url1 = raw_input(" \033[1;34mURL \033[1;33mCuks :\033[1;32m")
requests_code = urllib.urlopen (url1)
if requests_code.code == 200:
      print ( requests_code.headers )



