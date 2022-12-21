import random
import numpy as np

import common


class Agent:
  def __init__(self, n: int, num_counterfeit: int) -> None:
    self.counterfeits, self.coin_data = self.gen_counterfeits_data(num_counterfeit)
    self.mat = self.gen_mat(n)
    self.b = self.gen_b()


  def gen_counterfeits_data(self, num_counterfeit: int):
    counterfeits = random.sample(range(0, common.NUM_COIN),
                                 num_counterfeit)
    coin_data = np.array([1 if idx in counterfeits else 0
                          for idx in range(common.NUM_COIN)])
    return counterfeits, coin_data


  def get_counterfeits(self):
    return self.counterfeits


  def get_coin_data(self):
    return self.coin_data


  def gen_mat(self, n: int):
    return np.random.randint(low=0, high=2, size=(n, common.NUM_COIN))


  def get_mat(self):
    return self.mat


  def gen_b(self):
    b = self.mat @ self.coin_data
    return b


  def get_b(self):
    return self.b


  def check_result(self, cli_counterfeits: list[int]) -> bool:
    return sorted(cli_counterfeits) == sorted(self.counterfeits)
