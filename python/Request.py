import requests
import cognitive_sr
import io

def recognize_speaker(wav_data):
    people = {
        '00000000-0000-0000-0000-000000000000' : 'No Match',
        '2338f519-b782-4756-b0be-557fa731f1bf' : 'Pranav',
        '818a16b4-8068-418a-88b5-d9f45a803e93' : 'Saiyan',
        'b468f3aa-e303-4290-95ff-68a74524900e' : 'Jhosh' 
    }
    subscription_key = '38ca07d3e98a41889877dca1a68c884d'

    # Create a new profile
    speech_identification = cognitive_sr.SpeechIdentification(subscription_key)
    # result = speech_identification.create_profile()
    # print(result)
    profile_id = 'b468f3aa-e303-4290-95ff-68a74524900e'
    # Pranav - 2338f519-b782-4756-b0be-557fa731f1bf
    # Sayan - 818a16b4-8068-418a-88b5-d9f45a803e93
    # Daddy Jhosh - b468f3aa-e303-4290-95ff-68a74524900e

    profile_ids = ['b468f3aa-e303-4290-95ff-68a74524900e', '2338f519-b782-4756-b0be-557fa731f1bf', '818a16b4-8068-418a-88b5-d9f45a803e93']
    wav_path = 'pranav_recording.wav'
    # with io.open(wav_path, 'rb') as wav_file:
    #     wav_data = wav_file.read()
    # result = speech_identification.enroll_profile(profile_id, wav_data)
    # result = speech_identification.delete_profile(profile_id)
    result = speech_identification.identify_profile(profile_ids, wav_data, short_audio=True)
    # result = speech_identification.get_profile(profile_id)
    # profiles = speech_identification.get_all_profiles()
    # print(profiles)
    # print("Done")
    # print(result)
    if 'identifiedProfileId' in result.keys():
        print(people[result['identifiedProfileId']], result['confidence'])
    else:
        print("Pranav Normal Default")