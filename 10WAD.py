import random

vocab = {"Anachronistic": "Old fashioned",
         "Misconstrue": "Misunderstand",
         "Reprehensible": "deserving condemnation",
         "Ostracising": "To exclude someone from a group/society",
         "Disposition": "A persons qualities of mind/character",
         "Spontaneity": "The condition of being spontaneous",
         "Antiquated": "old/outdated",
         "Proclivities": "A tendency to do something regularly",
         "Demonstrably": "To demonstrate",
         "Superfluous": "unnecessary/ more than enough",
         "Ascertain": "find something out for certain",
         "Illustrious": "well known, respected and admired for past achievements",
         "Conceited": "egotistical/vain",
         "Pertain": "be related or applicable to something",
         "Scintillating": "brilliantly and excitingly clever/skillful | sparkling or shining brightly",
         "Felicitous": "well chosen or suited to the circumstance | pleasing and fortunate",
         "Infatuated": "obsessed",
         "Covet": "yearn to possess something",
         "Commiseration": "condolences",
         "Astounding": "amazing",
         "Astonishing": "amazing",
         "Covenant": "promise",
         "Intrinsic": "essential",
         "Pejorative": "a word or expression conveying disapproval",
         "Perpetuate": "continue something indefinitely",
         "Content": "a state of peacefulness / happiness",
         "Contempt": "feeling that someone / something is worthless or beneath consideration",
         "Astute": "an individual that is good at assessing people or situations to their own benefit",
         "Austere": "severe or strict in manner or attitude",
         "Guile": "characterised by slyness and cunning",
         "Cognisant": "having knowledge or awareness",
         "Indicative": "indication of something",
         "Apathetic": "showing no concern, enthusiasm or interest",
         "Myopic": "short sighted",
         "Demean": "cause severe loss in dignity and respect for someone or something",
         "Bemoan": "express discontent or sorrow over something",
         "Vehemently": "in forceful, passionate or intense manner with great feeling",
         "Vindicate": "To clear of blame or suspicion",
         "Ridicule": "to insult someone or something",
         "Succinct": "briefly and clearly expressed",
         "Incongruous": "not in harmony / keeping of the surroundings or other aspects of something",
         "Contention": "a heated disagreement / an assertion especially maintained in argument",
         "Altruism": "selflessness",
         "Pontificate": "expressing one’s opinions in a pompous / dogmatic way",
         "Derelict": "in very poor condition as a result of disuse / neglect",
         "Inadvertently": "a unintentional result or consequence of one’s actions",
         "Ambiguous": "open to interpretation",
         "Scandalous": "causing public outrage by a offence against morality / law",
         "Detestable": "deserving intense dislike",
         "Invigorating": "making one feel strong, healthy and full of energy",
         "Surmise": "deduce",
         "Apprehensive": "anxious or fearful that something bad will happen",
         "Discord": "disagreement between two people",
         "Quarrelsome": "argumentative",
         "Minacious": "menacing; threatening",
         "Extraordinaire": "outstanding in a particular capacity",
         "Aficionado": "someone who is very knowledgable in a specific subject",
         "Despondent": "in low spirits from loss of hope or courage",
         "Fortuitous": "happening by chance rather than intention",
         "Denigrate": "criticise unfairly / disparage",
         "Impertinent": "not showing proper respect / rude",
         "Adversarial": "confrontational",
         "Capricious": "changing according to no discernible rules; unpredictable",
         "Deplorable": "deserving strong condemnation, completely unacceptable",
         "Beguiled": "to charm or enchant someone, often in a deceptive way",
         "Expeditiously": "with great speed and effectivity",
         "Apoplectic": "furious",
         "Dichotomy": "the contrast between two things that are presented as completely different",
         "Futile": "pointless",
         "Belligerent": "hostile / aggressive",
         "Exuberant": "full of energy, excitement or cheerfulness | growing profusely",
         "Motif": "a dominant or recurring idea in an artistic work",
         "Parable": "a simple story used to illustrate a moral or spiritual lesson",
         "Elated": "ecstatic",
         "Illicit": "forbidden by rule or law",
         "Circumvent": "to avoid something",
         "Exasperation": "intense irritation or annoyance",
         "Repugnant": "extremely distasteful / unacceptable",
         "Regale": "entertain people / amuse someone with talk",
         "Abrasive": "Talking without concern for others feelings",
         "Inauspicious": "not conducive to success | unpromising",
         "Enthral": "capture the fascinated attention of",
         "Riveting": "completely engrossing / compelling",
         "Erroneous": "incorrect",
         "Candid": "truthful and straightforward",
         "Capitulate": "cease to resist an opponent or demand; yield",
         "Paradigm": "a typical example or pattern of something",
         "Mundane": "lacking interest or excitement; dull",
         "Obfuscate": "make obscure, unclear or unintelligible",
         "Scrupulous": "careful thorough and extremely attentive to details | Very concerned to avoid doing wrong",
         "Disparage": "regard or represent as being of little worth",
         "Vapid": "offering nothing challenging or stimulating; bland",
         "Inundated": "overburdened with requests",
         "Fatuous": "silly and pointless",
         "Prevalent": "widespread in a particular area or at a particular time",
         "Ruminate": "Think deeply on something",
         "Propagate": "spread or promote an idea / theory widely",
         "Deigned": "do something that one considers to be beneath ones dignity",
         "Enamoured": "be filled with love for | have a liking or admiration for",
         "Discern": "recognise or find out| distinguish someone/something with difficulty by sight or the other senses",
         "Saccharine": "excessively sweet or sentimental",
         "Hubristic": "excessively proud or self confident",
         "Bumptious": "irritatingly self assertive",
         "Rambunctious": "uncontrollably exuberant / boisterous",
         "Egregious": "outstandingly bad / shocking",
         "Abysmal": "extremely bad / appalling",
         "Tumultuous": "making an uproar or loud, confused noise | excited, confused disorderly",
         "Ostentatious": "characterised by pretentious or showy display; designed to impress",
         "Equidistant": "of equal distance",
         "Preposterous": "contrary to reason or common sense; utterly absurd / ridiculous",
         "Presume": "suppose that something is the case on  the basis of probability.",
         "Indoctrinate": "teach someone to accept a set of beliefs uncritically",
         "Cynical": "doubtful as to whether something will happen or whether it’ll be worthwhile",
         "Reverence": "deep respect for something / someone",
         "Acquiescence": "the reluctant acceptance of something without protest",
         "Allude": "suggest or call attention to indirectly; hint at.",
         "Permeate": "spread throughout",
         "Aspersion": "an attack on the reputation / integrity of someone / something",
         "Ameliorate": "improve something that’s bad",
         "Expostulate": "express strong disapproval or disagreement",
         "Serendipitous": "occurring or discovered by chance in a happy or beneficial way",
         "Facetious": "treating serious issues with deliberately inappropriate humour",
         "Ubiquitous": "present everywhere",
         "Reprimand": "a formal expression of disapproval",
         "Impetuous": "acting or done quickly without thought or care",
         "Paucity": "the presence of something in small or insufficient amounts",
         "Sequestered": "isolated",
         "Misanthropic": "having a dislike of other people",
         "Sully": "damage the purity or integrity of something",
         "Licentious": "promiscuous and unprincipled in sexual matters",
         "Reprobate": "unprincipled",
         "Dubious": "hesitating or doubting",
         "Besotted": "heavily infatuated",
         "Subterfuge": "deceit used in order to achieve one’s goal",
         "Benevolent": "well meaning and kindly | serving a charitable rather than a profit making purpose",
         "Bodacious": "excellent, admirable or attractive",
         "Culminate": "Reach a climax or point of highest development",
         "Nefarious": "(of an action or activity) Wicked or criminal",
         "Heinous": "(of a person or wrongful act) Utterly odious or wicked",
         "Impervious": "Unable to be affected by",
         "Sanctimonious": "Making a show of being morally superior to other people",
         "Tribulation": "A cause / state of great disturbance and suffering",
         "Exalt": "think or speak very highly of someone / something",
         "Jovial": "cheerful and friendly",
         "Disconcerting": "causing one to feel unsettled",
         "Ineffable": "Too great or extreme to be expressed or described in words",
         "Debauchery": "excessive indulgence in sex, alcohol or drugs",
         "Miscreant": "a person who has done something wrong / unlawful",
         "Arduous": "difficult, requiring great effort",
         "Anguish": "severe mental or physical pain / suffering",
         "Predilection": "a preference or special liking for something | a bias in favour of something",
         "Verbosity": "the quality of using more words than needed",
         "Immolation": "To kill or destroy especially by fire | to offer in sacrifice",
         "Disdain": "feeling that someone or something is unworthy of one’s consideration or respect",
         "Transcendental": "relating to a spiritual realm",
         "Innocuous": "not harmful or offensive",
         "Scoundrel": "a dishonest or unscrupulous person; a rogue",
         "Inadequate": "Lacking the quality or quantity required; insufficient for a purpose",
         "Amicable": "Characterised by friendliness and absence of discord"
         }

