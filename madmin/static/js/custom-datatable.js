$(document).ready(function() {
	$.ajax({
		url: '/static/js/data/teammate-analytics.json',
		type: 'get',
		dataType: 'json',
		success: function(data){
			console.log(data)
			var teammate_analytics = $('#teammate-analytics').DataTable({
				data: data,
				'paging': true,
				'sort': true,
				'searching': true,
				columns: [
			        { data: 'agent' },
			        { data: 'incoming' },
			        { data: 'resolved' },
			        { data: 'open' },
			        { data: 'first_response_pending' },
			        { data: 'first_response_time' },
			        { data: 'avg_resolution_time' }
			    ]
			});
	
			
		}
	})
	
	// Customer Ratings
	$.ajax({
		url: '/static/js/data/customer-rating.json',
		type: 'get',
		dataType: 'json',
		success: function(data){
			console.log(data)
			var teammate_analytics = $('#customer-rating').DataTable({
				data: data,
				'paging': true,
				'sort': true,
				'searching': true,
				columns: [
			        { data: 'name' },
			        { data: 'assignee' },
			        { data: 'rating' },
			        { data: 'comment' },
			        { data: 'date' },
			        { data: 'conversation' },
			    ]
			});
	
			
		}
	})
	
	// Bot Analytics
	$.ajax({
		url: '/static/js/data/bot-analytics.json',
		type: 'get',
		dataType: 'json',
		success: function(data){
			console.log(data)
			var teammate_analytics = $('#bot-analytics').DataTable({
				data: data,
				'paging': true,
				'sort': true,
				'searching': true,
				columns: [
			        { data: 'bot_name' },
			        { data: 'intent_name' },
			        { data: 'count' }
			    ]
			});
	
			
		}
	})
	
	// Bot Messages
	$.ajax({
		url: '/static/js/data/bot-messages.json',
		type: 'get',
		dataType: 'json',
		success: function(data){
			console.log(data)
			var teammate_analytics = $('#bot-messages').DataTable({
				data: data,
				'paging': true,
				'sort': true,
				'searching': true,
				columns: [
			        { data: 'bot_name' },
			        { data: 'intennse_name'},
			        { data: 'sentence'},
			        { data: 'category'},
			        { data: 'date'},
			        { data: 'conversation'}
			    ]
			});
	
			
		}
	})


	// User Details

	$.ajax({
		
		url: '/static/js/data/users.json',
		type: 'get',
		dataType: 'json',
		success: function(data){
			console.log(data)
			var teammate_analytics = $('#user-details').DataTable({
				data: data,
				'paging': true,
				'sort': false,
				'searching': true,
				columns: [
			        { data: 'name' },
			        { data: 'userid'},
			        { data: 'last_seen'},
			        { data: 'latest_conversation'},
			        { data: 'delete'},
			        { data: 'block'}
			    ]
			});	
		}
	})
	
	// Delete Block - Users - Popup
	
	$('#user-details').on('click','.fa-trash-alt',function() {
		$("#delete-user").modal();
		var user_delete = $(this).parent().parent().find('td:first-child').text();
		$('#user-delete').html(user_delete)
	});
	
	$('#user-details').on('click','.fa-stop-circle',function() {
		$("#block-user").modal();
		var user_block = $(this).parent().parent().find('td:first-child').text();
		$('#user-block').html(user_block)
	});
})