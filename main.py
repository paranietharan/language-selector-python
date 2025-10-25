import tkinter as tk
from tkinter import ttk, messagebox
from experta import *

class Answer(Fact):
    """User's answer to a question"""
    question_id = Field(str, mandatory=True)
    value = Field(str, mandatory=True)

class Recommendation(Fact):
    """Language recommendation"""
    language = Field(str, mandatory=True)
    score = Field(int, mandatory=True)
    reason = Field(str, mandatory=True)

class LanguageSelectorExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []
    
    @Rule(Answer(question_id='project-type', value='Web-API'))
    def web_api_python(self):
        self.declare(Recommendation(
            language='Python',
            score=85,
            reason='Python with frameworks like FastAPI or Django is excellent for Web APIs with rich ecosystem and rapid development.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Web-API'))
    def web_api_nodejs(self):
        self.declare(Recommendation(
            language='Node.js',
            score=88,
            reason='Node.js excels at Web APIs with Express or Fastify, offering non-blocking I/O and great performance.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Web-API'),
          Answer(question_id='performance-needs', value='High'))
    def web_api_go(self):
        self.declare(Recommendation(
            language='Go',
            score=92,
            reason='Go delivers exceptional performance for Web APIs with built-in concurrency and efficient memory usage.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Microservices'))
    def microservices_go(self):
        self.declare(Recommendation(
            language='Go',
            score=95,
            reason='Go is purpose-built for microservices with excellent concurrency, small binaries, and fast startup times.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Microservices'))
    def microservices_java(self):
        self.declare(Recommendation(
            language='Java',
            score=90,
            reason='Java with Spring Boot is battle-tested for microservices in enterprise environments with robust tooling.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Real-time'))
    def realtime_nodejs(self):
        self.declare(Recommendation(
            language='Node.js',
            score=93,
            reason='Node.js with WebSockets is perfect for real-time applications like chat, live updates, and collaborative tools.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Real-time'),
          Answer(question_id='performance-needs', value=L('High') | L('Critical')))
    def realtime_rust(self):
        self.declare(Recommendation(
            language='Rust',
            score=96,
            reason='Rust provides blazing-fast real-time performance with memory safety and zero-cost abstractions.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Data-Science'))
    def datascience_python(self):
        self.declare(Recommendation(
            language='Python',
            score=98,
            reason='Python dominates data science with libraries like NumPy, Pandas, scikit-learn, and TensorFlow.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Data-Science'))
    def datascience_r(self):
        self.declare(Recommendation(
            language='R',
            score=85,
            reason='R is specialized for statistical computing and data visualization with extensive academic support.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Desktop'))
    def desktop_python(self):
        self.declare(Recommendation(
            language='Python',
            score=82,
            reason='Python with PyQt or Tkinter enables rapid desktop application development with cross-platform support.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Desktop'))
    def desktop_csharp(self):
        self.declare(Recommendation(
            language='C#',
            score=88,
            reason='C# with .NET offers powerful desktop development with WPF, native Windows integration, and modern tooling.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Mobile-Backend'))
    def mobile_nodejs(self):
        self.declare(Recommendation(
            language='Node.js',
            score=87,
            reason='Node.js is excellent for mobile backends with JSON APIs, real-time features, and JavaScript code sharing.'
        ))
    
    @Rule(Answer(question_id='project-type', value='Mobile-Backend'))
    def mobile_kotlin(self):
        self.declare(Recommendation(
            language='Kotlin',
            score=85,
            reason='Kotlin with Ktor provides modern mobile backend development with coroutines and multiplatform capabilities.'
        ))
    
    # Experience level rules
    @Rule(Answer(question_id='experience-level', value='Beginner'),
          Answer(question_id='project-type', value=L('Web-API') | L('Mobile-Backend')))
    def beginner_python(self):
        self.declare(Recommendation(
            language='Python',
            score=90,
            reason='Python has gentle learning curve, readable syntax, and extensive beginner-friendly documentation.'
        ))
    
    @Rule(Answer(question_id='experience-level', value='Advanced'),
          Answer(question_id='performance-needs', value=L('High') | L('Critical')))
    def advanced_rust(self):
        self.declare(Recommendation(
            language='Rust',
            score=94,
            reason='Rust offers memory safety without garbage collection, perfect for advanced developers needing high performance.'
        ))
    
    @Rule(Answer(question_id='experience-level', value='Advanced'),
          Answer(question_id='performance-needs', value='Critical'))
    def advanced_cpp(self):
        self.declare(Recommendation(
            language='C++',
            score=92,
            reason='C++ provides ultimate control and performance for critical systems with decades of optimization.'
        ))
    
    # Team size rules
    @Rule(Answer(question_id='team-size', value=L('Medium-team') | L('Large-team')),
          Answer(question_id='project-type', value=L('Web-API') | L('Microservices')))
    def large_team_java(self):
        self.declare(Recommendation(
            language='Java',
            score=91,
            reason='Java excels in large teams with strong typing, extensive tooling, and established enterprise patterns.'
        ))
    
    @Rule(Answer(question_id='team-size', value='Solo'),
          Answer(question_id='development-speed', value=L('Very-important') | L('Critical')))
    def solo_rapid_python(self):
        self.declare(Recommendation(
            language='Python',
            score=93,
            reason='Python enables solo developers to build rapidly with batteries-included philosophy and minimal boilerplate.'
        ))
    
    # Development speed rules
    @Rule(Answer(question_id='development-speed', value=L('Very-important') | L('Critical')))
    def rapid_nodejs(self):
        self.declare(Recommendation(
            language='Node.js',
            score=89,
            reason='Node.js enables rapid prototyping with npm ecosystem and JavaScript full-stack development.'
        ))
    
    @Rule(Answer(question_id='development-speed', value=L('Very-important') | L('Critical')))
    def rapid_python(self):
        self.declare(Recommendation(
            language='Python',
            score=91,
            reason='Python maximizes development speed with concise syntax, dynamic typing, and extensive libraries.'
        ))
    
    # Performance-focused rules
    @Rule(Answer(question_id='performance-needs', value='Critical'))
    def critical_rust(self):
        self.declare(Recommendation(
            language='Rust',
            score=97,
            reason='Rust delivers C/C++ level performance with memory safety, ideal for systems requiring critical performance.'
        ))
    
    @Rule(Answer(question_id='performance-needs', value='Critical'))
    def critical_go(self):
        self.declare(Recommendation(
            language='Go',
            score=93,
            reason='Go provides excellent performance with simple concurrency model and fast compilation for critical systems.'
        ))
    
    # Collect recommendations
    @Rule(AS.rec << Recommendation())
    def collect_recommendation(self, rec):
        self.recommendations.append({
            'language': rec['language'],
            'score': rec['score'],
            'reason': rec['reason']
        })


class LanguageSelectorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Backend Language Selector")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f4f8')
        
        self.current_question = 0
        self.answers = {}
        self.expert = None
        
        # Define questions
        self.questions = [
            {
                'id': 'project-type',
                'text': 'What type of project are you building?',
                'options': [
                    ('Web-API', 'Web API'),
                    ('Microservices', 'Microservices'),
                    ('Real-time', 'Real-time'),
                    ('Data-Science', 'Data Science'),
                    ('Desktop', 'Desktop'),
                    ('Mobile-Backend', 'Mobile Backend')
                ]
            },
            {
                'id': 'experience-level',
                'text': 'What is your programming experience level?',
                'options': [
                    ('Beginner', 'Beginner'),
                    ('Intermediate', 'Intermediate'),
                    ('Advanced', 'Advanced')
                ]
            },
            {
                'id': 'performance-needs',
                'text': 'What are your performance requirements?',
                'options': [
                    ('Low', 'Low'),
                    ('Medium', 'Medium'),
                    ('High', 'High'),
                    ('Critical', 'Critical')
                ]
            },
            {
                'id': 'team-size',
                'text': 'What is your team size?',
                'options': [
                    ('Solo', 'Solo'),
                    ('Small-team', 'Small Team (2-5)'),
                    ('Medium-team', 'Medium Team (6-20)'),
                    ('Large-team', 'Large Team (20+)')
                ]
            },
            {
                'id': 'development-speed',
                'text': 'How important is development speed?',
                'options': [
                    ('Not-important', 'Not Important'),
                    ('Somewhat-important', 'Somewhat Important'),
                    ('Very-important', 'Very Important'),
                    ('Critical', 'Critical')
                ]
            }
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#f0f4f8')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        header_frame = tk.Frame(main_frame, bg='#2563eb', relief=tk.RAISED, bd=2)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            header_frame,
            text="Backend Language Selector",
            font=('Arial', 24, 'bold'),
            bg='#2563eb',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="Code by Paranietharan",
            font=('Arial', 10),
            bg='#2563eb',
            fg='#e0e7ff'
        )
        subtitle.pack(pady=(0, 10))
        
        # Progress frame
        self.progress_frame = tk.Frame(main_frame, bg='#f0f4f8')
        self.progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="Question 1 of 5",
            font=('Arial', 12),
            bg='#f0f4f8',
            fg='#4b5563'
        )
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=600,
            mode='determinate',
            maximum=100
        )
        self.progress_bar.pack(pady=10)
        
        # Question frame
        self.question_frame = tk.Frame(main_frame, bg='white', relief=tk.RAISED, bd=2)
        self.question_frame.pack(fill=tk.BOTH, expand=True)
        
        self.question_label = tk.Label(
            self.question_frame,
            text="",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#1f2937',
            wraplength=600,
            pady=20
        )
        self.question_label.pack()
        
        # Options frame
        self.options_frame = tk.Frame(self.question_frame, bg='white')
        self.options_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Navigation frame
        nav_frame = tk.Frame(main_frame, bg='#f0f4f8')
        nav_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.back_button = tk.Button(
            nav_frame,
            text="← Back",
            font=('Arial', 12),
            bg='#6b7280',
            fg='white',
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor='hand2',
            command=self.go_back
        )
        self.back_button.pack(side=tk.LEFT)
        self.back_button.config(state=tk.DISABLED)
        
        # Display first question
        self.display_question()
        
    def display_question(self):
        question = self.questions[self.current_question]
        
        # Update progress
        progress = ((self.current_question + 1) / len(self.questions)) * 100
        self.progress_bar['value'] = progress
        self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
        
        # Update question text
        self.question_label.config(text=question['text'])
        
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Create option buttons
        for value, label in question['options']:
            btn = tk.Button(
                self.options_frame,
                text=label,
                font=('Arial', 12),
                bg='#e0e7ff',
                fg='#1e40af',
                padx=20,
                pady=15,
                relief=tk.FLAT,
                cursor='hand2',
                anchor='w',
                command=lambda v=value: self.handle_answer(v)
            )
            btn.pack(fill=tk.X, pady=5)
            
            # Hover effect
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg='#c7d2fe'))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg='#e0e7ff'))
        
        # Update back button state
        if self.current_question > 0:
            self.back_button.config(state=tk.NORMAL)
        else:
            self.back_button.config(state=tk.DISABLED)
    
    def handle_answer(self, value):
        question_id = self.questions[self.current_question]['id']
        self.answers[question_id] = value
        
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
        else:
            self.run_expert_system()
    
    def go_back(self):
        if self.current_question > 0:
            self.current_question -= 1
            question_id = self.questions[self.current_question]['id']
            if question_id in self.answers:
                del self.answers[question_id]
            self.display_question()
    
    def run_expert_system(self):
        """Run Experta expert system and collect recommendations"""
        try:
            # Create new expert system instance
            self.expert = LanguageSelectorExpert()
            self.expert.reset()
            
            # Declare all answers as facts
            for question_id, value in self.answers.items():
                self.expert.declare(Answer(question_id=question_id, value=value))
            
            # Run the inference engine
            self.expert.run()
            
            # Get recommendations
            recommendations = self.expert.recommendations
            
            # Remove duplicates and keep highest score for each language
            lang_dict = {}
            for rec in recommendations:
                lang = rec['language']
                if lang not in lang_dict or rec['score'] > lang_dict[lang]['score']:
                    lang_dict[lang] = rec
            
            recommendations = list(lang_dict.values())
            
            # Sort by score
            recommendations = sorted(recommendations, key=lambda x: x['score'], reverse=True)
            
            # If no recommendations found, add default
            if not recommendations:
                recommendations.append({
                    'language': 'Python',
                    'score': 70,
                    'reason': 'No specific recommendation matched your criteria. Python is versatile and good for general purpose development.'
                })
            
            self.show_results(recommendations)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run expert system:\n{e}")
    
    def show_results(self, recommendations):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create results frame
        results_frame = tk.Frame(self.root, bg='#f0f4f8')
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header = tk.Label(
            results_frame,
            text="Your Recommendations",
            font=('Arial', 24, 'bold'),
            bg='#f0f4f8',
            fg='#1f2937'
        )
        header.pack(pady=(0, 10))
        
        subtitle = tk.Label(
            results_frame,
            text="Based on your answers, here are the best backend languages for your project",
            font=('Arial', 12),
            bg='#f0f4f8',
            fg='#6b7280'
        )
        subtitle.pack(pady=(0, 20))
        
        # Scrollable frame for recommendations
        canvas = tk.Canvas(results_frame, bg='#f0f4f8', highlightthickness=0)
        scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f4f8')
        
        scrollable_frame.bind(
            '<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display recommendations
        for i, rec in enumerate(recommendations):
            rec_frame = tk.Frame(scrollable_frame, bg='white', relief=tk.RAISED, bd=2)
            rec_frame.pack(fill=tk.X, pady=10, padx=5)
            
            # Language and score header
            header_frame = tk.Frame(rec_frame, bg='white')
            header_frame.pack(fill=tk.X, padx=20, pady=(15, 5))
            
            lang_label = tk.Label(
                header_frame,
                text=rec['language'],
                font=('Arial', 18, 'bold'),
                bg='white',
                fg='#1f2937'
            )
            lang_label.pack(side=tk.LEFT)
            
            score_label = tk.Label(
                header_frame,
                text=str(rec['score']),
                font=('Arial', 24, 'bold'),
                bg='white',
                fg=self.get_score_color(rec['score'])
            )
            score_label.pack(side=tk.RIGHT)
            
            # Reason
            reason_label = tk.Label(
                rec_frame,
                text=rec['reason'],
                font=('Arial', 11),
                bg='white',
                fg='#4b5563',
                wraplength=600,
                justify='left'
            )
            reason_label.pack(padx=20, pady=(0, 15), anchor='w')
            
            # Top recommendation badge
            if i == 0:
                badge = tk.Label(
                    rec_frame,
                    text="⭐ Top Recommendation",
                    font=('Arial', 10, 'bold'),
                    bg='#dbeafe',
                    fg='#1e40af',
                    padx=10,
                    pady=5
                )
                badge.pack(padx=20, pady=(0, 15), anchor='w')
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Restart button
        restart_btn = tk.Button(
            self.root,
            text="Start Over",
            font=('Arial', 14, 'bold'),
            bg='#2563eb',
            fg='white',
            padx=30,
            pady=15,
            relief=tk.FLAT,
            cursor='hand2',
            command=self.restart
        )
        restart_btn.pack(pady=20)
    
    def get_score_color(self, score):
        if score >= 90:
            return '#16a34a'  # Green
        elif score >= 80:
            return '#2563eb'  # Blue
        elif score >= 70:
            return '#ca8a04'  # Yellow
        else:
            return '#6b7280'  # Gray
    
    def restart(self):
        self.current_question = 0
        self.answers = {}
        self.expert = None
        
        # Clear and rebuild UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.setup_ui()


def main():
    root = tk.Tk()
    app = LanguageSelectorUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()