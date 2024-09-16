

document.getElementById('fetchButton').addEventListener('click', () => {
    
const url = 'http://127.0.0.1:5000/api/data';

fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); 
        })
        .then(data => {
            
            document.getElementById('dataContainer').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            document.getElementById('dataContainer').textContent = 'Error fetching data';
        });
});

