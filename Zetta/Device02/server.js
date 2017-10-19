var zetta = require('zetta');
var LED = require('zetta-led-mock-driver');

zetta()
  .name('Device02')
  .use(LED)
  .link('http://localhost:3000')
  .listen(1337, function(){
     console.log('Zetta is running at http://127.0.0.1:1337');
});