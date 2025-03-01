import { useState } from "react";
import axios from "axios";

export default function TravelPlanner() {
  const [formData, setFormData] = useState({
    start: "Alappuzha",
    place_type: "Hill Station",
    max_travel_hours: 6,
    budget: "Low",
    num_days: 3,
    return_to_start: true,
  });

  const [plan, setPlan] = useState(null);

  const TravelPlan = ({ plan }) => {
    if (!plan) return <p>No travel plan available.</p>;

    return (
        <div>
            <h2 className="text-xl font-bold mb-3">Recommended Travel Plan</h2>
            {Object.keys(plan).map((day, index) => (
                <div key={index} className="border rounded-lg p-4 mb-3 shadow">
                    <h3 className="text-lg font-semibold">{day}</h3>
                    {plan[day].map((trip, idx) => (
                        <div key={idx} className="pl-4 mt-2">
                            <p><strong>Route:</strong> {trip.route.join(" → ")}</p>
                            <p><strong>Travel Time:</strong> {trip.travel_time} hours</p>
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
};


  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/generate_plan", formData);
      setPlan(response.data);
    } catch (error) {
      console.error("Error fetching plan:", error);
    }
  };


  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Personalized Travel Plan</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <label className="block">Start Location:
          <input type="text" name="start" value={formData.start} onChange={handleChange} className="border p-2 w-full" />
        </label>
        <label className="block">Place Type:
          <select name="place_type" value={formData.place_type} onChange={handleChange} className="border p-2 w-full">
            <option value="Hill Station">Hill Station</option>
            <option value="Backwaters">Backwaters</option>
            <option value="Beach">Beach</option>
            <option value="City">City</option>
            <option value="Waterfalls">Waterfalls</option>
            <option value="Wildlife">Wildlife</option>
          </select>
        </label>
        <label className="block">Max Travel Hours:
          <input type="number" name="max_travel_hours" value={formData.max_travel_hours} onChange={handleChange} className="border p-2 w-full" />
        </label>
        <label className="block">Budget:
          <select name="budget" value={formData.budget} onChange={handleChange} className="border p-2 w-full">
            <option value="Low">Low</option>
            <option value="Mid">Mid</option>
            <option value="High">High</option>
          </select>
        </label>
        <label className="block">Number of Days:
          <input type="number" name="num_days" value={formData.num_days} onChange={handleChange} className="border p-2 w-full" />
        </label>
        <label className="flex items-center space-x-2">
          <input type="checkbox" name="return_to_start" checked={formData.return_to_start} onChange={handleChange} />
          <span>Return to Start Location</span>
        </label>
        <button type="submit" className="bg-blue-500 text-white p-2 rounded w-full">Generate Plan</button>
      </form>

      {plan && (
        <div className="mt-6 p-4 border rounded">
          <h2 className="text-lg font-bold">Recommended Travel Plan</h2>
          <pre className="whitespace-pre-wrap text-sm mt-2">{JSON.stringify(plan, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
