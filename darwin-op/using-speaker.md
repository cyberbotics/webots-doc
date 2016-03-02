## Using speaker

As speaker are not present in Webots, it is not possible to use the speakers in
simulation. In cross-compilation it is still possible to play sound by using
these two functions.

**Name**

**virtual void playFile(const char* filename)**, **virtual void playFileWait(const char* filename)** - *Play a sound file*

``` c
#include <webots/Speaker.hpp>

playFile(const char* filename)
playFileWait(const char* filename)
```

**Description**

Filename is the path to an audio file (MP3 for example). The `playFile` function
plays the file without stopping the controller (parallel execution) while the
`playFileWait` function stops the controller until the audio file playback is
complete (serial execution).

In order to use them you have to write something similar to this:

``` c
 #include <webots/Speaker.hpp>

 mSpeaker = getSpeaker("Speaker");
 mSpeaker->enable(mTimeStep);
 mSpeaker->playFile("hello.mp3"); // the file is in the same directory as the controller
```

Because Speaker are not yet present in simulation we recommend you to put all
your code concerning the speaker within `#ifdef CROSSCOMPILATION` statements in
order to keep the same code running in simulation and on the real robot. Here is
an example:

``` c
 #ifdef CROSSCOMPILATION
   mSpeaker = getSpeaker("Speaker");
   mSpeaker->enable(mTimeStep);
 #endif
```

Several audio files are already present on the robot in the "/darwin/Data/mp3/"
folder, you can freely use them this way:

``` c
mSpeaker->playFile("/darwin/Data/mp3/Introduction.mp3"); // this file is already on the robot, no need to send it.
```

The [appendix](audio-files.md) references all the audio files available.

You can also use this two text to speech functions of `Speaker` class:

---

**Name**

**virtual void  speak(const char * text, const char * voice = "en", int speed = 175)**, **virtual void  speakFile(const char * filename, const char * voice = "en", int speed = 175)** - *Text-to-speach methods*

``` c
#include <webots/Speaker.hpp>

speak(const char* text, const char* voice, int speed)
speakFile(const char* filename, const char* voice, int speed)
```

**Description**

In the first one you need to specify the path as an argument to the file
containing the text and in the second one you can directly specify the text. You
can also specify the voice you want to use ([appendix](available-voices.md)
lists all the voices) and the speed in words per minute.

