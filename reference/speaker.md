## Speaker

Derived from [Device](device.md).

```
Speaker {
field  SFString  language "en-US"  # language used for the text-to-speech
}
```

### Description

The [Speaker](#speaker) node can be used to play sounds and to perform text to speech.

### Field Summary

- `language`: Language used for the text to speech. The following languages are supported: "en-US", "en-UK", "de-DE", "es-ES", "fr-FR", and  "it-IT".

### Text to speach

The [Speaker](#speaker) node provide text to speech functionality, the following language are supported for now:
  - American English
  - British English
  - German
  - Spanish
  - French
  - Italian

The text send to the text to speech is converted in sound by Webots and then played using the speaker. The text can be enriched using tags in order to make it more realistic.

#### Text to speech tags

- `ignore`: A text portion marked by `<ignore> ... </ignore>` is fully ignored by the synthesis. Ignored sections may be nested. Example:
```
Hello <ignore> any text </ignore> Mister Smith.
```
In this example, the input text is synthesized as if it were only the sentence "Hello Mister Smith."

- `p` of `paragraph`: Paragraph structures can be marked by `<p> ... </p>` or its extended form `<paragraph> ... </paragraph>`. In most cases, Webots automatically detects paragraph structures. The `<p>` tag can be used to enforce the setting of a paragraph structure. Example:
```
<p> This is a paragraph. </p>
```
In this example, the enclosed text is structured as a paragraph.

- `s` of `sentence`: Sentence structures can be marked by `<s> ... </s>` or its extended form `<sentence>... </sentence>`. In most cases, Webots automatically detects sentence structures. The `<s>` tag can be used to enforce the setting of a sentence structure. Example:
```
<s> This is a sentence. </s>
```
In this example, the enclosed text is structured as a sentence.

- `pitch`: The markup tag `<pitch level="...">` changes the general pitch level of the specified text portion to the value given as a value of the parameter level. The normal pitch level is 100, the allowed values lie between 50 (one octave lower) and 200 (one octave higher). The end tag `</pitch>` resets the pitch level to 100. Example:
```
Hello, <pitch level="140"> Miss Jones </pitch> arrived.
```
In this example, the section "Miss Jones" will be produced at a pitch level of a factor of 1.4 higher than normal.
The pitch level can be set relative to the current setting by adding a percent character to the level value. E.g. setting the level to "150%" will set the pitch level to 150% of the current value. Allowed percentage values lie between 50% and 200%. Reducing and increasing the pitch level by a percentage is achievable by pre-prending a plus or minus character to the level value. When setting for example the level to "-20%" the current pitch will be reduced by 20%. Allowed percentage change values lie between -50% and +100%.

- `speed`: The markup tag `<speed level="...">` changes the general speed level of the specified text portion to the value given as a value of the parameter level. The normal speed level is 100, the allowed values lie between 20 (slowing down by a factor of 5) and 500 (speeding up by a factor of 5). The end tag `</speed>` resets the speed level to 100. Example:
```
Hello, <speed level="300"> Miss Jones </speed> arrived.
```
In this example, the section "Miss Jones" will be produced by a factor of 3 faster than normal.
As for the pitch markup tag, relative speed levels and percentage changes can be specified using the percent, plus, and minus characters in the level value.

- `volume`: The markup tag `<volume level="...">` changes the volume level of the specified text portion to the value given as a value of the parameter level. The normal volume level is 100. Increasing the volume level (values > 100) may result in degraded signal quality due to saturation effects (clipping) and is not recommended. The allowed volume levels lie between 0 (i.e. no audible output) and 500 (increasing the volume by a factor of 5). The end tag `</volume>` resets the volume level to 100. Example:
```
Hello, Miss <volume level="50"> Jones </volume> arrived.
```
In this example, the volume of the section "Jones" will be decreased by a factor of 2.
As for the pitch markup tag, relative volume levels and percentage changes can be specified using the percent, plus, and minus characters in the level value.

- `play`: Using the empty tag `<play file="..."/>` or tag pair `<play file="..."> ... </play>` results in insertion of the specified sound file or intermediate synthesis units in the synthesized signal at the place specified in the input text. In the first variant, the sound file is played at the position where the combined tag is set, in the second variant the sound file is played as a substitute of the text between the start and the end tag, that is, the text between the start and the end tag is ignored. The sampling frequency of the input sound file or the intermediate synthesis units file must be identical to the sampling frequency of the synthesized signal. Examples:
```
Hello, Miss <play file="miller.wav"/>.
Hello, Miss <play file="miller.wav"> Miller </play>.
```
If `<play>` is used as part of a longer sentence, the use of the markup section `<usesig>` might be more appropriate in order to produce a better sentence melody.
The volume of the played sound file or intermediate synthesis units file are modified within volume markup sections. The pitch and speed of intermediate synthesis units files are modified within pitch and speed markup sections, but sound files will always be played with their original pitch and speed.

- `usesig`: The markup tags `<usesig file="...">` and `</usesig>` are similar to the tags `</playfile="...">` and `</play>`, that is, the text enclosed between the start and the end tag is replaced by the specified sound or intermediate synthesis units file. There is, however, an important difference to the use of `<play>`: the orthographic text enclosed in the `<usesig>` section is used to interpret the entire sentence as if the `<usesig>` markup tags were not present. The contextual interpretation of the entire sentence determines the prosody (melody and rhythm) and in some cases even the pronunciation (the choice of phones) of the words. Example:
```
<usesig file="intro.wav"> Hello, Mister </usesig> Smith,
<usesig file="rem.wav"> welcome. </usesig>
```
In this example, the sound files `intro.wav` and `rem.wav` are played instead of synthesizing the text portions "Hello, Mister" and "welcome." The prosody (melody and rhythm) of the word "Smith, " is, however, generated as if the entire sentence "Hello, Mister Smith, welcome." were synthesized. By contrast, in the `<play>` variant:
```
<play file="intro.wav"> Hello, Mister </play> Smith,
<play file="rem.wav"> welcome. </play>
```
The prosody of "Smith" is determined as if the entire sentence were only "Smith." This could lead to unwanted discontinuities in the prosody of the entire utterance. As a general rule, the markup tag `<usesig>` should be preferred over `<play>` if only a part of a sentence is to be replaced by a sound file and the remainder is synthesized. `<usesig>` is especially suited if fixed parts of a sentence should be taken from pre-synthesized sound files, recorded prompts, or intermediate synthesis units files, and only varying parts (e.g., varying proper names) should be synthesized. In this case, the application of `<usesig>` may considerably speed up the synthesis, while the variable parts of the sentence still fit in the prosody of the overall sentence.
If recorded voice prompts are mixed with synthesized speech using the `<usesig>` tag, the perceived overall quality of the output can be increased. It is important though, that the same speaker is used for creating the prompts and to develop the synthetic voice.

- `genfile`: Using the markup section `<genfile file="..."> ... </genfile>` an arbitrary text portion can be saved to a separate sound file. The markup tag `<genfile>` can be used especially for creating synthetic voice prompts. Examples:
```
<genfile file="intro.wav"> Hello, Mister </genfile>
<genfile file="miller.wav"> Miller, </genfile>
<genfile file="rem.wav"> welcome.</genfile>
Hello, Mister <genfile file="smith.wav"> Smith, </genfile> welcome.
```
In this example, three parts of the first sentence "Hello, Mister Miller, welcome." are saved in separate sound files of type wav, and the part "Smith," of the second sentence is also saved in a separate file. These generated sound files can, for instance, be used to generate a newly combined utterance using the markup tag `<play>`:
```
<play file="intro.wav"/> <play file="smith.wav"/>
<play file="rem.wav"/>
```
This input "text", which consists only of markup tags, plays the generated sound files as if the (new) sentence "Hello, Mister Smith, welcome." had been synthesized, but, of  course, with much less processing time. It is essential to note that the sentence part "Smith," should be synthesized and saved to a sound file in the appropriate sentence environment in order for the newly combined utterance to have a continuous melody and rhythm.

### Speaker Functions

**Name**

**wb\_speaker\_play\_sound** - *plays a sound*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

``` c
#include <webots/speaker.h>

void wb_speaker_play_sound(WbDeviceTag left, WbDeviceTag right, const char *sound, double volume, double balance, bool loop)
```

**Description**

This function allows the user to play a sound file. Currently only wave file are supported. The function takes in argument two speaker `WbDeviceTag` respectively for the left and right channels. If booth channels should be played on the same speaker or the file has only one channel, it is possible to send the same tag twice. Alternatively, if one channel should be ignore, it is possible to send `0` instead of one of the two tags.

The `sound` argument should specify the path to the wave file that should be played. The volume allows the user to specify the volume of this sound (between 0.0 and 1.0). The balance allows the user to specify the balance between left and right speaker (between -1.0 and +1.0, for respectively only left and only right). Finaly, the `loop` argument allows the user to set if the sound should be played only once or in a loop.


> **note**:
The path to the sound file should be defined either absolutely or relatively to the controller.


---

**Name**

**wb\_speaker\_stop** - *stops the speaker*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

``` c
#include <webots/speaker.h>

void wb_speaker_stop(WbDeviceTag tag, const char *sound)
```

**Description**

This function stops the sound given in argument. The `sound` argument should be the path to an audio file currently played by the speaker.

It is possible to stop all the sound currently played by the speaker by setting `sound` to `NULL`.

---

**Name**

**wb\_speaker\_set\_language**, **wb\_speaker\_get\_language**, **wb\_speaker\_speak** - *perform text to speech*

{[C++](cpp-api.md#cpp_speaker)}, {[Java](java-api.md#java_speaker)}, {[Python](python-api.md#python_speaker)}, {[Matlab](matlab-api.md#matlab_speaker)}, {[ROS](ros-api.md)}

``` c
#include <webots/speaker.h>

void wb_speaker_set_language(WbDeviceTag tag, const char *language)
const char * wb_speaker_get_language(WbDeviceTag tag)
void wb_speaker_speak(WbDeviceTag tag, const char *text, double volume)
```

**Description**

The `wb_speaker_set_language` function allows the user to set the language of the text to speech.

The `wb_speaker_get_language` function allows the user to get the language of the text to speech.

The `wb_speaker_speak` function allows the user to perform text to speech on the speaker. 
