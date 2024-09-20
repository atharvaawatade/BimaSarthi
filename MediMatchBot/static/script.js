document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chatForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            resultDiv.textContent = data.response;
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
        }
    });
});