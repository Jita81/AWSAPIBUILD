document.addEventListener("DOMContentLoaded", function() {
    const testForm = document.getElementById("test-form");
    testForm.addEventListener("submit", async function(event) {
        event.preventDefault();

        const apiKey = document.getElementById("api-key").value;
        const apiEndpoint = document.getElementById("api-endpoint").value;
        const testInput = document.getElementById("test-input").value;
        const testResults = document.getElementById("test-results");

        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": apiKey
            },
            body: JSON.stringify({input: testInput})
        };

        try {
            const response = await fetch(apiEndpoint, requestOptions);
            const responseData = await response.json();
            testResults.textContent = JSON.stringify(responseData, null, 2);
        } catch (error) {
            testResults.textContent = `Error: ${error.message}`;
        }
    });
});
