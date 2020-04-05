import paho.mqtt.client as mqtt
from PyQt5.QtCore import QThread, pyqtSignal


class MqttThread(QThread):

    garageTemp = pyqtSignal(int)
    outsideTemp = pyqtSignal(int)
    insideTemp = pyqtSignal(int)
    garageFanState = pyqtSignal(bool)
    storageFanState = pyqtSignal(bool)
    acFanState = pyqtSignal(bool)

    def set_logging(self, logState):
        self.verbose = logState
        if self.verbose:
            self.client.on_log = self.on_log
        else:
            self.client.on_log = None

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("topic_test")

    def on_disconnect(self, client, userdata, rc):
        pass

    def on_message(self, client, userdata, msg):
        pass

    def on_log(self, client, userdata, level, buf):
        pass

    def publish_message(self, data):
        pass

    def __init__(self):
        super().__init__()
        self.verbose = False
        self.broker = "192.168.0.3"
        self.broker_port = 1883
        self.client = mqtt.Client("Display")
        self.client.on_log = None
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        self.client.connect(self.broker)
        self.client.loop_start()
