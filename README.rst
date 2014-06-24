.. Copyright (C) 2014  Jim Turner

   This file is part of raspbian_gpio_poweroffd.

   raspbian_gpio_poweroffd is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by the Free
   Software Foundation, either version 2 of the License, or (at your option) any
   later version.

   This program is distributed in the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
   PARTICULAR PURPOSE.  See the GNU General Public License for more details.

   You should have received a copy of the GNU General Public License along with
   this program.  If not, see <http://www.gnu.org/licenses/>.

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
