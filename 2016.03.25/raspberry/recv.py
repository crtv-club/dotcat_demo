#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Example program to receive packets from the radio
#
# based on João Paulo Barraca <jpbarraca@gmail.com>
#
from nrf24 import NRF24
import time

pipes = [[0xc2, 0xc2, 0xc2, 0xc2, 0xc2], [0xe7, 0xe7, 0xe7, 0xe7, 0xe7]]

radio = NRF24()
radio.begin(0, 0, 22, 25)  # Set CE and IRQ pins in BCM

radio.setRetries(15, 15)
radio.setPayloadSize(4)
radio.setChannel(0x4c)

radio.setCRCLength(NRF24.CRC_16)

radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MAX)

radio.setAutoAck(1)

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

radio.printDetails()

radio.startListening()

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)

    recv_buffer = []
    radio.read(recv_buffer)

    print(recv_buffer)
    time.sleep(1)
