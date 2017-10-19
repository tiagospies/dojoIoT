var zetta = require('zetta');
var LED = require('zetta-led-mock-driver');

zetta()
  .name('Device01')
  .use(LED)
  .link('http://localhost:3000')
  .listen(1338, function(){
     console.log('Zetta is running at http://127.0.0.1:1338');
});