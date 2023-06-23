import random

basic_math_floor = [ #1st floor basic math

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
    {
        "question": "Simplify: 4 × 5 - 3 × 2",
        "choices": ["12", "14", "16", "18"],
        "correct_choice": 1
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["4", "6", "8", "10"],
        "correct_choice": 2
    },
    {
        "question": "What is 3 times 5?",
        "choices": ["10", "12", "15", "18"],
        "correct_choice": 2
    },
    {
        "question": "Simplify: 12 ÷ 3 + 5",
        "choices": ["1", "5", "9", "11"],
        "correct_choice": 2
    },
    {
        "question": "What is the value of 3 squared?",
        "choices": ["3", "6", "9", "12"],
        "correct_choice": 2
    },
    {
        "question": "Simplify: 2 × (4 + 3)",
        "choices": ["8", "10", "14", "16"],
        "correct_choice": 2
    },
    {
        "question": "What is 20% of 80?",
        "choices": ["4", "16", "20", "64"],
        "correct_choice": 1
    },
    {
        "question": "What is the value of 7 × 9 - 2 × 4?",
        "choices": ["49", "51", "57", "63"],
        "correct_choice": 2
    },
    {
        "question": "Simplify: 6 ÷ 2 + 3 × 4",
        "choices": ["9", "12", "15", "18"],
        "correct_choice": 2
    },
    {
        "question": "What is 8 divided by 2?",
        "choices": ["2", "4", "6", "8"],
        "correct_choice": 1
    },
    {
        "question": "Simplify: 2 + 3 × 4 - 2",
        "choices": ["5", "9", "11", "14"],
        "correct_choice": 2
    },
    {
        "question": "What is the value of 9 squared?",
        "choices": ["18", "27", "81", "90"],
        "correct_choice": 2
    },
    {
        "question": "Simplify: 5 × (2 + 3) - 4",
        "choices": ["15", "20", "21", "25"],
        "correct_choice": 2
    },
    {
        "question": "What is the product of 7 and 6?",
        "choices": ["12", "36", "42", "49"],
        "correct_choice": 2
    },
    {
        "question": "Simplify: 15 ÷ 3 × 2",
        "choices": ["6", "8", "10", "12"],
        "correct_choice": 2
    },
    {
        "question": "What is 25% of 200?",
        "choices": ["40", "50", "75", "100"],
        "correct_choice": 1
    },
    {
        "question": "What is the value of 5 × (3 + 2) - 4 × 2?",
        "choices": ["5", "9", "13", "17"],
        "correct_choice": 3
    },
    {
        "question": "Simplify: 12 - 3 × 2 + 4",
        "choices": ["8", "10", "12", "14"],
        "correct_choice": 1
    },
    {
        "question": "What is the value of 6 cubed?",
        "choices": ["72", "216", "324", "648"],
        "correct_choice": 1
    }
]

filipino_floor = [ #2nd floor Filipino
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

    {
        "question":"Ito ay tumutukoy sa tiyak na pagkakaiba-iba ng mga wika sa lipunan?",
        "choices":["Barayti ng Wika", "Dayalek", "Sosyolek", "Etnolek"],
        "correct_choice":0
    },
    {
        'question': 'Ano ang pambansang wika natin?',
        'choices': ['Pilipino', 'Tagalog', 'Filipino', 'Ingles'],
        'correct_choice': 2
    },

    {
        'question': 'Ano ang pinakamababang antas ng wika?',
        'choices': ['lalawiganin', 'balbal', 'k0olokyal', 'pampanitikan'],
        'correct_choice': 1
    },
    {
        'question': 'Ano ang pinakamataas at pinakamayamang antas ng wika?',
        'choices': ['lalawiganin', 'balbal', 'kolokyal', 'pampanitikan'],
        'correct_choice': 3
    },
    {
        'question': 'Kadalasan itong ginagamit sa mga akdang naratibo tulad ng mga kuwento, salaysay, nobela, dula at iba pa, maging sa pelikula.',
        'choices': ['Abstrak', 'Buod', 'Bionote', 'Paglalagom'],
        'correct_choice': 1
    },
    {
        'question': 'Ito ay ginagamit sa paggawa ng bio-data, resume o anumang kagaya ng mga ito upang ipakilala ang sarili para sa isang propesyonal na layunin.',
        'choices': ['Buod', 'Abstrak', 'Paglalagom', 'Bionote'],
        'correct_choice': 3
    },
    {
        'question': 'Ito ang wikang natatanging magiging kinatawan ng pambansang pagkakakilanlan ng isang lahi at/o ng bansa.',
        'choices': ['Wikang Opisyal', 'Wikang Pambansa', 'Wikang Panturo', 'Wala sa nabanggit'],
        'correct_choice': 1
    },
    {
        'question': 'Ito ang wikang kadalasang ginagamit sa lehislatibong mga sangay ng bansa, bagama’t hinihiling din ng batas sa maraming bansa na isalin din sa ibang wika ang mga dokumento ng gobyerno.',
        'choices': ['Wikang Pambansa', 'Wikang Panturo', 'Wikang Opisyal', 'Wala sa nabanggit'],
        'correct_choice': 2
    },
    {
        'question': 'Mga natatanging punto sa pagsasalita at ekpresyong ikinaiba ng isa sa iba pang mananalita ng kaparehong wika.',
        'choices': ['Idyolek', 'Dayalek', 'Sosyolek', 'Etnolek'],
        'correct_choice': 0
    },
    {
        'question': 'Ito ang barayti ng wikang nakabatay sa katayuan o antas panlipunan o dimesiyong sosyal ng mga taong gumagamit ng wika.',
        'choices': ['Etnolek', 'Sosyolek', 'Idyolek', 'Dayalek'],
        'correct_choice': 1
    },
    {
        'question': 'Nilalaman nito ang iyong pangkalahatang balak tungkol sa isang materyal na siyang gagawing gabay upang makabuo nang maayos na sulatin o talumpati, sa tulong ng baha-bahaging pagtalakay ng mga kaisipan.',
        'choices': ['Balangkas', 'Pampanitikan', 'Wika', 'Walang tamang sagot'],
        'correct_choice': 0
    },
    {
        'question': 'Ito ay mula sa mga tunog, simbolo at tuntunin na binuo upang makalikha ng salitang nakapagpapahayag ng kahulugan o kaisipan.',
        'choices': ['Balangkas', 'Wika', 'Dila', 'Walang tamang sagot'],
        'correct_choice': 1
    },
    {
        'question': 'Ginagamit ang wika upang ipahayag ang sariling saloobin.',
        'choices': ['Interaksyonal', 'Personal', 'Regulatori', 'Impormatibo'],
        'correct_choice': 1
    },
    {
        'question': 'Ginagamit ang wika upang lumikha ng mga likhang sining tulad ng tula, bugtong, kwento, at iba pang malikhaing akda.',
        'choices': ['Interaksyonal', 'Personal', 'Impomatibo', 'Imahinatibo'],
        'correct_choice' :3
    },
    {
        'question': 'Ginagamit ang wika upang magbahagi ng kaalaman.',
        'choices': ['Impormatibo', 'Interaksyonal', 'Heuristiko', 'Regulatori'],
        'correct_choice': 0
    },
    {
        'question': 'May taglay itong 20 letra.',
        'choices': ['Katinig', 'Abakada', 'Alpabeto', 'Patinig'],
        'correct_choice': 1
    },
    {
        'question': 'Alin sa mga pagpipilian ang malapatinig?',
        'choices': ['o, u', 'k, l', 'w, y', 'f, g'],
        'correct_choice': 2
    },
    {
        'question': 'Ikinakabit sa isang salitang-ugat upang makabuo ng isang salita.',
        'choices': ['Panlapi', 'Pandiwa', 'Pang-abay', 'Pang-uri'],
        'correct_choice': 0
    },
    {
        'question': 'Ito ay isang salita na nagsasaad ng kilos o galaw.',
        'choices': ['Panlapi', 'Pandiwa', 'Pang-abay', 'Pang-uri'],
        'correct_choice': 1
    },
    {
        'question': 'Salitang naglalarawan o nagbibigay turing sa mga pangngalan o panghalip.',
        'choices': ['Panlapi', 'Pandiwa', 'Pang-abay', 'Pang-uri'],
        'correct_choice': 3
    }
]

