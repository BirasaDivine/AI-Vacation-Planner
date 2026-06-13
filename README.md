# AI Vacation Planner API

A REST API backend for planning vacations end-to-end. Users can register, log in, create trips, and store itineraries.

## Setup Instructions

1. Clone the repository
   git clone https://github.com/BirasaDivine/AI-Vacation-Planner.git
   cd AI-Vacation-Planner

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Create a `.env` file in the root folder with:
   SECRET_KEY=yoursecretkey
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ANTHROPIC_API_KEY=your_anthropic_key_here

5. Run the app
   uvicorn app.main:app --reload

6. Visit http://127.0.0.1:8000/docs to explore the API

## Architecture


models:SQLAlchemy database tables (User, Trip, Itinerary)

schemas:Pydantic schemas that define the shape of data sent and received

routers:API route handlers (auth, trips, itineraries)

services:Business logic separated from routing

core:Security layer (password hashing, JWT tokens)

database:Database connection, session management

claude.py: Handle all communication 
with the Claude API

## Endpoints

### Auth
- POST /api/register  → Register a new user
- POST /api/login     → Authenticate an existing user and return a JWT token

### Trips
- GET    /api/trips        → Get all trips
- POST   /api/trips        → Create a new trip
- GET    /api/trips/{id}   → Get a single trip
- PUT    /api/trips/{id}   → Update a trip
- DELETE /api/trips/{id}   → Delete a trip

### Itineraries
- POST /api/itineraries            → Create an itinerary
- GET  /api/itineraries/{trip_id}  → Get itinerary for a trip

### LLM Integration
- **Model:** Claude Haiku
- **Library:** Anthropic
- **How it works:** When a user sends a POST request to 
  /api/itineraries with a trip_id, the backend:
  1. Validates the trip_id exists in the database
  2. Fetches trip details (destination, days, budget, travel style)
  3. Builds a prompt using the trip details and sends it to Claude
  4. Claude generates a day by day itinerary in JSON format
  5. Backend parses the response and saves each day to the database
  6. Returns the generated itinerary to the client

- **Prompt:** The prompt includes the destination, number of days,
  budget and travel style to generate a realistic day by day itinerary.

## Technologies Used
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Anthropic (Claude Haiku)