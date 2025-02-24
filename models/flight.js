const axios = require('axios');

// Function to fetch flight options from Skyscanner API
async function GetFlightOptions(origin, destination, date) {
    const url = `https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/US/USD/en-US/${origin}-sky/${destination}-sky/${date}`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'x-rapidapi-key': process.env.SKYSCANNER_API_KEY
            }
        });

        // Parse the flight data to return essential details
        return response.data.Quotes.map(flight => ({
            name: `Flight from ${origin} to ${destination}`,
            price: `$${flight.MinPrice}`,
            direct: flight.Direct ? 'Yes' : 'No',
            departureDate: flight.OutboundLeg.DepartureDate
        }));
    } catch (error) {
        console.error('Error fetching flight options:', error);
        return [];
    }
}

module.exports = { GetFlightOptions };
