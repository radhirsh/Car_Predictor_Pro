import numpy as np
from sklearn.impute import SimpleImputer
import pickle
lr_model = pickle.load(open('./models/New_lr_model.pkl', 'rb'))


def predict_price(engine_size, horsepower, city_mpg):
    # Prepare input data as a numpy array
    new_data = np.array([[engine_size, horsepower, city_mpg]])

    # Impute missing values with the mean of each column
    imputer = SimpleImputer(strategy='mean')
    new_data_imputed = imputer.fit_transform(new_data)

    # Predict the output
    prediction = lr_model.predict(new_data_imputed)
    return prediction[0]
