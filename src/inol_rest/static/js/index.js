//event handlers

$("#russian_calc_btn").click(function(e) {

	e.preventDefault();

	var max = $("#russian_calc_input").val()
	var russian80 = max * 0.8
	var russian85 = max * 0.85
	var russian90 = max * 0.9
	var russian95 = max * 0.95
	var russian105 = max * 1.05

	$(".russian80").html(russian80 + "kg")
	$(".russian85").html(russian85 + "kg")
	$(".russian90").html(russian90 + "kg")
	$(".russian95").html(russian95 + "kg")
	$(".russian100").html(max + "kg")
	$(".russian105").html(russian105 + "kg")
});
