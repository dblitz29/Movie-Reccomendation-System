const express = require('express');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const PORT = 5000;  // Change to a different port if necessary

// Function to call the Python script
function callPythonScript(title, genre, origin, n_recommendations) {
    return new Promise((resolve, reject) => {
        const scriptPath = path.join(__dirname, 'recommendation.py');  // Use the current directory
        const args = [
            scriptPath,
            title,
            '--genre', genre || '',
            '--origin', origin || '',
            '--n_recommendations', n_recommendations.toString()
        ];
        
        const pythonProcess = spawn('python3', args);

        let data = '';
        pythonProcess.stdout.on('data', (chunk) => {
            data += chunk.toString();
        });

        pythonProcess.stderr.on('data', (chunk) => {
            console.error(`stderr: ${chunk}`);
        });

        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                return reject(`Python script exited with code ${code}`);
            }
            try {
                const recommendations = JSON.parse(data);
                resolve(recommendations);
            } catch (error) {
                reject(`Failed to parse JSON: ${error.message}`);
            }
        });
    });
}

app.get('/recommend', async (req, res) => {
    const { title, genre, origin, n_recommendations } = req.query;

    try {
        const recommendations = await callPythonScript(
            title,
            genre || '',
            origin || '',
            n_recommendations || 10
        );
        console.log(`Recommendations for "${title}":`, recommendations);
        res.json(recommendations);
    } catch (error) {
        console.error(`Error fetching recommendations for "${title}":`, error);
        res.status(500).send(error);
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
