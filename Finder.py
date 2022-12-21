import common
from Agent import Agent
from Client import Client

class Finder:
  def __init__(self) -> None:
    self.result = self.gen_result()


  def test(self, n: int, num_counterfeit: int) -> bool:
    agent = Agent(n, num_counterfeit)
    mat = agent.get_mat()
    b = agent.get_b()

    client = Client(mat, b, num_counterfeit)
    cli_counterfeits = client.get_counterfeits()

    isCorrect = agent.check_result(cli_counterfeits)
    return isCorrect


  def test_rep(self, n: int, num_counterfeit: int) -> float:
    print('\t\tn: {:2d}'.format(n), end='\r')
    success_cnt = 0

    for t in range(common.TEST_CNT):
      print('\t\t\t test #{:4d}/{:4d}'.format(t + 1, common.TEST_CNT),
            end='\r')
      if self.test(n, num_counterfeit) == True:
        success_cnt += 1

    success_rate = success_cnt / common.TEST_CNT
    return success_rate


  def test_n_counterfeit(self, num_counterfeit: int) -> dict[int, float]:
    print(f"\tNumber of counterfeits: {num_counterfeit}")

    success_rates = {n: self.test_rep(n, num_counterfeit)
                    for n in common.N_LIST}

    print('\t\tFinished')
    return success_rates


  def gen_result(self) -> dict[int, dict[int, float]]:
    success_rates_all = {num_counterfeit: self.test_n_counterfeit(num_counterfeit)
                        for num_counterfeit in common.NUM_COUNTERFEIT_LIST}
    return success_rates_all


  def get_result(self) -> dict[int, dict[int, float]]:
    return self.result
