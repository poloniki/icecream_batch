from icecream.model.prediction import regression_model


def test_positive_values():
    assert regression_model(20, 10) > 0, "Values should be positives"
