from __future__ import annotations
from abc import ABC, abstractmethod

trace1 = ['A', 'B', 'C', 'D', 'E', 'F']
trace2 = ['L', 'E12', 'D16', 'C', 'D', 'E', 'F']
placebyindex = {'A': 0, 'B': 1, 'C' :2, 'D': 3, 'E': 4, 'F': 5}
Busess = {"busA": trace1, "busB": trace2}
class Navigator():
    def __init__(self, strategy: Strategy) -> None:
        """
        Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self, start, end):
        result = self._strategy.do_algorithm(start, end)
        return result


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, startpoint, pointend):
        pass

class Strategypublictransport(Strategy):
    def do_algorithm(self, pointstart, pointend):
        a = [i for i in Busess if pointstart in Busess[i] and pointend in Busess[i]]
        if len(a) > 0:
            print(f"trace from {pointstart} to {pointend} could be completed by public transport with such buses:{a}")
            return a
        else:
            print("no trace by public transport")
            return None


class StrategybyFoot(Strategy):
    def __init__(self):
        self._matrix = [0] * 6
        self._matrix[0] = 1
        self._matrix[1] = 2
        self._matrix[2] = 3

    def do_algorithm(self, startpoint, endpoint):
        if startpoint in placebyindex.keys() and endpoint in placebyindex.keys():
            index1 = placebyindex[startpoint]
            index2 = placebyindex[endpoint]
            if self._matrix[index1] == index2:
                print(f"you can go by foot from place {startpoint } to {endpoint} by foot")
                return f"you can go by foot from place {startpoint } to {endpoint} by foot"
            else:
                print("no way by Foot")
                return "no way by Foot"

        else:
            print("Sorry no place in map")
            return None


if __name__ == "__main__":
    # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы сделать
    # правильный выбор.

    context = Navigator(Strategypublictransport())
    print("Client: Strategy is set to public transport.")
    context.do_some_business_logic('A', 'B')
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = StrategybyFoot()
    context.do_some_business_logic('A', 'R')