words = list(vocab.keys())

quiz = []


def running():
    word_count = 1
    while word_count <= 10:
        word = random.choice(words)
        definition = vocab.get(word)
        if word in quiz:
            pass
        print("\n" * 5)
        print(f"Word {word_count}")
        print("------------------------------------------------------------------------------------------------------")
        print(f"{word} ---> {definition}")
        print("------------------------------------------------------------------------------------------------------")
        print("\n" * 5)
        quiz.append(word)
        words.remove(word)

        continue_or_quit = input("Press ENTER to continue or type Q to quit:")
        if continue_or_quit.upper() == "Q":
            start_screen()
        else:
            print('\n' * 5)
            word_count += 1
            continue
    quiz_screen()


def start_screen():
    print("\n" * 5)
    print("Welcome to 10WAD! (10 Words A Day)")
    print("\n" * 2)
    print("(Created by Panj)")
    print("\n" * 2)
    begin = input("Type START to begin:")
    if begin.upper() == "START":
        running()
    else:
        invalid_start_input()


def end_screen():
    print("\n" * 5)
    print("That was your 10WAD!")
    print("\n" * 2)
    return_to_start = input("Type MENU to return to start screen:")
    if return_to_start.upper() == "MENU":
        start_screen()
    else:
        invalid_restart_input()


