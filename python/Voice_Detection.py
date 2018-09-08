import pyaudio
import wave
import webrtcvad

CHUNK = 160
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "pranav_recording.wav"

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
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        if (vad.is_speech(data, RATE)):
            print('Contains speech:' + str(i))
            only_voice_frames.append(data)

    print("Done recording")
    print(frames)
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    main()