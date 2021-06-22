from googletrans import Translator

print("Çıkış yapmak için q yazmanız yeterlidir. :)")
word = input("Çevirmek istediğiniz kelime nedir...\n> ")
print("Hangi dile çevirmek istiyorsunuz... \nÇevirebildiğimiz Diller: \nTürkçe \nIngilizce \nAlmanca \nFransızca \nItalyanca \nArapça \nIspanyolca \nJaponca \nRusça \nIsveççe \nPortekizce")
language = input(">")

language = language.lower()

languages_codes = {
    "türkçe" : "tr",
    "ingilizce" : "en",
    "almanca" : "de",
    "fransızca" : "fr",
    "italyanca" : "it",
    "arapça" : "ar",
    "ispanyolca" : "es",
    "japonca" : "ja",
    "rusça" : "ru",
    "isveçce" : "sv",
    "portekizce" : "pt"
}
def translate():
     for i in languages_codes.keys():
        print(i)
        if language == i:
            translator = Translator()
            result = translator.translate(word,dest=f"{languages_codes[i]}")
            print(f"Kelimenin türkçesi : {result.text}\n")
            break

if word == "q" or language == "q":
    quit()
else:
   translate()