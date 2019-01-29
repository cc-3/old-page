var express = require('express');
var app = express();

app.use(express.static(__dirname + '/build'));
app.get('*', (request, response) => response.sendFile(__dirname + '/build/index.html'))
app.listen(3000);
