import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

def graph_N1():
 DataFrame = pd.read_csv("GlobalWeatherRepository.csv")

 Required_values = DataFrame[['wind_kph', 'feels_like_celsius', 'temperature_celsius']]
 Required_values['wind_kph_rounded'] = Required_values['wind_kph'].round()

 grouped = Required_values.groupby('wind_kph_rounded').agg(real_temp=('temperature_celsius', 'mean'),feels_temp=('feels_like_celsius', 'mean')).reset_index()

 grouped = grouped[grouped['wind_kph_rounded'] <= 40]

 plt.bar(grouped['wind_kph_rounded'], grouped['real_temp'], color='red', label='Реальна температура')

 plt.scatter(grouped['wind_kph_rounded'], grouped['feels_temp'], color='skyblue', label='Відчутна температура', zorder=5)

 plt.xlabel('Швидкість вітру (км/год)')
 plt.ylabel('Температура (°C)')
 plt.title('Залежність температури від швидкості вітру')
 plt.legend()
 plt.legend(loc='upper left')
 plt.grid(axis='y', linestyle='-')
 plt.show()

def graph_N2():
 DataFrame = pd.read_csv("GlobalWeatherRepository.csv")

 DataFrame['last_updated'] = pd.to_datetime(DataFrame['last_updated'])

 DataFrame['wind_category'] = pd.cut(DataFrame['wind_kph'], bins=[0, 0.2, 1.5, 3.3, 5.4, 7.9,20,32,100],labels=['Штиль', 'Тихий', 'Легкий', 'Слабкий', 'Помірний','Міцний','Шторм',"Ураган"])

 DataFrame['day_of_week'] = DataFrame['last_updated'].dt.dayofweek

 wind_day = DataFrame.groupby(['day_of_week', 'wind_category'], observed=False).size().unstack(fill_value=0)

 wind_day.index = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']

 wind_day.plot(kind='bar', stacked=True, figsize=(22, 11),color = ['gray', 'blue', 'green', 'yellow', 'orange', 'red', 'purple', 'darkblue'])
 plt.title('Розподіл категорій вітрів по днях')
 plt.ylabel('Зафіксовано')
 plt.xticks(rotation=0)
 plt.legend(title='Легенда діаграми')
 plt.grid(axis='y', linestyle='-')
 plt.show()

def graph_N3():
 DataFrame = pd.read_csv("GlobalWeatherRepository.csv")
 DataFrame['last_updated'] = pd.to_datetime( DataFrame['last_updated'])

 DataFrame['wind_category'] = pd.cut( DataFrame['wind_kph'], bins=[0, 0.2, 1.5, 3.3, 5.4, 7.9, 20, 32, 100],labels=['Штиль', 'Тихий', 'Легкий', 'Слабкий', 'Помірний', 'Міцний', 'Шторм', "Ураган"])

 DataFrame['hour_of_day'] =  DataFrame['last_updated'].dt.hour

 wind_hour =  DataFrame.groupby(['hour_of_day', 'wind_category']).size().unstack(fill_value=0)

 wind_hour.plot(kind='bar', stacked=True, figsize=(12, 6),color=['gray', 'blue', 'green', 'yellow', 'orange', 'red', 'purple', 'darkblue'])

 plt.title('Типи вітру за годинами доби')
 plt.xlabel('Година доби')
 plt.ylabel('Кількість випадків')
 plt.xticks(rotation=0)
 plt.legend(title='Категорії вітру')
 plt.grid(axis='y', linestyle='-')
 plt.show()


root = tk.Tk()
root.title("Графічний інтерфейс для аналізу вітру")
root.geometry("500x250")
button_N1 = tk.Button(root, text="Графік різниці температур", command=graph_N1)
button_N1.pack(pady=15)
button_N2 = tk.Button(root, text="Графік інтенсивності типів відрів (дні)", command=graph_N2)
button_N2.pack(pady=15)
button_N3 = tk.Button(root, text="Графік інтенсивності типів відрів (години)", command=graph_N3)
button_N3.pack(pady=15)
root.mainloop()




