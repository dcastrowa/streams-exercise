"""
USAGE: `python try.py 123456`
"""

import io
import sys

from stream_exercise import StreamProcessor

value = sys.argv[1]

my_stream_processor = StreamProcessor(io.BytesIO(value))
result = my_stream_processor.process()
print("Processed {} and got {}".format(value, result))
