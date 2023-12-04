import json

def calculate_overall_accuracy():
    with open('results/intent_report.json', 'r') as file:
        report_data = json.load(file)

    total_examples = 0
    correctly_classified = 0

    for intent, data in report_data['report'].items():
        true_positives = data['predictions']['true_positives']
        false_positives = data['predictions']['false_positives']
        false_negatives = data['predictions']['false_negatives']

        correctly_classified += true_positives
        total_examples += true_positives + false_positives + false_negatives

    overall_accuracy = (correctly_classified / total_examples) * 100 if total_examples > 0 else 0

    return overall_accuracy

# Calculate overall accuracy
accuracy = calculate_overall_accuracy()
print(f"Overall Intent Classification Accuracy: {accuracy:.2f}%")