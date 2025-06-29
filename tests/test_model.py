from src import train

def test_train_model_runs():
    model, acc = train.train_model()
    # Simple check: accuracy should be above 0 (meaning model predicts something)
    assert acc > 0
