const form = document.getElementById('tvm-form');
const calculateButton = document.getElementById('calculate-button');
const resultsDiv = document.getElementById('tvm-results');

calculateButton.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    fetch('/calculate_tvm', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const presentValue = data.present_value;
        const futureValue = data.future_value;

        resultsDiv.innerHTML = `
            <h2>Time Value of Money Results</h2>
            <p>Present Value: ${presentValue}</p>
            <p>Future Value: ${futureValue}</p>
        `;
    });
});