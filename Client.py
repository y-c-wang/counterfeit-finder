import warnings
from sklearn.linear_model import Lasso, LassoCV
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings(action='ignore', category=ConvergenceWarning)


class Client:
  def __init__(self, mat, b, num_counterfeit: int) -> None:
    self.x = self.solve_l1_regularization(mat, b, num_counterfeit)
    self.counterfeits = self.extract_counterfeits(num_counterfeit)


  def gen_alphas(self, mat, b):
    lassocv = LassoCV(cv=5, n_alphas=100, n_jobs=-1)
    lassocv.fit(mat, b)
    return lassocv.alphas_


  def gen_lasso_solution(self, mat, b, alpha_: float):
    lasso = Lasso(alpha=alpha_)
    lasso.fit(mat, b)
    return lasso.coef_


  def solve_l1_regularization(self, mat, b, num_counterfeit):
    threshold = 0.2
    alphas = self.gen_alphas(mat, b)
    for alpha in alphas:
      x = self.gen_lasso_solution(mat, b, alpha)
      if sum(xi >= threshold for xi in x) >= num_counterfeit:
        break
    return x


  def get_x(self):
    return self.x
  

  def extract_counterfeits(self, num_counterfeit: int) -> list[int]:
    x_with_idx = [(val, i) for i, val in enumerate(self.x)]
    counterfeits = [i for val, i in sorted(x_with_idx, reverse=True)[:num_counterfeit]]
    return counterfeits


  def get_counterfeits(self) -> list[int]:
    return self.counterfeits
