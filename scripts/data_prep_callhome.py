
import os
import gzip
import io
import re
import string


# remove punctuation
translator = str.maketrans('', '', string.punctuation)

indir = '../data/callhome/LDC96T16-CALLHOME-Mandarin-Chinese-Transcripts/transcrp/'
folder = ['train/', 'devtest/', 'evltest/']
for ds in folder:
    text, segment, utt2spk, spk2utt, scp = [], [], [], [], []
    
    for root, dirs, filenames in os.walk(indir+ds):
        for gzf in filenames:
            if(os.path.join(root, gzf)[-3:] == '.gz'):
                with gzip.open(os.path.join(root, gzf), 'rt', encoding="gb2312") as f:
                    fname = gzf[:-7]
                    spk2utt = {}
                    while f.readline():
                        line = f.readline().strip()

                        if "<" in line:            # remove sentences with other languages
                            continue
                        if "[" in line:            # remove sentences with comments (usually distortion)
                            continue
                        if "{" in line:            # replace speaker made non-word sounds by {nomeaning}
                            line = re.sub(r"\{(.*?)\}", "{nomeaning}", line)

                        s = line.split()
                        if len(s) < 4:
                            continue

                        start = s[0]
                        start_name = start.translate(translator) 
                        end = s[1]
                        end_name = end.translate(translator) 
                        spk = s[2].translate(translator)
                        utt = " ".join(s[3:])

                        spkid = fname + "-" + spk
                        uttid = fname + "-" + start_name + "-" + end_name
                        utt = utt.translate(translator) 

                        text.append(uttid + " " + utt)
                        segment.append(uttid + " " + spkid + " " + start + " " + end)
                        utt2spk.append(uttid + " " + spkid)
                        if spkid not in spk2utt:
                            spk2utt[spkid] = []
                            scp.append(spkid + " " + "sph2pipe -f wav -p " + indir+fname+".sph" + " |")
                        spk2utt[spkid].append(uttid)

                        
    spk2utt_compiled = []
    for spkid in spk2utt.keys():
        spk2utt_compiled.append(spkid + " " + " ".join(spk2utt[spkid]))

    outdir = '../data/callhome/'
    output_files = [["text", text], ["segment", segment], ["utt2spk", utt2spk], ["spk2utt", spk2utt_compiled], ["wav.scp", scp]]                        
    for output_fname, output_data in output_files:
        outfile = open(outdir+ds+output_fname, "w")
        for l in output_data:
            outfile.write("%s\n" % l)
        outfile.close()