english_floor = [ #3rd floor English
{
        'question': 'Marry ______ a castle if she ____ 10 million dollar.',
        'choices': ['Was, would go', 'Was, would goes', 'Were, would go', 'Were, would goes'],
        "correct_choice": 2
    },
    {
        'question': 'If the snow ______ down in Thailand, I ______ a snow man.',
        'choices': ['Fall, would built', 'Fell, would build', 'Fall, would build', 'Fell, would built'],
        "correct_choice": 1
    },
    {
        'question': 'Which one is correct?',
        'choices': ['If I were a famous star, I would be very rich', 'If I was a famous star, I would be very rich.', 'If I was a famous star, I would very rich.', 'If I were a famous star, I would very rich'],
        "correct_choice": 1
    },
    {
        'question': 'There was no _____ in waiting until ten o’clock so we left.',
        'choices': ['A. point', 'B. time', 'C. use', 'D. worth'],
        "correct_choice": 0
    },
    {
        'question': 'You ____ better return the books to the library today, to avoid paying a fine.',
        'choices': ['A. could', 'B. should', 'C. had', 'D. would'],
        "correct_choice": 2
    },
    {
        'question': 'He __ on the course because he was off sick for five days.',
        'choices': ['A. got over', 'B. got through', 'C. fell behind', 'D. left behind'],
        "correct_choice": 2
    },
    {
        'question': 'I will not stand __ any more of his rudeness.',
        'choices': ['A. for', 'B. up to', 'C. out', 'D. by'],
        "correct_choice": 0
    },
    {
        'question': 'Mr. Bamboo speaks Spanish very_____.',
        'choices': ['good', 'fluently', 'Good', 'Fluently'],
        "correct_choice": 1
    },
    {
        'question': "The manager didn't take part_____the discussion.",
        'choices': ['at', 'for', 'in', 'None of the above'],
        "correct_choice": 2
    },
    {
        'question': "I always go to school by bus. However, this week_____ by car with my mom.",
        'choices': ['I go', "I'm going", "I've going", "I'll go"],
        "correct_choice": 1
    },
    {
        'question': "Tony: We got here at 6:00 o'clock this morning. More than forty people__ ____________here waiting for tickets when we arrived.",
        'choices': ['had already been standing', 'already standed', 'had already standed', 'were already standing'],
        "correct_choice": 3
    },
    {
        'question': 'He _____ in this company since 2000',
        'choices': ['has worked', 'works', 'is working', 'has been working'],
        "correct_choice": 0
    },
    {
        'question': 'This was the first time I________to Mexico!',
        'choices': ['have been', 'had been', 'was', 'am'],
        "correct_choice": 1
    },
    {
        'question': 'Look out! The floor is slippery. You ________________ down.',
        'choices': ['will fallen', 'will have fallen', "'re going to fall", "'re falling"],
        "correct_choice": 2
    },
    {
        'question': 'This hotel is big, but Grand Hotel is __________ and the airport hotel is the biggest.',
        'choices': ['Bigger', 'Most big', 'Biger', 'More big'],
        "correct_choice": 0
    },
    {
        'question': 'The shopkeeper wrapped the China vases ________.',
        'choices': ['softly', 'carefully', 'gracefully', 'roughly'],
        "correct_choice": 1
    },
    {
        'question': 'There was a tough fight _______the two men.',
        'choices': ['among', 'beside', 'opposite', 'between'],
        "correct_choice": 3
    },
    {
        'question': 'I bought this dress ____ four hundred pesos.',
        'choices': ['A. for', 'B. by', 'C. with', 'D. at'],
        "correct_choice": 0
    },
    {
        'question': 'I had _____ money, so I couldn’t buy lunch.',
        'choices': ['A. little', 'B. a little', 'C. few', 'D. a few'],
        "correct_choice": 0
    },
    {
        'question': 'I didn’t see ____ of those movies.',
        'choices': ['A. none', 'B. any', 'C. much', 'D. many'],
        "correct_choice": 1
    }
]

