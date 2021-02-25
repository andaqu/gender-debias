# calculates bias as proposed by  Caliskan et al. (2017): Word Embedding Association Test (WEAT)
# given some word vector and two sets, it calculates the association between them
# the larger the bias, the stronger its association with the gender concepts
def sum(wv, A):
    r = 0
    for a in A:
        av = E.v(a)
        r += av.dot(wv)
    return r

def s(wv, M, F):
    return sum(wv, M) - sum(wv, F)

def b(w, M, F):
    wm = E.v(w[0])
    wf = E.v(w[1])
    return abs(abs(s(wm, M, F)) - abs(s(wf, M, F)))

def calculate_bias(embedding, M, F, key_words):
    bias = {}
    global E
    E = embedding
    for w in key_words:
        try:
            wm = E.v(w[0])
            wf = E.v(w[1])
            bias[f"{w[0]} / {w[1]}"] = b(w, M, F)
        except KeyError:
            continue
    return bias

E = None