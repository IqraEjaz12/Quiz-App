# 📄 Product Requirements Document (PRD)

**Project Name:** Ultimate Quiz App  
**Author:** Iqra Ejaz  
**Date:** 2025-09-24  
**Version:** 1.0  

---

## 1. Overview
The **Ultimate Quiz App** is a desktop application built using **Python (Tkinter)**.  
The goal is to provide users with an interactive and fun way to test their knowledge across different subjects and difficulty levels.  

The app supports multiple-choice questions, tracks user performance, and provides detailed results and statistics.  

---

## 2. Objectives
- Provide an engaging quiz experience with subject & difficulty selection.  
- Offer randomized questions & answer order for fairness.  
- Track and display quiz statistics (scores, accuracy, time taken).  
- Store past results for performance tracking.  
- Allow users to retry or attempt new quizzes.  

---

## 3. Key Features
### 3.1 Quiz Management
- Subjects: Computer Science, General Knowledge, Science, Space.  
- Difficulty Levels: Easy 🟢, Medium 🟡, Hard 🔴.  
- Randomized selection of up to 5 questions per quiz.  
- Multiple-choice questions with shuffled options.  

### 3.2 User Interaction
- Main menu with subject selection.  
- Difficulty selection screen with descriptions.  
- Interactive quiz with **previous/next navigation**.  
- Warnings when trying to proceed without selecting an answer.  
- Quit confirmation dialog.  

### 3.3 Scoring & Results
- Automatic scoring based on correct answers.  
- Final results page with:  
  - Score & percentage.  
  - Performance message.  
  - Subject, difficulty, and time taken.  
- Retry option for the same quiz.  
- Start a new quiz option.  

### 3.4 Statistics & Storage
- Persistent storage of quiz history in `quiz_results.json`.  
- Displays:  
  - Total quizzes taken.  
  - Average score.  
  - Best score (with subject & difficulty).  
  - Last 10 results with date, score, and time.  

---

## 4. Functional Requirements
1. **Question Randomization:** Ensure no quiz follows the same sequence of questions.  
2. **Answer Persistence:** User-selected answers should be restored when navigating back.  
3. **Scoring Accuracy:** Results must reflect correct/incorrect answers precisely.  
4. **Time Tracking:** Track quiz duration using start & end timestamps.  
5. **Statistics Storage:** Store results in JSON with fields: `date, subject, difficulty, score, total, percentage, time_taken`.  
6. **UI Design:**  
   - Dark theme (background `#2c3e50`, question frame `#34495e`).  
   - Consistent styling with custom fonts and colors.  
   - Responsive widget layout.  

---

## 5. Non-Functional Requirements
- **Usability:** Simple navigation with minimal clicks.  
- **Performance:** Should load quizzes and results instantly (<1s).  
- **Portability:** Runs on Windows, Mac, Linux with Python & Tkinter.  
- **Reliability:** JSON file must not get corrupted; handle missing files gracefully.  
- **Scalability:** Easy to add more subjects/questions later.  

---

## 6. Success Metrics
- Users can complete quizzes without crashes or UI issues.  
- Correct results are displayed consistently.  
- Statistics accurately reflect past performance.  
- At least **90% of users** should rate the app as easy to use.  

---

## 7. Future Enhancements
- Add more subjects & question sets.  
- User authentication (profiles & leaderboards).  
- Export results as PDF/Excel.  
- Timed quizzes with countdowns.  
- Mobile-friendly (Kivy/Flutter) version.
