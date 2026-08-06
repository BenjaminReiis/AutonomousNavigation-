import RobotStatus from "./components/RobotStatus";

import ControlPanel from "./components/ControlPanel";

import Telemetry from "./components/Telemetry";


function App(){


return (

<div className="app">


<h1>
Autonomous Navigation Control
</h1>


<RobotStatus />


<ControlPanel />


<Telemetry />


</div>

);


}


export default App;
