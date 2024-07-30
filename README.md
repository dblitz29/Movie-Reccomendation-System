
# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System** repository! This project leverages the power of Python, Node.js, XGBoost, and Express.js to provide personalized movie recommendations based on user input. It uses a rich dataset from Kaggle containing Wikipedia movie plots for training.

## 📝 Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 📖 About the Project
This system allows users to receive movie recommendations by entering a movie title, genre, and origin. The recommendation engine is powered by XGBoost, and the frontend is built with Node.js and Express.js.

![Movie Recommendation System](https://raw.githubusercontent.com/your-repository/image.png)

## 🚀 Getting Started
Follow these instructions to set up the project locally.

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js 14+
- npm 6+
- XGBoost

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system
   ```
3. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## 🎮 Usage
1. Train the model:
   ```bash
   python processing.py
   ```
2. Activate the backend server:
   ```bash
   node app.js
   ```
3. Start the frontend server:
   ```bash
   python -m http.server 8000
   ```
4. Open your browser and navigate to `http://localhost:8000`.

## 📊 Dataset
We use the [Wikipedia Movie Plots dataset](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots) from Kaggle. This dataset contains information about movie plots, which is utilized to train the recommendation model.

## 🧠 Model Training
The model is trained using XGBoost. The training script can be found in the `model_training` directory. To train the model:
1. Ensure the dataset is downloaded and placed in the `data` directory.
2. Run the training script:
   ```bash
   python reccomendation.py
   ```

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
