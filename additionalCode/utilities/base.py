# -*- coding: UTF-8 -*-
import abc


class BaseConverter(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def convert(f, t):
        raise NotImplementedError


if __name__ == '__main__':
    i = BaseConverter()
