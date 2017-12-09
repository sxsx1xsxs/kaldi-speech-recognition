def main():
    # read utt2spk file
    file_input = open('utt2spk', 'r')
    file_output = open('wav.scp', 'w')

    # use dict to store speaker and file path
    spk2file = {}

    for line in file_input.readlines():
        line_split = line.split(' ')
        spk = line_split[0]
        spk = spk.split('-')[0] + '-' + spk.split('-')[1]
        corresponding_file = '\sph\\' + spk.split('_')[3] + '_' + spk.split('_')[4] + '\\' + spk.split('-')[0] + '.sph'

        # to check whether there is duplicate in speakers
        if spk2file.has_key(spk):
            if spk2file[spk] != corresponding_file:
                print spk2file[spk] + ' is different from ' + corresponding_file
        else:
            spk2file[spk] = corresponding_file

    # write results to output file
    for k in spk2file:
        file_output.write(k + ' sph2pipe -f wav -p ' + spk2file[k] + ' |\n')


if __name__ == '__main__':
    main()
