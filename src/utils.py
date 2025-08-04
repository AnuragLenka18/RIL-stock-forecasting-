import matplotlib.pyplot as plt

def plot_forecast(actual, forecast, title='RIL Forecast'):
    plt.figure(figsize=(10,6))
    actual.plot(label='Actual')
    forecast.plot(label='Forecast', style='--')
    plt.title(title)
    plt.legend()
    plt.savefig('outputs/forecast_plot.png')
    plt.show()
