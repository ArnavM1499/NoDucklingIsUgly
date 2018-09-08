import pyaudio
import wave
import webrtcvad

CHUNK = 160
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "recording {wav_file_num}.wav"

def main():
    p = pyaudio.PyAudio()
    vad = webrtcvad.Vad()
    vad.set_mode(3)

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Recording")

    frames = []
    only_voice_frames = []
    silent_frames = 0
    wav_file_num = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        if (vad.is_speech(data, RATE)):
            print('Contains speech:' + str(i))
            only_voice_frames.append(data)
            silent_frames = 0
        else:
            silent_frames += 1
        if silent_frames >= 100:
            print("100 frames of silence detected, writing frames so far to new wav file: ", WAVE_OUTPUT_FILENAME.format(wav_file_num=wav_file_num))
            wf = wave.open(WAVE_OUTPUT_FILENAME.format(wav_file_num=wav_file_num), 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(only_voice_frames))
            wf.close()
            only_voice_frames = []
            silent_frames = 0
            wav_file_num += 1


    print("Done recording")
    print(frames)
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME.format(wav_file_num=wav_file_num), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(only_voice_frames))
    wf.close()

if __name__ == "__main__":
    main()