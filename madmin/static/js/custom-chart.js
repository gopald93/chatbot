
// Bot Conversation

var ctx = document.getElementById('bot-conv-chart');
ctx.height = 300;
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
    	labels: ['Oct10', 'Oct11', 'Oct12', 'Oct13', 'Oct14', 'Oct15'],
        datasets: [{
            label: 'Conversations handled by bot',
            data: [1, 0, 1, 0, 1, 0, 6],
            backgroundColor: [
                'rgba(255, 99, 132, 0)',
                'rgba(54, 162, 235, 0)',
                'rgba(255, 206, 86, 0)',
                'rgba(75, 192, 192, 0)',
                'rgba(153, 102, 255, 0)',
                'rgba(255, 159, 64, 0)'
            ],
            borderColor: [
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        maintainAspectRatio: false,
        title: {
            display: true,
            text: 'Conversations handled by bot'
        },
        legend: {
            display: false,
            labels: {
                fontColor: 'rgb(255, 99, 132)'
            }
        }
    }
});


// Teammate's conversation
var ctx2 = document.getElementById('agent-conv-chart');
ctx2.height = 300;
var myChart = new Chart(ctx2, {
    type: 'line',
    data: {
    	labels: ['Oct10', 'Oct11', 'Oct12', 'Oct13', 'Oct14', 'Oct15'],
        datasets: [{
            label: 'Conversations handled by bot',
            data: [0, 0, 0, 0, 0, 0, 6],
            backgroundColor: [
                'rgba(255, 99, 132, 0)',
                'rgba(54, 162, 235, 0)',
                'rgba(255, 206, 86, 0)',
                'rgba(75, 192, 192, 0)',
                'rgba(153, 102, 255, 0)',
                'rgba(255, 159, 64, 0)'
            ],
            borderColor: [
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
                'rgba(0, 0, 0, 0.6)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        maintainAspectRatio: false,
        title: {
            display: false,
            text: 'Conversations handled by bot'
        },
        legend: {
            display: false,
            labels: {
                fontColor: 'rgb(255, 99, 132)'
            }
        }
    }
});

// Conversation Sattus - Doughnut chart

var ctx3 = document.getElementById('conv-status');
ctx2.height = 300;
var myChart = new Chart(ctx3, {
	type: 'doughnut',
    data: {
        datasets: [{
            data: [10, 20, 30],
            backgroundColor: ['#6AD9A9','#EB7E38', '#F4CC65'],
        }],
        backgroundColor: [
            'rgba(255, 99, 132, 0)',
            'rgba(54, 162, 235, 0)',
            'rgba(255, 206, 86, 0)',
        ],
        labels: [
            'Resolved',
            'First Response Pending',
            'In Progress'
        ],
       
    },
    
    
    options: {
    	maintainAspectRatio: true,
       
        legend: {
        	
        	fontColor: '#ccc',
        	position: 'bottom',
        	
        	align: 'center',
        	display: true,
            labels: {
            	boxWidth: 15,
            	fullWidth: true,
                fontColor: '#202020'
            }
        }
    }
   
});

