async function checkEmail() {
    const emailContent = document.getElementById("emailInput").value;
    const resultDiv = document.getElementById("result");

    if (!emailContent.trim()) {
        resultDiv.innerText = "Please enter email content.";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email: emailContent }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch prediction.");
        }

        const data = await response.json();
        resultDiv.innerHTML = `Result: <strong>${data.result}</strong><br>Confidence: <strong>${data.confidence}</strong>`;
    } catch (error) {
        resultDiv.innerText = "Error: " + error.message;
    }
}
