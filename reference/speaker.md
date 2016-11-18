## Speaker

Derived from [Device](device.md).

```
Speaker {
}
```

### Description

The [Speaker](#speaker) node represents a loudspeaker device that can be embbeded onboard a robot or standing in the environment. It can be used to play sounds and perform text-to-speech from the controller API.

### Speaker Functions

**Name**

**wb\_speaker\_play\_sound** - *plays a sound*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

```c
#include <webots/speaker.h>

void wb_speaker_play_sound(WbDeviceTag left, WbDeviceTag right, const char *sound, double volume, double pitch, double balance, bool loop);
```

**Description**

This function allows the user to play a sound file. Currently only wave files are supported. The function takes as arguments two speaker `WbDeviceTag` respectively for the left and right channels. If both channels should be played on the same speaker or the file has only one channel, it is possible to pass the same device tag for both left and right arguments. Alternatively, if one channel should be ignored, it is possible to pass `0` instead of one of the two tags.

The `sound` argument specifies the path to the wave file that should be played. The `volume` argument allows the user to specify the volume of this sound (between 0.0 and 1.0). The `pitch` argument allows the user to modify the pitch of the sound, the default sound pitch is multiplied by the pitch argument. The `pitch` argument should be positive. A value of 1.0 means no pitch change. The `balance` argument allows the user to specify the balance between the left and the right speaker (between -1.0 and 1.0). A value of 0 means no balance: both channels have the same volume. A value of -1.0 means that the right channel is muted. A value of 1.0 means that the left channel is muted. Intermediate values define a difference of volume between the left and right channels. Finally, the boolean `loop` argument defines if the sound will be played only once or repeatedly.

It is possible to change the volume, pitch, balance, and loop parameters of a sound currently playing by calling again the `wb_speaker_play_sound` function with the same speakers and `sound` arguments.

> **Note**:
The path to the sound file should be defined either absolutely or relatively. If defined relatively, it will be searched first relatively to the robot controller folder. If not found there and if the robot is a PROTO, it will be searched relatively to the PROTO folder of the robot.

---

**Name**

**wb\_speaker\_stop** - *stops the speaker*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

```c
#include <webots/speaker.h>

void wb_speaker_stop(WbDeviceTag tag, const char *sound);
```

**Description**

This function stops a specific sound. The `sound` argument is the path to an audio file currently playing in the speaker. It should be the same path as the one previously provided to the `wb_speaker_play_sound` function.

It is possible to stop all the sounds currently playing in a speaker by setting `sound` to `NULL`.

---

**Name**

**wb\_speaker\_set\_language**, **wb\_speaker\_get\_language**, **wb\_speaker\_speak** - *perform text-to-speech*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

```c
#include <webots/speaker.h>

void wb_speaker_set_language(WbDeviceTag tag, const char *language);
const char * wb_speaker_get_language(WbDeviceTag tag);
void wb_speaker_speak(WbDeviceTag tag, const char *text, double volume);
```

**Description**

The `wb_speaker_set_language` function allows the user to set the language of the text-to-speech engine. The `language` parameter should be set to one of the following values:

  - `"en-US"` for American English (default value)
  - `"en-UK"` for British English
  - `"de-DE"` for German
  - `"es-ES"` for Spanish
  - `"fr-FR"` for French
  - `"it-IT"` for Italian

The `wb_speaker_get_language` function allows the user to get the language of the text-to-speech.

The `wb_speaker_speak` function allows the user to execute text-to-speech on the speaker. The value of the `text` parameter is converted into sound by Webots using the language specified by the `wb_speaker_set_language` function. The resulting sound is played through the speaker. The specified text could be plain text including punctuation signs such as "Hello world!", or can be enriched with special effects to make it more realistic. Such effects are speficied with XML tags.

**Text-to-speech XML tags**

- `ignore`: A text portion marked by `<ignore> ... </ignore>` is fully ignored by the synthesis. Ignored sections may be nested. Example:

    ```xml
Hello <ignore> any text </ignore> Mister Smith.
    ```

    This example is equivalent to sending "Hello Mister Smith." to the text-to-speech engine.

- `p` of `paragraph`: Paragraph structures can be marked by `<p> ... </p>` or its extended form `<paragraph> ... </paragraph>`. In most cases, Webots automatically detects paragraph structures. The `<p>` tag can be used to enforce the setting of a paragraph structure. Example:

    ```xml
 <p> This is a paragraph. </p>
    ```

    In this example, the enclosed text is structured as a paragraph.

- `s` of `sentence`: Sentence structures can be marked by `<s> ... </s>` or its extended form `<sentence>... </sentence>`. In most cases, Webots automatically detects sentence structures. The `<s>` tag can be used to enforce the setting of a sentence structure. Example:

    ```xml
<s> This is a sentence. </s>
    ```

    In this example, the enclosed text is structured as a sentence.

- `pitch`: The markup tag `<pitch level="...">` changes the general pitch level of the specified text portion to the value given by the parameter level. The normal pitch level is 100, the allowed values lie between 50 (one octave lower) and 200 (one octave higher). The end tag `</pitch>` resets the pitch level to 100. Example:

    ```xml
Hello, <pitch level="140"> Miss Jones </pitch> arrived.
    ```

    In this example, the section "Miss Jones" will be produced at a pitch level of a factor of 1.4 higher than normal.

- `speed`: The markup tag `<speed level="...">` changes the general speed level of the specified text portion to the value given by the parameter level. The normal speed level is 100, the allowed values lie between 20 (slowing down by a factor of 5) and 500 (speeding up by a factor of 5). The end tag `</speed>` resets the speed level to 100. Example:

    ```xml
Hello, <speed level="300"> Miss Jones </speed> arrived.
    ```

    In this example, the section "Miss Jones" will be produced by a factor of 3 faster than normal.

- `volume`: The markup tag `<volume level="...">` changes the volume level of the specified text portion to the value given by the parameter level. The normal volume level is 100. Increasing the volume level (values > 100) may result in degraded signal quality due to saturation effects (clipping) and is not recommended. The allowed volume levels lie between 0 (i.e. no audible output) and 500 (increasing the volume by a factor of 5). The end tag `</volume>` resets the volume level to 100. Example:

    ```xml
Hello, Miss <volume level="50"> Jones </volume> arrived.
    ```

    In this example, the volume of the section "Jones" will be decreased by a factor of 2.

- `play`: Using the empty tag `<play file="..."/>` or tag pair `<play file="..."> ... </play>` results in insertion of the specified sound file in the synthesized signal at the place specified in the input text. In the first variant, the sound file is played at the position where the combined tag is set, in the second variant the sound file is played as a substitute of the text between the start and the end tag, that is, the text between the start and the end tag is ignored. The sampling frequency of the input sound file must be identical to the sampling frequency of the synthesized signal. Examples:

    ```xml
Hello, Miss <play file="miller.wav"/>.
Hello, Miss <play file="miller.wav"> Miller </play>.
    ```

    In this example, the "miller.wav" sound file is played instead of pronouncing the "Miller" word using text-to-speech.

- `genfile`: Using the markup section `<genfile file="..."> ... </genfile>` an arbitrary text portion can be saved to a separate sound file. The markup tag `<genfile>` can be used especially for creating synthetic voice prompts. Examples:

    ```xml
<genfile file="intro.wav"> Hello, Mister </genfile>
<genfile file="miller.wav"> Miller, </genfile>
<genfile file="rem.wav"> welcome.</genfile>
Hello, Mister <genfile file="smith.wav"> Smith, </genfile> welcome.
    ```

    In this example, three parts of the first sentence "Hello, Mister Miller, welcome." are saved in separate sound files of type wav, and the part "Smith," of the second sentence is also saved in a separate file. These generated sound files can, for instance, be used to generate a newly combined utterance using the markup tag `<play>`:

    ```xml
<play file="intro.wav"/> <play file="smith.wav"/>
<play file="rem.wav"/>
    ```

    This input "text", which consists only of markup tags, plays the generated sound files as if the (new) sentence "Hello, Mister Smith, welcome." had been synthesized, but, of course, with much less processing time. It is essential to note that the sentence part "Smith," should be synthesized and saved to a sound file in the appropriate sentence environment in order for the newly combined utterance to have a continuous melody and rhythm.
