$('document').ready(function() {
	// Show hide password
	$('.show-hide-pwd').click(function() {
		if($(this).find('i').hasClass('fa-eye')) {
			$(this).find('i').removeClass('fa-eye').addClass('fa-eye-slash');
			$(this).prev().attr('type','text');
		} else {
			$(this).find('i').removeClass('fa-eye-slash').addClass('fa-eye');
			$(this).prev().attr('type','password');
		}
	})
})