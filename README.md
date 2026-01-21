# Sentiment Analysis Web App 💬

A simple and interactive **Sentiment Analysis Web Application** built using **Machine Learning (TF‑IDF + Logistic Regression)** and **Streamlit**.
The app predicts whether a given sentence expresses **Positive** or **Negative** sentiment in real time.

This project is suitable for:

* College mini‑projects
* Machine Learning practice
* Resume / internship portfolio

---

## 🚀 Features

* Clean text preprocessing using NLTK stopwords
* TF‑IDF vectorization for feature extraction
* Logistic Regression classifier for sentiment prediction
* Streamlit web interface for real‑time predictions
* Cached model loading for faster performance

---

## 🧠 Model & Dataset

* **Algorithm:** Logistic Regression
* **Vectorizer:** TF‑IDF (TfidfVectorizer)
* **Dataset:** Kaggle – Sentiment Analysis Dataset (used for training)

The trained model and vectorizer are saved as:

* `model.pkl`
* `vectorizer.pkl`

---

## 📁 Project Structure

```
sa/
│── app.py            # Streamlit application
│── model.pkl         # Trained ML model
│── vectorizer.pkl    # TF‑IDF vectorizer
│── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Project

```bash
git clone <your-repo-link>
cd sa
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Required Libraries

```bash
pip install streamlit scikit-learn nltk pandas numpy
```

---

### 4️⃣ Download NLTK Stopwords (One Time Only)

```bash
python -c "import nltk; nltk.download('stopwords')"
```

---

## ▶️ Run the Application

Use this command (recommended on Linux/Nobara):

```bash
python -m streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🧪 Example

Input:

```
I love this movie
```

Output:

```
😊 Positive Sentiment
```

---

## 🛠️ Training the Model (Optional)

If you want to retrain the model:

1. Load the Kaggle sentiment dataset
2. Clean and preprocess text
3. Train using `TfidfVectorizer` + `LogisticRegression`
4. Save files:

```python
import pickle
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
```

---

## 🔮 Future Improvements

* Add confidence/probability score
* Support neutral sentiment
* Upload CSV file and predict multiple sentences
* Deploy online using Streamlit Cloud / Render
* Add charts and sentiment distribution

---

## ⚠️ Notes

* Twitter scraping was removed due to API restrictions and instability.
* This version uses offline trained data for stable predictions.
* Recommended Python version: **3.10 or 3.11** for best compatibility.

---

## 👨‍💻 Author

Developed by **Aniesh**
B.Tech – Artificial Intelligence & Data Science

---

## 📜 License

This project is open‑source and free to use for educational purposes.
