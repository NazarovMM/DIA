from abc import ABC, abstractmethod
from contextlib import contextmanager
from datetime import datetime
from time import sleep

allowusers = ['alexeyzer', "andrey-kireev", "valerdon"]


@contextmanager
def workwithfile():
    a = open("../log", 'a')
    yield a
    a.close()


class Subject(ABC):
    @abstractmethod
    def request(self, login) -> None:
        pass


class RealSubject(Subject):
    def request(self, login, request):
        print("RealSubject: Handling request.")
        return ("some data")


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self, login, request) -> None:

        if self.check_access(login):
            self.log_access(f"User {login} Logging successfully request: {request}")
            return(self._real_subject.request(login, request))
        else:
            self.log_access(f"No rights to enter, attempted by {login} with request: {request}")
            print("no permission")
            return None

    def check_access(self, login) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        if (login in allowusers):
            return True
        else:
            return False

    @staticmethod
    def log_access(massage) -> None:
        with workwithfile() as f:
            f.write(f"{datetime.isoformat(datetime.now())}- {massage}\n")


def client_code(subject: Subject) -> None:
    subject.request('user', "select * from passwd")
    sleep(0.2)
    subject.request('alexeyzer', "select * from todo")


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
