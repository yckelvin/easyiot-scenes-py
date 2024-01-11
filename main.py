def on_microiot_mqtt_topic_0(message):
    global Mode
    Mode = message
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "Mode: " + Mode)
microIoT.microIoT_MQTT_Event(microIoT.TOPIC.TOPIC_0, on_microiot_mqtt_topic_0)

Mode = ""
basic.show_number(0)
wifi_name = "izowifi"
password = "izo1234@"
iot_id = "lmZB9bXGR"
iot_pwd = "liWfrxXMgz"
topic_0 = "qwPmNL37g"
basic.show_number(1)
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
basic.show_number(2)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.ENGLISH)
basic.show_number(3)

def on_forever():
    if Mode == "sunny mode":
        pins.analog_write_pin(AnalogPin.P0, 1023)
        pins.digital_write_pin(DigitalPin.P1, 0)
        if True:
            pass
    elif Mode == "rainy mode":
        pass
    elif Mode == "sleeping mode":
        pass
    elif Mode == "security mode":
        pass
basic.forever(on_forever)
