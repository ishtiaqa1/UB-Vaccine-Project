"use strict";


//AJAX functions

function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}

//Requests to main.py
function getData() {
  ajaxGetRequest("/bar", Bar);
  ajaxGetRequest("/pie", Pie);
}

//Bar plotting function
function Bar(response) {
  let data = JSON.parse(response);
  let layout = {
    xaxis: {title: 'Location'},
    yaxis: {title: '% Fully Vaccinated'},
    title: 'Vaccination Rate By Location'
  };
  Plotly.newPlot('bar', data, layout);
}

//Pie plotting function
function Pie(response) {
  let data = JSON.parse(response);
  let layout = {
    title: 'Vaccine Manufacturer Market Share',
    height: 400,
    width: 500
  };
  Plotly.newPlot('pie', data, layout);
}

//Post requests 
function getLocData() {
  let locText = document.getElementById('locText');
  let Blob = JSON.stringify(locText['value']);
  ajaxPostRequest("line", Blob, Line);
}

//Line plotting function
function Line(response) {
  console.log(response)
  let data = JSON.parse(response);
  let layout = {
    title : "% Fully Vaccinated by Date",
    xaxis : {
      title : "Date"
    },
    yaxis : {
      title : "% Fully Vaccinated"
    },
  };
  Plotly.newPlot('line', data, layout);
}
