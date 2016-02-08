## Starting Webots

The first time you start Webots it will open the "Welcome to Webots!" menu with
a list of possible starting points.

### Linux

Open a terminal and type `webots` to launch Webots.

### Mac OS X

Open the directory in which you installed the Webots package and double-click on
the Webots icon.

### Windows

On Windows 10 and Windows 7, open the `Start` menu, go to the `Program Files >
Cyberbotics` menu and click on the `Webots
webots_major_version.webots_minor_version.webots_bugfix_version` menu item.

On Windows 8, open the `Start` screen, scroll to the screen's right until
spotting the Cyberbotics section and click on the `Webots` icon.

### Command Line Arguments

Following command line options are available when starting Webots from a
Terminal (Linux/Mac) or a Command Prompt (Windows):

```
SYNOPSIS: webots [options] [worldfile]
OPTIONS:
  --minimize                  minimize Webots window on startup
  --mode=ltmodegt               choose startup mode (overrides
                              application preferences)
                              argument ltmodegt must be one of:
                              pause, realtime, run or fast
                              (Webots PRO is required to use:
                              --mode==run or --mode=fast)
  --help                      display this help message and exit
  --sysinfo                   display information of the system and
                              exit
  --version                   display version information and exit
  --uuid                      display the UUID of the computer and exit
  --stdout                    redirect the controller stdout to the 
                              terminal
  --stderr                    redirect the controller stderr to the 
                              terminal
  --disable-modules-download  skip the check for module updates
  --force-modules-download    automatically download module updates
                              (if any) at startup
  --start-streaming-server    starts the Webots streaming server
                              (Webots PRO is required)
    [="key[=value];..."]         parameters may be given as an option:
                                   port=1234 :
                                     starts the streaming server
                                     on port 1234
                                   monitorActivity :
                                     prints a dot '.' on stdout every
                                     5 seconds
                                   disableStandardStreamsRedirection :
                                     disables the streaming of the
                                     standard output and error streams
  --log-performance="ltfile pathgt[,ltsteps countgt]"
                              measure the performance of Webots and
                              log it in the specified ltfile pathgt
                              file. ltsteps countgt is an optional
                              integer value that specifies how many
                              steps are analyzed. If '--sysinfo' is
                              also set then the system information are
                              printed in the log file.
```



The optional `worldfile` argument specifies the name of a .wbt file to open. If
it is not specified, Webots attempts to open the most recently opened file.

The `--minimize` option is used to minimize (iconize) Webots window on startup.
This also skips the splash screen and the eventual Welcome Dialog. This option
can be used to avoid cluttering the screen with windows when automatically
launching Webots from scripts. Note that Webots PRO does automatically enable
the `Fast` mode when `--minimize` is specified.

The `--mode=ltmodegt` option can be used to start Webots in the specified
execution mode. The four possible execution modes are: `pause`, `realtime`,
`run` and `fast`; they correspond to the simulation control buttons of Webots'
graphical user interface. This option overrides, but does not modify, the
startup mode saved in Webots' preferences. For example, type `webots
--mode=pause filename.wbt` to start Webots in `pause` mode. Note that `run` and
`fast` modes are only available in Webots PRO.

The `--sysinfo` option displays misc information about the current system on the
standard output stream and quits Webots.

The `--stdout` and `--stderr` options have the effect of redirecting Webots
console output to the calling terminal or process. For example, this can be used
to redirect the controllers output to a file or to pipe it to a shell command.
`--stdout` redirects the *stdout* stream of the controllers, while `--stderr`
redirects the *stderr* stream. Note that the *stderr* stream may also contain
Webots error or warning messages.

The `--disable-modules-download` option disables the download of new modules and
therefore prevents the `Webots Update Manager` window from poping up. The
`--force-modules-download` will instead force the automatic download of new
modules (if available) without asking the user. Both options are mutually
exclusive.

The `--start-streaming-server` option starts the Webots streaming server. An
option can be given to change the default parameters of the streaming server.
This option is a string containing a list of parameter keys and their values
separated by semicolons. The supported options are described in .

%figure "Streaming server options"
| Key | Value example | Description |
| --- | --- | --- |
| port | 1234 | The port on which the streaming server is open |
%%end

For example, the following command will start Webots with the streaming server
enabled on the TCP port '1234': `webots --start-streaming-server="port:1234"`

