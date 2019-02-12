# Aristos Athens

'''
    Keep track of timeouts.
'''

from timeit import default_timer as timer

class _request:
    '''
        Store data for a single requests.
    '''
    def __init__(self, duration):
        self._start = timer()
        self._duration = duration

    def timed_out(self):
        if timer() - self._start >= self._duration:
            return True
        else:
            return False


class TimeOut:
    '''
        Track timeouts.
        Static class.
    '''
    _requests = {}

    @staticmethod
    def add(requester, request_type, duration):
        '''
            Add a _request.
            requester should be the IP address of the sender.
            request_type should be the name of the module, ex: contact, index, etc.
            duration is in seconds.
        '''
        key = (requester, request_type)
        if key in TimeOut._requests:
            if TimeOut._requests[key].timed_out():
                TimeOut._requests.pop(key)
            else:
                raise Exception("The last request has not yet timed out." + str(key))

        TimeOut._requests[key] = _request(duration)

    @staticmethod
    def timed_out(requester, request_type):
        '''
            Check if the matching _request has timed out.
            Return True if no matching _request found.
        '''
        key = (requester, request_type)
        if key not in TimeOut._requests:
            return True
        elif TimeOut._requests[key].timed_out():
            TimeOut._requests.pop(key)
            return True
        else:
            return False
