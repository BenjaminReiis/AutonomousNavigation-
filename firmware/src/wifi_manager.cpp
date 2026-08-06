#include "wifi_manager.h"

#include "config.h"

#include <WiFi.h>

void WiFiManager::begin()
{

    WiFi.begin(
        WIFI_SSID,
        WIFI_PASSWORD
    );

    while(WiFi.status()!=WL_CONNECTED)
    {
        delay(500);
    }

}

bool WiFiManager::connected()
{
    return WiFi.status()==WL_CONNECTED;
}
