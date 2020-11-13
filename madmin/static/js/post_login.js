function uploadFile(target) {
    document.getElementById("file-name").innerHTML = target.files[0].name;
    document.getElementById('custom-icon-url').value = target.files[0].name;
    console.log( target.files[0].name) 
}
var adminInfo = [];

$(document).ready(function() {
	$('.tab-name').click(function() {
		var tabname = $(this).attr('data-attr');
		$('.tab-name').removeClass('active');
		$(this).addClass('active');
		
		$('.tab-content').removeClass('current');
		$(tabname).addClass('current');

		//$('#default-chat-icon').val();
	});


	// Chat widget Config - Tab name
	
	$('.tab-name-heading').click(function() {
		$('.tab-name-heading').removeClass('active');
		$(this).addClass('active');
		let chat_widget_tabs = $(this).attr('data-attr')
		$('.tab-content').removeClass('current');
		$(chat_widget_tabs).addClass('current');
	})
	

	// 3D On - Off

			$('.slider').each(function() {
				if($(this).find('.slider-inp').val() == 'True') {
					$(this).find('.round').css('left','30px');
					$(this).css('background-color','#080C62');
				} else {
					$(this).find('.round').css('left','5px');
					$(this).css('background-color','#cccccc');
				}
			})
			
			$('.slider').click(function() {
				var inpVal = $(this).find('.slider-inp');
				if(inpVal.val() == 'False') {
					inpVal.val('True');
					$(this).css('background-color','#080C62');
					$(this).find('.round').css('left','30px');
				} else {
					inpVal.val('False');
					$(this).css('background-color','#cccccc');
					$(this).find('.round').css('left','5px');
				}	
			})
	
	// Chat  Configuration  - Accordion

	if($('.content').hasClass('active')) {
		$('.content.active').prev().find('.fas').removeClass('fa-plus').addClass('fa-minus');
	}
	$('.accordion-box').click(function() {
		var icon = $(this).find('.fas.collapse-expand');
		var content = $(this).find('.accordion-content')
		accordionToggle(icon, content);
	});
	
	function accordionToggle(icon, content) {
		content.parents().siblings().find('.accordion-content').removeClass('expand-acc');
		icon.parents().siblings().find('.fas.collapse-expand').removeClass('fa-minus').addClass('fa-plus');
		if(content.hasClass('expand-acc')) {
			content.removeClass('expand-acc');
			icon.addClass('fa-plus');
			icon.removeClass('fa-minus');
		} else {
			content.addClass('expand-acc');
			icon.addClass('fa-minus');
			icon.removeClass('fa-plus');
		}
	}
	
	/*$('.accordion-box').click(function() {
		$('.accordion-content').removeClass('expand-acc');
		$(this).find('.accordion-content').addClass('expand-acc');
		$('.accordion-icon i').addClass('fa-plus');
		if($(this).find('.accordion-content').hasClass('expand-acc')) {
			$(this).find('.accordion-icon i').removeClass('fa-plus');
			$(this).find('.accordion-icon i').addClass('fa-minus');
		} else {
			$(this).find('.accordion-icon i').removeClass('fa-minus');
			$(this).find('.accordion-icon i').addClass('fa-plus');
		}
	})*/
	

	$('.tab-icon').click(function() {
		//alert($(this).attr('src'));
		$('#default-chat-icon').val($(this).parent().attr('name'))
	});

	$.ajax({
		type : "get",
		url : "http://127.0.0.1:8000/madmin/username_email_collection/",
		dataType : 'json',
		async : true,
		
		success : function(result) {
			result.forEach(function(ele) {
				adminInfo.push(ele)
			});
		}
	});
	
	console.log('After',adminInfo)
	
	$('#add-teammate').submit(function(e) {
		let ret = true;
		var username = $('#username').val();
		var email = $('#email').val();
		var form = $(this)
		function search(username, email, arr) {
			arr.forEach(function(ele) {
				if(ele.username == username || ele.email == email) {
					if(ele.username == username) {
						alert('User already exists');
						ret = false; 
						return ret;
					} 
					
					if(ele.email == email) {
						alert('Email already exists');
						ret = false; 
						return ret;
					}
				}
			});
		}
		search(username, email, adminInfo);
		if(!(ret)) {
			e.preventDefault();
		}
		//e.preventDefault();
	})

	// Profile Update
	
	$('.logout').click(function() {
		$("#signout").modal();
	})
	
	$('.profile-icon .profile').click(function() {
		$("#profile-info").modal();
	});
	
	$('#change-password').click(function() {
		$("#profile-info").modal('hide');
		$("#password-reset").modal();
	});

	$('#invite').click(function() {
		//$("#profile-info").modal('hide');
		$("#teamate-popup").modal();
	});
	
	$('#form-pwd-reset').submit(function(e) {
		e.preventDefault();
		/*var passwordChange = {
				oldPass: $('#old-pwd').val(),
				newPass: $('#new-pwd').val(),
				confirmPass: $('#confirm-pwd').val(),
		}*/
		$.ajax({
			type : "POST",
			url : "action.html",
			/*data : JSON.stringify(passwordChange),
			dataType : 'json',*/
			async : true,
			beforeSend : function() {
			},
			error : function(jqXHR, error_textStatus, errorThrown) {
				//alert("jqXHR.readyState:" + jqXHR.readyState);
				//alert("jqXHR.status:" + jqXHR.status);
				//alert("jqXHR.statusText:" + jqXHR.statusText);
				//alert("jqXHR.responseText:" + jqXHR.responseText);
			},

			success : function(result) {
				console.log(result);
				$('#password-reset').modal('hide');
				$('#password-reset-confirm').modal();
			}
		});
	})

	// Chat widget and notification settings
	
	
	// $("#theme-setting").modal();
	$('#chat-widget-setting').click(function() {
		$("#theme-setting").modal();
	})
	
	//$("#notification-setting").modal();
	
	$('#notification-sound-setting').click(function() {
		$("#notification-setting").modal();
	})
	
	var deficon = $('.chat-launch-icon-type.active').find('object').attr('data');
	$('#selected-launch-icon').val(deficon);
	$('.chat-launch-icon-type').click(function() {
		$('.chat-launch-icon-type').removeClass('active');
		$(this).addClass('active');
		$('.chat-launch-icon #launcher-chat-box').html($(this).html());
		
		var iconUrl = $(this).find('object').attr('data');
		
		$('#selected-launch-icon').val(iconUrl);
	});
	
	// Select Notification Sound
	
	$('.dropdown-menu .dropdown-item').click(function() {
		$('#selected-sound').text($(this).text())
	})

	 $('.chat-header').css('background',$('#color-code').val());
 	 $('.sent-msg-text').css('background',$('#color-code').val());
 	 $('.chat-widget-demo').css('border-color',$('#color-code').val());
 	 $('.chat-launch-icon').css('background',$('#color-code').val());
 	 $('#color-picker').css("background", $('#color-code').val());
	
	// Color setting for chat widget
	 $('#color-picker').colorpicker().on('changeColor.colorpicker', function(event){
 	  	//console.log(event.color.toHex());
		$('#color-code').val(event.color.toHex());
 	    $(this).css("background", $('#color-code').val()); 
 	    $('.chat-header').css('background',$('#color-code').val());
 	    $('.sent-msg-text').css('background',$('#color-code').val());
 	    $('.chat-widget-demo').css('border-color',$('#color-code').val())
 	    $('.chat-launch-icon').css('background',$('#color-code').val())
   }); 
	
	// Color setting for chat widget
	/* $('#color-picker').colorpicker().on('changeColor.colorpicker', function(event){
 	  	//console.log(event.color.toHex());
 	    $(this).css("background", event.color.toHex()); 
 	    $('.chat-header').css('background',event.color.toHex());
 	    $('.sent-msg-text').css('background',event.color.toHex());
 	    $('#color-code').val(event.color.toHex());
 	    $('.chat-widget-demo').css('border-color', event.color.toHex())
 	    $('.chat-launch-icon').css('background', event.color.toHex())
   }); */
	
	$('.file-button').click(function() {
		$('input[type="file"]').trigger('click');
	});
	
	// Select Sound
	
	
	
});