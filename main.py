#!/usr/bin/env python3
"""Seed Round — entry for Pigeon Pitch, One Line on make.fun.

Prints exactly one line (at most 200 characters): the elevator pitch a
city pigeon gives to investors for its startup.
"""

LINE = "Investors: we control every statue, every rooftop, and the city's entire crumb supply chain. Our seed round is, fittingly, seed."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
