# qr-code-play
A simple script to play around with QR code encoding in Python using the `qrcode` package.

# Depends

    $ sudo apt-get install python3-pip libopenjp2-7 libtiff5
    $ pip3 install -U pillow qrcode

# Usage

When invoked, should produce the outputs like so:

```
$ ./gen_qr.py
width: 25 height: 25
saved: /tmp/homepage.png
width: 29 height: 29
saved: /tmp/deepdotweb-onion.png
width: 37 height: 37
saved: /tmp/blockstream-info-onion-v3.png
width: 37 height: 37
saved: /tmp/12-word-seed-phrase.png
width: 53 height: 53
saved: /tmp/bolt11.png
```

# Examples

![homepage.png](img/homepage.png)
![deepdotweb-onion.png](img/deepdotweb-onion.png)
![blockstream-info-onion-v3.png](img/blockstream-info-onion-v3.png)
![12-word-seed-phrase.png](img/12-word-seed-phrase.png)
![bolt11.png](img/bolt11.png)
