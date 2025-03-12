import { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles.css"; // Make sure to create a styles.css file

// Modern Navbar
function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white shadow-sm fixed-top">
      <div className="container">
        <a className="navbar-brand fw-bold fs-3 text-primary" href="#">
          ✈️ WanderSync
        </a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link" href="#">Home</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Destinations</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

// Hero Section with Modern Design
function Hero() {
  return (
    <section className="hero-section text-white text-center d-flex align-items-center">
      <div className="container">
        <h1 className="display-3 fw-bold">Your Next Adventure Awaits</h1>
        <p className="lead">Plan your dream trip with AI-powered recommendations.</p>
        <a href="#planner" className="btn btn-lg btn-light fw-bold mt-3">Start Planning</a>
      </div>
    </section>
  );
}

// Travel Plan Display
function TravelPlan({ plan }) {
  if (!plan) return <p className="text-center text-muted">No travel plan available.</p>;

  return (
    <div className="travel-plan p-4 bg-light shadow-sm rounded">
      <h2 className="text-center text-primary">Your Personalized Travel Plan</h2>
      <div className="row mt-3">
        {Object.keys(plan).map((day, index) => (
          <div key={index} className="col-md-6">
            <div className="bg-white p-3 rounded shadow-sm mb-3">
              <h3 className="text-primary">{day}</h3>
              {plan[day].map((trip, idx) => (
                <div key={idx} className="p-3 bg-light border rounded mt-2">
                  <p><strong>Route:</strong> {trip.route.join(" → ")}</p>
                  <p><strong>Travel Time:</strong> {trip.travel_time} hours</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// Footer with Social Icons
function Footer() {
  return (
    <footer className="footer bg-dark text-white text-center py-4">
      <p className="mb-2">© 2025 WanderSync </p>
      <div>
        <a href="#" className="text-light me-3"><i className="bi bi-facebook"></i></a>
        <a href="#" className="text-light me-3"><i className="bi bi-instagram"></i></a>
        <a href="#" className="text-light"><i className="bi bi-twitter"></i></a>
      </div>
    </footer>
  );
}

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
    <div>
      <Navbar />
      <Hero />

      {/* Main Content */}
      <div id="planner" className="container py-5">
        <div className="row align-items-start">
          {/* Form Section */}
          <div className="col-lg-5">
            <form onSubmit={handleSubmit} className="bg-white p-4 shadow-sm rounded">
              <h4 className="text-primary text-center mb-4">Plan Your Trip</h4>
              <div className="mb-3">
                <label className="form-label">Start Location</label>
                <input type="text" name="start" value={formData.start} onChange={handleChange} className="form-control" />
              </div>
              <div className="mb-3">
                <label className="form-label">Place Type</label>
                <select name="place_type" value={formData.place_type} onChange={handleChange} className="form-select">
                  <option value="Hill Station">Hill Station</option>
                  <option value="Backwaters">Backwaters</option>
                  <option value="Beach">Beach</option>
                </select>
              </div>
              <div className="mb-3">
                <label className="form-label">Max Travel Hours</label>
                <input type="number" name="max_travel_hours" value={formData.max_travel_hours} onChange={handleChange} className="form-control" />
              </div>
              <button type="submit" className="btn btn-primary w-100">Generate Plan</button>
            </form>
          </div>

          {/* Travel Plan Section */}
          <div className="col-lg-7">
            {plan && <TravelPlan plan={plan} />}
          </div>
        </div>
      </div>

      <Footer />
    </div>
  );
}
