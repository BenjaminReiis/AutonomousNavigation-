#include "security.h"


bool Security::authenticate(
    String key
)
{

    String savedKey =
    "ROBOT_SECRET_2026";


    if(key == savedKey)
    {

        return true;

    }


    return false;

}
