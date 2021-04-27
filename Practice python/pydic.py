# pip install pydictionary
from PyDictionary import PyDictionary
# Author = TECH_IN_SECONDS

def dic(word):
    dictionary=PyDictionary()
    mean = dictionary.meaning(word)
    ac, vc, nc = 1,1,1
    full_sentense = ""
    if str(dictionary.meaning(word))!="None":
        try:
            full_sentense = full_sentense + "Noun :"
            for noun in mean["Noun"]:
                full_sentense = full_sentense + "\n"+ str(nc)+") "+noun
                nc = nc + 1
            full_sentense = full_sentense + "\n"
        except:
            full_sentense = full_sentense + "\n"
        try:
            full_sentense = full_sentense + "\n"+ "Adjective :"
            for ad in mean["Adjective"]:
                full_sentense = full_sentense + "\n"+ str(ac)+") "+ad
                ac = ac + 1
            full_sentense = full_sentense + "\n"
        except:
            full_sentense = full_sentense + "\n"
        try:
            full_sentense = full_sentense + "\n"+ "Verb :"
            for verb in mean["Verb"]:
                full_sentense = full_sentense + "\n"+ str(vc)+") "+verb
                vc = vc + 1
            full_sentense = full_sentense + "\n"
        except:
            full_sentense = full_sentense + "\n"
        return(full_sentense)
    else:
        return(f"\"{word}\" \nWord not Found")

print(dic(input("Enter a word = ")))


# Enter a word = light
# Noun :
# 1) (physics
# 2) any device serving as a source of illumination
# 3) a particular perspective or aspect of a situation
# 4) the quality of being luminous; emitting or reflecting light
# 5) an illuminated area
# 6) a condition of spiritual awareness; divine illumination
# 7) the visual effect of illumination on objects or scenes as created in pictures
# 8) a person regarded very fondly
# 9) having abundant light or illumination
# 10) mental understanding as an enlightening experience
# 11) merriment expressed by a brightness or gleam or animation of countenance
# 12) public awareness
# 13) a divine presence believed by Quakers to enlighten and guide the soul
# 14) a visual warning signal
# 15) a device for lighting or igniting fuel or charges or fires

# Adjective :
# 1) of comparatively little physical weight or density
# 2) (used of color
# 3) of the military or industry; using (or being
# 4) not great in degree or quantity or number
# 5) psychologically light; especially free from sadness or troubles
# 6) characterized by or emitting light
# 7) (used of vowels or syllables
# 8) easily assimilated in the alimentary canal; not rich or heavily seasoned
# 9) (used of soil
# 10) (of sound or color
# 11) moving easily and quickly; nimble
# 12) demanding little effort; not burdensome
# 13) of little intensity or power or force
# 14) (physics, chemistry
# 15) weak and likely to lose consciousness
# 16) very thin and insubstantial
# 17) marked by temperance in indulgence
# 18) less than the correct or legal or full amount often deliberately so
# 19) having little importance
# 20) intended primarily as entertainment; not serious or profound
# 21) silly or trivial
# 22) designed for ease of movement or to carry little weight
# 23) having relatively few calories
# 24) or lite
# 25) or light
# 26) (of sleep
# 27) casual and unrestrained in sexual behavior
# 28) or light

# Verb :
# 1) make lighter or brighter
# 2) begin to smoke
# 3) to come to rest, settle
# 4) cause to start burning; subject to fire or great heat
# 5) fall to somebody by assignment or lot
# 6) alight from (a horse
# 7) start or maintain a fire in