import pip


def install_packages():
   print('starting to install packages')
   def install_package(package):
     try:
        __import__(package)
     except ImportError:
        pip.main(['install', package])
   install_package('pyttsx3')
   print("Installed 'pyttsx3'")
   install_package('mysql-connector-python')
   print("Installed 'mysql-connector-python'")
   install_package('playsound')
   print("Installed 'playsound')
   f=open('initial.vira','w')
   f.write('initisalised')
   f.close()
   print("added file 'initial.vira'")

