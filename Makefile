all: install

install:
	install -m 755 ./deauth-attack.py /usr/bin/deauth-attack

clean:
	rm -rf /usr/bin/deauth-attack
