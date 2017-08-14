//event handlers

$(init)

function init() {
	russian_inol_sparkline();
}

$("#russian_calc_input").change(function(e) {
	e.preventDefault();
	updateRussian();
});

$("#russian_calc_input").keyup(function(e) {
	e.preventDefault();
	updateRussian();
});

function updateRussian() {
	var max = $("#russian_calc_input").val()
	var russian80 = Math.round(max * 0.8)
	var russian85 = Math.round(max * 0.85)
	var russian90 = Math.round(max * 0.9)
	var russian95 = Math.round(max * 0.95)
	var russian105 = Math.round(max * 1.05)

	$(".russian80").html(russian80 + "kg")
	$(".russian85").html(russian85 + "kg")
	$(".russian90").html(russian90 + "kg")
	$(".russian95").html(russian95 + "kg")
	$(".russian100").html(max + "kg")
	$(".russian105").html(russian105 + "kg")

}


function russian_inol_sparkline() {
	var russian_inol_values = [ 0.6, 0.9, 0.6, 1.2, 0.6, 1.5, 0.6, 1.8, 0.6, 1.6, 0.6, 1.6, 0.6 , 1.8 , 0.6, 4,0.6,2];
	$('.sparkline_russian_inol').sparkline(russian_inol_values, {type: 'line',
		    spotColor: '#0000ff',
		    minSpotColor: '#00bf5f',
		    maxSpotColor: '#00007f',
		    highlightLineColor: '#00ff00',
		    width: '20em',
		    height: '10em',
		    chartRangeMin: 0});
}