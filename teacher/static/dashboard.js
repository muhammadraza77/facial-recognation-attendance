var ctxD = document.getElementById("doughnutChart").getContext('2d');
  var myLineChart = new Chart(ctxD, {
    type: 'doughnut',
    data: {
      labels: ["Abset", "Present", "Late"],
      datasets: [{
        data: [4, 20, 2],
        backgroundColor: ["#F7464A", "#34AB17", "#FDB45C"],
        hoverBackgroundColor: ["#FF5A5E", "#34AB17", "#FFC870"]
      }]
    },
    options: {
      responsive: true
    }
  });