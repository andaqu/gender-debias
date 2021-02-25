import xml.etree.ElementTree as xml
from tqdm import tqdm
import convert
import pickle 
import os
import re

# dataset creation and split script, taking the original dataset and formating it to our need
name = "original"
path = "dataset/dataset-raw"
folders = ["parliament", "news", "academic", "culture", "law", "religion", "sport"]

re1 = re.compile("&")
re2 = re.compile("\n")
re3 = re.compile("\t[^\s*]*")
re4 = re.compile("[^\s]*\t[^\s]*\t")

for folder in folders:

    print(f"Reading {folder}...")
    for file in os.listdir(f"{path}/{folder}"):

        with open(f"{path}/{folder}/{file}", "r", encoding="utf8") as f:
            s = f"<root>{f.read()}</root>"

        # Remove '&', else it doesn't get recognised as XML
        s = re1.sub("", s) 

        # Convert maltese letters to english equivalents
        s = convert.maltese_to_english(s)

        # Initialise XML library
        tree = xml.ElementTree(xml.fromstring(s))
        root = tree.getroot()

        # List of sentences in file
        sentences = []
        
        for paragraph in tqdm(root.iter("text")):     

            for s in paragraph.iter("s"):
                
                sentence = s.text[1:]

                # Extra regex expression if taking lemmatised word
                if name == "original": sentence = re3.sub("", re2.sub(" ",  sentence))
                elif: sentence = re3.sub("", re4.sub("", re2.sub(" ",  sentence)))

                sentences.append(sentence)

        with open(f"dataset/dataset-{name}/{file}", "w", encoding="utf8") as f:
            for sentence in sentences:
                f.write("%s\n" % sentence)