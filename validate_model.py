from predict_images import model
metrics = model.val()  # Evaluate using the validation set
print(metrics)
