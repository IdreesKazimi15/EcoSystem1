const form = document.getElementById('energy-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    if (validateForm()) {
        sendData();
    }
});

function validateForm() {
    const requiredFields = [
        'householdSize', 'houseSize', 'location', 
        'applianceAge', 'applianceUsage', 
        'lightingType', 'lightingUsage', 
        'averageBill', 'energyEfficiencyInterest'
    ];
    
    for (const field of requiredFields) {
        const input = document.getElementById(field);
        if (!input.value.trim()) {
            alert(`Please fill in ${input.previousElementSibling.textContent}`);
            input.focus();
            return false;
        }
    }
    
    return true;
}

function sendData() {
    const formData = new FormData(form);

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            form.reset();
        } else {
            alert('Failed to submit form. Please try again later.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    });
}
