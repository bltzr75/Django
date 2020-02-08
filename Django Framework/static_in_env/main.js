
var btn = document.getElementById("btn")
var container = document.getElementById("ourcontainer")
var url = 'http://127.0.0.1:8000/'

btn.addEventListener("click", function(){
        var ourRequest = new XMLHttpRequest();
        ourRequest.open("GET",  url);
        ourRequest.onload = function(){
            console.log(ourRequest.responseText);
            var ourData = JSON.parse(ourRequest.responseText);
            console.log(ourData);
        }


  })