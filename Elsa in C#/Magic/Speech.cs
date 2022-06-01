using System.Speech.Synthesis;

namespace Magic;

public static  class Speech
{
    public static void Speak(string textToSpeak)
    {
        // Initialize a new instance of the SpeechSynthesizer.  
        using SpeechSynthesizer synth = new();

        // Configure the audio output.

        synth.SelectVoice(synth.GetInstalledVoices()[1].VoiceInfo.Name);
        synth.SetOutputToDefaultAudioDevice();

        // Speak a string.  
        synth.Speak(textToSpeak);
    }
}