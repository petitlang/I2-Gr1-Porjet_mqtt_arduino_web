# Projet_MQTT_Arduino_Web

Etablisement : ISEP  
Auteur : Mouzheng LI, Lianghong LI, Guokuang DENG, Zhendong XU  

## Structure

Project/
│
├── PythonCode/
│   ├── data_processing.py  # 数据处理脚本
│   └── dashboard_basic.py  # 基础版仪表板实现（使用turtle等）
│
├── ArduinoCode/
│   └── collar_device.ino   # Arduino项圈设备代码，包括数据发送逻辑
│
└── WebInterface/  # 使用Flask或Django等Python Web框架
    ├── app.py             # 主应用程序，定义路由和视图
    ├── templates/         # 存放HTML文件的文件夹
    │   └── index.html     # 网页版仪表板的HTML结构
    └── static/            # 存放CSS和JavaScript文件的文件夹
        ├── styles.css     # 网页版仪表板的CSS样式
        └── script.js      # 可选的JavaScript文件，用于增强前端交互
