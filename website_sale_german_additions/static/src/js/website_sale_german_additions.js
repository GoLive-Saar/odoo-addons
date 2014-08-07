$(document).ready(function () {

	//check if revocation checkbox is checked and stop submit
	$("form").submit(function(e) {
		if(!$('#revbox').attr('checked')) {
			e.preventDefault();
			$('#revlabel').addClass('has-error');
			$('#rev').addClass('has-error');
		}
	});
	
});