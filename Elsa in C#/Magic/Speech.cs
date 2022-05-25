using System.Speech.Synthesis;

namespace MagicC
{
    public static  class Speech
    {
        public static void Speak(string textToSpeak)
        {
            // Initialize a new instance of the SpeechSynthesizer.  
#pragma warning disable CA1416 // Validate platform compatibility
            using SpeechSynthesizer synth = new();
#pragma warning restore CA1416 // Validate platform compatibility

            // Configure the audio output.
            
#pragma warning disable CA1416 // Validate platform compatibility
            synth.SelectVoice(synth.GetInstalledVoices()[1].VoiceInfo.Name);
#pragma warning restore CA1416 // Validate platform compatibility
#pragma warning disable CA1416 // Validate platform compatibility
            synth.SetOutputToDefaultAudioDevice();
#pragma warning restore CA1416 // Validate platform compatibility

            // Speak a string.  
#pragma warning disable CA1416 // Validate platform compatibility
            synth.Speak(textToSpeak);
#pragma warning restore CA1416 // Validate platform compatibility
        }
    }
}
