/* jshint node:true, esversion:6 */

'use strict';

(function() {

	
var mosca = require('mosca');
var io = require('socket.io').listen(5000);

var ascoltatore = {
  //using ascoltatore
  type: 'mongo',
  url: 'mongodb://localhost:27017/mqtt',
  pubsubCollection: 'ascoltatori',
  mongo: {}
};

var settings = {
  port: 1883,
  backend: ascoltatore
};

var server = new mosca.Server(settings);

var clients = [];

server.on('clientConnected', function(client) {
    console.log('client connected', client.id);
    clients.push(client);
});

// fired when a message is received
server.on('published', function(packet, client) {
  if(packet.topic == '/temperature'){
    var data = JSON.parse(packet.payload);
    io.emit('updateData', data);
  }
  if(packet.topic == '/luminosity'){
    var data = JSON.parse(packet.payload);
    io.emit('updateData', data);
  }
});

server.on('ready', setup);

// fired when the mqtt server is ready
function setup() {
  console.log('Mosca server is up and running');
}
	

}());