def invalid_start_input():
    print("\n" * 5)
    print("Invalid input, please try again!")
    begin = input("Type START to begin:")
    if begin.upper() == "START":
        running()
    else:
        invalid_start_input()


def invalid_restart_input():
    print("\n" * 5)
    print("Invalid input, please try again!")
    return_to_start = input("Type MENU to return to start screen:")
    if return_to_start.upper() == "MENU":
        start_screen()
    else:
        invalid_restart_input()


def quiz_screen():
    print("\n" * 12)
    print("Welcome to the quiz section!")
    print("\n" * 1)
    print("Carefully recollect the words you've been shown so far and correctly assign them to their definitions")
    print("\n" * 1)
    print("Good luck!")
    score = 0
    for word in quiz:
        definition = vocab.get(word)
        print("\n" * 10)
        print("What word does this definition belong to?")
        print("------------------------------------------------------------------------------------------------------")
        print(definition)
        print("------------------------------------------------------------------------------------------------------")
        print("\n" * 10)

        answer = input("Please type your answer here: ")
        if answer.lower() == word.lower():
            print("\n" * 1)
            print("Correct answer!")
            print("---------------------------------------------------------------------------------------------------")
            print(f"{word} ---> {definition}")
            print("---------------------------------------------------------------------------------------------------")
            score += 1
            continue
        else:
            print("\n" * 1)
            print("Your answer is incorrect :(")
            print("---------------------------------------------------------------------------------------------------")
            print(f"Correct answer: {word} ---> {definition}")
            print("---------------------------------------------------------------------------------------------------")
            continue
    print("\n" * 2)
    print(f"You got {score}/10 questions correct")
    if score == 10:
        print("\n" * 2)
        print(f"Congratulations! You have a perfect score!")
    end_screen()


start_screen()