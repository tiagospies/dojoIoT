var zetta = require('zetta');
var BeagleBoneLedDevice = require('./device.js');

  zetta()
    .name('BeagleBone LED')
    .use(BeagleBoneLedDevice, 'USR1')
    .use(BeagleBoneLedDevice, 'USR2')
    .use(BeagleBoneLedDevice, 'USR3')
    .link('http://192.168.7.1:3000')
    .listen(1337, function(){
       console.log('Zetta is running at http://192.168.7.1:3000');
  });