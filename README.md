# 🛒 AI-Powered Grocery Recommendation System using Django & Collaborative Filtering
This project is an AI-powered grocery recommendation system built using **Django**. It recommends grocery products to customers based on their purchase history using collaborative filtering (user-based KNN algorithm) implemented with the **Surprise** library.

---

## 🚀 Features

- Trains a recommendation model from Instacart dataset files:
  - `orders.csv`
  - `all_order_products.csv`
  - `products.csv`
- Provides REST API endpoints for:
  - Training the model
  - Fetching personalized product recommendations
- Built with Django and Docker-ready for easy deployment

---

## 📊 Dataset

Dataset files are based on the [Instacart Market Basket Analysis dataset](https://www.kaggle.com/datasets/brendanartley/simplifiedinstacartdata/data)

- `orders.csv` — customer orders
- `all_order_products.csv` — products in each order
- `products.csv` — product metadata

Place these CSV files in the `recommender/data/` directory.

---

## ⚙️ Tech Stack

- Backend: Django (Python)
- Machine Learning: Surprise library (KNN-based collaborative filtering)
- Data processing: Pandas, NumPy
- Deployment: Docker, Docker Compose

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/grocery-recommendation-system-django.git
cd grocery-recommendation-system-django