algebra_floor = [ #4th floor Algebra
    {
        "question": "Solve the equation: 3x + 5 = 17",
        "choices": ["x = 4", "x = 6", "x = 7", "x = 9"],
        "correct_choice": 0
    },
    {
        "question": "Simplify the expression: 4x + 2y - 3x + 5y",
        "choices": ["x + 7y", "x + 3y", "x - 7y", "x - 3y"],
        "correct_choice": 0
    },
    {
        "question": "Factorize the expression: x^2 - 9",
        "choices": ["(x - 3)(x + 3)", "(x - 2)(x + 2)", "(x - 4)(x + 4)", "(x - 5)(x + 5)"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 2(x + 3) = 10",
        "choices": ["x = 1", "x = 2", "x = 3", "x = 4"],
        "correct_choice": 1
    },
    {
        "question": "Solve the equation: 2x^2 - 9 = 0",
        "choices": ["x = 3/2", "x = 3", "x = 4", "x = 9/2"],
        "correct_choice": 0
    },
    {
        "question": "Simplify the expression: (4x^2 - 9) / (2x + 3)",
        "choices": ["2x - 3", "2x + 3", "2x - 4", "2x + 4"],
        "correct_choice": 0
    },
    {
        "question": "Expand the expression: (x + 2)(x - 3)",
        "choices": ["x^2 - x - 6", "x^2 + x - 6", "x^2 - x + 6", "x^2 + x + 6"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 3(2x - 1) = 4(x + 3)",
        "choices": ["x = 7/5", "x = 5/7", "x = 7/3", "x = 3/7"],
        "correct_choice": 0
    },
    {
        "question": "Simplify the expression: 2(x^2 + 3x) - 3(x^2 - 2x)",
        "choices": ["-x^2 + 8x", "-x^2 - 8x", "x^2 - 8x", "x^2 + 8x"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 5 - 2x = 3x + 7",
        "choices": ["x = -2", "x = -1", "x = 1", "x = 2"],
        "correct_choice": 0
    },
    {
        "question": "Simplify the expression: (2x + 3)(x - 4)",
        "choices": ["2x^2 - 5x - 12", "2x^2 - 5x + 12", "2x^2 + 5x - 12", "2x^2 + 5x + 12"],
        "correct_choice": 0
    },
    {
        "question": "Factorize the expression: 4x^2 - 25",
        "choices": ["(2x - 5)(2x + 5)", "(2x - 4)(2x + 4)", "(2x - 3)(2x + 3)", "(2x - 6)(2x + 6)"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 3(2x - 4) = 2(3x + 1)",
        "choices": ["x = -6/7", "x = -7/6", "x = 7/6", "x = 6/7"],
        "correct_choice": 3
    },
    {
        "question": "Simplify the expression: 2x^2 + 5x - 3 - (3x^2 - 2x + 1)",
        "choices": ["-x^2 + 7x - 4", "-x^2 + 7x + 4", "x^2 - 7x - 4", "x^2 - 7x + 4"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 2(3x + 4) - 3(2x - 1) = 4x - 5",
        "choices": ["x = -11/3", "x = -3/11", "x = 3/11", "x = 11/3"],
        "correct_choice": 3
    },
    {
        "question": "Simplify the expression: (x - 2)(x + 3) - (2x - 1)(x + 2)",
        "choices": ["-x^2 + 3x - 7", "-x^2 + 3x + 7", "x^2 - 3x - 7", "x^2 - 3x + 7"],
        "correct_choice": 0
    },
    {
        "question": "Factorize the expression: x^2 + 8x + 15",
        "choices": ["(x + 3)(x + 5)", "(x + 2)(x + 7)", "(x + 4)(x + 4)", "(x + 5)(x + 5)"],
        "correct_choice": 0
    },
    {
        "question": "Solve the equation: 5x + 2(3x - 1) = 3(x + 4) - 2x",
        "choices": ["x = -2/3", "x = -3/2", "x = 2/3", "x = 3/2"],
        "correct_choice": 0
    },
    {
        "question": "Simplify the expression: 2(2x^2 - 3) - (3x^2 + 4)",
        "choices": ["x^2 - 10", "-x^2 - 10", "x^2 + 10", "-x^2 + 10"],
        "correct_choice": 1
    },
    {
        "question": "Solve the equation: 4(x + 3) = 2(2x - 1) + 3(x - 4)",
        "choices": ["x = -11/5", "x = -5/11", "x = 5/11", "x = 11/5"],
        "correct_choice": 2
    },
    {
        "question": "Simplify the expression: (x - 1)^2",
        "choices": ["x^2 - 1", "x^2 - 2x + 1", "x^2 + 2x + 1", "x^2 + 1"],
        "correct_choice": 1
    }
]

philosophy_floor = [ #5th floor Philosophy
    {
        'question': 'Student of Plato, and equally proficient in the field of metaphysics and ethics as Plato.',
        'choices': ['Socrates', 'Descartes', 'Aristotle', 'Pythagoras'],
        "correct_choice": 2
    },
    {
        'question': 'He was an ancient Greek philosopher and a student of Socrates. He is regarded as one of the, if not the greatest Western philosophers of all time.',
        'choices': ['Plato', 'Descartes', 'Aristotle', 'Socrates'],
        "correct_choice": 0
    },
    {
        'question': '______ is understanding using scientific, mathematical, or abstract thinking.',
        'choices': ['Knowledge', 'Belief', 'Opinion', 'Dianoia'],
        "correct_choice": 3
    },
    {
        'question': '______ is the study of arguments and how to determine whether an argument is successful or not.',
        'choices': ['Statement', 'Logic', 'Schema', 'Belief'],
        "correct_choice": 1
    },
    {
        'question': '______ is the study of arguments and how to determine whether an argument is successful or not.',
        'choices': ['Reason', 'Appetite', 'Spirit', 'Wisdom'],
        "correct_choice": 0
    },
    {
        'question': 'Plato uses the ______ to illustrate the Tripartite Soul.',
        'choices': ['Chariot Allegory', 'Metaphysics', 'Socratic Methods', 'Aesthetics'],
        "correct_choice": 0
    },
    {
        'question': 'A metaphysical theory, developed by Plato, that says that reality consists of ideal forms, or ideas, that are timeless, unchanging, immaterial, and more perfect than things in the material world of sense perception.',
        'choices': ['Dualism', 'Idealism', 'Realism', 'Theism'],
        "correct_choice": 2
    },
    {
        'question': 'A metaphysical theory that says that reality consists of ideas and minds that house them.',
        'choices': ['Theism', 'Realism', 'Deism', 'Idealism'],
        "correct_choice": 3
    },
    {
        'question': 'Harmony in society, collective theory. Working together to create a harmonious society. "Do not do onto anyone else that you would not have done onto you." Attributed to Kongfuzi. 5 Virtues',
        'choices': ['Gold Mean', 'Confucianism', 'Egoism', 'Buddhism'],
        "correct_choice": 1
    },
    {
        'question': 'Focuses on the individual and their harmony with nature. An individual reaching Nirvana. School of ethical, metaphysical, and epistemological thought. Developed by Siddhartha Gautama, the Buddha. 8 Virtues',
        'choices': ['Gold Mean', 'Confucianism', 'Egoism', 'Buddhism'],
        "correct_choice": 3
    },
    {
        'question': 'Developed the idea of the golden mean. He said that virtue-or moral excellence- is the mean, which is the middle path between two extremes of behavior. Him and Plato came up with a list of what makes someone a good person. Included justice, courage, generosity, and modesty.',
        'choices': ['Aristotle', 'Socrates', 'Guatama-Buddha', 'Kongfuzi'],
        "correct_choice": 0
    },
    {
        'question': 'In logic, a group of statements consisting of a premise or premises designed to justify a conclusion.',
        'choices': ['Conclusion', 'Premise', 'Argument', 'Validity'],
        "correct_choice": 2
    },
    {
        'question': 'He believed that works of art should mimic reality and that nature sets the standard of truth and beauty. "The artist can do no better than to try to accurately portray the universe in its infinite variety".',
        'choices': ['Aristotle', 'Plato', 'Guatama-Buddha', 'Descartes'],
        "correct_choice": 1
    },
    {
        'question': 'The four main divisions of philosophy are metaphysics, epistemology, axiology, and ________',
        'choices': ['categorical logic', 'bioethics', 'aesthetics', 'logic'],
        "correct_choice": 3
    },
    {
        'question': 'For Socrates, an unexamined life is a tragedy because it results in grievous harm to _____.',
        'choices': ['the soul', 'the body', 'the justice system', 'the state'],
        "correct_choice": 0
    },
    {
        'question': 'If you assume that a set of statements is true, and yet you can deduce a false or absurd statement from it, then the original set of statements as a whole must be false. This kind of argument is known as _____.',
        'choices': ['hypothetical syllogism', 'modus ponens', 'reductio ad absurdum', 'modus tollens'],
        "correct_choice": 2
    },
    {
        'question': 'A question-and-answer dialogue in which propositions are methodically scrutinized to uncover the truth is known as _____.',
        'choices': ['The Socratic method', 'A debate', 'An argument', 'The Socratic jest'],
        "correct_choice": 0
    },
    {
        'question': 'The famous statement "An unexamined life is not worth living" is attributed to _____.',
        'choices': ['Plato', 'Socrates', 'Aristotle', 'John Locke'],
        "correct_choice": 1
    },
    {
        'question': 'According to Socrates, a clear sign that a person has _____ is her exclusive pursuit of social status, wealth, power, and pleasure.',
        'choices': ['Exceptional desires', 'An unhealthy soul', 'Worldly wisdom', 'Philosophical ambition'],
        "correct_choice": 1
    },
    {
        'question': 'For Socrates, the soul is harmed by lack of _____.',
        'choices': ['Knowledge', 'Wealth', 'Community', 'Courage'],
        "correct_choice": 0
    }
]

twenty_first_century_floor = [ #6th floor 21st Century
    {
        'question': 'What is the definition of literature?',
        'choices': ['Non-fiction written works', 'Imaginative or creative writing', 'Scientific research papers', 'Historical documents'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following is NOT a major division of literature?',
        'choices': ['Poetry', 'Fiction', 'Drama', 'Biography'],
        "correct_choice": 3
    },
    {
        'question': 'Which of the following is a characteristic of 21st-century literature?',
        'choices': ['Heavy use of archaic language', 'Traditional plot structures', 'Exploration of digital and technological themes', 'Strict adherence to classic literary forms'],
        "correct_choice": 2
    },
    {
        'question': 'What is literary criticism?',
        'choices': ['The process of editing and proofreading literary works', 'The study and evaluation of literary works', 'The marketing and promotion of literary works', 'The process of translating literary works into different languages'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following literary movements focuses on the natural world and environmental themes?',
        'choices': ['Romanticism', 'Realism', 'Modernism', 'Ecocriticism'],
        "correct_choice": 3
    },
    {
        'question': 'Which of the following is NOT an example of environmental literature?',
        'choices': ['"Walden" by Henry David Thoreau', '"Silent Spring" by Rachel Carson', '"Pride and Prejudice" by Jane Austen', '"The Lorax" by Dr. Seuss'],
        "correct_choice": 2
    },
    {
        'question': 'What is the purpose of literary analysis?',
        'choices': ['To summarize the plot of a literary work', 'To interpret and evaluate the meaning and significance of a literary work', 'To create new works of literature inspired by existing ones', 'To identify the author\'s intended audience for a literary work'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following is NOT a literary device?',
        'choices': ['Simile', 'Foreshadowing', 'Bibliography', 'Metaphor'],
        "correct_choice": 2
    },
    {
        'question': 'Which literary period is known for its focus on individualism, imagination, and emotion?',
        'choices': ['Romanticism', 'Realism', 'Renaissance', 'Modernism'],
        "correct_choice": 0
    },
    {
        'question': 'What is the purpose of a literary theme?',
        'choices': ['To provide a chronological account of events in a story', 'To convey a moral or message to the reader', 'To create a realistic and detailed setting', 'To establish the tone or mood of a literary work'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following is an example of a classic tragedy?',
        'choices': ['"Romeo and Juliet" by William Shakespeare', '"The Great Gatsby" by F. Scott Fitzgerald', '"Pride and Prejudice" by Jane Austen', '"To Kill a Mockingbird" by Harper Lee'],
        "correct_choice": 0
    },
    {
        'question': 'What is the significance of the point of view in literature?',
        'choices': ['It determines the physical location of the story', 'It shapes the perspective from which the story is narrated', 'It determines the time period in which the story is set', 'It establishes the overall theme of the story'],
        "correct_choice": 1
    },
    {
        'question': 'Which literary movement emphasized the portrayal of everyday life and ordinary people?',
        'choices': ['Realism', 'Romanticism', 'Modernism', 'Surrealism'],
        "correct_choice": 0
    },
    {
        'question': 'Which literary device involves the use of words that imitate the sounds they describe?',
        'choices': ['Onomatopoeia', 'Personification', 'Metonymy', 'Synecdoche'],
        "correct_choice": 0
    },
    {
        'question': 'In literature, what does the term "foil" refer to?',
        'choices': ['A type of poetic form', 'A character who contrasts with the main character', 'A technique used to build suspense in a story', 'A narrative technique that reveals the thoughts of multiple characters'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following is NOT a form of literary criticism?',
        'choices': ['Feminist criticism', 'Historical criticism', 'Psychological criticism', 'Philosophical criticism'],
        "correct_choice": 3
    },
    {
        'question': 'What is the purpose of a thesis statement in a literary analysis essay?',
        'choices': ['To provide a brief summary of the plot', 'To present the main argument or interpretation of the essay', 'To introduce the main characters and their motivations', 'To list the supporting evidence for the analysis'],
        "correct_choice": 1
    },
    {
        'question': 'What is the purpose of an epilogue in a literary work?',
        'choices': ['To introduce the main characters and setting', 'To build suspense and tension', 'To provide a resolution or final commentary on the story', 'To establish the central conflict of the narrative'],
        "correct_choice": 2
    },
    {
        'question': 'What is the purpose of a protagonist in a literary work?',
        'choices': ['To provide comic relief', 'To serve as the primary antagonist', 'To undergo a significant transformation or journey', 'To provide historical context'],
        "correct_choice": 2
    },
    {
        'question': 'What is the role of conflict in literature?',
        'choices': ['To provide a resolution to the story', 'To establish the setting and atmosphere', 'To create tension and propel the plot forward', 'To provide historical context for the narrative'],
        "correct_choice": 2
    }
]

social_science_floor = [ #7th floor Social Science
    {
        'question': 'Culture refers to:',
        'choices': ['Biological traits and genetic makeup', 'Shared beliefs, values, and practices of a group', 'Social interactions and relationships', 'Economic activities and production processes'],
        "correct_choice": 1
    },
    {
        'question': 'Cultural relativism is important in attaining cultural understanding because it:',
        'choices': ['Promotes the dominance of one culture over others', 'Allows for objective judgments and comparisons across cultures', 'Recognizes and respects the diversity of cultural practices and beliefs', 'Advocates for cultural assimilation and homogenization'],
        "correct_choice": 2
    },
    {
        'question': 'A norm is:',
        'choices': ['A statistical measure used in social research', 'A set of cultural practices and beliefs', 'A legal principle governing social behavior', 'A social rule or expectation that guides behavior in a group'],
        "correct_choice": 3
    },
    {
        'question': 'Society refers to:',
        'choices': ['Individual thoughts and feelings', 'Cultural norms and traditions', 'Political ideologies and systems', 'Economic transactions and market dynamics'],
        "correct_choice": 1
    },
    {
        'question': 'Sociology emerged as a distinct discipline in the:',
        'choices': ['17th century', '18th century', '19th century', '20th century'],
        "correct_choice": 2
    },
    {
        'question': 'In social groups, a role is:',
        'choices': ['The position one occupies in a social hierarchy', 'The behavior expected of an individual in a particular position', 'The network of social relationships an individual has', 'The set of norms and values guiding group behavior'],
        "correct_choice": 1
    },
    {
        'question': 'Differentiate between primary and secondary groups:',
        'choices': ['Primary groups are larger and more impersonal than secondary groups', 'Primary groups are characterized by limited personal relationships, while secondary groups involve strong emotional bonds', 'Primary groups are formed based on shared interests and goals, while secondary groups are formed based on family ties', 'Primary groups involve face-to-face interactions and strong personal relationships, while secondary groups are more formal and task-oriented'],
        "correct_choice": 3
    },
    {
        'question': 'Which theory suggests that social networks and social connections influence individuals\' behavior, attitudes, and opportunities?',
        'choices': ['Functionalism', 'Conflict theory', 'Symbolic interactionism', 'Social network theory'],
        "correct_choice": 3
    },
    {
        'question': 'Analyze the forms and functions of social organizations. Which of the following is an example of a bureaucratic organization?',
        'choices': ['A family unit', 'A religious congregation', 'A political party', 'A friendship circle'],
        "correct_choice": 2
    },
    {
        'question': 'Which anthropological perspective focuses on the study of the ways in which power and social inequality intersect with gender, race, and class?',
        'choices': ['Functionalism', 'Structuralism', 'Feminist anthropology', 'Evolutionary anthropology'],
        "correct_choice": 2
    },
    {
        'question': 'Who is considered the founder of sociology?',
        'choices': ['Karl Marx', 'Émile Durkheim', 'Max Weber', 'Auguste Comte'],
        "correct_choice": 3
    },
    {
        'question': 'The process of learning and internalizing the beliefs, values, and norms of a culture is known as:',
        'choices': ['Enculturation', 'Acculturation', 'Socialization', 'Assimilation'],
        "correct_choice": 0
    },
    {
        'question': 'A normative cultural practice that prohibits incestuous relationships is an example of a:',
        'choices': ['Folkway', 'More', 'Taboo', 'Ritual'],
        "correct_choice": 2
    },
    {
        'question': 'What is the term for the system in which social status is determined by birth and is relatively fixed?',
        'choices': ['Hierarchy', 'Prestige', 'Caste system', 'Class system'],
        "correct_choice": 2
    },
    {
        'question': 'Which sociological perspective focuses on how individuals actively construct their social reality through symbolic interactions?',
        'choices': ['Functionalism', 'Conflict theory', 'Symbolic interactionism', 'Feminist theory'],
        "correct_choice": 2
    },
    {
        'question': 'In the context of social stratification, what does "social mobility" refer to?',
        'choices': ['The movement of individuals across different social classes', 'The cultural exchange between different societies', 'The process of enculturation and assimilation', 'The establishment of social norms and values'],
        "correct_choice": 0
    },
    {
        'question': 'Analyze social and political structures. Which sociological theory argues that social stratification is necessary for maintaining social order and stability?',
        'choices': ['Conflict theory', 'Structural functionalism', 'Symbolic interactionism', 'Feminist theory'],
        "correct_choice": 1
    },
    {
        'question': 'According to the concept of cultural capital developed by Pierre Bourdieu, which of the following best represents an example of cultural capital?',
        'choices': ['Physical assets and possessions', 'Educational qualifications and degrees', 'Social connections and networks', 'Financial resources and wealth'],
        "correct_choice": 1
    },
    {
        'question': 'Analyze social and political structures. Which sociological theory focuses on how power and social inequality are reproduced and maintained through social institutions?',
        'choices': ['Conflict theory', 'Symbolic interactionism', 'Structural functionalism', 'Feminist theory'],
        "correct_choice": 0
    },
    {
        'question': 'What term refers to a set of cultural beliefs and practices that are considered superior or more desirable than others within a society?',
        'choices': ['Cultural relativism', 'Cultural hegemony', 'Cultural pluralism', 'Cultural appropriation'],
        "correct_choice": 1
    }
]

earth_science_floor = [ #8th floor Earth Science
    {
        'question': 'breaking rock into smaller pieces',
        'choices': ['Weathering', 'Erosion', 'Fault', 'Fossil'],
        "correct_choice": 0
    },
    {
        'question': 'Both energy and matter flow through ecosystems but, at times, they are also stored within the system.',
        'choices': ['Isolated System', 'Open System', 'Closed System', 'Semi-Closed System'],
        "correct_choice": 1
    },
    {
        'question': 'it exchanges energy but not matter with its environment.',
        'choices': ['Isolated System', 'Open System', 'Closed System', 'Semi-Closed System'],
        "correct_choice": 2
    },
    {
        'question': 'it exchanges neither matter nor energy with its environment.',
        'choices': ['Isolated System', 'Open System', 'Closed System', 'Semi-Closed System'],
        "correct_choice": 0
    },
    {
        'question': 'a complex ecosystem. It is made up of minerals, organic material, gases, and liquids which forms the habitat for many animals and plants.',
        'choices': ['Fertilizer', 'Soil', 'Sand', 'Cement'],
        "correct_choice": 1
    },
    {
        'question': 'it feels slippery like wet talcum powder and holds together better than sandy soils.',
        'choices': ['Silty soils', 'Clay soils', 'Sandy soils', 'Soil texture'],
        "correct_choice": 0
    },
    {
        'question': 'feel sticky and can be rolled up into a ball easily.',
        'choices': ['Silty soils', 'Clay soils', 'Sandy soils', 'Loam soils'],
        "correct_choice": 1
    },
    {
        'question': 'is the tendency of the system to return to an original state following disturbance.',
        'choices': ['Steady-state equilibrium', 'Unstable Equilibrium', 'Equilibrium', 'New Equilibrium'],
        "correct_choice": 2
    },
    {
        'question': 'a characteristic of open systems where there are continuous inputs and outputs of energy and matter, but the system as a whole remains in a more-or-less constant state.',
        'choices': ['Steady-state equilibrium', 'Unstable Equilibrium', 'Equilibrium', 'New Equilibrium'],
        "correct_choice": 0
    },
    {
        'question': 'it refers to the area of land and water required to sustainably provide all resources at the rate at which they are being consumed by a given population.',
        'choices': ['Sustainability', 'Ecological Indicators', 'Ecological footprint', 'Natural Capital'],
        "correct_choice": 2
    },
    {
        'question': 'the use and management of resources that allows full natural replacement of the resources exploited and full recovery of the ecosystems affected by their extraction and use.',
        'choices': ['Sustainability', 'Ecological Indicators', 'Ecological footprint', 'Natural Capital'],
        "correct_choice": 0
    },
    {
        'question': '_______ do not persist in the environment and break down quickly. They may be broken down by decomposers or physical processes.',
        'choices': ['Acute pollution', 'Biodegradable pollutants', 'Chronic pollution', 'Persistent organic pollutants'],
        "correct_choice": 1
    },
    {
        'question': '_________ are resistant to breaking down and remain active in the environment for a long time.',
        'choices': ['Persistent organic pollutants', 'Acute pollution', 'Biodegradable pollutants', 'Chronic pollution'],
        "correct_choice": 0
    },
    {
        'question': 'occurs when large amounts of a pollutant are released, causing a lot of harm.',
        'choices': ['Persistent organic pollutants', 'Biodegradable pollutants', 'Chronic pollution', 'Acute pollution'],
        "correct_choice": 3
    },
    {
        'question': 'the process by which modern organisms have descended from ancient ancestors.',
        'choices': ['Evolution', 'Diversity', 'Extinction', 'Mutation'],
        "correct_choice": 0
    },
    {
        'question': 'A change in DNA, the hereditary material of life.',
        'choices': ['Gene flow', 'Genetic Drift', 'Mutation', 'Natural Selection'],
        "correct_choice": 2
    },
    {
        'question': 'Is any movement of individuals, and/or the genetic material they carry, from one population to another.',
        'choices': ['Gene flow', 'Genetic Drift', 'Mutation', 'Natural Selection'],
        "correct_choice": 0
    },
    {
        'question': 'Humans have destroyed or changed most of the original natural habitat',
        'choices': ['Fragmentation', 'Habitat loss', 'Introduced Species', 'Overharvesting/ Overexploitation'],
        "correct_choice": 1
    },
    {
        'question': 'Large area is divided up into a patchwork of fragments, separated from each other.',
        'choices': ['Habitat loss', 'Introduced Species', 'Overharvesting/ Overexploitation', 'Fragmentation'],
        "correct_choice": 3
    },
    {
        'question': 'Photosynthesis by ________ supports a highly diverse range of food webs.',
        'choices': ['Phytoplankton', 'Fishes', 'Plants', 'Sunlight'],
        "correct_choice": 0
    },
    {
        'question': 'What very important food for humans that contains the following: \n\n• High in protein \n• Low in saturated fats \n• Contain various vitamins(A,B,D)',
        'choices': ['Meat', 'Fish', 'Vegetables', 'Dairy'],
        "correct_choice": 1
    }
]

bio_floor = [ #9th floor Biology
    {
        'question': 'In which process does a cell spend the least amount of energy?',
        'choices': ['Active transport', 'Facilitated diffusion', 'Osmosis', 'Simple diffusion'],
        "correct_choice": 3
        
    },
    {
        'question': 'Which of the following organelles is responsible for protein synthesis in eukaryotic cells?',
        'choices': ['Golgi apparatus', 'Endoplasmic reticulum', 'Lysosome', 'Mitochondria'],
        "correct_choice": 1
    },
    {
        'question': 'What is the primary function of white blood cells in the immune system?',
        'choices': ['Phagocytosis', 'Oxygen transport', 'Nutrient absorption', 'Hormone production'],
        "correct_choice": 0
    },
    {
        'question': 'Which of the following is NOT a function of the skeletal system?',
        'choices': ['Protection of internal organs', 'Storage of minerals', 'Production of red blood cells', 'Facilitation of movement'],
        "correct_choice": 2
    },
    {
        'question': 'What is the role of the hormone insulin in the human body?',
        'choices': ['Increase blood sugar levels', 'Promote fat breakdown', 'Stimulate muscle growth', 'Lower blood sugar levels'],
        "correct_choice": 3
    },
    {
        'question': 'In meiosis, when does crossing over occur?',
        'choices': ['Prophase I', 'Metaphase I', 'Anaphase I', 'Telophase I'],
        "correct_choice": 0
    },
    {
        'question': 'What is the correct sequence of events in cellular respiration?',
        'choices': ['Glycolysis, Krebs cycle, electron transport chain', 'Krebs cycle, electron transport chain, glycolysis', 'Electron transport chain, glycolysis, Krebs cycle', 'Glycolysis, electron transport chain, Krebs cycle'],
        "correct_choice": 0
    },
    {
        'question': 'Which of the following is responsible for carrying oxygen in red blood cells?',
        'choices': ['Hemoglobin', 'Platelets', 'Lymphocytes', 'Erythrocytes'],
        "correct_choice": 0
    },
    {
        'question': 'What is the process by which DNA is copied into mRNA?',
        'choices': ['Translation', 'Transcription', 'Replication', 'Mutation'],
        "correct_choice": 1
    },
    {
        'question': 'Which of the following is responsible for regulating the body\'s internal temperature?',
        'choices': ['Hypothalamus', 'Pituitary gland', 'Thyroid gland', 'Adrenal gland'],
        "correct_choice": 0
    },
    {
        'question': 'What is the correct order of the stages of mitosis?',
        'choices': ['Prophase, Metaphase, Anaphase, Telophase', 'Prophase, Anaphase, Metaphase, Telophase', 'Anaphase, Prophase, Metaphase, Telophase', 'Telophase, Anaphase, Metaphase, Prophase'],
        "correct_choice": 0
    },
    {
        'question': 'Which of the following is responsible for converting light energy into chemical energy during photosynthesis?',
        'choices': ['Chlorophyll', 'Stomata', 'Thylakoids', 'Nucleus'],
        "correct_choice": 0
    },
    {
        'question': 'What is the role of tRNA (transfer RNA) in protein synthesis?',
        'choices': ['Carrying the genetic code from DNA to the ribosomes', 'Binding to mRNA and catalyzing the formation of peptide bonds', 'Carrying amino acids to the ribosomes', 'Initiating the process of translation'],
        "correct_choice": 2
    },
    {
        'question': 'What is the term for the process by which cells differentiate and become specialized in structure and function?',
        'choices': ['Apoptosis', 'Homeostasis', 'Metabolism', 'Differentiation'],
        "correct_choice": 3
    },
    {
        'question': 'Which of the following is responsible for producing antibodies in response to antigens?',
        'choices': ['B cells', 'T cells', 'Natural killer cells', 'Macrophages'],
        "correct_choice": 0
    },
    {
        'question': 'What is the function of the enzyme helicase in DNA replication?',
        'choices': ['Breaking hydrogen bonds between DNA strands', 'Adding nucleotides to the growing DNA strand', 'Proofreading and repairing DNA errors', 'Stabilizing the DNA double helix structure'],
        "correct_choice": 0
    },
    {
        'question': 'Which of the following is responsible for coordinating voluntary muscle movement?',
        'choices': ['Brainstem', 'Cerebellum', 'Spinal cord', 'Cerebrum'],
        "correct_choice": 3
    },
    {
        'question': 'Which of the following is responsible for the production of insulin in the human body?',
        'choices': ['Adrenal glands', 'Thyroid gland', 'Pancreas', 'Pituitary gland'],
        "correct_choice": 2
    },
    {
        'question': 'What is the function of the enzyme catalase in cells?',
        'choices': ['Breaking down lipids', 'Breaking down proteins', 'Breaking down nucleic acids', 'Breaking down hydrogen peroxide'],
        "correct_choice": 3
    },
    {
        'question': 'What is the function of the enzyme RNA polymerase in gene expression?',
        'choices': ['Unwinding the DNA double helix', 'Adding nucleotides to the growing RNA strand', 'Repairing damaged DNA', 'Initiating translation'],
        "correct_choice": 1
    }
]

chem_floor = [ #10 floor Chemistry
    {
        "question": "Which of the following elements is a noble gas?",
        "choices": ["Oxygen", "Nitrogen", "Helium", "Carbon"],
        "correct_choice": 2
    },
    {
        "question": "What is the atomic number of sodium?",
        "choices": ["10", "11", "12", "13"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is an example of a strong acid?",
        "choices": ["Vinegar (acetic acid)", "Lemon juice (citric acid)", "Hydrochloric acid", "Carbonic acid"],
        "correct_choice": 2
    },
    {
        "question": "Which of the following is an example of an exothermic reaction?",
        "choices": ["Photosynthesis", "Combustion", "Melting ice", "Electrolysis"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is NOT a state of matter?",
        "choices": ["Solid", "Gas", "Liquid", "Energy"],
        "correct_choice": 3
    },
    {
        "question": "Which of the following elements has the symbol 'Fe'?",
        "choices": ["Iron", "Fluorine", "Iodine", "Indium"],
        "correct_choice": 0
    },
    {
        "question": "What is the chemical formula for water?",
        "choices": ["CO2", "H2O", "NaCl", "CH4"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is a greenhouse gas?",
        "choices": ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"],
        "correct_choice": 2
    },
    {
        "question": "What is the pH value of a neutral solution?",
        "choices": ["7", "1", "10", "14"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following elements is a metal?",
        "choices": ["Chlorine", "Sulfur", "Calcium", "Fluorine"],
        "correct_choice": 2
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Au", "Ag", "Fe", "Cu"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following is an example of a heterogeneous mixture?",
        "choices": ["Saltwater", "Air", "Orange juice (without pulp)", "Granite"],
        "correct_choice": 3
    },
    {
        "question": "What is the formula for calculating density?",
        "choices": ["Mass × Volume", "Mass ÷ Volume", "Volume × Mass", "Volume ÷ Mass"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is an example of a renewable energy source?",
        "choices": ["Natural gas", "Coal", "Solar power", "Oil"],
        "correct_choice": 2
    },
    {
        "question": "Which of the following is NOT a type of chemical bond?",
        "choices": ["Covalent bond", "Ionic bond", "Hydrogen bond", "Magnetic bond"],
        "correct_choice": 3
    },
    {
        "question": "What is the chemical symbol for helium?",
        "choices": ["He", "H", "Cl", "Ne"],
        "correct_choice": 0
    },
    {
        "question": "What is the main component of natural gas?",
        "choices": ["Carbon dioxide", "Methane", "Oxygen", "Nitrogen"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is a property of acids?",
        "choices": ["They turn litmus paper blue", "They taste bitter", "They react with bases to form salts", "They have a pH greater than 7"],
        "correct_choice": 2
    },
    {
        "question": "Which of the following is an example of a physical change?",
        "choices": ["Rusting of iron", "Burning of wood", "Cooking an egg", "Melting ice"],
        "correct_choice": 3
    },
    {
        "question": "What is the chemical formula for glucose?",
        "choices": ["C6H12O6", "H2SO4", "NaCl", "CO2"],
        "correct_choice": 0
    }
]

calculus_floor = [ #11th floor Calculus 
    {
        "question": "What is the derivative of x^2 with respect to x?",
        "choices": ["2x", "x^2", "1", "0"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of 3x^2 with respect to x?",
        "choices": ["x^3 + C", "3x^3 + C", "3x + C", "3x^2 + C"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of sin(x) with respect to x?",
        "choices": ["cos(x)", "sin(x)", "tan(x)", "-cos(x)"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of e^x with respect to x?",
        "choices": ["e^x", "ln(x)", "x^2", "e^x + C"],
        "correct_choice": 3
    },
    {
        "question": "What is the derivative of ln(x) with respect to x?",
        "choices": ["1/x", "x", "e^x", "ln(x)"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of 1/x with respect to x?",
        "choices": ["ln(x)", "x^2", "e^x", "1/x"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of 4x^3 with respect to x?",
        "choices": ["3x^2", "12x^2", "4x^2", "4"],
        "correct_choice": 1
    },
    {
        "question": "What is the integral of cos(x) with respect to x?",
        "choices": ["sin(x)", "cos(x)", "-sin(x)", "tan(x)"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of 2e^(3x) with respect to x?",
        "choices": ["2e^(3x)", "3e^(3x)", "6e^(3x)", "e^(3x)"],
        "correct_choice": 2
    },
    {
        "question": "What is the integral of x*sin(x) with respect to x?",
        "choices": ["x^2*sin(x)", "x*cos(x)", "-x*cos(x)", "x*sin(x)"],
        "correct_choice": 2
    },
    {
        "question": "What is the derivative of tan(x) with respect to x?",
        "choices": ["sin(x)", "cos(x)", "sec^2(x)", "-sec^2(x)"],
        "correct_choice": 2
    },
    {
        "question": "What is the integral of 5 with respect to x?",
        "choices": ["5x", "5/x", "5", "0"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of x^3 - 2x^2 + 4x - 1 with respect to x?",
        "choices": ["3x^2 - 4x + 4", "3x^2 - 4x + 1", "4x^3 - 3x^2 + 2x - 1", "3x^3 - 2x^2 + 4x"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of 1/(x^2 + 1) with respect to x?",
        "choices": ["arctan(x)", "ln(x)", "sin(x)", "cos(x)"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of e^(2x) - 3x^2 with respect to x?",
        "choices": ["2e^(2x) - 6x", "e^(2x) - 6x", "2e^(2x) - 6", "e^(2x) - 3x"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of (2x + 1)^2 with respect to x?",
        "choices": ["x^2 + 2x + C", "(2x + 1)^3/3 + C", "4x^2 + 2x + 1", "2x^2 + x + C"],
        "correct_choice": 1
    },
    {
        "question": "What is the derivative of ln(2x^3) with respect to x?",
        "choices": ["3/x", "3x^2", "1/x", "2/x"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of e^(3x) - 2x with respect to x?",
        "choices": ["e^(3x) - x^2 + C", "e^(3x) - x + C", "3e^(3x) - x^2 + C", "e^(3x) - 2x + C"],
        "correct_choice": 0
    },
    {
        "question": "What is the derivative of cos^2(x) with respect to x?",
        "choices": ["-2sin(x)", "2cos(x)", "2sin(x)", "-sin(2x)"],
        "correct_choice": 0
    },
    {
        "question": "What is the integral of (3x^2 + 2x - 1)/(x^2 + x) with respect to x?",
        "choices": ["3ln(x) + 2x - ln(x^2 + x) + C", "3ln(x) + 2ln(x) - ln(x^2 + x) + C", "3ln(x) + 2ln(x^2 + x) - ln(x) + C", "3ln(x) + 2ln(x^2 + x) - ln(x^2) + C"],
        "correct_choice": 2
    },
    {
        "question": "What is the derivative of 1/ln(x) with respect to x?",
        "choices": ["1/(xln(x))", "-1/(xln(x))", "ln(x)", "1/(xln^2(x))"],
        "correct_choice": 1
    },
    {
        "question": "What is the integral of sec^2(x) with respect to x?",
        "choices": ["tan(x)", "cos(x)", "csc(x)", "cot(x)"],
        "correct_choice": 0
    }
]

physics_floor = [ #12th floor Physics
    {
        "question": "Which of the following equations represents Newton's second law of motion?",
        "choices": ["F = ma", "F = mv", "F = ms", "F = mg"],
        "correct_choice": 0
    },
    {
        "question": "In which medium does sound travel the fastest?",
        "choices": ["Air", "Water", "Vacuum", "Steel"],
        "correct_choice": 3
    },
    {
        "question": "A spring with a spring constant of 200 N/m is compressed by 0.1 meters. What is the potential energy stored in the spring?",
        "choices": ["0.01 J", "0.02 J", "0.05 J", "0.1 J"],
        "correct_choice": 2
    },
    {
        "question": "Which of the following is an example of a scalar quantity?",
        "choices": ["Velocity", "Force", "Acceleration", "Temperature"],
        "correct_choice": 3
    },
    {
        "question": "A car travels at a constant speed of 60 km/h for 2 hours. What is the total distance traveled?",
        "choices": ["120 km", "100 km", "80 km", "60 km"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following is a unit of electric current?",
        "choices": ["Joule", "Volt", "Watt", "Ampere"],
        "correct_choice": 3
    },
    {
        "question": "When an object is immersed in a fluid, it experiences an upward force called:",
        "choices": ["Friction", "Tension", "Gravity", "Buoyancy"],
        "correct_choice": 3
    },
    {
        "question": "A car accelerates uniformly from rest to a speed of 25 m/s in 8 seconds. What is its acceleration?",
        "choices": ["1.25 m/s²", "2.5 m/s²", "3.125 m/s²", "6.25 m/s²"],
        "correct_choice": 2
    },
    {
        "question": "The bending of light when it passes from one medium to another is called:",
        "choices": ["Reflection", "Refraction", "Diffraction", "Dispersion"],
        "correct_choice": 1
    },
    {
        "question": "Which of the following is a renewable source of energy?",
        "choices": ["Coal", "Natural gas", "Solar power", "Nuclear power"],
        "correct_choice": 2
    },
    {
        "question": "A ball is thrown vertically upwards with an initial velocity of 20 m/s. How high does it go before it starts falling back down?",
        "choices": ["20 m", "40 m", "80 m", "100 m"],
        "correct_choice": 1
    },
    {
        "question": "According to the law of conservation of energy, energy cannot be:",
        "choices": ["Created", "Destroyed", "Transferred", "Dissipated"],
        "correct_choice": 1
    },
    {
        "question": "The SI unit of electric charge is:",
        "choices": ["Volt", "Ampere", "Ohm", "Coulomb"],
        "correct_choice": 3
    },
    {
        "question": "Which of the following is a vector quantity?",
        "choices": ["Speed", "Distance", "Displacement", "Time"],
        "correct_choice": 2
    },
    {
        "question": "A circuit consists of three resistors in parallel: R1 = 4 Ω, R2 = 6 Ω, and R3 = 8 Ω. What is the equivalent resistance of the circuit?",
        "choices": ["3 Ω", "4 Ω", "6 Ω", "12 Ω"],
        "correct_choice": 0
    },
    {
        "question": "The phenomenon of a change in frequency and pitch of a sound source as it approaches or moves away from an observer is called:",
        "choices": ["Doppler effect", "Interference", "Resonance", "Diffraction"],
        "correct_choice": 0
    },
    {
        "question": "What is the momentum of an object with a mass of 5 kg and a velocity of 10 m/s?",
        "choices": ["50 kg·m/s", "15 kg·m/s", "5 kg·m/s", "2 kg·m/s"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following is an example of static friction?",
        "choices": ["A car skidding on a wet road", "Sliding a book on a table", "Pushing a box on the floor", "A person walking on the ground"],
        "correct_choice": 2
    },
    {
        "question": "A block of mass 2 kg is pushed with a force of 10 N at an angle of 30 degrees with the horizontal. If the coefficient of friction between the block and the surface is 0.2, what is the acceleration of the block?",
        "choices": ["4 m/s²", "5 m/s²", "7 m/s²", "8 m/s²"],
        "correct_choice": 0
    },
    {
        "question": "Which of the following statements about gravity is true?",
        "choices": ["Gravity depends on the mass of the object only.", "Gravity depends on the distance between two objects only.", "Gravity depends on both the mass and the distance between two objects.", "Gravity does not exist."],
        "correct_choice": 2
    }
]
