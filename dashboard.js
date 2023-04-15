/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars

  const file_location = "https://drive.google.com/uc?id=1tswwNfrNDx6_xIVpPLKJijKHcZTpeBu4&export=download";

  const json_data = fetch(file_location)
    .then((response) => response.json())
    .then((json) => {return json});

  let co2_timestamp = new Array();
  let co2_data = new Array();

  json_data.forEach(element => {
    test = new Date(element.date).getDate();
    today = new Date().getDate();
    if (today - test <= 86400000) {/* one day in milsec */ 
      co2_timestamp.push(element.date);
      co2_data.push(element.eCO2);
  }
  });

  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: co2_timestamp,
      datasets: [{
        data: co2_data,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()
