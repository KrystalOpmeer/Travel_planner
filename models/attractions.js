const axios = require('axios');

// Function to get travel time between two locations using Google Maps API
async function getTravelTime(origin, destination) {
    try {
        const response = await axios.get('https://maps.googleapis.com/maps/api/distancematrix/json', {
            params: {
                origins: origin,
                destinations: destination,
                key: process.env.GOOGLE_MAPS_API_KEY
            }
        });

        const distanceInfo = response.data.rows[0].elements[0];
        return distanceInfo.duration.text; // Duration (e.g., "15 mins")
    } catch (error) {
        console.error('Error fetching travel time:', error);
        return 'Unknown';
    }
}

// Function to get attractions (real attraction data can be fetched from Google Places API)
async function GetTopAttractions(destination, interests) {
    // Placeholder list of attractions. In a real scenario, you would query Google Places API or any service.
    const attractions = [
        { name: 'Central Park', type: 'nature', rating: 4.8 },
        { name: 'Statue of Liberty', type: 'historic', rating: 4.9 },
        { name: 'Broadway Shows', type: 'business', rating: 4.7 }
    ];

    // Get travel times for each attraction (using Google Maps API)
    for (let attraction of attractions) {
        attraction.travelTime = await getTravelTime(destination, attraction.name);
    }

    return attractions;
}

module.exports = { GetTopAttractions };
