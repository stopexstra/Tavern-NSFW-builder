import json

JSON_PATH = "database_generated.json"
TARGET_SECTIONS = [
    "enemyKnowledge",
    "events",
    "cgSeen",
    "animatedCgSeen"
]
MARKER = "__ADDED_BY_SCRIPT__"


# pls note. Be VERY careful with adding corrections to this file, because it is VERY sensetive. For example, if u make "cept" change to "accept", 
# then it will also "correct" correct ones, since the word "cept" is also in a word "acCEPT" so it would become --> "acaccept".


# corrections 
REPLACEMENTS = {
    "WW": "W",
    "AA": "A",
    "SCREW": "DKCREW",
    "CAG_TEAM": "TAG_TEAM",
    "KITSUNE_MEET_ANAL_PROPOSAL_THICKENOUT": "KITSUNE_MEET_ANAL_PROPOSAL_CHICKENOUT",
    "KITSUNE-MEET-ANAL-PROPOSAL-THICKENOUT": "KITSUNE-MEET-ANAL-PROPOSAL-CHICKENOUT",
    "GOBLIN_DATE_TAVERN_THICKEN": "GOBLIN_DATE_TAVERN_THICKEN",
    "GOBLIN-DATE-TAVERN-THICKEN": "GOBLIN-DATE-TAVERN-CHICKEN",
    "OUTPOST-ARMOR-NIGHT": "OUTPOST-ARMOR-TIGHT",
    "NAGA_CAVEIN_LOST_EXHAUSTED_TOLLAPSE": "NAGA_CAVEIN_LOST_EXHAUSTED_COLLAPSE",
    "NAGA-CAVEIN-LOST-EXHAUSTED-TOLLAPSE": "NAGA-CAVEIN-LOST-EXHAUSTED-COLLAPSE",
    "OUTPOST_ARMOR_NIGHT": "OUTPOST_ARMOR_TIGHT",
    "DARK-KNIGHT-DEFEAT-NIGHT": "DARK-KNIGHT-DEFEAT-TIGHT",
    "DARK-KNIGHT_DEFEAT_NIGHT": "DARK_KNIGHT_DEFEAT_TIGHT",
    "NOCOCKNDOM": "NOCONDOM",
    "KNOT_NIGHT": "KNOT_TIGHT", 
    "MMASSAGE": "MASSAGE",
    "BRIGAND_CHIEF": "BRIGAND_THIEF",
    "BRIGAND-CHIEF": "BRIGAND-THIEF",
    "CHIEF_STEAL": "THIEF_STEAL",
    "CHIEF-STEAL": "THIEF-STEAL",
    "NOCOCKOCHIE": "NOCOOCHIE",
    "KNOT-NIGHT": "KNOT-TIGHT",
    "GOBLIN_PLUGGED_DEFEATED": "GOBLIN_PLUGGED_HEATED",
    "GOBLIN-PLUGGED-DEFEATED": "GOBLIN-PLUGGED-HEATED",
    "CONQJS": "CONVINCE",
    "ETTIN_DATE_ANAL_NIGHT": "ETTIN_DATE_ANAL_TIGHT",
    "ETTIN-DATE-ANAL-NIGHT": "ETTIN-DATE-ANAL-TIGHT",
    "DULLAHAN_ANAL_NIGHT": "DULLAHAN_ANAL_TIGHT",
    "DULLAHAN-ANAL-NIGHT": "DULLAHAN-ANAL-TIGHT",
    "DEMON-KING-DEAR": "DEMON-KING-HEAR",
    "DEMON_KING_DEAR": "DEMON_KING_HEAR",
    "SLIME_PLUGGED_DEFEATED": "SLIME_PLUGGED_HEATED",
    "SLIME-PLUGGED-DEFEATED": "SLIME-PLUGGED-HEATED",
    "MJONEY": "MONEY",
    "BRIGAND_PLUGGED_DEFEATED": "BRIGAND_PLUGGED_HEATED",
    "BRIGAND-PLUGGED-DEFEATED": "BRIGAND-PLUGGED-HEATED",
    "KITSUNE_ABOUT_DER": "KITSUNE_ABOUT_HER",
    "KITSUNE-ABOUT-DER": "KITSUNE-ABOUT-HER",
    "QUETZAL_RIDE": "QUETZAL_HIDE",
    "QUETZAL-RIDE": "QUETZAL-HIDE",
    "CATGIRL_WARLOCK_RIDE": "CATGIRL_WARLOCK_HIDE",
    "CATGIRL-WARLOCK-RIDE": "CATGIRL-WARLOCK-HIDE",
    "GIANTESS_RIDE": "GIANTESS_HIDE",
    "GIANTESS-RIDE": "GIANTESS-HIDE",
    "TRUDY_COMPANION_PLUGGED_DEFEATED": "TRUDY_COMPANION_PLUGGED_HEATED",
    "TRUDY-COMPANION-PLUGGED-DEFEATED": "TRUDY-COMPANION-PLUGGED-HEATED",
    "NJINOFAURESS": "MINOTAURESS",
    "CROSSED": "TOSSED",
    "MINOFAURESS": "MINOTAURESS",
    "CHONG": "THONG",
    "CRAINING": "TRAINING",
    "NMUTUAL": "MUTUAL",
    "AMUTUAL": "MUTUAL",
    "DEFEATEDPLUG": "HEATEDPLUG",
    "AMINOTAURESS": "MINOTAURESS",
    "MMINOTAURESS": "MINOTAURESS",
    "DOGGY_NIGHT": "DOGGY_TIGHT",
    "DOGGY-NIGHT": "DOGGY-TIGHT",
    "PERACCEPTION": "PERCEPTION",
    "PERACCEPTIVE": "PERCEPTIVE",
    "NOCOCKCK": "NOCOCK",
    "ACACCEPT": "ACCEPT",
    "ACCEPTPT": "ACCEPT",
    "CCOMPANION": "COMPANION",
    "DCONT": "DONT",
    "SPCONTANEOUS": "SPONTANEOUS",
    "YWARLOCK": "WARLOCK",
    "CAME": "GAME",
    "CCONFRCONT": "CONFRONT",
    "CONFRCONT": "CONFRONT",
    "OVER_RIDE": "OVER_HIDE",
    "OVER-RIDE": "OVER-HIDE",
    "ANAL_CONTENT": "ANAL_TORMENT",
    "ANAL-CONTENT": "ANAL-TORMENT",
}

