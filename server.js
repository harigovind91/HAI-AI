const express = require('express');
const app = express();
const path = require('path');

app.use(express.static('public'));
app.use(express.json());

// API: Save & Publish Project
app.post('/publish', (req, res) => {
    const projectData = req.body;
    // यहाँ डेटाबेस में सेव करने का लॉजिक
    res.json({ success: true, url: "https://hai-studio.com/project_live" });
});

app.listen(9000, () => {
    console.log("● HAI GLOBAL BRAIN ACTIVE ON PORT 9000");
});
