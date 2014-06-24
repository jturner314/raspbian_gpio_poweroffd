#################################
GPIO Poweroff Daemon for Raspbian
#################################

This is a daemon for Raspbian Wheezy that listens for GPIO pin 3 to be
shorted to ground.  If the pin is shorted to ground for at least 5
seconds, then the daemon executes the ``poweroff`` command to safely
shutdown the Raspberry Pi.

To install, run::

  # make install

To enable the daemon to start at boot, run::

  # update-rc.d gpio_poweroffd enable

To disable starting at boot, run::

  # update-rc.d gpio_poweroffd disable
