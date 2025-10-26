from experta import KnowledgeEngine, Rule, AS, L
from models import Answer, Recommendation

class LanguageSelectorExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []
    
    # Project type rules
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
    
    def get_recommendations(self, answers):
        """
        Run the expert system with given answers and return recommendations
        
        Args:
            answers: Dictionary of {question_id: value}
            
        Returns:
            List of recommendation dictionaries sorted by score
        """
        self.reset()
        self.recommendations = []
        
        # Declare all answers as facts
        for question_id, value in answers.items():
            self.declare(Answer(question_id=question_id, value=value))
        
        # Run the inference engine
        self.run()
        
        # Remove duplicates and keep highest score for each language
        lang_dict = {}
        for rec in self.recommendations:
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
        
        return recommendations