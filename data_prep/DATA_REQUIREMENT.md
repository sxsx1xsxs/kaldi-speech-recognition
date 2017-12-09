DATA REQUIREMENT 

tools to use to check whether valid or not:
utils/validate_data_dir.sh

usage: utils/validate_data_dir.sh --option data_directory (details please look at utils/validate_data_dir.sh)


required files:
1. text
2. segments
3. utt2spk
4. spk2utt
5. wav.scp


optinal:
1. utt2dur
2. reco2file_and_channel

format:
1.text
every line: utterance_id utterance

2.segments
every line: utterance_id speaker_id start_time end_time

3.utt2spk
every line: utterance_id speaker_id

4.spk2utt
every line: speaker_id utt_id_1 utt_id_2 utt_id_3 utt_id_4 ...

5.wav.scp:
speaker_id path_to_audio_file/ways_to_get_corresponding_audio_file



script examples can be found in local/prepare_data.sh



Text --> segment
segment --> utt2spk
utt2spk --> spk2utt
wav.scp 