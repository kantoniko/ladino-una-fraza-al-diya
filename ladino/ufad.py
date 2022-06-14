import csv
import os
import re

def ufad():
    filename = 'una-fraze-al-dia_lad-tur-eng-spa.csv'
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(root, filename)
    #print(filepath)

    audios = os.listdir(os.path.join(root, 'audio'))
    #print(audios)
    #audios_lower_case = [name.lower() for name in audios]
    #print(audios_lower_case)
    #audio_numbers = [re.search(r'^[0-9.]+', name).group(0) for name in audios_lower_case]
    #print(audio_numbers)
    #print(len(audio_numbers))
    #print(sorted(audio_numbers))
    #print(len(set(audio_numbers)))
    #an = set()
    #for x in audio_numbers:
    #   if x in an:
    #        print(x)
    #   an.add(x)
    #audios_no_ext = [name[0:-4] for name in audios_lower_case]
    #assert len(audios_no_ext) == len(set(audios_no_ext))


    with open(filepath) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        entries = []
        jpegs = []
        for row in rd:
            if row['filename'] == 'EXTRAS':
                break
            if row['audio'] in audios:
                entries.append(row)
            #jpegs.append(row['filename'][0:-5].lower())
            #print(row)
            #row['filename']
            # TODO where are the images ? Can we get those too?
    #assert len(audios_no_ext) == len(jpegs)
    #print(jpegs)
    #print(len(set(audios_no_ext) - set(jpegs)))

    return(entries)

if __name__ == '__main__':
    ufad()

