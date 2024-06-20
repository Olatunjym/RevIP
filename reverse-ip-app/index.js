const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/reverse-ip', { useNewUrlParser: true, useUnifiedTopology: true });

// Define a schema and model
const ipSchema = new mongoose.Schema({ reversedIp: String });
const Ip = mongoose.model('Ip', ipSchema);

app.get('/', (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    const reversedIp = ip.split('.').reverse().join('.');
    res.send(`Reversed IP: ${reversedIp}`);
    
    // Save to database
    const ipEntry = new Ip({ reversedIp });
    ipEntry.save().then(() => console.log('Reversed IP saved to database'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
