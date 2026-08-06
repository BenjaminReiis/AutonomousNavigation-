#ifndef MQTT_CLIENT_H
#define MQTT_CLIENT_H

class MQTTClientManager
{
public:

    void begin();

    void loop();

    void publishTelemetry();

};

#endif
