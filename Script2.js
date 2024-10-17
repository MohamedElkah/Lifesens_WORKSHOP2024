document.addEventListener('DOMContentLoaded', loadQuestion);

let currentQuestion = {};

async function loadQuestion() {
    const response = await fetch('http://localhost:5000/api/question');  // Remplacez par l'URL de votre backend
    currentQuestion = await response.json();
    displayQuestion();
}

function displayQuestion() {
    document.getElementById('question').textContent = currentQuestion.question;
    const answers = [currentQuestion.right_answer, currentQuestion.wrong_answer1, currentQuestion.wrong_answer2];
    shuffleArray(answers);

    const answerBtns = document.querySelectorAll('.answer-btn');
    answerBtns.forEach((btn, index) => {
        btn.textContent = answers[index];
        btn.onclick = () => {
            if (answers[index] === currentQuestion.right_answer) {
                btn.style.backgroundColor = '#4CAF50'; // Vert si bonne réponse
            } else {
                btn.style.backgroundColor = '#f44336'; // Rouge si mauvaise réponse
            }
        };
    });
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function nextQuestion() {
    document.querySelectorAll('.answer-btn').forEach(btn => btn.style.backgroundColor = '#6237c8');
    loadQuestion();
}