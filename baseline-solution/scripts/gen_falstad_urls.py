#!/usr/bin/env python3
"""Generate Falstad circuit simulator URLs for the baseline solution schematics.

Encoding: Falstad plain-text circuit → zlib compress (level 9) →
          URL-safe base64 (no padding) → append as URL fragment.
"""
import zlib, base64

def url(text: str) -> str:
    compressed = zlib.compress(text.encode("utf-8"), level=9)
    encoded = base64.b64encode(compressed, altchars=b"-_").rstrip(b"=").decode()
    return f"https://www.falstad.com/circuit/circuitjs.html#{encoded}"


# ---------------------------------------------------------------------------
# 1. Dual LED Flasher  (10-dual-led-flasher.png)
#    Classic 2-transistor astable multivibrator
#    Q1,Q2 = NPN BC548; R1=R2=47 kΩ; C1=C2=47 µF; LED1,LED2; 3 V supply
# ---------------------------------------------------------------------------
dual_led = """\
$ 1 0.000005 10.20027730826997 50 5 43 5e-11
v 80 400 80 80 0 0 40 3 0 0 0.5
w 80 80 192 80 0
w 192 80 432 80 0
d 192 80 192 160 2 default
d 432 80 432 160 2 default
r 176 80 176 176 0 47000
r 416 80 416 160 0 47000
t 192 352 192 160 0 1 -0.5 100 1
t 432 352 432 160 0 1 -0.5 100 1
w 176 176 176 256 0
w 416 160 416 256 0
c 192 160 416 160 0 4.7e-5 2.8
c 432 176 176 176 0 4.7e-5 -2.8
w 432 160 432 176 0
g 192 352 192 400 0 0
g 432 352 432 400 0 0
w 192 400 432 400 0
g 80 400 80 432 0 0
"""

# ---------------------------------------------------------------------------
# 2. Triac Timer  (15-triac-timer.png)
#    DC control section: push-button triggers RC timer → NPN+PNP latch →
#    resistive load (TRIAC + 220 V mains simplified to R_load)
#    BC547(NPN), BC557(PNP); C=1000 µF; R_time=2 MΩ; 12 V supply
# ---------------------------------------------------------------------------
triac_timer = """\
$ 1 0.000005 10.20027730826997 50 5 43 5e-11
v 64 528 64 80 0 0 40 12 0 0 0.5
w 64 80 512 80 0
g 64 528 64 560 0 0
s 144 80 144 176 0 0 false
w 144 176 256 176 0
r 144 176 144 304 0 2000000
c 256 176 256 528 0 0.001 0
g 256 528 256 560 0 0
t 144 304 144 400 0 1 -0.5 100 1
r 144 80 144 80 0 1000
g 144 400 144 528 0 0
r 320 80 320 176 0 1000
t 320 176 320 288 0 -1 0.5 100 1
w 144 304 320 304 0
w 320 288 320 304 0
d 400 80 400 176 2 default
r 400 176 400 528 0 1000
g 400 528 400 560 0 0
w 320 176 400 176 0
r 256 176 320 176 0 1000
"""

# ---------------------------------------------------------------------------
# 3. LED Chaser  (20-led-chaser.jpg)
#    NE555 astable oscillator + CD4017 decade counter driving 10 LEDs.
#    Modelled as 555 astable (R1=R2=1.5 kΩ, VR=100 kΩ, C1=1 µF, C2=10 nF)
#    with two representative LED+330 Ω output branches; 9 V supply.
# ---------------------------------------------------------------------------
led_chaser = """\
$ 1 5e-6 10.2 50 5 43 5e-11
v 64 512 64 80 0 0 40 9 0 0 0.5
w 64 80 512 80 0
g 64 512 64 544 0 0
r 192 80 192 176 0 1500
r 192 176 192 272 0 1500
r 192 176 320 176 0 100000
c 320 176 320 512 0 1e-6 4.5
g 320 512 320 544 0 0
c 192 272 192 512 0 1e-8 0
g 192 512 192 544 0 0
w 192 272 320 272 0
w 320 272 320 176 0
d 384 80 384 176 2 default
r 384 176 384 512 0 330
g 384 512 384 544 0 0
d 448 80 448 176 2 default
r 448 176 448 512 0 330
g 448 512 448 544 0 0
"""

