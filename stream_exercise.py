

class StreamProcessor(object):

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
        
        :return: int
        """

        count = 0
        total = 0

        while total < 200 and count <= 10:
            digits = self._stream.read(2)
            try:
                total += int(digits)
                count += 1

            except ValueError:

                return count

        return count
