import matplotlib.pyplot as plt

def inflation():
    years = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]
    inf_rate = [3.33,4.41,5.39,8.02,9.7,8.9,19.87,29.18,23.41,4.49,9.02]

    plt.figure(figsize=(12,6))

    plt.bar(years,inf_rate, width=0.6)
    plt.plot(years,inf_rate, alpha=0.2)

    plt.title("Pakistan Inflation crises (2016-2026)", fontsize= 21)
    plt.xlabel("Years (2016-2026)", color= 'green')
    plt.ylabel("Inflation rate(%)", color= 'red')

    plt.axvspan(2022,2023, alpha=0.3)
    plt.axvspan(2024,2026, alpha=0.1)

    for i in range(len(years)):
        plt.text(years[i],inf_rate[i], f"{inf_rate[i]}", ha='center')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

inflation()