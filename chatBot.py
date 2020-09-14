import nltk
from nltk.chat.util import Chat, reflections

reflections

set_pairs = [
    [

        "UKIMWI ni nini?|nini maana ya UKIMWI?|ukimwi|ukimwi nini|maana ya UKIMWI",
        ["Ni upungufu wa kinga mwilini",]
            
    ],
    [
        r"VVU ni nini?|vvu|nini maana ya vvu?|maana ya VVU",
        ["Ni virusi vinavyosababisha ukimwi",]
    ], 
    [
        "uambukizwaji wa ukimwi|uambukizwaji|njia za kuambukiza ukimwi|unaambukizwaji| " +
        "kinachoambukiza|nini kinaambukiza|njia za uambukizaji|namna ya uambukizwaji",
        ["1. Ngono zembe. \n2. kuongezewa damu. \n3. Mama kwenda kwa mtoto. ",]
    ],
    [
        r"njia za kujikinga|kujikinga|kuikinga na ukimwi|kinga|kinga ya ukimwi|" +
        "jinsi ya kujikinga na ukimwi",
        ["1. kutumia CONDOM \n2. kutumia mafuta ya ukeni \n3. Tohara \n"
         "4. Mawaidha na elimu n5. dawa kabla na baada ya hatari \n6. Dawa ya" + 
         "kudhabiti ukimwi \n7. Tiba mbadala",]
    ],
    [
        r"Ondoka|maliza|funga|mwisho",
    ["Karibu tena! Chukua tahadhari UKIMWI upo na unaua!"]
],
]

 
def chatbot():
    print("\n")
    print("HABARI KARIBU KWENYE GUMZO LA UKIMWI.") 
    print("_____________________________________ \n")
    print("ULIZA CHOCHOTE KUHUSU UKIMWI. \n")

chatbot()
chat = Chat(set_pairs, reflections)
"""print(chat)"""

chat.converse()
if __name__ == "__main__":
    chatbot()
    
     

        


