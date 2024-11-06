from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# Mock data for modules with detailed content
modules = [
    {
        "id": 1, 
        "title": "Corporate Security Policies", 
        "content": (
            "In this module, you will learn about the essential security policies in place to protect our organization’s assets. "
            "Understanding these policies is crucial to maintaining the security and integrity of our data and systems. "
            "Topics include:<br><br>"
            "<ul>"
            "<li><strong>Data Handling Protocols:</strong> This section outlines the guidelines for storing, transmitting, and disposing of sensitive data. "
            "This includes encryption techniques, secure file storage, and ensuring that data is properly erased when no longer needed.</li>"
            "<li><strong>Password Policies:</strong> This section emphasizes the importance of strong, unique passwords for each account. "
            "It also covers the guidelines for periodic password updates and the use of multi-factor authentication (MFA) to enhance account security.</li>"
            "<li><strong>Remote Access Guidelines:</strong> Remote access to company systems should be done securely. "
            "This includes the use of Virtual Private Networks (VPNs) and ensuring secure Wi-Fi connections when accessing corporate data remotely.</li>"
            "</ul><br>"
            "By the end of this module, you will understand how following these protocols helps to minimize security risks, ensures compliance with regulations, "
            "and safeguards our company’s digital resources."
        ),
        "completed": False,
       "quiz": {
            "questions": [
                {"question": "What is the purpose of corporate security policies?", 
                 "options": ["To protect company data", "To improve marketing", "To enhance public relations"], 
                 "answer": "To protect company data"},
                {"question": "What should you do with sensitive information on paper?", 
                 "options": ["Leave it on your desk", "Dispose of it securely", "Share it with colleagues"], 
                 "answer": "Dispose of it securely"},
                {"question": "Why are strong passwords important?", 
                 "options": ["To make login easy", "To keep data secure", "To avoid forgetting them"], 
                 "answer": "To keep data secure"}
            ],
            "completed": False
        }
    },
    {
        "id": 2, 
        "title": "Ethical Standards", 
        "content": (
            "In this module, we focus on the ethical standards that guide our behavior within the organization. Upholding ethical behavior ensures a respectful, "
            "safe, and professional environment for everyone. Topics include:<br><br>"
            "<ul>"
            "<li><strong>Code of Conduct:</strong> This document establishes a set of principles for responsible decision-making, transparency, and accountability. "
            "It covers areas such as conflict of interest, workplace integrity, and maintaining confidentiality.</li>"
            "<li><strong>Respectful Workplace Behavior:</strong> This section promotes a harassment-free environment, emphasizing the importance of respect, inclusivity, "
            "and diversity in the workplace. It encourages open communication and addresses how to report inappropriate behavior.</li>"
            "<li><strong>Professional Responsibilities:</strong> Ethical work behavior includes fulfilling professional duties, meeting deadlines, being honest in communication, "
            "and maintaining the highest standards of service and customer care. This section also covers reporting unethical behavior and following organizational policies.</li>"
            "</ul><br>"
            "Understanding and following these standards helps create a positive and productive work culture, which is essential for both individual and organizational success."
        ),
        
        "completed": False,
        "quiz": {
            "questions": [
                {"question": "What is the purpose of a code of conduct?", 
                 "options": ["To set expectations for ethical behavior", "To manage project deadlines", "To set sales goals"], 
                 "answer": "To set expectations for ethical behavior"},
                {"question": "Why is integrity important in the workplace?", 
                 "options": ["It promotes trust and accountability", "It’s only for managers", "It’s optional"], 
                 "answer": "It promotes trust and accountability"},
                {"question": "What should you do if you witness unethical behavior?", 
                 "options": ["Ignore it", "Report it", "Encourage it"], 
                 "answer": "Report it"}
            ],
            "completed": False
        }
    },
    {
        "id": 3, 
        "title": "Phishing Awareness", 
        "content": (
            "Phishing attacks are one of the most common cybersecurity threats. This module teaches you how to identify and avoid phishing attempts. "
            "Phishing can come in various forms, but recognizing it early can prevent serious security breaches. Topics covered include:<br><br>"
            "<ul>"
            "<li><strong>Recognizing Phishing Tactics:</strong> Phishing emails often appear to be from trusted sources and contain urgent requests to click on links or download attachments. "
            "Learn how to recognize fake emails, common red flags like spelling mistakes, unfamiliar email addresses, and suspicious-looking links.</li>"
            "<li><strong>Avoiding Malicious Links:</strong> Phishing emails often trick users into clicking malicious links that lead to fake websites or download malware. "
            "Best practices include hovering over links to inspect URLs and using browser extensions to verify the legitimacy of websites.</li>"
            "<li><strong>Reporting Suspicious Emails:</strong> If you receive a suspicious email, it's crucial to report it to your IT department immediately. "
            "Learn how to report phishing attempts and take the necessary steps if you've clicked on a malicious link or provided personal information.</li>"
            "</ul><br>"
            "By the end of this module, you will have the knowledge to recognize phishing attempts and act swiftly to protect yourself and the organization from harm."
        ),
       "completed": False,
        "quiz": {
            "questions": [
                {"question": "What is phishing?", 
                 "options": ["A type of email scam", "A secure email protocol", "A harmless email"], 
                 "answer": "A type of email scam"},
                {"question": "What is one sign of a phishing attempt?", 
                 "options": ["Grammatical errors", "Official company email", "Clear language"], 
                 "answer": "Grammatical errors"},
                {"question": "What should you do if you receive a suspicious email?", 
                 "options": ["Click all links", "Report it to IT", "Reply immediately"], 
                 "answer": "Report it to IT"}
            ],
            "completed": False
        }
    },
    {
        "id": 4, 
        "title": "Data Protection Basics", 
        "content": (
            "Data protection is a vital aspect of maintaining trust, confidentiality, and compliance with legal and regulatory frameworks. "
            "In this module, you will learn the basics of data protection, covering the best practices for handling sensitive information. Topics include:<br><br>"
            "<ul>"
            "<li><strong>Data Privacy Laws:</strong> This section provides an overview of major data protection laws such as GDPR (General Data Protection Regulation) and CCPA (California Consumer Privacy Act). "
            "Key principles include ensuring transparency in data collection, respecting user consent, and providing individuals with the right to access, rectify, or delete their personal data.</li>"
            "<li><strong>Secure Data Storage:</strong> Data must be securely stored to prevent unauthorized access. This includes encryption techniques, securing physical storage devices, "
            "and implementing access controls to ensure that only authorized personnel can access sensitive information.</li>"
            "<li><strong>Access Control Measures:</strong> Limiting access to sensitive data is crucial for data protection. Learn about role-based access control (RBAC), strong password policies, and "
            "multi-factor authentication (MFA) to secure access to company systems and data.</li>"
            "</ul><br>"
            "By completing this module, you will understand the importance of data protection and how to comply with relevant data privacy laws to avoid legal consequences and protect personal data."
        ),
        "completed": False,
        "quiz": {
            "questions": [
                {"question": "What is the purpose of data protection?", 
                 "options": ["To secure personal and sensitive data", "To increase data access", "To encourage data sharing"], 
                 "answer": "To secure personal and sensitive data"},
                {"question": "Which of these is a principle of data protection?", 
                 "options": ["Data minimization", "Unlimited data sharing", "Data selling"], 
                 "answer": "Data minimization"},
                {"question": "What should you do before sharing sensitive information?", 
                 "options": ["Check permissions and encryption", "Share with everyone", "Post it online"], 
                 "answer": "Check permissions and encryption"}
            ],
            "completed": False
        }
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', modules=modules)

@app.route('/module/<int:module_id>', methods=['GET', 'POST'])
def module(module_id):
    # Find the module by ID
    module = next((m for m in modules if m['id'] == module_id), None)
    
    if module:
        if request.method == 'POST':
            # If the user submits the module completion form
            module['completed'] = True  # Mark the module as completed after the user interaction (quiz submission)
        
        return render_template('module.html', module=module)
    else:
        return redirect(url_for('dashboard'))

# Route to mark a module as completed and unlock the quiz
@app.route('/complete/<int:module_id>', methods=['POST'])
def complete_module(module_id):
    for module in modules:
        if module['id'] == module_id:
            module['completed'] = True
            return redirect(url_for('module', module_id=module_id))
    return redirect(url_for('dashboard'))

@app.route('/module/<int:module_id>/quiz', methods=['GET', 'POST'])
def module_quiz(module_id):
    module = next((m for m in modules if m['id'] == module_id), None)
    if module and module['completed'] and 'quiz' in module:
        if request.method == 'POST':
            # Evaluate the quiz answers
            user_answers = request.form
            correct_answers = 0
            for idx, question in enumerate(module['quiz']['questions']):
                user_answer = user_answers.get(f"answer_{idx}", "").strip().lower()
                correct_answer = question['answer'].strip().lower()
                if user_answer == correct_answer:
                    correct_answers += 1
            
            # Set a passing score threshold, e.g., 70%
            passing_score = 0.7 * len(module['quiz']['questions'])
            passed = correct_answers >= passing_score
            
            # Only mark module as completed if passing score is achieved
            if passed:
                module['quiz']['completed'] = True
                module['completed'] = True  # Only mark the module as completed if they pass the quiz
                score = f"Congratulations! You passed with a score of {correct_answers} / {len(module['quiz']['questions'])} correct."
            else:
                score = f"You scored {correct_answers} / {len(module['quiz']['questions'])} correct. Please try again to pass."

            return render_template('quiz_result.html', module=module, score=score, passed=passed)

        return render_template('quiz.html', module=module, enumerate=enumerate)
    return redirect(url_for('dashboard'))








    
# @app.route('/module/<int:module_id>')
# def module(module_id):
#     module = next((m for m in modules if m['id'] == module_id), None)
#     if module:
#         return render_template('module.html', module=module)
#     return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)