def correct_key(key):
    for wrong, correct in REPLACEMENTS.items():
        key = key.replace(wrong, correct)
    return key

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)


for section_name in TARGET_SECTIONS:
    if section_name not in data:
        continue

    section = data[section_name]
    started = False
    changes = []

    for key in list(section.keys()):
        if key == MARKER:
            started = True
            continue
        if not started:
            continue
        new_key = correct_key(key)
        if new_key != key:
            changes.append((key, new_key))

    for old_key, new_key in changes:

        if new_key in section:
            del section[old_key]
            print(f"Skipped duplicate: {old_key} -> {new_key}")
            continue

        section[new_key] = section.pop(old_key)
        print(f"Corrected: {old_key} -> {new_key}")

# This section is entirely for names. For some reason, the game needs that in the json file there is not only the events, 
# but also names as a string in there. So you need both smth like "CATGIRL":1, and "catgirl":1, for catgirl to appear in "pervert" section (only for some of them).
# So if there is a new character, then just write their name in the list and the programm will do it for u.
# Also this game is so strange and I dont know why some of them named this way in the code ¯\_(ツ)_/¯ 
# And to be frank with u, I dont even know wether you need that much. I am almost guessing at this point
# YOU NEED ALSO BLANK SPACES???? WHYYYY????? "Dark Knight":1, not "dark_knight"
# I swear to god I GONNA KILL THIS FK GAME. Iam going more and more insane as I try to figure out this shit. 
# Ok, so (for some reason only for some of them) u need to have it like this "Ettin":1, so not "ETTIN":1, and not "ettin":1, . See the pattern? no? Yea mee too.
# I hate my life
# I made it work. :) ... but now it makes many unnecessary strings :(
 
NAMES = [
    "angel",
    "catgirl",
    "kylira",
    "elf",
    "gadgeteer",
    "brothel", # = brothel madam
    "mouth fiend",
    "vampire hunter",
    "shopkeep",
    "shop catgirl shopkeep", # = catgirl shopkeep
    "innkeep", #pretty sure u dont need this one
    "catgirl innkeep",
    "innkeep catgirl",
    "inn catgirl",
    "catgirl inn", # I dont think u need both catgirl inn and catgirl innkeep (and others) but i am unsure
    "story catgirl inn",
    "salon", # ¯\_(ツ)_/¯
    "salon catgirl", #Im pretty sure that is "hairdresser" but idk
    "fluffy",
    "inn catgirl brothel fluffy",
    "catgirl brothel fluffy",
    "chattenoire",
    "inn catgirl brothel chattenoire",
    "catgirl brothel chattenoire",
    "lupa",
    "story lupa",
    "lupa story",
    "mimic",
    "dryad",
    "cultist",
    "merrybelle",
    "nurse", #I think u dont need her at all, but eh
    "cherry nurse",
    "tavern gloryhole",
    "evoker",
    "alraune", # dont need that one 99% sure
    "wereslut",
    "feral wereslut",
    "harpy",
    "elite harpy",
    "slime",
    "brigand",
    "centaur",
    "unicorn",
    "goblin",
    "goblin (male)",
    "orc",
    "adventurer",
    "trudy",
    "ogre",
    "beast mistress",
    "arachne",
    "golem",
    "ghost",
    "puca",
    "naga",
    "quetzal",
    "quetzal goddess",
    "mermaid",
    "warlock",
    "giantess",
    "Dullahan",
    "wasp",
    "doppelganger",
    "persephone",
    "helena",
    "minotauress",
    "fire elemental",
    "ettin",
    "jester",
    "dark knight",
    "tentacle witch",
    "demon king",
    "town", #????
    "Kitsune",
    #the only three exeption for now. I just could not make OCR recognise "0", so I making it like that. Cheesy but works
    "town square 0",
    "sperm bank milkshake 0",
    "forage 0",
]

def add_names(data):
    TARGET_SECTIONS = [
        "enemyKnowledge",
        "events",
        "cgSeen",
        "animatedCgSeen"
    ]

    MARKER = "__ADDED_BY_SCRIPT__"

    for section_name in TARGET_SECTIONS:
        if section_name not in data:
            continue
        section = data[section_name]
        if MARKER not in section:
            section[MARKER] = 1
        for name in NAMES:
            name = " ".join(name.split())
            title_case = name.title()
            variants = {
                name.upper().replace(" ", "_"),
                name.upper().replace(" ", "-"),
                name.lower().replace(" ", "_"),
                name.lower().replace(" ", "-"),
                title_case,
            }
            for variant in variants:
                if variant not in section:
                    section[variant] = 1
                    print(f"Added in the Pervert section: {variant}") 

add_names(data)

#finishing

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Finished!")

