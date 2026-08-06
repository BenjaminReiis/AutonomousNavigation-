let socket:WebSocket;



export function connectWS(){


socket = new WebSocket(

"ws://localhost:8000/ws"

);



socket.onopen=()=>{

console.log(
"Connected"
);

};



return socket;

}



export function sendCommand(
command:string
){


if(socket){

socket.send(

JSON.stringify({

command

})

);

}

}
