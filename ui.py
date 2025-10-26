"""
Responsive Tkinter UI for the Backend Language Selector
"""
import tkinter as tk
from tkinter import ttk, messagebox
from expert_system import LanguageSelectorExpert
from config import QUESTIONS, COLORS, FONTS

class LanguageSelectorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Backend Language Selector")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = max(700, min(1200, int(screen_width * 0.8)))
        height = max(600, min(900, int(screen_height * 0.85)))

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.minsize(600, 500)
        self.root.configure(bg=COLORS['bg_primary'])

        self.root.resizable(True, True)
        
        self.current_question = 0
        self.answers = {}
        self.expert = LanguageSelectorExpert()
        self.questions = QUESTIONS

        self.root.bind('<Configure>', self.on_window_resize)
        self.last_width = width
        
        self.setup_ui()
        
    def on_window_resize(self, event):
        """Handle window resize events"""
        if hasattr(self, 'question_label') and abs(self.root.winfo_width() - self.last_width) > 50:
            self.last_width = self.root.winfo_width()
            new_wrap = max(400, self.root.winfo_width() - 150)
            self.question_label.config(wraplength=new_wrap)
    
    def get_responsive_padding(self):
        """Calculate responsive padding based on window size"""
        width = self.root.winfo_width()
        if width < 700:
            return (10, 10)
        elif width < 900:
            return (15, 15)
        else:
            return (20, 20)
    
    def get_responsive_font(self, base_font):
        """Get responsive font size based on window size"""
        width = self.root.winfo_width()
        font_name, base_size, *style = base_font

        if width < 700:
            size_multiplier = 0.85
        elif width < 900:
            size_multiplier = 0.92
        else:
            size_multiplier = 1.0
        
        new_size = int(base_size * size_multiplier)
        return (font_name, new_size, *style)
        
    def setup_ui(self):
        """Set up the main UI components with responsive layout"""
        main_frame = tk.Frame(self.root, bg=COLORS['bg_primary'])
        main_frame.pack(fill=tk.BOTH, expand=True)

        main_frame.grid_rowconfigure(1, weight=0)  # Header
        main_frame.grid_rowconfigure(2, weight=0)  # Progress
        main_frame.grid_rowconfigure(3, weight=1)  # Question
        main_frame.grid_rowconfigure(4, weight=0)  # Navigation
        main_frame.grid_columnconfigure(0, weight=1)
        
        padx, pady = self.get_responsive_padding()

        self._create_header(main_frame)
        
        self._create_progress_bar(main_frame)

        self._create_question_frame(main_frame)

        self._create_navigation(main_frame)

        self.display_question()
    
    def _create_header(self, parent):
        """Create the responsive header section"""
        header_frame = tk.Frame(parent, bg=COLORS['header_bg'], relief=tk.RAISED, bd=2)
        header_frame.grid(row=0, column=0, sticky='ew', padx=0, pady=0)

        title_font = self.get_responsive_font(FONTS['title'])
        subtitle_font = self.get_responsive_font(FONTS['subtitle'])
        
        title_label = tk.Label(
            header_frame,
            text="Backend Language Selector",
            font=title_font,
            bg=COLORS['header_bg'],
            fg=COLORS['header_fg'],
            pady=15
        )
        title_label.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="Code by Paranietharan",
            font=subtitle_font,
            bg=COLORS['header_bg'],
            fg=COLORS['subtitle_fg']
        )
        subtitle.pack(pady=(0, 10))

        self.title_label = title_label
        self.subtitle_label = subtitle
    
    def _create_progress_bar(self, parent):
        """Create the responsive progress bar section"""
        padx, pady = self.get_responsive_padding()
        
        progress_container = tk.Frame(parent, bg=COLORS['bg_primary'])
        progress_container.grid(row=1, column=0, sticky='ew', padx=padx, pady=(pady, 0))
        
        self.progress_label = tk.Label(
            progress_container,
            text="Question 1 of 5",
            font=self.get_responsive_font(FONTS['body']),
            bg=COLORS['bg_primary'],
            fg=COLORS['text_secondary']
        )
        self.progress_label.pack(pady=(10, 5))

        progress_frame = tk.Frame(progress_container, bg=COLORS['bg_primary'])
        progress_frame.pack(fill=tk.X, padx=20)
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            maximum=100
        )
        self.progress_bar.pack(fill=tk.X, pady=10)
    
    def _create_question_frame(self, parent):
        """Create scrollable question frame"""
        padx, pady = self.get_responsive_padding()

        question_container = tk.Frame(parent, bg=COLORS['bg_primary'])
        question_container.grid(row=2, column=0, sticky='nsew', padx=padx, pady=pady)
        question_container.grid_rowconfigure(0, weight=1)
        question_container.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(question_container, bg=COLORS['bg_primary'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(question_container, orient='vertical', 
                                 command=canvas.yview)
        
        self.question_frame = tk.Frame(canvas, bg=COLORS['bg_secondary'], 
                                      relief=tk.RAISED, bd=2)

        canvas_frame = canvas.create_window((0, 0), window=self.question_frame, 
                                           anchor='nw')

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
            canvas_width = event.width
            canvas.itemconfig(canvas_frame, width=canvas_width)
        
        self.question_frame.bind('<Configure>', configure_scroll_region)
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_frame, 
                                                               width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.question_label = tk.Label(
            self.question_frame,
            text="",
            font=self.get_responsive_font(FONTS['subheader']),
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            wraplength=max(400, self.root.winfo_width() - 150),
            pady=20
        )
        self.question_label.pack(fill=tk.X, padx=20)

        self.options_frame = tk.Frame(self.question_frame, bg=COLORS['bg_secondary'])
        self.options_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        self.canvas = canvas
    
    def _create_navigation(self, parent):
        """Create responsive navigation buttons"""
        padx, pady = self.get_responsive_padding()
        
        nav_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        nav_frame.grid(row=3, column=0, sticky='ew', padx=padx, pady=(0, pady))
        
        button_font = self.get_responsive_font(('Arial', 12, 'bold'))
        
        # Back button
        self.back_button = tk.Button(
            nav_frame,
            text="← Back",
            font=button_font,
            bg='#3b82f6',
            fg='white',
            padx=25,
            pady=12,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.go_back
        )
        self.back_button.pack(side=tk.LEFT, padx=5)
        self.back_button.config(state=tk.DISABLED)
        
        # Exit button
        exit_button = tk.Button(
            nav_frame,
            text="✕ Exit",
            font=button_font,
            bg='#dc2626',
            fg='white',
            padx=25,
            pady=12,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.exit_application
        )
        exit_button.pack(side=tk.RIGHT, padx=5)

        self.back_button.bind('<Enter>', lambda e: self.back_button.config(bg='#2563eb') 
                             if self.back_button['state'] == 'normal' else None)
        self.back_button.bind('<Leave>', lambda e: self.back_button.config(bg='#3b82f6') 
                             if self.back_button['state'] == 'normal' else None)
        
        exit_button.bind('<Enter>', lambda e: exit_button.config(bg='#b91c1c'))
        exit_button.bind('<Leave>', lambda e: exit_button.config(bg='#dc2626'))
    
    def display_question(self):
        """Display the current question with responsive layout"""
        question = self.questions[self.current_question]

        progress = ((self.current_question + 1) / len(self.questions)) * 100
        self.progress_bar['value'] = progress
        self.progress_label.config(
            text=f"Question {self.current_question + 1} of {len(self.questions)}"
        )

        self.question_label.config(
            text=question['text'],
            wraplength=max(400, self.root.winfo_width() - 150)
        )

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        button_font = self.get_responsive_font(FONTS['body'])

        for value, label in question['options']:
            btn = tk.Button(
                self.options_frame,
                text=label,
                font=button_font,
                bg=COLORS['button_primary'],
                fg=COLORS['button_primary_fg'],
                padx=20,
                pady=15,
                relief=tk.FLAT,
                cursor='hand2',
                anchor='w',
                command=lambda v=value: self.handle_answer(v)
            )
            btn.pack(fill=tk.X, pady=5)

            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=COLORS['button_hover']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg=COLORS['button_primary']))

        if self.current_question > 0:
            self.back_button.config(state=tk.NORMAL, bg='#3b82f6')
        else:
            self.back_button.config(state=tk.DISABLED, bg='#9ca3af')
        
        self.canvas.yview_moveto(0)
    
    def handle_answer(self, value):
        """Handle user's answer to current question"""
        question_id = self.questions[self.current_question]['id']
        self.answers[question_id] = value
        
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
        else:
            self.run_expert_system()
    
    def go_back(self):
        """Go back to the previous question"""
        if self.current_question > 0:
            self.current_question -= 1
            question_id = self.questions[self.current_question]['id']
            if question_id in self.answers:
                del self.answers[question_id]
            self.display_question()
    
    def run_expert_system(self):
        """Run the expert system and show results"""
        try:
            recommendations = self.expert.get_recommendations(self.answers)
            self.show_results(recommendations)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run expert system:\n{e}")
    
    def show_results(self, recommendations):
        """Display responsive recommendation results"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        padx, pady = self.get_responsive_padding()
        
        main_container = tk.Frame(self.root, bg=COLORS['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True)

        main_container.grid_rowconfigure(2, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        header_frame = tk.Frame(main_container, bg=COLORS['bg_primary'])
        header_frame.grid(row=0, column=0, sticky='ew', padx=padx, pady=(pady, 10))
        
        header = tk.Label(
            header_frame,
            text="Your Recommendations",
            font=self.get_responsive_font(FONTS['title']),
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary']
        )
        header.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="Based on your answers, here are the best backend languages for your project",
            font=self.get_responsive_font(FONTS['body']),
            bg=COLORS['bg_primary'],
            fg=COLORS['text_muted'],
            wraplength=max(400, self.root.winfo_width() - 100)
        )
        subtitle.pack(pady=(5, 0))

        self._create_scrollable_recommendations(main_container, recommendations, 
                                               row=1, padx=padx)

        button_frame = tk.Frame(main_container, bg=COLORS['bg_primary'])
        button_frame.grid(row=2, column=0, sticky='s', pady=pady)
        
        restart_btn = tk.Button(
            button_frame,
            text="Start Over",
            font=self.get_responsive_font(FONTS['button']),
            bg=COLORS['header_bg'],
            fg=COLORS['header_fg'],
            padx=30,
            pady=15,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.restart
        )
        restart_btn.pack()
        
        # Hover effect
        restart_btn.bind('<Enter>', lambda e: restart_btn.config(bg='#1e40af'))
        restart_btn.bind('<Leave>', lambda e: restart_btn.config(bg=COLORS['header_bg']))
    
    def _create_scrollable_recommendations(self, parent, recommendations, row, padx):
        """Create scrollable recommendations with responsive cards"""
        # Container
        scroll_container = tk.Frame(parent, bg=COLORS['bg_primary'])
        scroll_container.grid(row=row, column=0, sticky='nsew', padx=padx, pady=(0, 10))
        scroll_container.grid_rowconfigure(0, weight=1)
        scroll_container.grid_columnconfigure(0, weight=1)
        
        # Canvas and scrollbar
        canvas = tk.Canvas(scroll_container, bg=COLORS['bg_primary'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_container, orient='vertical', 
                                 command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['bg_primary'])
        
        canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, 
                                           anchor='nw')
        
        def configure_scroll(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
            canvas.itemconfig(canvas_frame, width=event.width)
        
        scrollable_frame.bind('<Configure>', configure_scroll)
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_frame, 
                                                               width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display recommendations
        for i, rec in enumerate(recommendations):
            self._create_recommendation_card(scrollable_frame, rec, i == 0)
        
        canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Mouse wheel scrolling
        canvas.bind_all("<MouseWheel>", 
                       lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    
    def _create_recommendation_card(self, parent, rec, is_top):
        """Create responsive recommendation card"""
        rec_frame = tk.Frame(parent, bg=COLORS['bg_secondary'], 
                            relief=tk.RAISED, bd=2)
        rec_frame.pack(fill=tk.X, pady=8, padx=5)
        
        # Responsive padding
        card_padx = max(15, int(self.root.winfo_width() * 0.02))
        
        # Header with language and score
        header_frame = tk.Frame(rec_frame, bg=COLORS['bg_secondary'])
        header_frame.pack(fill=tk.X, padx=card_padx, pady=(15, 5))
        
        lang_label = tk.Label(
            header_frame,
            text=rec['language'],
            font=self.get_responsive_font(FONTS['header']),
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary']
        )
        lang_label.pack(side=tk.LEFT)
        
        score_label = tk.Label(
            header_frame,
            text=str(rec['score']),
            font=self.get_responsive_font(FONTS['title']),
            bg=COLORS['bg_secondary'],
            fg=self._get_score_color(rec['score'])
        )
        score_label.pack(side=tk.RIGHT)
        
        # Reason with responsive wraplength
        reason_label = tk.Label(
            rec_frame,
            text=rec['reason'],
            font=self.get_responsive_font(FONTS['small']),
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_secondary'],
            wraplength=max(350, self.root.winfo_width() - 120),
            justify='left'
        )
        reason_label.pack(padx=card_padx, pady=(0, 15), anchor='w')
        
        # Top recommendation badge
        if is_top:
            badge = tk.Label(
                rec_frame,
                text="Top Recommendation Programming Language",
                font=self.get_responsive_font(('Arial', 10, 'bold')),
                bg=COLORS['badge_bg'],
                fg=COLORS['badge_fg'],
                padx=10,
                pady=5
            )
            badge.pack(padx=card_padx, pady=(0, 15), anchor='w')
    
    def _get_score_color(self, score):
        """Get color based on score value"""
        if score >= 90:
            return COLORS['score_excellent']
        elif score >= 80:
            return COLORS['score_good']
        elif score >= 70:
            return COLORS['score_fair']
        else:
            return COLORS['score_low']
    
    def restart(self):
        """Restart the application"""
        self.current_question = 0
        self.answers = {}
        
        # Clear and rebuild  the UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.setup_ui()
    
    def exit_application(self):
        """Exit the application with confirmation"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()