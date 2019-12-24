## Language Learning

### Goal - Build app that associates words with images to facilitate memorization

Example:

Japanese - Ohayou - Good morning

User inputs a name based on pronounciation

Ohayou: sounds like **Ohio**

Program generates based on following inputs:

- English translation
- User input 

User should also provide type of info, such as:

- Noun/Verb/Adjective
- Verb tense (if verb)

Program uses templates to autofill data.  For example:

Program has a template of:

The people of (Location) say (Expression) to each other

Our program has this information

- English translation: Good morning
- Type : Expression

Our user provides this information

- Sounds like: Ohio
- Type: Location

The program autofills this data:

The people of **Ohio** say **Good Morning** to each other.

Ideally, there should be several templates so that if something doesn't make 
sense, the user can choose another option.

![ohio](img/ohio.png)

### Files used:

- csv file containing 20 japanese words with english meanings.
  (dataSample.csv)

The key value store should look like this:
(japaneseWord:englishMeaning:type:soundslike:soundslikeType)

Program displays ichi and one. Stores 'number1' as property for template (singular)
User inputs "itchy" as word link.  Need to store
User inputs "adjective" as word link type. Need to store
New store looks like this
(ichi:one:number1):(itchy:one:adjective)
Program looks for template based on (number1) and (adjective)
This (number1) coat is really (adjective)
Returns:
This (one) coat is really (itchy)

Part 2:
Go to next value. The key value store should look like this:
(ni:two:number)
Program displays ni and two. Stores 'number' as property for template (plural)
User inputs "knee" as word link. Need to store
User inputs "noun" as word link type.  Need to store.
New store looks like this:
(ni:two:number):(knee:two:noun)
Program looks for template based on (number) and (noun)
These (number) (noun) are very heavy
Returns:
These two knee are very heavy
This doesn't really work.  But lets say we had six (roku) and rock
These six rock are very heavy
This works better.  User can modify and save output so it makes sense
These six rocks are very heavy
Back to two. We can find a new template:
We found (number) (noun) on the beach
We found two knee on the beach
Still doesn't make sense. But the user can change the input.
We found two knees on the skeleton
So the user can be prompted by the output enough to customize and save the
generated text.