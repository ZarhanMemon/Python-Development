# Predicting Pune City House Prices

---

## 1. Why Are We Building This?

Pune, a rapidly growing city in India, has seen a sharp rise in real estate development over the past decade. With its proximity to Delhi, booming IT hubs, and modern infrastructure, Pune has become a major attraction for both homebuyers and investors. However, the real estate market here is highly dynamic and often difficult to assess without proper data-driven tools.

We’re building a Pune house price prediction model to help:

* **Understand Market Drivers:** Analyze how factors like location, size, number of rooms, and amenities affect property prices in Pune.
* **Assist Buyers:** Identify fair prices based on historical trends.
* **Help Sellers:** Estimate an appropriate asking price.
* **Empower Professionals:** Enable real estate agents and platforms to improve recommendations and negotiations.


---

### 2. How Will We Build It?

While we don’t have access to a large, clean dataset of house prices in Pune right now, we will use a well-known and cleaned dataset—the California housing dataset—as a proxy. This will allow us to build, test, and evaluate a working model with real-world variables like:

* Median income of the area
* Proximity to the city center
* Number of rooms
* Latitude and longitude
* Population density

> **The Simulation Strategy:** We'll treat this as a simulation: suppose the California data is Pune data, and suppose we are building this model for a neighborhood where both you and I live or work nearby.
>
> Once the model is developed and understood, we can later adapt the same approach to real Pune data when available, using the same techniques and logic.


Hint : Multiple Regression to get predicted house price
