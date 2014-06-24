.PHONY: install

install:
	install -d "$(DESTDIR)/etc/init.d/"
	install -m 755 gpio_poweroffd -t "$(DESTDIR)/etc/init.d/"
#
	install -d "$(DESTDIR)/usr/local/bin/"
	install -m 744 gpio_poweroffd.py -t "$(DESTDIR)/usr/local/bin/"
