const form = document.getElementById('depreciation-form');
const calculateButton = document.getElementById('calculate-button');
const resultsDiv = document.getElementById('depreciation-results');

calculateButton.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    fetch('/calculate_cash_flow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })

    fetch('/calculate_depreciation', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })

    .then(response => response.json())
    .then(data => {
        fetch('/results', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => response.text())
        .then(html => {
            const straightLineDepreciation = data.straight_line_depreciation;
            const reducingBalanceDepreciation = data.reducing_balance_depreciation;
            resultsDiv.innerHTML = `
            <h2>Depreciation Results</h2>
            <p>Straight-Line Depreciation: ${straightLineDepreciation}</p>
            <h3>Reducing Balance Depreciation:</h3>
            <ul>
                ${reducingBalanceDepreciation.map((depreciation, index) => `
                    <li>Period ${index + 1}: ${depreciation}</li>
                `).join('')}
            </ul>
        `;  
            resultsDiv.innerHTML = html;
        });
    });
});