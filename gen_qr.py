#!/usr/bin/env python3
# Copyright (c) 2019 Jarret Dyrbye
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php

import qrcode

# depends on:
#
# $ sudo apt-get install python3-pip libopenjp2-7 libtiff5
# $ pip3 install -U pillow qrcode

PNG_BOX_SIZE = 10
QR_BORDER = 2
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_L # 7% ECC
#ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_M # 15% ECC
#ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_Q # 25% ECC
#ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H # 30% ECC

def make_qr_png(content, filename):
    # using uppercase in bech32-style strings allows for efficient
    # alphanumeric-mode encoding
    content = content.upper() if content.isalnum() else content
    qr = qrcode.QRCode(error_correction=ERROR_CORRECTION,
                       box_size=PNG_BOX_SIZE, border=QR_BORDER)
    qr.add_data(content)
    img = qr.make_image(fill_color="black", back_color="white")
    l = img.convert("L")
    w, h = img.size
    print("width: %d height: %d" % (w / 10, h / 10))
    l.save(filename)
    print("saved: %s" % filename)



make_qr_png("jarretdyrbye.com", "/tmp/homepage.png")
make_qr_png("deepdot35wvmeyd5.onion", "/tmp/deepdotweb-onion.png")
make_qr_png("explorerzydxu5ecjrkwceayqybizmpjjznk5izmitf2modhcusuqlid.onion",
            "/tmp/blockstream-info-onion-v3.png")
make_qr_png("dilemma explain adjust begin fashion tree village cave "
            "pioneer only dove coin", "/tmp/12-word-seed-phrase.png")
make_qr_png("lnbc10n1pwghhjwpp5awjn5hgthxz0xxlv80x9uwmpaxd2f6vq98qfrh88r40gmsx"
            "hrhhqdq9v3jkvcqp2rzjqvp62xyytkuen9rc8asxue3fuuzultc89ewwnfxch70zf"
            "80yl0gpjzy5ygqq3yqqqqqqqqqqqqqqrssq0q0daet5waljvep6yqnv03xd0g5789"
            "psrjydauxnxv2l6fvl60gjfykd07u6ueulmm49kssceefn99cpc73zmq6h2lc6ezu"
            "7lx96yv4zgq6pq8kk", "/tmp/bolt11.png")
