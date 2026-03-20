import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("Loading Dataset...")
    # 1. Load the built-in Breast Cancer dataset
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    print("Splitting Data into Training and Testing sets...")
    # 2. Split the data (80% for training, 20% for testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training the Random Forest AI Model...")
    # 3. Initialize and Train the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Making Predictions...\n")
    # 4. Make predictions on the test set
    y_pred = model.predict(X_test)

    # 5. Evaluate the Model
    accuracy = accuracy_score(y_test, y_pred)
    print("=" * 40)
    print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")
    print("=" * 40)

    print("\n📊 Detailed Classification Report:\n")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    # 6. Visualize the Confusion Matrix
    print("\nGenerating Confusion Matrix Plot...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=data.target_names,
                yticklabels=data.target_names)

    plt.xlabel('Predicted Label (AI Decision)')
    plt.ylabel('True Label (Actual Diagnosis)')
    plt.title('Confusion Matrix - Breast Cancer Detection')
    plt.tight_layout()
    plt.show()  # This will open a window with the graph


if __name__ == "__main__":
    main()