/* jshint node:true, esversion:6 */

'use strict';

(function() {

	var mqtt    = require('mqtt');
  const client = mqtt.connect("mqtt://m10.cloudmqtt.com", {
    username: 'vvhfvxbv',
    password: 'WMcRJi8SO4Rx',
    port: 19758
  });//'mqtt://192.168.0.193:1883');
  client.on('connect', function() { 
    console.log('test');
  });

  client.on('error', function(err) {
    console.log(err);
});
  
    client.subscribe('/tiagospies@gmail.com/test');
  
    client.publish('/tiagospies@gmail.com/test', 'Current time is: ' + new Date());
  

  client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString());
  //client.end();
});

	

}());
