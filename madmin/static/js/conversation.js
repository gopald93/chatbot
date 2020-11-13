
$(document).ready(function() {
	// Conversation tabs
	/*$('.conv-tab').click(function() {
		$('.conv-tab').removeClass('active');
		$(this).addClass('active');
	})
	*/
	
	// Search agent
	
/*	$('#serach-agent').keyup(function() {
		var name = $(this).val().toLowerCase();
		
	})*/

	const agname = JSON.parse(document.getElementById('ag_name').textContent);
	var chatSocket = new WebSocket('wss://call2transact.com/ws/agent/'+agname+'/');
	var client_div = [];
	var customersObjectArray = [], currentTab,currentClient ='' ,changeDetected = false;
	var msg, inputMsg_html;
	
	
	chatSocket.onmessage = function(e) {
		var data = JSON.parse(e.data);
		var type = data.fe_type || data.content.fe_type; 
		
		if(type == 'new_user'){
			customerObject = {};
			customerObject.clientName = data.content.client_name;
			customerObject.messages = [];
			customerObject.counter = 0;
			customersObjectArray.push(customerObject);
		}
		
		
		if(type == 'usr_chat_message') {
			var client_name = data.content.client_name;
			var clientMsg = data.content.text;
			
			if(customersObjectArray.length>0){
				customersObjectArray.forEach((element,index)=>{
					if(element.clientName == client_name){
						var msg = {}; 
						msg.fromMsg =  clientMsg;
						msg.toMsg = '';
						element.messages.push(msg);
						element.counter = element.counter + 1;
					}
				})
				refreshCustormersSidepanel();
				
			if(customersObjectArray.length == 1){
				$('.user-element:last-child').trigger( "click" ).addClass('active');
			}else if(!changeDetected){
				$('.user-element:last-child').trigger( "click" ).addClass('active');
			}
				
			}
			
	    }
	}
	
	function refreshCustormersSidepanel(){
		$('#user-grid').html('');
		customersObjectArray.forEach((element,index)=>{
			var badgeValue;
			if(currentTab == index){
				badgeValue = '';
			}else{
				if(element.counter == 0 || element.counter == '' || element.counter == undefined){
					badgeValue = '';
				}else{
					badgeValue = element.counter;
				}
			}
			
			if(badgeValue == ''){
				var ele = document.getElementById('user-grid');
				ele.insertAdjacentHTML('afterbegin', `
				<div class="user-element" id='${index}'>
								<div class="agent-img">
									<img src="/static/admin/images/agent.jpg" alt="" />
								</div>
								<div class="agent-info">
									<div class="title-text">
										${element.clientName}
									</div>
									<div class="created-date">
										Apr 10
									</div>
									<div class="user-lst-msg" id='${index}'>
										${element.messages[element.messages.length-1].fromMsg}
									</div>
								</div>
							</div>
				`);
				
				
			} else {
				var ele = document.getElementById('user-grid');
				ele.insertAdjacentHTML('afterbegin', `
				<div class="user-element" id='${index}'>
						<div class="agent-img">
							<img src="/static/admin/images/agent.jpg" alt="" />
						</div>
						<div class="agent-info">
							<div class="title-text">
								${element.clientName}
							</div>
							<div class="created-date">
								Apr 10
							</div>
							<div class="user-lst-msg" id='${index}'>
								${element.messages[element.messages.length-1].fromMsg}
							</div>
							<span class="badge"><span class="counter">${badgeValue}</span></span>
						</div>
					</div>
				`);
			}
			
		
		});
		
		$('#'+currentTab).trigger('click');
	}

	$('#user-grid').on('click','.user-element',function() {
		var client_id = $(this).attr('id');
		if(client_id!= 0){
			changeDetected = true;
		}
		currentClient = customersObjectArray[client_id].clientName;
		currentTab = client_id ;
		$('.chat-message-list').html('');
		var client = $(this).find('.title-text');
		$('#client-name').html(client.text());
		var ele = $('.user-grid');
		var messages = customersObjectArray[client_id].messages;
		customersObjectArray[client_id].counter = 0;
		var badge = $(this).find('.badge');
		badge.html('');
		
		$('.user-element').removeClass('active');
		$(this).addClass('active');
		$(this).find('.badge').removeClass('badge');
		messages.forEach((element,index)=>{
			var prependString = '';
			if(element.fromMsg && element.toMsg){
				prependString = `
			<div class="message-row you-message" id="chat-log"><div class="message-text">${element.toMsg}</div></div>
			
			<div class="message-row other-message" id="chat-log">
					<div class="message-text">
					${element.fromMsg}
				</div>
			</div> 
			`
			
			}else if(element.fromMsg && !element.toMsg){
				prependString = `<div class="message-row other-message" id="chat-log">
					<div class="message-text">
					${element.fromMsg}
				</div>
			</div>`
			}else {
				prependString =`<div class="message-row other-message" id="chat-log">
				<div class="message-text">
				${element.fromMsg}
			</div>
		</div> `
			}			
			$('.chat-message-list').prepend(`
				${prependString}
			`)
		})
	
	})
	
		$('#chat').on('focus', function(e) {
		  $(this).on('keyup', function(e) {
			  
			  msg = $(this).val();
			   if(e.keyCode == 13) {
				   
				   if($(this).val() == '') {
					   //alert('Field should not be empty')
					   return false;
				   }
				   $('.chat-message-list').prepend(`<div class="message-row you-message" id="chat-log"><div class="message-text">${msg}</div></div>`);
				   customersObjectArray[parseInt(currentTab)].messages[ customersObjectArray[parseInt(currentTab)].messages.length-1].toMsg = msg;
				   
				   chatSocket.send(JSON.stringify({
							'message': msg,
							'client_name': currentClient
				   }));
				   $(this).val('');
				   
			   }
		  })  
	})
})

  

        


      