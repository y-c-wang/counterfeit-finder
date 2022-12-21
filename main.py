import sys
import json

from Finder import Finder
from Plot import Plot


def usage_hint_and_exit(status = 0) -> None:
  print('usage: python main.py [run | plot]')
  sys.exit(status)


def main():
  if len(sys.argv) != 2:
    usage_hint_and_exit()

  match sys.argv[1]:
    case 'run':
      finder = Finder()
      result = finder.get_result()
      with open('success_rates_all.json', 'w+') as f:
        json.dump(result, f)
    case 'plot':
      with open('success_rates_all.json', 'r') as f:
        result = json.load(f)
      Plot(result)
    case _:
      usage_hint_and_exit()


if __name__ == '__main__':
  main()
