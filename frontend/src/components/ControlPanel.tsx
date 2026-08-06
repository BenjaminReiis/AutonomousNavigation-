import {
sendCommand
}
from "../services/websocket";


function ControlPanel(){


return (

<div className="card">


<h2>
Controle
</h2>


<button

onClick={()=>sendCommand("START")}

>

INICIAR

</button>



<button

onClick={()=>sendCommand("STOP")}

>

PARAR

</button>



<button

onClick={()=>sendCommand("EMERGENCY")}

>

EMERGÊNCIA

</button>


</div>

);


}


export default ControlPanel;
