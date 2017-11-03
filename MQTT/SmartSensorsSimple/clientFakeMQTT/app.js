/* jshint node:true, esversion:6 */

'use strict';

(function() {

	var mqtt = require('mqtt');
  const client = mqtt.connect("mqtt://10.99.3.43:1883");
  client.on('connect', function() { 
    console.log('Conected');
  });

  client.on('error', function(err) {
      console.log(err);
  });

  function publishFakes(){
    publishLumenFake();
    publishTempFake();
  }

  function publishLumenFake() {
    var tempObj = { sensorId: 1, luminosity: Math.floor(Math.random() * 256).toString() };
    client.publish('/luminosity', JSON.stringify(tempObj));
  }

  function publishTempFake() {
    var tempObj = { sensorId: 1, temperature: Math.floor(Math.random() * 100).toString() };
    client.publish('/temperature', JSON.stringify(tempObj));
  }
  
  client.subscribe('/luminosity');
  client.subscribe('/temperature');
  
  setInterval(
    publishFakes
    , 3000
  );
}());
