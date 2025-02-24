const express = require('express');
const router = express.Router();
const { GetFlightOptions } = require('../models/flight');
const { GetAccommodations } = require('../models/accommodation');
const { GetTopAttractions } = require('../models/attractions');

router.post('/', async (req, res) => {
    const { source, destination, group_size, days, interests, budget } = req.body;
    
    try {
        // Fetch flight options
        const flights = await GetFlightOptions(source, destination, '2025-03-01');
        
        // Fetch accommodation options
        const accommodations = await GetAccommodations(destination, 'hotel', budget);
        
        // Fetch top attractions and their travel times
        const attractions = await GetTopAttractions(destination, interests);

        // Generate daily itinerary (simplified version)
        const itinerary = [];
        for (let i = 0; i < days; i++) {
            itinerary.push({
                day: i + 1,
                activities: attractions.slice(i * 3, (i + 1) * 3)
            });
        }

        // Render the results in the itinerary view
        res.render('itinerary', { itinerary, flights, accommodations });
    } catch (error) {
        console.error('Error generating itinerary:', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
