from FederatedXGBoost import FederatedXGBoost

# Instantiate a FederatedXGBoost instance
fxgb = FederatedXGBoost()

# Get number of federating parties
print(fxgb.get_num_parties())

# Load training data
fxgb.load_training_data('/data/dummy_data.csv')

# Train a model
params = {'max_depth': 3, 'min_child_weight': 1.0, 'lambda': 1.0}
num_rounds = 50
fxgb.train(params, num_rounds)

# Save the model
fxgb.save_model("tutorial_model.model")

# Load the test data
fxgb.load_test_data('/data/dummy_data.csv')

# Evaluate the model
print(fxgb.eval())

# Get predictions
ypred = fxgb.predict()

# Shutdown
fxgb.shutdown()
