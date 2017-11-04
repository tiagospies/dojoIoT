/* jshint node:true, esversion:6 */

'use strict';

(function() {

  var mqtt = require('mqtt');
  var bb = require('bonescript');
  
  var tmp = 1000;//bb.readTextFile('/sys/class/hwmon/hwmon0/device/temp1_input');
  
  const client = mqtt.connect("mqtt://192.168.43.84:1883");
  client.on('connect', function() { 
    console.log('Conected');
  });

  client.on('error', function(err) {
      console.log(err);
  });

  function publishTemp() {
    var tempObj = { sensorId: 2, temperature: Math.floor(Math.random() * 100).toString() }; //(tmp / 1000) - 37
    client.publish('/temperature', JSON.stringify(tempObj));
  }
  
  client.subscribe('/luminosity');
  client.subscribe('/temperature');
  
  setInterval(
    publishTemp
    , 3000
  );
}());
