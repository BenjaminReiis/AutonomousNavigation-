#include "ota_manager.h"

#include <ArduinoOTA.h>


void OTAManager::begin()
{

    ArduinoOTA.setHostname(
        "ANS-Robot"
    );


    ArduinoOTA.onStart([](){

    });


    ArduinoOTA.onEnd([](){

    });


    ArduinoOTA.onError([](ota_error_t error){

    });


    ArduinoOTA.begin();

}



void OTAManager::handle()
{

    ArduinoOTA.handle();

}
