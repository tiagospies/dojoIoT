/* jshint node:true, esversion:6 */

'use strict';

(function() {

	
var mosca = require('mosca');

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
  if(packet.topic == 'messages'){
    console.log('Published', JSON.parse(packet.payload));
  }
});

server.on('ready', setup);

// fired when the mqtt server is ready
function setup() {
  console.log('Mosca server is up and running');
}
	

}());
