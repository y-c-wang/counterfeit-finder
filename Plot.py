import matplotlib.pyplot as plt

COLOR_DICT = {
  '1': 'darkred', 
  '2': 'darkorange', 
  '3': 'darkgoldenrod', 
  '4': 'darkgreen', 
  '5': 'darkblue'
}

class Plot:
  def __init__(self, success_rates_all: dict[int, dict[int, float]]) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlabel("Number of weighings", fontsize=18)
    ax.set_ylabel("Probability of success", fontsize=18)
    ax.set_xlim([4, 41])
    ax.set_ylim([-0.1, 1.1])

    for num_counterfeit, success_rates in success_rates_all.items():
      xs = [int(x) for x, y in success_rates.items()]
      ys = [y for x, y in success_rates.items()]
      ax.plot(xs, ys, marker='o', color=COLOR_DICT[num_counterfeit], 
              label=f'{num_counterfeit} counterfeit(s)')
    
    ax.legend()
    plt.savefig('success_rate_all.png')
