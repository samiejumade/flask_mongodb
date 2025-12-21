// express app that serve html files
var express = require('express');   
var app = express();    
app.use(express.static('public'));  

app.set('view engine', 'ejs');
const URL = process.env.BACKEND_URL || 'http://127.0.0.1:9000/api';

const fetch = require('node-fetch');

app.get('/', async function(req, res) {
    const options = {
        method: 'GET'
    };
    
    try {
        const response = await fetch(URL, options);
        const data = await response.json();
        console.log('Data received from backend:', data);
        res.render('index', { data: data });
    }
    catch(error) {
        console.log('Error fetching data:', error);
        res.render('index', { data: null });
    }
});

app.listen(3000, function() {
    console.log('Server started on port 3000');
});