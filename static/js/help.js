$(document).ready(function() {


	$('form').on('submit', function(event) {
		$.ajax({
			data: {
				string : $('#inputString').val()
			},
			type: 'POST',
			url : '/process'
		})
		.done(function(data){
			
			if(data.message) {
				$('#errorAlert').text(data.message).show()
				$('#successAlert').hide()
			}
			else {
				$('#errorAlert').hide()
				$('#successAlert').text(data.result).show()				
			}
		});

		event.preventDefault();
	});
});
