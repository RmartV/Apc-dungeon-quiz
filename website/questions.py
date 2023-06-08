import random

basic_math_floor = [
    {
        "question": "What is the value of π (pi)?",
        "choices": ["3.14", "3.141", "3.1415", "3.14159"],
        "correct_choice": 0
    },
    {
        "question": "What is the square root of 16?",
        "choices": ["2", "4", "8", "16"],
        "correct_choice": 1
    },
    {
        "question": "What is the result of 5 + 3 * 2?",
        "choices": ["10", "11", "13", "16"],
        "correct_choice": 1
    },
]

filipino_floor = [
    {
        "question": "Ano ang tawag sa salitang pumapalit sa pangngalan?",
        "choices": ["Panghalip", "Pang-uring Pamilang", "Pandiwa", "Pang-ukol"],
        "correct_choice": 0
    },
    {
        "question": "Ano ang kahulugan ng salitang 'kariktan'?",
        "choices": ["Kagandahan", "Kasayahan", "Kalusugan", "Kabaitan"],
        "correct_choice": 0
    },
    {
        "question": "Alin sa mga sumusunod ang uri ng pang-uri?",
        "choices": ["Pang-uring Pamilang", "Pang-uring Pantangi", "Pang-uring Pambalana", "Pang-uring Panlarawan"],
        "correct_choice": 1
    },
  
]

english_floor = [
    {
        "question": "What is the plural form of 'child'?",
        "choices": ["Childs", "Childrens", "Childes", "Children"],
        "correct_choice": 3
    },
    {
        "question": "What is a synonym for 'happy'?",
        "choices": ["Sad", "Angry", "Joyful", "Tired"],
        "correct_choice": 2
    },
    {
        "question": "What is the past tense of 'eat'?",
        "choices": ["Eaten", "Ate", "Eat", "Eating"],
        "correct_choice": 1
    },
    # Add more questions...
]

algebra_floor = [
    {
        "question": "What is the solution to the equation 2x + 5 = 13?",
        "choices": ["x = 4", "x = 6", "x = 8", "x = 10"],
        "correct_choice": 1
    },
    {
        "question": "What is the quadratic formula?",
        "choices": ["x = (-b ± √(b^2 - 4ac)) / (2a)", "x = -b / a", "x = √a", "x = a^2 + b^2"],
        "correct_choice": 0
    },
    {
        "question": "What is the product of (a + b)(a - b)?",
        "choices": ["a^2 + b^2", "a^2 - b^2", "a^2 - 2ab + b^2", "a^2 + 2ab + b^2"],
        "correct_choice": 1
    },
    # Add more questions...
]

philosophy_floor = [
    {
        "question": "Who is the philosopher known for his theory of forms?",
        "choices": ["Plato", "Aristotle", "Socrates", "Descartes"],
        "correct_choice": 0
    },
    {
        "question": "What is the branch of philosophy that deals with the nature of beauty and art?",
        "choices": ["Aesthetics", "Epistemology", "Ethics", "Metaphysics"],
        "correct_choice": 0
    },
    {
        "question": "What is the philosophical concept of 'cogito ergo sum' commonly translated as?",
        "choices": ["I think, therefore I am", "The end justifies the means", "God is dead", "Life has no meaning"],
        "correct_choice": 0
    },
    # Add more questions...
]

twenty_first_century_floor = [
    {
        "question": "Who is the founder of SpaceX?",
        "choices": ["Elon Musk", "Jeff Bezos", "Richard Branson", "Bill Gates"],
        "correct_choice": 0
    },
    {
        "question": "Which social media platform was launched in 2004?",
        "choices": ["Facebook", "Twitter", "Instagram", "Snapchat"],
        "correct_choice": 0
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "choices": ["Brazil", "China", "United States", "Russia"],
        "correct_choice": 0
    },
    # Add more questions...
]

social_science_floor = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Rome", "Berlin"],
        "correct_choice": 0
    },
    {
        "question": "Who wrote the book '1984'?",
        "choices": ["George Orwell", "William Shakespeare", "Jane Austen", "J.R.R. Tolkien"],
        "correct_choice": 0
    },
    {
        "question": "What is the political ideology that advocates for the abolition of private property?",
        "choices": ["Communism", "Capitalism", "Socialism", "Anarchism"],
        "correct_choice": 0
    },
    # Add more questions...
]

earth_science_floor = [
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
        "correct_choice": 0
    },
    {
        "question": "What is the primary gas that makes up the Earth's atmosphere?",
        "choices": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
        "correct_choice": 2
    },
    {
        "question": "What is the process by which water changes from a liquid to a gas?",
        "choices": ["Evaporation", "Condensation", "Precipitation", "Transpiration"],
        "correct_choice": 0
    },
    # Add more questions...
]

bio_floor = [
    {
        "question": "Which of the following is responsible for carrying oxygen in the blood?",
        "choices": ["Red blood cells", "White blood cells", "Platelets", "Plasma"],
        "correct_choice": 0
    },
    {
        "question": "What is the powerhouse of the cell?",
        "choices": ["Mitochondria", "Nucleus", "Golgi apparatus", "Endoplasmic reticulum"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following is NOT a function of the liver?",
        "choices": ["Regulation of blood sugar levels", "Detoxification of harmful substances", "Production of insulin", "Synthesis of proteins"],
        "correct_choice": 2
    },
    # Add more questions...
]

chem_floor = [
    {
        "question": "What is the atomic number of carbon?",
        "choices": ["6", "12", "14", "16"],
        "correct_choice": 0
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Ag", "Au", "Cu", "Fe"],
        "correct_choice": 1
    },
    {
        "question": "What is the pH value of a neutral solution?",
        "choices": ["0", "7", "14", "1"],
        "correct_choice": 1
    },
    # Add more questions...
]

calculus_floor = [
    {
        "question": "What is the derivative of x^2 with respect to x?",
        "choices": ["2x", "x^2", "x^3", "1"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of 3x^2 with respect to x?",
        "choices": ["3x^3", "3x", "x^2", "x^3"],
        "correct_choice": 0
    },
    {
        "question": "What is the limit of (1/x) as x approaches infinity?",
        "choices": ["0", "1", "Infinity", "Does not exist"],
        "correct_choice": 0
    },
    # Add more questions...
]

physics_floor = [
    {
        "question": "What is the SI unit of force?",
        "choices": ["Newton", "Joule", "Watt", "Pascal"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following is a vector quantity?",
        "choices": ["Speed", "Distance", "Mass", "Velocity"],
        "correct_choice": 3
    },
    {
        "question": "What is the acceleration due to gravity on Earth?",
        "choices": ["9.8 m/s^2", "6.6 m/s^2", "3.2 m/s^2", "5.5 m/s^2"],
        "correct_choice": 0
    },
    # Add more questions...
]
