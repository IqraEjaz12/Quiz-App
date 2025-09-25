import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
from datetime import datetime


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Quiz App")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        # Initialize variables
        self.current_question = 0
        self.score = 0
        self.selected_subject = ""
        self.selected_difficulty = ""
        self.questions = []
        self.user_answers = []
        self.start_time = None

        # Configure style
        self.setup_styles()

        # Load questions database
        self.load_questions()

        # Start with main menu
        self.show_main_menu()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Configure styles
        style.configure('Title.TLabel',
                        font=('Arial', 24, 'bold'),
                        background='#2c3e50',
                        foreground='#ecf0f1')

        style.configure('Heading.TLabel',
                        font=('Arial', 16, 'bold'),
                        background='#2c3e50',
                        foreground='#ecf0f1')

        style.configure('Custom.TButton',
                        font=('Arial', 12),
                        padding=10)

        style.configure('Question.TLabel',
                        font=('Arial', 14),
                        background='#34495e',
                        foreground='#ecf0f1',
                        wraplength=600)

    def load_questions(self):
        # Expanded questions database with more questions for randomization
        self.questions_db = {
            "Computer Science": {
                "Easy": [
                    {
                        "question": "What does CPU stand for?",
                        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit",
                                    "Computer Processing Unit"],
                        "correct": 0
                    },
                    {
                        "question": "Which programming language is known as the 'mother of all languages'?",
                        "options": ["Python", "C", "Java", "FORTRAN"],
                        "correct": 1
                    },
                    {
                        "question": "What does HTML stand for?",
                        "options": ["Hyper Text Markup Language", "High Tech Modern Language",
                                    "Home Tool Markup Language", "Hyperlink and Text Markup Language"],
                        "correct": 0
                    },
                    {
                        "question": "What does RAM stand for?",
                        "options": ["Random Access Memory", "Read Access Memory", "Rapid Access Memory",
                                    "Real Access Memory"],
                        "correct": 0
                    },
                    {
                        "question": "Which company developed Java programming language?",
                        "options": ["Microsoft", "Sun Microsystems", "Apple", "IBM"],
                        "correct": 1
                    },
                    {
                        "question": "What does WWW stand for?",
                        "options": ["World Wide Web", "World Wild Web", "Wide World Web", "World Web Wide"],
                        "correct": 0
                    },
                    {
                        "question": "Which is not a programming language?",
                        "options": ["Python", "Java", "HTML", "C++"],
                        "correct": 2
                    },
                    {
                        "question": "What does GUI stand for?",
                        "options": ["General User Interface", "Graphical User Interface", "Global User Interface",
                                    "Great User Interface"],
                        "correct": 1
                    }
                ],
                "Medium": [
                    {
                        "question": "Which data structure follows LIFO principle?",
                        "options": ["Queue", "Stack", "Array", "Linked List"],
                        "correct": 1
                    },
                    {
                        "question": "What is the time complexity of binary search?",
                        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                        "correct": 1
                    },
                    {
                        "question": "Which protocol is used for secure web communication?",
                        "options": ["HTTP", "HTTPS", "FTP", "SMTP"],
                        "correct": 1
                    },
                    {
                        "question": "What does SQL stand for?",
                        "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language",
                                    "System Query Language"],
                        "correct": 0
                    },
                    {
                        "question": "Which data structure follows FIFO principle?",
                        "options": ["Stack", "Queue", "Tree", "Graph"],
                        "correct": 1
                    },
                    {
                        "question": "What is the default port number for HTTP?",
                        "options": ["21", "25", "80", "443"],
                        "correct": 2
                    }
                ],
                "Hard": [
                    {
                        "question": "Which sorting algorithm has the best worst-case time complexity?",
                        "options": ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"],
                        "correct": 1
                    },
                    {
                        "question": "What is the space complexity of merge sort?",
                        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                        "correct": 2
                    },
                    {
                        "question": "Which design pattern ensures a class has only one instance?",
                        "options": ["Factory", "Singleton", "Observer", "Strategy"],
                        "correct": 1
                    },
                    {
                        "question": "What is the worst-case time complexity of quick sort?",
                        "options": ["O(n log n)", "O(n²)", "O(log n)", "O(n)"],
                        "correct": 1
                    }
                ]
            },
            "General Knowledge": {
                "Easy": [
                    {
                        "question": "Which planet is known as the Red Planet?",
                        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                        "correct": 1
                    },
                    {
                        "question": "What is the capital of France?",
                        "options": ["London", "Berlin", "Paris", "Madrid"],
                        "correct": 2
                    },
                    {
                        "question": "How many continents are there?",
                        "options": ["5", "6", "7", "8"],
                        "correct": 2
                    },
                    {
                        "question": "Which is the largest ocean on Earth?",
                        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
                        "correct": 2
                    },
                    {
                        "question": "What is the currency of Japan?",
                        "options": ["Yuan", "Yen", "Won", "Rupee"],
                        "correct": 1
                    },
                    {
                        "question": "Which country is known as the Land of the Rising Sun?",
                        "options": ["China", "Japan", "South Korea", "Thailand"],
                        "correct": 1
                    },
                    {
                        "question": "What is the largest mammal in the world?",
                        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                        "correct": 1
                    }
                ],
                "Medium": [
                    {
                        "question": "Who wrote '1984'?",
                        "options": ["Aldous Huxley", "George Orwell", "Ray Bradbury", "H.G. Wells"],
                        "correct": 1
                    },
                    {
                        "question": "Which river is the longest in the world?",
                        "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
                        "correct": 1
                    },
                    {
                        "question": "In which year did World War II end?",
                        "options": ["1944", "1945", "1946", "1947"],
                        "correct": 1
                    },
                    {
                        "question": "What is the smallest country in the world?",
                        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
                        "correct": 1
                    },
                    {
                        "question": "Who painted the Mona Lisa?",
                        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
                        "correct": 2
                    }
                ],
                "Hard": [
                    {
                        "question": "Which element has the atomic number 79?",
                        "options": ["Silver", "Platinum", "Gold", "Mercury"],
                        "correct": 2
                    },
                    {
                        "question": "What is the capital of Bhutan?",
                        "options": ["Thimphu", "Paro", "Punakha", "Wangdue"],
                        "correct": 0
                    },
                    {
                        "question": "Which treaty ended World War I?",
                        "options": ["Treaty of Versailles", "Treaty of Paris", "Treaty of Vienna", "Treaty of Ghent"],
                        "correct": 0
                    },
                    {
                        "question": "What is the rarest blood type?",
                        "options": ["AB-", "O-", "AB+", "Rh-null"],
                        "correct": 3
                    }
                ]
            },
            "Science": {
                "Easy": [
                    {
                        "question": "What is the chemical symbol for water?",
                        "options": ["H2O", "CO2", "NaCl", "CH4"],
                        "correct": 0
                    },
                    {
                        "question": "How many bones are in the adult human body?",
                        "options": ["206", "208", "210", "204"],
                        "correct": 0
                    },
                    {
                        "question": "What gas do plants absorb from the atmosphere?",
                        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
                        "correct": 2
                    },
                    {
                        "question": "What is the hardest natural substance?",
                        "options": ["Gold", "Iron", "Diamond", "Silver"],
                        "correct": 2
                    },
                    {
                        "question": "At what temperature does water boil?",
                        "options": ["90°C", "100°C", "110°C", "120°C"],
                        "correct": 1
                    },
                    {
                        "question": "What is the center of an atom called?",
                        "options": ["Electron", "Proton", "Neutron", "Nucleus"],
                        "correct": 3
                    },
                    {
                        "question": "Which organ produces insulin?",
                        "options": ["Liver", "Kidney", "Pancreas", "Heart"],
                        "correct": 2
                    }
                ],
                "Medium": [
                    {
                        "question": "What is the powerhouse of the cell?",
                        "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
                        "correct": 1
                    },
                    {
                        "question": "What is the pH of pure water?",
                        "options": ["6", "7", "8", "9"],
                        "correct": 1
                    },
                    {
                        "question": "What type of bond holds water molecules together?",
                        "options": ["Ionic", "Covalent", "Hydrogen", "Metallic"],
                        "correct": 2
                    },
                    {
                        "question": "Which blood type is known as the universal donor?",
                        "options": ["A", "B", "AB", "O"],
                        "correct": 3
                    },
                    {
                        "question": "What is the most abundant gas in Earth's atmosphere?",
                        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
                        "correct": 2
                    }
                ],
                "Hard": [
                    {
                        "question": "What is the half-life of Carbon-14?",
                        "options": ["5,730 years", "10,000 years", "1,200 years", "25,000 years"],
                        "correct": 0
                    },
                    {
                        "question": "What is Avogadro's number?",
                        "options": ["6.022 × 10²³", "3.14 × 10⁸", "1.602 × 10⁻¹⁹", "9.81 × 10²"],
                        "correct": 0
                    },
                    {
                        "question": "Which enzyme breaks down starch?",
                        "options": ["Pepsin", "Amylase", "Lipase", "Trypsin"],
                        "correct": 1
                    },
                    {
                        "question": "What is the molecular formula of glucose?",
                        "options": ["C₆H₁₂O₆", "C₂H₆O", "CH₄", "C₁₂H₂₂O₁₁"],
                        "correct": 0
                    }
                ]
            },
            "Space": {
                "Easy": [
                    {
                        "question": "Which planet is closest to the Sun?",
                        "options": ["Venus", "Earth", "Mercury", "Mars"],
                        "correct": 2
                    },
                    {
                        "question": "How many moons does Earth have?",
                        "options": ["0", "1", "2", "3"],
                        "correct": 1
                    },
                    {
                        "question": "What is the largest planet in our solar system?",
                        "options": ["Saturn", "Jupiter", "Neptune", "Uranus"],
                        "correct": 1
                    },
                    {
                        "question": "Which planet is known for its rings?",
                        "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                        "correct": 2
                    },
                    {
                        "question": "What is the name of our galaxy?",
                        "options": ["Andromeda", "Milky Way", "Whirlpool", "Sombrero"],
                        "correct": 1
                    },
                    {
                        "question": "How long does it take for light from the Sun to reach Earth?",
                        "options": ["8 minutes", "1 hour", "1 day", "1 second"],
                        "correct": 0
                    },
                    {
                        "question": "What is the hottest planet in our solar system?",
                        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
                        "correct": 1
                    }
                ],
                "Medium": [
                    {
                        "question": "What is the largest moon of Jupiter?",
                        "options": ["Europa", "Io", "Ganymede", "Callisto"],
                        "correct": 2
                    },
                    {
                        "question": "Which space agency launched the Hubble Space Telescope?",
                        "options": ["ESA", "NASA", "JAXA", "Roscosmos"],
                        "correct": 1
                    },
                    {
                        "question": "What is the boundary around a black hole called?",
                        "options": ["Photon sphere", "Event horizon", "Ergosphere", "Singularity"],
                        "correct": 1
                    },
                    {
                        "question": "Which planet has the most moons?",
                        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                        "correct": 1
                    },
                    {
                        "question": "What is the closest star to our solar system?",
                        "options": ["Sirius", "Proxima Centauri", "Alpha Centauri A", "Vega"],
                        "correct": 1
                    }
                ],
                "Hard": [
                    {
                        "question": "What is the approximate age of the universe?",
                        "options": ["13.8 billion years", "15.2 billion years", "10.5 billion years",
                                    "20.1 billion years"],
                        "correct": 0
                    },
                    {
                        "question": "What is the Chandrasekhar limit?",
                        "options": ["Maximum mass of a white dwarf", "Speed of light limit", "Black hole radius",
                                    "Neutron star limit"],
                        "correct": 0
                    },
                    {
                        "question": "Which mission first landed humans on the Moon?",
                        "options": ["Apollo 10", "Apollo 11", "Apollo 12", "Gemini 7"],
                        "correct": 1
                    },
                    {
                        "question": "What is dark matter estimated to comprise of the universe?",
                        "options": ["27%", "68%", "5%", "15%"],
                        "correct": 0
                    }
                ]
            }
        }

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        # Title
        title_label = ttk.Label(self.root, text="🎓 Ultimate Quiz App", style='Title.TLabel')
        title_label.pack(pady=30)

        # Subject selection frame
        subject_frame = tk.Frame(self.root, bg="#2c3e50")
        subject_frame.pack(pady=20)

        ttk.Label(subject_frame, text="Choose Your Subject:", style='Heading.TLabel').pack(pady=10)

        subjects = ["Computer Science", "General Knowledge", "Science", "Space"]
        for subject in subjects:
            btn = ttk.Button(subject_frame, text=f"📚 {subject}",
                             command=lambda s=subject: self.select_subject(s),
                             style='Custom.TButton')
            btn.pack(pady=5, padx=20, fill='x')

        # Statistics button
        stats_btn = ttk.Button(self.root, text="📊 View Statistics",
                               command=self.show_statistics,
                               style='Custom.TButton')
        stats_btn.pack(pady=20)

    def select_subject(self, subject):
        self.selected_subject = subject
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        self.clear_window()

        # Title
        title_label = ttk.Label(self.root, text=f"Subject: {self.selected_subject}", style='Title.TLabel')
        title_label.pack(pady=30)

        # Difficulty selection frame
        diff_frame = tk.Frame(self.root, bg="#2c3e50")
        diff_frame.pack(pady=20)

        ttk.Label(diff_frame, text="Choose Difficulty Level:", style='Heading.TLabel').pack(pady=10)

        difficulties = [
            ("Easy", "🟢", "Simple questions to get you started"),
            ("Medium", "🟡", "Moderately challenging questions"),
            ("Hard", "🔴", "Difficult questions for experts")
        ]

        for diff, emoji, desc in difficulties:
            frame = tk.Frame(diff_frame, bg="#34495e", relief='raised', bd=2)
            frame.pack(pady=5, padx=20, fill='x')

            btn = ttk.Button(frame, text=f"{emoji} {diff}",
                             command=lambda d=diff: self.select_difficulty(d),
                             style='Custom.TButton')
            btn.pack(side='left', padx=10, pady=10)

            desc_label = tk.Label(frame, text=desc, bg="#34495e", fg="#ecf0f1", font=('Arial', 10))
            desc_label.pack(side='left', padx=10)

        # Back button
        back_btn = ttk.Button(self.root, text="← Back", command=self.show_main_menu)
        back_btn.pack(pady=20)

    def select_difficulty(self, difficulty):
        self.selected_difficulty = difficulty
        self.start_quiz()

    def start_quiz(self):
        # Get all available questions for selected subject and difficulty
        available_questions = self.questions_db[self.selected_subject][self.selected_difficulty].copy()

        # Randomize and select questions (limit to 5 questions max per quiz)
        random.shuffle(available_questions)
        max_questions = min(5, len(available_questions))  # Take up to 5 questions
        self.questions = available_questions[:max_questions]

        # Further randomize the selected questions
        random.shuffle(self.questions)

        # Also randomize the order of options for each question
        for question in self.questions:
            # Store the correct answer text before shuffling
            correct_answer_text = question["options"][question["correct"]]

            # Create a list of (option, is_correct) pairs
            options_with_correctness = [(option, i == question["correct"])
                                        for i, option in enumerate(question["options"])]

            # Shuffle the options
            random.shuffle(options_with_correctness)

            # Update the question with shuffled options and new correct index
            question["options"] = [option for option, _ in options_with_correctness]
            question["correct"] = next(i for i, (_, is_correct) in
                                       enumerate(options_with_correctness) if is_correct)

        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.start_time = datetime.now()

        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.current_question >= len(self.questions):
            self.show_results()
            return

        question_data = self.questions[self.current_question]

        # Progress bar
        progress_frame = tk.Frame(self.root, bg="#2c3e50")
        progress_frame.pack(fill='x', padx=20, pady=10)

        progress_label = tk.Label(progress_frame,
                                  text=f"Question {self.current_question + 1} of {len(self.questions)}",
                                  bg="#2c3e50", fg="#ecf0f1", font=('Arial', 12))
        progress_label.pack(side='left')

        # Score display
        score_label = tk.Label(progress_frame,
                               text=f"Score: {self.score}/{self.current_question}",
                               bg="#2c3e50", fg="#ecf0f1", font=('Arial', 12))
        score_label.pack(side='right')

        # Question frame
        question_frame = tk.Frame(self.root, bg="#34495e", relief='raised', bd=3)
        question_frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Question text
        question_label = ttk.Label(question_frame, text=question_data["question"],
                                   style='Question.TLabel')
        question_label.pack(pady=20, padx=20)

        # Options
        self.selected_answer = tk.IntVar(value=-1)

        options_frame = tk.Frame(question_frame, bg="#34495e")
        options_frame.pack(pady=10)

        for i, option in enumerate(question_data["options"]):
            rb = tk.Radiobutton(options_frame, text=f"{chr(65 + i)}. {option}",
                                variable=self.selected_answer, value=i,
                                bg="#34495e", fg="#ecf0f1", font=('Arial', 12),
                                selectcolor="#3498db", activebackground="#34495e",
                                activeforeground="#ecf0f1")
            rb.pack(anchor='w', pady=5, padx=20)

        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=20)

        if self.current_question > 0:
            prev_btn = ttk.Button(button_frame, text="← Previous",
                                  command=self.previous_question)
            prev_btn.pack(side='left', padx=10)

        next_btn = ttk.Button(button_frame,
                              text="Next →" if self.current_question < len(self.questions) - 1 else "Finish",
                              command=self.next_question)
        next_btn.pack(side='right', padx=10)

        # Quit button
        quit_btn = ttk.Button(self.root, text="Quit Quiz", command=self.confirm_quit)
        quit_btn.pack(pady=10)

    def next_question(self):
        if self.selected_answer.get() == -1:
            messagebox.showwarning("No Answer", "Please select an answer before proceeding.")
            return

        # Store answer
        if len(self.user_answers) <= self.current_question:
            self.user_answers.append(self.selected_answer.get())
        else:
            self.user_answers[self.current_question] = self.selected_answer.get()

        # Check if correct
        if self.selected_answer.get() == self.questions[self.current_question]["correct"]:
            if self.current_question >= len(self.user_answers) - 1:  # Only increment for new answers
                self.score += 1

        self.current_question += 1
        self.show_question()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()
            # Restore previous answer
            if self.current_question < len(self.user_answers):
                self.selected_answer.set(self.user_answers[self.current_question])

    def confirm_quit(self):
        if messagebox.askyesno("Quit Quiz", "Are you sure you want to quit the quiz?"):
            self.show_main_menu()

    def show_results(self):
        self.clear_window()

        # Calculate final score
        final_score = 0
        for i, user_answer in enumerate(self.user_answers):
            if user_answer == self.questions[i]["correct"]:
                final_score += 1

        end_time = datetime.now()
        time_taken = end_time - self.start_time

        # Results frame
        results_frame = tk.Frame(self.root, bg="#34495e", relief='raised', bd=3)
        results_frame.pack(pady=30, padx=30, fill='both', expand=True)

        # Title
        ttk.Label(results_frame, text="🎉 Quiz Results", style='Title.TLabel').pack(pady=20)

        # Score
        percentage = (final_score / len(self.questions)) * 100
        score_text = f"Your Score: {final_score}/{len(self.questions)} ({percentage:.1f}%)"

        score_color = "#e74c3c" if percentage < 50 else "#f39c12" if percentage < 75 else "#27ae60"
        score_label = tk.Label(results_frame, text=score_text,
                               bg="#34495e", fg=score_color, font=('Arial', 18, 'bold'))
        score_label.pack(pady=10)

        # Performance message
        if percentage >= 90:
            message = "🌟 Excellent! Outstanding performance!"
        elif percentage >= 75:
            message = "👍 Great job! Well done!"
        elif percentage >= 50:
            message = "👌 Good effort! Keep practicing!"
        else:
            message = "💪 Don't give up! Practice makes perfect!"

        msg_label = tk.Label(results_frame, text=message,
                             bg="#34495e", fg="#ecf0f1", font=('Arial', 14))
        msg_label.pack(pady=10)

        # Additional stats
        stats_text = f"Subject: {self.selected_subject}\nDifficulty: {self.selected_difficulty}\nTime taken: {str(time_taken).split('.')[0]}"
        stats_label = tk.Label(results_frame, text=stats_text,
                               bg="#34495e", fg="#bdc3c7", font=('Arial', 12))
        stats_label.pack(pady=15)

        # Save result
        self.save_result(final_score, len(self.questions), percentage, time_taken)

        # Buttons
        button_frame = tk.Frame(results_frame, bg="#34495e")
        button_frame.pack(pady=20)

        retry_btn = ttk.Button(button_frame, text="🔄 Retry Same Quiz",
                               command=self.start_quiz)
        retry_btn.pack(side='left', padx=10)

        new_btn = ttk.Button(button_frame, text="🆕 New Quiz",
                             command=self.show_main_menu)
        new_btn.pack(side='right', padx=10)

    def save_result(self, score, total, percentage, time_taken):
        try:
            # Load existing results
            try:
                with open('quiz_results.json', 'r') as f:
                    results = json.load(f)
            except FileNotFoundError:
                results = []

            # Add new result
            result = {
                'date': datetime.now().isoformat(),
                'subject': self.selected_subject,
                'difficulty': self.selected_difficulty,
                'score': score,
                'total': total,
                'percentage': percentage,
                'time_taken': str(time_taken).split('.')[0]
            }
            results.append(result)

            # Save results
            with open('quiz_results.json', 'w') as f:
                json.dump(results, f, indent=2)
        except Exception as e:
            print(f"Error saving results: {e}")

    def show_statistics(self):
        try:
            with open('quiz_results.json', 'r') as f:
                results = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo("No Data", "No quiz results found. Take a quiz first!")
            return

        if not results:
            messagebox.showinfo("No Data", "No quiz results found. Take a quiz first!")
            return

        self.clear_window()

        # Statistics frame
        stats_frame = tk.Frame(self.root, bg="#34495e", relief='raised', bd=3)
        stats_frame.pack(pady=20, padx=20, fill='both', expand=True)

        ttk.Label(stats_frame, text="📊 Your Statistics", style='Title.TLabel').pack(pady=20)

        # Create scrollable text widget for statistics
        text_frame = tk.Frame(stats_frame, bg="#34495e")
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')

        text_widget = tk.Text(text_frame, bg="#2c3e50", fg="#ecf0f1",
                              font=('Arial', 11), yscrollcommand=scrollbar.set)
        text_widget.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=text_widget.yview)

        # Calculate statistics
        total_quizzes = len(results)
        avg_score = sum(r['percentage'] for r in results) / total_quizzes
        best_score = max(results, key=lambda x: x['percentage'])

        stats_text = f"Total Quizzes Taken: {total_quizzes}\n"
        stats_text += f"Average Score: {avg_score:.1f}%\n"
        stats_text += f"Best Score: {best_score['percentage']:.1f}% ({best_score['subject']} - {best_score['difficulty']})\n\n"
        stats_text += "Recent Results:\n" + "=" * 50 + "\n"

        for result in results[-10:]:  # Show last 10 results
            date = datetime.fromisoformat(result['date']).strftime("%Y-%m-%d %H:%M")
            stats_text += f"{date}\n"
            stats_text += f"Subject: {result['subject']} ({result['difficulty']})\n"
            stats_text += f"Score: {result['score']}/{result['total']} ({result['percentage']:.1f}%)\n"
            stats_text += f"Time: {result['time_taken']}\n\n"

        text_widget.insert('1.0', stats_text)
        text_widget.config(state='disabled')

        # Back button
        back_btn = ttk.Button(self.root, text="← Back to Main Menu", command=self.show_main_menu)
        back_btn.pack(pady=20)


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()