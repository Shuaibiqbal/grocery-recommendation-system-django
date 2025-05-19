import os
import pandas as pd 
from surprise import Dataset, Reader, KNNBasic
import pickle

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
def train_model():
    # Load CSV files 
    orders = pd.read_csv(os.path.join(DATA_PATH, "orders.csv"))
    prior = pd.read_csv(os.path.join(DATA_PATH, "all_order_products.csv"))
    products = pd.read_csv(os.path.join(DATA_PATH, "products.csv"))

    merged = pd.merge(prior, orders, on = "order_id")
    user_product_df = merged[['user_id', 'product_id']].copy()
    user_product_df["rating"] = 1  # Implicit feedback

    reader = Reader(rating_scale = (1,5))
    data = Dataset.load_from_df(user_product_df[["user_id", "product_id", "rating"]], reader)

    trainset = data.build_full_trainset()

    algo = KNNBasic(sim_options = {"user_based": False})
    algo.fit(trainset)

    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    with open(model_path, 'wb') as f:
        pickle.dump(algo, f)
def get_recommendations(user_id, n=5):
    with open(os.path.join(os.path.dirname(__file__), 'model.pkl'), 'rb') as f:
        algo = pickle.load(f)

    products = pd.read_csv(os.path.join(DATA_PATH, 'products.csv'))
    orders = pd.read_csv(os.path.join(DATA_PATH, 'orders.csv'))
    prior = pd.read_csv(os.path.join(DATA_PATH, 'all_order_products.csv'))

    user_orders = orders[orders['user_id'] == user_id]
    user_prior = pd.merge(user_orders, prior, on='order_id')
    user_products = set(user_prior['product_id'].unique())
    all_products = set(prior['product_id'].unique())
    products_to_predict = list(all_products - user_products)

    predictions = []
    for pid in products_to_predict:
        pred = algo.predict(uid=user_id, iid=pid)
        predictions.append((pid, pred.est))

    top_n = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]
    top_product_ids = [pid for pid, _ in top_n]
    recommended = products[products['product_id'].isin(top_product_ids)][['product_id', 'product_name']]

    return recommended.to_dict(orient='records')