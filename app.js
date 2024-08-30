// Example of a progress chart using Chart.js
document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('progressChart').getContext('2d');
    var progressChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['July', 'August', 'September'],
            datasets: [{
                label: 'Blood Pressure (mmHg)',
                data: [140, 135, 130],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
});
