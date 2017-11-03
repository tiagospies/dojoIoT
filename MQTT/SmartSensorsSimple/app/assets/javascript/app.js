$(document).on('ready', function() {
    
        function setBackground(value) {
            return 'rgb(' + value + ', ' + value + ', ' + value + ')';
        }
    
        function setColor(value) {
            value = 255 - value;
            return value < 128 ? 'rgb(0, 0, 0)' : 'rgb(255, 255, 255)';
        }
        var socket = io.connect("http://localhost:5000");
        var ready = false;
        
        socket.on("updateData", function(data) {
            if(data.temperature !== undefined){
                $('#sensor-' + data.sensorId).html(data.temperature);
            } 
            if(data.luminosity !== undefined){
                $('#sensor-' + data.sensorId).parent().parent().css({
                    background: setBackground(data.luminosity),
                    color: setColor(data.luminosity)
                });
            }
        });    
    });