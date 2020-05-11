import random


class InsultGenerator:
    a_list = ['a confoundedly', 'a conspicuously', 'a cruelly', 'a deucedly', 'a devilishly', 'a dreadfully',
              'a frightfully',
              'a grievously', 'a lamentably', 'a miserably', 'a monstrously', 'a piteously', 'a precociously',
              'a preposterously', 'a shockingly', 'a sickly', 'a wickedly', 'a woefully', 'an abominably',
              'an egregiously',
              'an incalculably', 'an indescribably', 'an ineffably', 'an irredeemably', 'an outrageously',
              'an unconscionably',
              'an unequivocally', 'an unutterably']
    b_list = ['appalling', 'babbling', 'backward', 'bantering', 'blabbering', 'blighted', 'boorish', 'contemptible',
              'corpulent', 'cretinous', 'debauched', 'decadent', 'demented', 'depraved', 'detestable', 'dissolute',
              'execrable', 'fiendish', 'foolish', 'foul', 'gluttonous', 'grotesque', 'gruesome', 'hermaphroditic',
              'hideous', 'ignominious', 'ignorant', 'ill-bred', 'ill-mannered', 'incompetent', 'incorrigible',
              'indecent',
              'inept', 'insignificant', 'insufferable', 'insufferable', 'lascivious', 'lecherous', 'licentious',
              'loathsome', 'maladjusted', 'malignant', 'minuscule', 'miserable', 'myopic', 'naive', 'narcissistic',
              'non-intuitive', 'obese', 'obtuse', 'offensive', 'parasitic', 'pedestrian', 'perverted', 'petty',
              'primitive',
              'promiscuous', 'reprehensible', 'repugnant', 'repulsive', 'revolting', 'salacious', 'subliterate',
              'sybaritic', 'uncivilized', 'uncouth', 'unseemly', 'unsightly', 'vile', 'vulgar', 'witless']
    c_list = ['barbarian', 'cannibal', 'coccydynia', 'cretin', 'degenerate', 'delinquent', 'derelict', 'dingleberry',
              'dolt', 'dullard', 'dunce', 'fiend', 'filcher', 'glutton', 'half-wit', 'heathen', 'hemorrhoid', 'idiot',
              'ignoramus', 'imbecile', 'lackey', 'lecher', 'libertine', 'loafer', 'lout', 'malefactor', 'menace',
              'microphallus', 'miscreant', 'misdemeanant', 'moron', 'narcissist', 'neanderthal', 'nincompoop', 'ninny',
              'nose picker', 'oaf', 'onanist', 'parasite', 'peon', 'pervert', 'pick pocket', 'plebeian', 'polisson',
              'prostitute', 'rapscallion', 'reprobate', 'reprobate', 'reptile', 'rogue', 'ruffian', 'scoundrel',
              'simpleton', 'slattern', 'sphincter', 'subhuman', 'swine', 'sycophant', 'sycophant', 'troglodyte',
              'trollop',
              'twit', 'varmint', 'vermin', 'wretch']
    d_list = ['belligerent', 'catatonic', 'corrupt', 'dastardly', 'debased', 'debauched', 'decadent', 'decrepit',
              'degenerate', 'demented', 'deplorable', 'depraved', 'disgusting', 'fecal', 'feculent', 'fiendish',
              'flaccid',
              'flagitious', 'flagrant', 'frightful', 'gaudy', 'glaring', 'gluttonous', 'gross', 'grotesque', 'heinous',
              'hopeless', 'horribly atrocious', 'infamous', 'loathsome', 'ludicrous', 'maladjusted', 'malingering',
              'malingering', 'malodorous', 'maniacal', 'maniacal', 'masturbatory', 'miscreant', 'miserable',
              'monstrous',
              'myopic', 'myopic', 'naive', 'narcissistic', 'narcissistic', 'nefarious', 'nefarious', 'outrageous',
              'perverse', 'perverted', 'petty', 'preposterous', 'preposterous', 'primitive', 'primitive', 'putrid',
              'putrid', 'rank', 'reprehensible', 'repugnant', 'revolting', 'rotten', 'vacuous', 'vapid', 'villainous',
              'wearisome']
    e_list = ['acidly acrimonious', 'air-polluting', 'all-befouling', 'all-defiling', 'armpit-licking',
              'blood-curdling',
              'blood-freezing', 'bug-eyed', 'buttock-rimming', 'cantankerously-caterwauling', 'chromosome deficient',
              'chronically flatulent', 'cold-hearted', 'coma-inducing', 'congenitally clueless', 'dandruff-eating',
              'disease-ridden', 'dull-witted', 'enema-addicted', 'feces-collecting', 'feeble-minded', 'flea-infested',
              'flesh-creeping', 'foul-smelling', 'gossip-mongering', 'grudge-festering', 'halitosis-infested',
              'heart-sickening', 'Internet-addicted', 'irredeemably boring', 'maliciously malodorous',
              'mattress-soiling',
              'monotonous solitaire playing', 'mucous-eating', 'nose-picking', 'nostril-offending',
              'odiously suffocating',
              'one dimensional', 'orgasm faking', 'scruffy-looking', 'sheep-molesting', 'simple-minded', 'small-minded',
              'snake-eyed', 'sock-sucking', 'soul-destroying', 'stench-emitting', 'thick-headed', 'toe-sucking',
              'urine-reeking']
    f_list = ['aberration of nature', 'abomination of humanity', 'abomination to all the senses',
              'abomination to all the senses', 'acrid smog of oppressively caustic oral effluvium',
              'amalgamation of loathsome repulsiveness', 'arbitrary dereliction of genetics',
              'assault on the ocular senses', 'black hole of soul-destroying, coma-inducing dullness',
              'blight upon society', 'buggering buttock bandit', 'cacophonous catastrophe',
              'cesspool of putrid effluvium',
              'cesspool of sub-human filth', 'cheap Internet loiterer', 'chromosome-deficient test tube experiment',
              'conglomerate of intellectual constipation', 'conglomerate of intellectual constipation',
              'corporate bowel movement', 'delinquent who has delusions of adequacy', 'deplorable calamity of birth',
              'depraved orgy of subhuman indecency', 'depravity of genetics', 'display of indecency',
              'dreg of the Internet', 'derelict whose birth certificate is an apology from the condom factory',
              'derelict whose birth certificate is an apology from the condom factory',
              'evangelical crusader of sub-mediocrity', 'evangelical crusader of sub-mediocrity',
              'excrement stain on a Sumo Wrestler\'s underpants', 'glob of grease', 'grotesque visual experience',
              'grudge-festering haggard', 'gruesome vista to all eyes assaulted by the sight of you',
              'hysterical mass of warbling inanity',
              'lamentable mistake by your parent\'s reckless exchange of genetic material',
              'malfunctioning little twerp',
              'offensively uninspired malodorous half-wit', 'malodorous marinade of sweat and fear',
              'manifestation of contraceptive personality', 'mass of existential impotence',
              'mass of loathsome repulsiveness', 'mass of neuroses and complexes', 'mass of neuroses and pathologies',
              'mean-spirited poltroon', 'mediocrity-afflicted neophyte with glacially slow cognitive faculties',
              'menace to, not only society, but all living creatures',
              'mental midget with the natural grace of an intoxicated beluga whale', 'molester of small furry animals',
              'moving stench of leprosy', 'mutilation of decency', 'nauseating assault on the senses',
              'nefarious vermin',
              'obfuscation of all that is good', 'object of execration', 'ocular depravity to all of discrimination',
              'odious leach-covered blob of quivering slime', 'offense to all of good taste and decency',
              'oppressive orgy of perversion', 'orgy of indecency', 'orgy of indignity',
              'parasite on the state\'s resources', 'personification of vulgarity', 'pitiful sideshow freak',
              'plague upon humanity', 'plot-less melodrama of uneventful life',
              'plot-less melodrama of uneventful life',
              'practitioner of non-consentual bestiality', 'proof that evolution can go in reverse',
              'proof that test tube experiments can go horribly wrong', 'pulp of stultifying inanity',
              'putrid waste of flesh', 'repulsive polisson', 'sadistic hippophilic necrophile',
              'shameless exhibition of genetic deficiency', 'shameless exhibition of genetic deficiency',
              'spawn of a mad scientist and a disastrous test tube experiment',
              'sub-literate simple minded mental midget',
              'sub-literate simple minded mental midget', 'tainted spawn of a syphilitic swamp rat',
              'tasteless amalgam of dross', 'unfortunate occurrence of unprotected intercourse',
              'unspeakably offensive barbarian', 'vulgarity to all and sundry',
              'wretched horror to all who encounter you']
    name = ""

    def __init__(self, name):
        self.name = name

    def get_insult(self):
        return f"{self.name} is {random.choice(self.a_list)} {random.choice(self.b_list)} {random.choice(self.c_list)}" \
               f" and a {random.choice(self.d_list)} {random.choice(self.e_list)} {random.choice(self.f_list)}"


if __name__ == '__main__':
    ig = InsultGenerator("Hari")
    print(ig.get_insult())
