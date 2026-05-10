#!/usr/bin/env python3
"""Ackermann motion built in code, then played live at 0.5× speed with logging.

Shows the same parameters as :func:`amr.play_motion_by_kind` but with a custom path.

Run::

    PYTHONPATH=. python examples/live_ackermann_session.py

Optional: append logs to a file by setting ``LOG_PATH`` below.
"""

from __future__ import annotations

import math
import sys

import AuroraMR as amr #The core library

# Set to a path string to tee logs to a file, or None for stdout only
LOG_PATH: str | None = None


def main() -> None:
    params = amr.AckermannParams(
        wheelbase=0.55, #distance between the front and rear 
        track_width=0.36, #distance between the right and left wheels
        max_steering_angle=0.5,
        max_speed=1.0, #Max linear velocity
    )
    session = amr.MotionSession.create(
        amr.pose(0.0, 0.0, 0.0), #Starting position (X=0, Y=0, facing North)
        amr.KinematicsModel.ACKERMANN, #Uses the ackermaan maths model
        dt=0.02, 
        ackermann=params,
    )
    session.forward(1.8, 01.5) #moves in a straight linefor 1.8m and 0.5m/s linear velocity
    session.turn_left(math.radians(45), 0.75) # The left wheel turns leftat 45 degrees at 0.75
    session.forward(1.2, 0.45) #moves in a straight linefor 1.2m and 0.45m/s linear velocity

    log_stream = open(LOG_PATH, "w", encoding="utf-8") if LOG_PATH else None # checks if LOG_PATH was provided earlier, if provided it opens for writing
    try:

        class Tee:
            def __init__(self, *streams: object) -> None:
                self.streams = streams

            def write(self, data: str) -> None: # 
                for s in self.streams: # Loops through all the stream to write all the data at once
                    s.write(data)
                    s.flush()

            def flush(self) -> None:
                for s in self.streams:
                    s.flush()

        out: object = Tee(sys.stdout, log_stream) if log_stream else sys.stdout # if file is open sends data to the file else prints to terminal alonme

        opts = amr.PlaybackLogOptions(
            enabled=True,
            every_n_frames=8,
            detailed_block=True,
            include_velocity=True,
            file=out,  # type: ignore[arg-type]
        )

        amr.play_motion( # This animates the instructions given above
            session,
            interval_ms=30, #Time intervals between animations to be 30ms
            playback_speed=0.5,
            title="Ackermann (custom path)",
            show=True,
            log_options=opts,
        )
    finally: #Serves as a safety net, it closes the log file
        if log_stream is not None:
            log_stream.close()


if __name__ == "__main__": # Tells python to only run main() if i am running this specific file directly
    main()
