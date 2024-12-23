# Typing Speed Test Application

An interactive **Typing Speed Test Application** built with Python and Tkinter to measure users' typing speed and accuracy. This application provides an engaging way to improve typing skills while competing with others via a leaderboard.

---

## Features

### 🎯 **Core Functionalities**
- **Typing Test**: Type a randomly fetched paragraph to evaluate your typing speed and accuracy.
- **Performance Metrics**: Calculates:
  - **Words Per Minute (WPM)**.
  - **Accuracy (%)**.
  - **Time Taken (in seconds)**.
- **Live WPM Preview**: Real-time display of WPM as the user types.

### 📊 **Leaderboard**
- Stores the top performers with:
  - **Name**.
  - **WPM**.
  - **Accuracy**.
- Displays the leaderboard in descending order of WPM.
- Allows viewing all records in a separate window.

### 🎨 **Modern UI/UX**
- Aesthetic **Black and Yellow Theme** for an engaging experience.
- Scrollable main screen for smaller screens to ensure accessibility.

### 📚 **Dynamic Paragraphs**
- Fetches meaningful random paragraphs from an API.
- Fallback to a default paragraph if the API fails.

### ⚙️ **Difficulty Levels**
- Choose from:
  - **Easy**: Shorter paragraphs.
  - **Medium**: Moderate-length paragraphs.
  - **Hard**: Long paragraphs with advanced vocabulary.

---

## How It Works

### Step 1: Start the Test
- Launch the application and enter your **name** in the input field.
- Choose a **difficulty level**:
  - **Easy**: Shorter paragraphs with simple words.
  - **Medium**: Moderately lengthy paragraphs with a mix of simple and complex words.
  - **Hard**: Longer paragraphs with advanced vocabulary and sentence structures.
- A randomly fetched paragraph will be displayed based on the chosen difficulty.

---

### Step 2: Begin Typing
- Focus on the paragraph area and start typing as accurately and quickly as possible.
- The application starts the timer automatically when you begin typing.
- You can see a **live WPM preview** that updates as you type.

---

### Step 3: Submit Your Result
- Once you've finished typing the paragraph, click the **Submit** button.
- The application calculates and displays the following metrics:
  - **Time Taken**: The total time you spent typing the paragraph.
  - **Words Per Minute (WPM)**: Your typing speed in terms of words per minute.
  - **Accuracy**: The percentage of correctly typed words compared to the original paragraph.

---

### Step 4: View Leaderboard
- Click on the **Leaderboard** button to see the top performances.
- The leaderboard displays:
  - **Name**: The name entered by the user.
  - **WPM**: Words per minute achieved.
  - **Accuracy**: Typing accuracy in percentage.
- The leaderboard is sorted by WPM in descending order to highlight the fastest typists.

---

### Step 5: Reset the Test
- Click the **Reset** button to start a new typing session.
- A new random paragraph will be fetched, and you can take the test again.

---

## Project Structure
Enjoy improving your typing skills and competing with others for the top spot on the leaderboard!

typing-speed-test/
├── main.py               # Main application script
├── leaderboard.json      # File storing leaderboard data
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── assets/               # Images and other assets for UI

---

## Technologies Used

- **Python**: Core programming language for building the application.
- **Tkinter**: For creating the graphical user interface (GUI).
- **Requests**: To fetch random meaningful paragraphs via APIs.
- **JSON**: For storing and managing leaderboard data.

---

## Contributing

Contributions are welcome to enhance this project! Follow these steps to contribute:

1. **Fork the Repository**:
   - Click the **Fork** button on the top-right corner of the repository page.

2. **Clone the Repository**:
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/typing-speed-test.git
     ```

3. **Create a New Branch**:
   - Create a branch for your feature or fix:
     ```bash
     git checkout -b feature-branch-name
     ```

4. **Make Your Changes**:
   - Implement your changes or add new features.

5. **Commit Your Changes**:
   - Commit the changes with a descriptive message:
     ```bash
     git commit -m "Add feature: description"
     ```

6. **Push to the Branch**:
   - Push the changes to your forked repository:
     ```bash
     git push origin feature-branch-name
     ```

7. **Open a Pull Request**:
   - Open a pull request to the main repository and describe your changes.

---

## Contact

For any inquiries or suggestions, feel free to reach out:  
- **Email**: vedant.jadhav1928@gmail.com  
- **GitHub**: [VedDevX](https://github.com/VedDevX)  

---

## Acknowledgments

- **API Provider**: Meaningful paragraphs fetched using [Zenquotes.io].
- **Inspiration**: Inspired by the need for a fun and educational typing practice tool.  
- **Contributors**: A special thanks to everyone contributing to this project.

---

Thank you for using the Typing Speed Test Application! 🙌

