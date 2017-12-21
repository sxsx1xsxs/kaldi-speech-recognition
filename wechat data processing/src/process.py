


# encoding: utf-8
import jieba
import os
import re
end_punctuations = re.compile("[。？！~]")
def cut_sentence(input_str):
    sentence_list = end_punctuations.split(input_str)
    # for s in sentence_list:
    # 	print(s)
    return sentence_list
output_file_path = "output_seg_fulljson.aa.txt"
if os.path.exists(output_file_path):
    os.remove(output_file_path)
output_file = open(output_file_path, mode="a")
input_str = open("data/output.aa", encoding="utf8").read()
sentences = cut_sentence(input_str)
punctuations = re.compile("[，。《》（）“”？~！‘’]")
for sentence in sentences:
    trimed_str = punctuations.sub("", sentence).strip()
    if not trimed_str:
        continue
    word_list = jieba.cut(trimed_str)
    line = " ".join(word_list)
    output_file.write(line + "\n")