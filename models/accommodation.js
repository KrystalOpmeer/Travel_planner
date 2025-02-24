const axios = require('axios');

// Function to fetch accommodations from Google Hotels API
async function GetAccommodations(destination, accommodation_type, budget) {
    try {
        const url = `https://www.googleapis.com/hotels/v1/hotel/availabilities`;
        
        const response = await axios.get(url, {
            params: {
                destination: destination,
                checkin_date: '2025-03-01',
                checkout_date: '2025-03-07',
                adults: 2, // Number of people
                key: process.env.GOOGLE_HOTEL_API_KEY
            }
        });

        // Parsing hotel data (replace with actual response structure from Google Hotels API)
        return response.data.hotels.map(hotel => ({
            name: hotel.name,
            price: hotel.price,
            rating: hotel.rating
        }));
    } catch (error) {
        console.error('Error fetching accommodations:', error);
        return [];
    }
}

module.exports = { GetAccommodations };