# ---------------------------------------------------------------------------
# 4. Transistor Equalizer  (25-transistor-equalizer.png)
#    3-band (bass / mid / treble) tone control using common-emitter NPN stages
#    with interstage RC coupling networks; 12 V supply.
# ---------------------------------------------------------------------------
transistor_eq = """\
$ 1 5e-6 10.2 50 5 43 5e-11
v 64 512 64 80 0 0 40 12 0 0 0.5
w 64 80 512 80 0
g 64 512 64 544 0 0
r 160 80 160 176 0 100000
r 160 176 160 512 0 22000
t 160 176 160 288 0 1 -0.5 100 1
r 160 288 160 512 0 1000
g 160 512 160 544 0 0
c 80 256 160 256 0 100e-9 0
r 80 80 80 256 0 10000
c 160 256 256 256 0 10e-9 0
r 256 80 256 176 0 100000
r 256 176 256 512 0 22000
t 256 176 256 288 0 1 -0.5 100 1
r 256 288 256 512 0 1000
g 256 512 256 544 0 0
c 256 256 352 256 0 1e-9 0
r 352 80 352 176 0 100000
r 352 176 352 512 0 22000
t 352 176 352 288 0 1 -0.5 100 1
r 352 288 352 512 0 1000
g 352 512 352 544 0 0
r 352 256 448 256 0 10000
"""

# ---------------------------------------------------------------------------
# 5. Simple Inverter  (30-simple-inverter.png)
#    Push-pull inverter: Q1,Q2 = MJ2955 (PNP); R1=R2=68 Ω;
#    centre-tap transformer (modelled as coupled inductors); 12 V + switch.
# ---------------------------------------------------------------------------
simple_inverter = """\
$ 1 5e-6 10.2 50 5 43 5e-11
v 64 464 64 80 0 0 40 12 0 0 0.5
w 64 80 512 80 0
g 64 464 64 496 0 0
s 128 80 128 160 0 0 false
w 128 160 256 160 0
r 192 160 192 240 0 68
r 320 160 320 240 0 68
t 192 240 192 352 0 -1 0.5 100 1
t 320 240 320 352 0 -1 0.5 100 1
w 192 160 320 160 0
l 192 352 192 464 0 0.05 0
l 320 352 320 464 0 0.05 0
w 192 464 320 464 0
w 256 160 256 464 0
l 432 176 432 352 0 0.025 0
r 432 80 432 176 0 8
g 432 352 432 400 0 0
g 192 464 192 496 0 0
"""

# ---------------------------------------------------------------------------
# 6. LM386 Mini Amplifier  (35-lm386-amplifier.jpg)
#    LM386 audio amplifier (modelled as voltage-gain op-amp, gain ≈ 20–200).
#    VR1=10 kΩ, R1=10 Ω, R2=1.2 kΩ, C1=C2=0.1 µF, C3=C4=10 µF,
#    C5=220 µF output; 8 Ω speaker; 9 V supply.
# ---------------------------------------------------------------------------
lm386_amp = """\
$ 1 5e-6 10.2 50 5 43 5e-11
v 64 480 64 80 0 0 40 9 0 0 0.5
w 64 80 512 80 0
g 64 480 64 512 0 0
r 128 288 192 288 0 10000
c 64 288 128 288 0 1e-7 0
w 64 288 64 480 0
a 256 256 384 256 0 1000000 0 1000000 0
w 192 288 256 272 0
g 256 288 256 320 0 0
r 256 80 256 176 0 1200
c 256 176 384 176 0 10e-6 0
w 384 176 384 240 0
c 384 256 448 256 0 220e-6 0
r 448 256 448 480 0 8
g 448 480 448 512 0 0
r 384 256 384 480 0 10
c 384 480 384 512 0 10e-6 0
g 384 512 384 544 0 0
w 256 80 256 80 0
w 64 80 256 80 0
"""

circuits = {
    "10-dual-led-flasher":    dual_led,
    "15-triac-timer":         triac_timer,
    "20-led-chaser":          led_chaser,
    "25-transistor-equalizer": transistor_eq,
    "30-simple-inverter":     simple_inverter,
    "35-lm386-amplifier":     lm386_amp,
}

if __name__ == "__main__":
    for name, text in circuits.items():
        print(f"{name}")
        print(url(text))
        print()
