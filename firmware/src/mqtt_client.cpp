#include "mqtt_client.h"

#include "config.h"

#include <WiFi.h>

#include <PubSubClient.h>

WiFiClient wifiClient;

PubSubClient client(wifiClient);

void MQTTClientManager::begin()
{
    client.setServer("192.168.1.100",1883);
}

void MQTTClientManager::loop()
{
    if(!client.connected())
    {
        client.connect(ROBOT_NAME);
    }

    client.loop();
}

void MQTTClientManager::publishTelemetry()
{
    client.publish(
        "robot/telemetry",
        "{\"status\":\"online\"}"
    );
}
