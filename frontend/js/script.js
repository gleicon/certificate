$(function(){
	$('#el_clicko').click(function() {
		$.post('http://certs.yourdomain.cc/api/v1/certs/create', {name: $("#url").val() }, function(data) {
			$('#result').html("<a href=" + data + ">"+ data + "</a>");
		});
	});
});
