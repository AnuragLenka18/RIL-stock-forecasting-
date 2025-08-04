from statsmodels.tsa.arima.model import ARIMA

def train_model(df, column='Close', order=(5,1,0)):
    model = ARIMA(df[column], order=order)
    model_fit = model.fit()
    return model_fit

def forecast_prices(model_fit, steps=30):
    forecast = model_fit.forecast(steps=steps)
    return forecast
