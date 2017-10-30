# coding=utf-8

from sklearn.preprocessing import Imputer
import traceback


def fill_strategy(raw_data, strategy):
    try:
        if isinstance(strategy, str):
            impute = Imputer(strategy=strategy)
        else:
            impute = Imputer(missing_values=strategy)
        new_data = impute.fit_transform(raw_data)
    except ValueError:
        traceback.print_exc()
        raise ValueError
    return new_data