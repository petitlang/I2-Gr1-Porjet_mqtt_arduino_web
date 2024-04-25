# Projet_MQTT_Arduino_Web

Etablisement : ISEP  
Auteur : Mouzheng LI, Lianghong LI, Guokuang DENG, Zhendong XU  

## Structure

Project/  
│  
├── PythonCode/  
│   ├── data_processing.py  # Pour recevoire les messages et creer une base des donnees  
│   └── dashboard_basic.py  # interface par fonction python "turtle" et lire les donnees de la base des donnees  
│  
├── ArduinoCode/  
│   └── collar_device.ino   # Arduino MKRWAN, envoyer les messages par LoraWan  
│  
└── WebInterface/  # utilise Flask et HTML  
    ├── app.py             # Action de Web par python-Flask  
    ├── templates/         # dossier pour poser les fiches de HTML  
    │   └── position.html     # webInterface  
