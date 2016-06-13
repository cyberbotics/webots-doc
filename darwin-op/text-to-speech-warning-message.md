## Text-to-speech warning message

When using one of the two functions of text to speech from the `Speaker` module
in cross-compilation, you might see the following message:

```
bt_audio_service_open : connect() failed : Connection refused (111)
```

You can simply ignore this message. This message is due to the fact that the
robot is trying to communicate with a non-existent bluetooth device. You can
supress this message by executing the following command on the robot:

```
sudo apt-get purge bluez-alsa
```
