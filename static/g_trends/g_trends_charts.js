$(function () {

  var $populationChart = $("#bar-chart");
  $.ajax({
    url: $populationChart.data("url"),
    success: function (data) {

      var ctx = $populationChart[0].getContext("2d");

      new Chart(ctx, {
        type: 'bar',
        data:data,
        options: {
          responsive: true,
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: ''
          }
        }
      });

    }
  });
});

$(function () {

var $populationChart = $("#line-chart");
$.ajax({
url: $populationChart.data("url"),
success: function (data) {

var ctx = $populationChart[0].getContext("2d");

new Chart(ctx, {
type: 'line',
data: data,
options: {
responsive: true,
legend: {
  position: 'top',
},
title: {
  display: true,
  text: ''
}
}
});

}
});
});	