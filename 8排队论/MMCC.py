class MMccQueue(object):
    def __init__(self, arrival, departure, capacity):
        """
        Given the parameter of one M/M/c/c Queue,
        initialize the queue with these parameter and calculate p0
        """
        self._arrival = float(arrival)
        self._departure = float(departure)
        self._capacity = capacity
        preSum = 1
        powerTerm = 1
        factorTerm = 1
        for i in range(1, self._capacity + 1):
            powerTerm *= self._arrival / self._departure
            factorTerm /= float(i)
            preSum += powerTerm * factorTerm
        self._p0 = 1 / preSum

    @property
    def arrival(self):
        return self._arrival

    @property
    def departure(self):
        return self._departure

    @property
    def capacity(self):
        return self._capacity

    def getPk(self, k):
        """
        Return the probability when there is k busy server in the System
        """
        if k > self._capacity:
            return 0
        factorTerm = 1
        powerTerm = 1
        for i in range(1, k+1):
            factorTerm /= float(i)
            powerTerm *= self._arrival / self._departure
        return factorTerm * powerTerm * self._p0

    def getIdleProb(self):
        return self._p0

    def getBlockProb(self):
        """
        Return the probability when a packet comes, it would be blocked.
        That is, P(N=c)
        Also known as Erlang-B function
        """
        return self.getPk(self._capacity)

if __name__ == '__main__':
    thisQueue = MMccQueue(15, 1, 25)
    print(thisQueue.getBlockProb())